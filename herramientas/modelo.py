# -*- coding: utf-8 -*-
"""
Construye el modelo del Portal de Datos ESAP a partir de una extracción (carpeta de JSONL).

Lo usan generar_portal.py (portal HTML, CSV y Markdown) y generar_resumen.py (resumen ejecutivo).
Todo lo que aquí se calcula sale de la extracción y de los archivos de config/; nada se inventa:
si una tabla o columna no tiene comentario en la base, queda como «por documentar».
"""
import collections
import csv
import json
import os
import re

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CONFIG = os.path.join(RAIZ, "config")

ARCHIVOS = ["00_contexto", "01_esquemas", "02_tablas", "03_columnas", "04_restricciones", "05_indices",
            "06_programables", "07_triggers", "08_vistas", "09_tipos", "10_conteo_filas",
            "11_cardinalidad_fk", "12_relaciones_implicitas", "13_identidad"]

# Tablas de apoyo: respaldos, copias, temporales, migraciones y pruebas (por su nombre).
APOYO = re.compile(r"(bkp|backup|respaldo|_old$|^old_|_tmp$|^tmp_|^temp_|_temp$|copia|_copy$|"
                   r"(^|_)\d{8}($|_)|(^|_)20\d{2}_?\d{2}_?\d{2}|deprecated|_test$|^test_|prueba|"
                   r"migrations?(_|$)|flyway|knex_|typeorm_|sequelize)", re.I)

# Datos personales por nombre de columna (Ley 1581 de 2012). Orden: la primera categoría que coincide.
CATEGORIAS_PII = [
    ("Credencial de acceso", "alta", r"(password|passwd|contrasena|clave_acceso|pass_hash|secret|(^|_)token($|_)|token_acceso|token_hash|"
                                     r"sesion_token|token_invitacion|token_microsoft)"),
    ("Dato sensible", "alta", r"(salud|enfermedad|diagnostico_(medico|salud)|discapacidad|etnia|etnic|(^|_)raza|religion|orientacion_sexual|"
                              r"biometr|huella_dactilar|dactilar|rostro|(^|_)foto($|_)|fotografia|sindical|afiliacion_politica|partido_politico)"),
    ("Identificación", "alta", None),          # ver es_documento_identidad()
    ("Identificador en línea (IP)", "media", r"(ip_address|direccion_ip|(^|_)ip($|_))"),
    ("Contacto", "media", r"(e_?mail|correo|(^|_)tel(_|$)|telefono|phone|celular|movil|mobile|whatsapp|"
                          r"(^|_)direccion$|dir_residencia|direccion_residencia|(^|_)address$)"),
    ("Nombre de persona", "media", r"(first_name|last_name|full_name|middle_name|(^|_)nombres$|nombre_completo|nombre_persona|"
                                   r"apellido|nom_tercero|nom_largo|primer_nombre|segundo_nombre)"),
    ("Dato personal", "media", r"(nacimiento|birth|(^|_)edad|genero|gender|(^|_)sexo|estado_civil|gen_tercero)"),
]
# Documento de identidad de una persona (no el nombre, la URL, el tipo o el estado de un documento/archivo).
DOC_IDENTIDAD = re.compile(r"(num_identificacion|(^|_)identificacion$|^identificacion|numero_documento|num_documento|nro_documento|"
                           r"document_number|cedula|(^|_)dni($|_)|pasaporte|passport|[a-z]+_documento$|^documento_(docente|persona|"
                           r"contratista|identidad)$|^documento$)", re.I)
NO_DOC_IDENTIDAD = re.compile(r"(nombre|name|url|tipo|type|estado|status|hash|pdf|archivo|file|origen|biblioteca|adjunto|"
                              r"solicitad|entregad|carpeta|version|fecha|requiere|soporte|(^|_)id_|_id$|^id|id$)", re.I)
# Columnas de contacto institucional (sede, seccional, empresa…): no se tratan como dato personal.
INSTITUCIONAL = re.compile(r"(sede|seccional|empresa|institucion|entidad|dependencia|oficina|soporte|organismo|"
                           r"geopolitica|divipola|remitente|sender|smtp|from_)", re.I)
# «dirección» también nombra dependencias de la ESAP (Dirección Territorial, alta dirección).
NO_DIRECCION = re.compile(r"(territorial|alta_direccion|decision|justificacion|autoriza|delegad)", re.I)
TIPO_DOC = re.compile(r"^(tip|tipo|type)_", re.I)
# Bitácoras: guardan el dato como estaba en el momento del evento; no se cuentan como réplica de identidad.
BITACORA = re.compile(r"(^log_|_logs?$|^logs?$|auditlog|^audit_|_audit$|historial|bitacora)", re.I)


def es_bitacora(esquema, tabla):
    return esquema.lower() == "audit" or bool(BITACORA.search(tabla))


def pl(n, singular, plural):
    """'1 tabla' / '3 tablas' con el número formateado."""
    return f"{n:,}".replace(",", ".") + " " + (singular if n == 1 else plural)
TEXTO = re.compile(r"^(character|text|citext|jsonb?|bytea|name)", re.I)

def es_documento_identidad(col):
    return bool(DOC_IDENTIDAD.search(col)) and not NO_DOC_IDENTIDAD.search(col) and not TIPO_DOC.search(col)


KIND_TABLA = {"r": "Tabla", "p": "Tabla particionada", "v": "Vista", "m": "Vista materializada", "f": "Tabla foránea"}
KIND_PROG = {"f": "Función", "p": "Procedimiento", "a": "Agregada", "w": "Ventana"}
ACCION_FK = {"a": "sin acción", "r": "restringir", "c": "cascada", "n": "poner nulo", "d": "poner valor por defecto"}


class ErrorExtraccion(Exception):
    pass


def leer_jsonl(carpeta, nombre):
    ruta = os.path.join(carpeta, nombre + ".jsonl")
    if not os.path.isfile(ruta):
        raise ErrorExtraccion(f"falta {nombre}.jsonl en {carpeta}")
    filas = []
    for linea in open(ruta, encoding="utf-8-sig"):
        linea = linea.strip()
        if linea:
            filas.append(json.loads(linea))
    if not filas or "_fin" not in filas[-1] or filas[-1]["_fin"] != len(filas) - 1:
        raise ErrorExtraccion(f"{nombre}.jsonl no cierra con su fila de control: la extracción quedó incompleta")
    return filas[:-1]


def leer_csv(nombre):
    ruta = os.path.join(CONFIG, nombre)
    if not os.path.isfile(ruta):
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f, delimiter=";") if any((v or "").strip() for v in r.values())]


def pct(a, b):
    return round(100.0 * a / b, 1) if b else 0.0


def clasificar_pii(col, tabla, tipo=""):
    """Categoría de dato personal según el nombre de la columna (y su tipo: banderas, fechas e ids no guardan el dato)."""
    if TIPO_DOC.search(col):
        return None
    for nombre, nivel, patron in CATEGORIAS_PII:
        coincide = es_documento_identidad(col) if patron is None else re.search(patron, col, re.I)
        if not coincide:
            continue
        # banderas, fechas e ids no guardan el dato; la excepción son los datos personales propios de una fecha o un número
        if tipo and not TEXTO.search(tipo) and not (nombre == "Dato personal" and re.search(r"(date|timestamp|int|numeric|smallint)", tipo, re.I)):
            return None
        if nombre == "Contacto":
            if INSTITUCIONAL.search(col) or INSTITUCIONAL.search(tabla) or NO_DIRECCION.search(col):
                return None
            if col.lower() == "direccion" and re.search(r"(correo|mensaje|email|mail)", tabla, re.I):
                return None          # sentido del correo (entrante/saliente), no domicilio
        return {"cat": nombre, "nivel": nivel}
    return None


def cardinalidad_uml(obligatoria, maxh, dist, padres, unica):
    """Multiplicidad UML de cada extremo: padre (lo que ve un hijo) e hijo (lo que ve un padre)."""
    lado_padre = "1" if obligatoria else "0..1"
    if unica or (maxh is not None and maxh <= 1):
        lado_hijo = "0..1"
    elif dist is not None and padres and dist >= padres:
        lado_hijo = "1..*"
    else:
        lado_hijo = "0..*"
    return lado_padre, lado_hijo


def construir(carpeta):
    ex = {n: leer_jsonl(carpeta, n) for n in ARCHIVOS}
    ctx = ex["00_contexto"][0]

    dominios_cfg = {r["esquema"]: r for r in leer_csv("dominios.csv")}
    desc_cfg = {}
    for r in leer_csv("descripciones.csv"):
        clave = (r.get("esquema", ""), r.get("tabla", ""), r.get("columna", "") or "")
        if (r.get("descripcion") or "").strip():
            desc_cfg[clave] = {"d": r["descripcion"].strip(), "estado": (r.get("estado") or "propuesta").strip().lower()}

    filas = {(r["s"], r["t"]): r["filas"] for r in ex["10_conteo_filas"]}

    # ---- tablas y columnas
    tablas = collections.OrderedDict()
    for r in ex["02_tablas"]:
        k = f'{r["s"]}.{r["t"]}'
        d_bd = (r.get("d") or "").strip()
        extra = desc_cfg.get((r["s"], r["t"], ""))
        if d_bd:
            desc, estado = d_bd, "base"
        elif extra:
            desc, estado = extra["d"], extra["estado"]
        else:
            desc, estado = "", ""
        tablas[k] = {
            "s": r["s"], "t": r["t"], "k": r["k"], "tipo": "Partición" if r.get("particion") else KIND_TABLA.get(r["k"], r["k"]),
            "d": desc, "de": estado,
            "filas": filas.get((r["s"], r["t"])), "est": r.get("est"), "bytes": r.get("bytes") or 0,
            "pk": [], "cols": [], "fk_out": [], "fk_in": [], "imp_out": [], "imp_in": [],
            "idx": [], "uq": [], "ck": [], "trg": [], "usada_por": [], "prog": [],
            "apoyo": bool(APOYO.search(r["t"])), "particion": r.get("particion", False),
            "owner": r.get("owner"), "analizada": r.get("analizada"),
        }
    for r in ex["03_columnas"]:
        k = f'{r["s"]}.{r["t"]}'
        if k not in tablas:
            continue
        d_bd = (r.get("d") or "").strip()
        extra = desc_cfg.get((r["s"], r["t"], r["c"]))
        if d_bd:
            desc, estado = d_bd, "base"
        elif extra:
            desc, estado = extra["d"], extra["estado"]
        else:
            desc, estado = "", ""
        pii = clasificar_pii(r["c"], r["t"], r["ty"])
        tablas[k]["cols"].append({
            "n": r["c"], "ty": r["ty"], "nul": r["nul"], "def": r.get("def"), "d": desc, "de": estado,
            "ident": r.get("ident"), "gen": r.get("gen"),
            "nf": None if r.get("nf") is None else round(r["nf"], 4), "nd": r.get("nd"),
            "pii": pii, "pk": False, "fk": None, "imp": None, "uq": False,
        })

    # ---- restricciones
    fks = []
    for r in ex["04_restricciones"]:
        k = f'{r["s"]}.{r["t"]}'
        if k not in tablas:
            continue
        t = tablas[k]
        if r["ty"] == "p":
            t["pk"] = r["cols"]
        elif r["ty"] == "u":
            t["uq"].append({"n": r["n"], "cols": r["cols"]})
        elif r["ty"] in ("c", "x"):
            t["ck"].append({"n": r["n"], "def": r["def"]})
        elif r["ty"] == "f":
            fk = {"n": r["n"], "c": k, "cols": r["cols"], "p": f'{r["rs"]}.{r["rt"]}', "pcols": r["rcols"],
                  "upd": ACCION_FK.get(r.get("on_upd"), r.get("on_upd")), "del": ACCION_FK.get(r.get("on_del"), r.get("on_del")),
                  "validada": r.get("validada", True), "def": r["def"]}
            fks.append(fk)
    for t in tablas.values():
        nombres = {c["n"]: c for c in t["cols"]}
        for c in t["pk"]:
            if c in nombres:
                nombres[c]["pk"] = True
        for u in t["uq"]:
            if len(u["cols"]) == 1 and u["cols"][0] in nombres:
                nombres[u["cols"][0]]["uq"] = True

    # índices
    for r in ex["05_indices"]:
        k = f'{r["s"]}.{r["t"]}'
        if k in tablas:
            tablas[k]["idx"].append({"n": r["n"], "cols": r["cols"], "uni": r["uni"], "pk": r["pk"],
                                     "def": r["def"], "bytes": r["bytes"], "usos": r.get("usos")})

    # cardinalidad medida
    card = {(f'{r["s"]}.{r["t"]}', r["n"]): r for r in ex["11_cardinalidad_fk"]}
    for fk in fks:
        t = tablas[fk["c"]]
        nombres = {c["n"]: c for c in t["cols"]}
        m = card.get((fk["c"], fk["n"]))
        obligatoria = all(not nombres[c]["nul"] for c in fk["cols"] if c in nombres)
        unica = any(set(u["cols"]) == set(fk["cols"]) for u in t["uq"]) or set(t["pk"]) == set(fk["cols"])
        indexada = any(i["cols"][:len(fk["cols"])] == fk["cols"] for i in t["idx"])
        fk.update({"oblig": obligatoria, "unica": unica, "indexada": indexada})
        if m:
            fk.update({"filas": m["filas"], "nn": m["nn"], "dist": m["dist"], "maxh": m["maxh"],
                       "padres": m["padres"], "huerf": m["huerf"]})
        fk["mp"], fk["mh"] = cardinalidad_uml(obligatoria, fk.get("maxh"), fk.get("dist"), fk.get("padres"), unica)
        t["fk_out"].append(fk["n"])
        if fk["p"] in tablas:
            tablas[fk["p"]]["fk_in"].append(fk["n"])
        if len(fk["cols"]) == 1 and fk["cols"][0] in nombres:
            nombres[fk["cols"][0]]["fk"] = fk["p"] + "." + fk["pcols"][0]

    # relaciones implícitas: por columna se queda el candidato con mayor cobertura (mismo esquema primero)
    # R1 (mismo nombre) solo cuenta si la columna destino es la clave primaria: una columna UNIQUE con el mismo
    # nombre suele ser otra referencia (p. ej. usuario_id único en otra tabla), no el registro padre.
    por_col = collections.defaultdict(list)
    for r in ex["12_relaciones_implicitas"]:
        c, p = f'{r["s"]}.{r["t"]}', f'{r["rs"]}.{r["rt"]}'
        if c not in tablas or p not in tablas or tablas[c]["particion"] or tablas[p]["particion"]:
            continue
        if r["regla"] == "R1" and tablas[p]["pk"] != [r["rcol"]]:
            continue
        por_col[(c, r["col"])].append(r)
    implicitas = []
    for (k, col), cands in por_col.items():
        cands.sort(key=lambda r: (-(r["ok"] / r["nn"] if r["nn"] else 0), not r["mismo_esquema"], r["regla"]))
        r = cands[0]
        cob = pct(r["ok"], r["nn"])
        imp = {"c": k, "col": col, "p": f'{r["rs"]}.{r["rt"]}', "pcol": r["rcol"], "regla": r["regla"],
               "nn": r["nn"], "ok": r["ok"], "sin_padre": r["nn"] - r["ok"], "cob": cob,
               "alternativas": [f'{x["rs"]}.{x["rt"]}' for x in cands[1:]],
               "estado": ("confirmada por datos" if r["nn"] and cob >= 95 else
                          "parcial" if r["nn"] and cob > 0 else
                          "sin datos para validar" if not r["nn"] else "no se confirma")}
        implicitas.append(imp)
        if k in tablas:
            tablas[k]["imp_out"].append(len(implicitas) - 1)
            for c in tablas[k]["cols"]:
                if c["n"] == col:
                    c["imp"] = imp["p"] + "." + imp["pcol"]
        if imp["p"] in tablas:
            tablas[imp["p"]]["imp_in"].append(len(implicitas) - 1)

    # ---- programables, triggers, vistas
    nombres_tablas = {t["t"].lower(): k for k, t in tablas.items()}
    calificadas = {k.lower(): k for k in tablas}
    patron_ref = re.compile(r'\b(?:from|join|into|update|table)\s+((?:"?[\w]+"?\.)?"?[\w]+"?)', re.I)
    patron_esc = re.compile(r'\b(?:insert\s+into|update|delete\s+from|merge\s+into|truncate(?:\s+table)?)\s+((?:"?[\w]+"?\.)?"?[\w]+"?)', re.I)

    def resolver(ref, esquema):
        ref = ref.replace('"', "").lower()
        if "." in ref:
            return calificadas.get(ref)
        return calificadas.get(f"{esquema}.{ref}".lower()) or nombres_tablas.get(ref)

    programables = []
    for r in ex["06_programables"]:
        src = r.get("src") or ""
        usa = sorted({x for x in (resolver(m, r["s"]) for m in patron_ref.findall(src)) if x})
        escribe = sorted({x for x in (resolver(m, r["s"]) for m in patron_esc.findall(src)) if x})
        p = {"s": r["s"], "n": r["n"], "k": r["k"], "tipo": KIND_PROG.get(r["k"], r["k"]), "lang": r["lang"],
             "args": r["args"], "ret": r.get("ret"), "d": (r.get("d") or "").strip(),
             "secdef": r.get("secdef"), "usa": usa, "escribe": escribe, "lineas": src.count("\n") + 1 if src else 0,
             "_src": src,
             "trg_fn": (r.get("ret") or "") == "trigger"}
        programables.append(p)
        for k in usa:
            tablas[k]["prog"].append(f'{r["s"]}.{r["n"]}')
    por_nombre = collections.defaultdict(set)
    for p in programables:
        por_nombre[p["n"].lower()].add(f'{p["s"]}.{p["n"]}')
    patron_llamada = re.compile(r'(?:\b|")((?:"?[\w]+"?\.)?"?[\w]+"?)\s*\(', re.I)
    for p in programables:
        llama = set()
        for ref in patron_llamada.findall(p.pop("_src") or ""):
            ref = ref.replace('"', "")
            nombre = ref.split(".")[-1].lower()
            destinos = por_nombre.get(nombre, set())
            if "." in ref:
                destinos = {d for d in destinos if d.lower() == ref.lower()}
            llama |= {d for d in destinos if d != f'{p["s"]}.{p["n"]}'}
        p["llama"] = sorted(llama)
    triggers = []
    for r in ex["07_triggers"]:
        k = f'{r["s"]}.{r["t"]}'
        tr = {"tabla": k, "n": r["n"], "fn": f'{r["fs"]}.{r["fn"]}', "estado": "activo" if r["estado"] != "D" else "deshabilitado",
              "def": r["def"]}
        triggers.append(tr)
        if k in tablas:
            tablas[k]["trg"].append(tr)
    vistas = []
    for r in ex["08_vistas"]:
        k = f'{r["s"]}.{r["t"]}'
        vistas.append({"v": k, "usa": r["usa"], "def": r["def"]})
        if k in tablas:
            tablas[k]["vdef"] = r["def"]
            tablas[k]["vusa"] = r["usa"]
        for u in r["usa"]:
            if u in tablas:
                tablas[u]["usada_por"].append(k)

    tipos = [{"s": r["s"], "n": r["n"], "vals": r["vals"], "d": r.get("d")} for r in ex["09_tipos"]]

    # ---- identidad replicada
    identidad = []
    for r in ex["13_identidad"]:
        k = f'{r["s"]}.{r["t"]}'
        if INSTITUCIONAL.search(r["col"]) or INSTITUCIONAL.search(r["t"]) or (k in tablas and tablas[k]["particion"]):
            continue
        if r["tipo"] == "documento" and not es_documento_identidad(r["col"]):
            continue
        identidad.append({"tipo": r["tipo"], "tabla": f'{r["s"]}.{r["t"]}', "col": r["col"], "maestro": r["maestro"],
                          "es_maestro": r["es_maestro"], "nn": r["nn"], "dist": r["dist"], "en_maestro": r["en_maestro"],
                          "fuera": r["dist"] - r["en_maestro"], "apoyo": bool(APOYO.search(r["t"])),
                          "bitacora": es_bitacora(r["s"], r["t"])})

    # ---- esquemas / dominios
    esquemas = []
    for r in ex["01_esquemas"]:
        s = r["s"]
        ts = [t for t in tablas.values() if t["s"] == s]
        cfg = dominios_cfg.get(s, {})
        esquemas.append({
            "s": s, "nombre": (cfg.get("nombre") or s.replace("_", " ").capitalize()),
            "d": (r.get("d") or "").strip() or (cfg.get("descripcion") or "").strip(),
            "de": "base" if (r.get("d") or "").strip() else ("propuesta" if (cfg.get("descripcion") or "").strip() else ""),
            "orden": int(cfg.get("orden") or 999), "owner": r.get("owner"),
            "tablas": sum(1 for t in ts if t["k"] in "rpf" and not t["particion"]), "vistas": sum(1 for t in ts if t["k"] in "vm"),
            "columnas": sum(len(t["cols"]) for t in ts if t["k"] in "rpf" and not t["particion"]),
            "filas": sum(t["filas"] or 0 for t in ts if t["k"] in "rpf" and not t["particion"]),
            "vacias": sum(1 for t in ts if t["k"] in "rp" and not t["particion"] and t["filas"] == 0),
            "apoyo": sum(1 for t in ts if t["k"] in "rp" and not t["particion"] and t["apoyo"]),
            "bytes": sum(t["bytes"] for t in ts),
            "prog": sum(1 for p in programables if p["s"] == s),
        })
    esquemas = [e for e in esquemas if e["tablas"] or e["vistas"] or e["prog"]]
    esquemas.sort(key=lambda e: (e["orden"], e["s"]))

    modelo = {"ctx": ctx, "esquemas": esquemas, "tablas": tablas, "fks": fks, "implicitas": implicitas,
              "programables": programables, "triggers": triggers, "vistas": vistas, "tipos": tipos,
              "identidad": identidad}
    modelo["kpi"] = indicadores(modelo)
    return modelo


def indicadores(m):
    """Indicadores de calidad del modelo, con su dimensión (ISO/IEC 25012) y la meta de referencia."""
    ts = [t for t in m["tablas"].values() if t["k"] in "rp" and not t["particion"]]
    oper = [t for t in ts if not t["apoyo"]]
    cols = [c for t in oper for c in t["cols"]]
    fks, imp = m["fks"], m["implicitas"]
    imp_conf = [i for i in imp if i["estado"] in ("confirmada por datos", "parcial")]
    fk1 = [f for f in fks if len(f["cols"]) == 1]
    ident = [i for i in m["identidad"] if not i["es_maestro"] and not i["apoyo"] and not i["bitacora"] and i["fuera"]]
    pii = [c for t in oper for c in t["cols"] if c["pii"]]
    huerf = sum(f.get("huerf") or 0 for f in fks)

    def k(id_, nombre, dim, v, meta, detalle, ok, vista):
        return {"id": id_, "nombre": nombre, "dim": dim, "valor": v, "meta": meta, "detalle": detalle, "ok": ok, "vista": vista}

    con_desc_t = sum(1 for t in oper if t["d"] and t["de"] in ("base", "validada"))
    con_desc_c = sum(1 for c in cols if c["d"] and c["de"] in ("base", "validada"))
    prop_c = sum(1 for c in cols if c["d"] and c["de"] == "propuesta")
    con_pk = sum(1 for t in oper if t["pk"])
    con_datos = sum(1 for t in oper if t["filas"])
    idx_fk = sum(1 for f in fks if f["indexada"])
    decl = len(fk1) + len(imp_conf)
    return [
        k("K01", "Tablas con descripción", "Comprensibilidad", pct(con_desc_t, len(oper)), "≥ 95 %",
          f"{con_desc_t} de {pl(len(oper), 'tabla operativa', 'tablas operativas')} con descripción registrada o validada", pct(con_desc_t, len(oper)) >= 95, "catalogo"),
        k("K02", "Columnas con descripción", "Comprensibilidad", pct(con_desc_c, len(cols)), "≥ 95 %",
          f"{con_desc_c} de {pl(len(cols), 'columna', 'columnas')} de tablas operativas con descripción registrada o validada"
          + (f" · {prop_c} propuestas por validar" if prop_c else ""), pct(con_desc_c, len(cols)) >= 95, "catalogo"),
        k("K03", "Tablas con clave primaria", "Unicidad", pct(con_pk, len(oper)), "100 %",
          f"{con_pk} de {pl(len(oper), 'tabla operativa', 'tablas operativas')} con clave primaria declarada", con_pk == len(oper), "calidad"),
        k("K04", "Relaciones declaradas como FK", "Integridad referencial", pct(len(fk1), decl), "≥ 95 %",
          f"{pl(len(fk1), 'FK declarada', 'FK declaradas')} y {pl(len(imp_conf), 'relación implícita', 'relaciones implícitas')} que los datos confirman total o parcialmente",
          pct(len(fk1), decl) >= 95, "relaciones"),
        k("K05", "FK con índice en la columna hija", "Eficiencia", pct(idx_fk, len(fks)), "100 %",
          f"{idx_fk} de {len(fks)} FK con un índice que empieza por sus columnas", idx_fk == len(fks), "relaciones"),
        k("K06", "Valores sin registro padre en FK", "Consistencia", huerf, "0",
          f"{pl(huerf, 'valor', 'valores')} en columnas FK sin fila correspondiente en la tabla padre", huerf == 0, "relaciones"),
        k("K07", "Tablas operativas con datos", "Actualidad", pct(con_datos, len(oper)), "referencia",
          f"{con_datos} de {pl(len(oper), 'tabla operativa', 'tablas operativas')} con filas en QA; {len(oper) - con_datos} sin filas", None, "calidad"),
        k("K08", "Tablas de apoyo", "Mantenibilidad", len(ts) - len(oper), "referencia",
          f"{pl(len(ts) - len(oper), 'tabla', 'tablas')} de respaldo, copia, migración o temporal identificadas por su nombre", None, "calidad"),
        k("K09", "Copias de datos de identidad fuera de la fuente maestra", "Consistencia", len(ident), "referencia",
          f"{pl(len(ident), 'columna', 'columnas')} de correo o documento en tablas operativas con valores fuera de la fuente maestra (sin contar bitácoras)", None, "identidad"),
        k("K10", "Columnas con datos personales identificadas", "Confidencialidad", len(pii), "referencia",
          f"{pl(len(pii), 'columna clasificada', 'columnas clasificadas')} por su nombre (Ley 1581 de 2012); "
          f"{sum(1 for c in pii if c['pii']['nivel'] == 'alta')} de nivel alto", None, "personales"),
    ]


def vista_cliente(m):
    """Copia del modelo para el entregable: de las relaciones implícitas solo quedan las confirmadas por datos.
    Las parciales y las no confirmadas son diagnóstico y van al informe y al portal internos."""
    import copy
    c = copy.deepcopy(m)
    conservar = [i for i, x in enumerate(m["implicitas"]) if x["estado"] == "confirmada por datos"]
    nuevo = {viejo: n for n, viejo in enumerate(conservar)}
    c["implicitas"] = [c["implicitas"][i] for i in conservar]
    for t in c["tablas"].values():
        t["imp_out"] = [nuevo[i] for i in t["imp_out"] if i in nuevo]
        t["imp_in"] = [nuevo[i] for i in t["imp_in"] if i in nuevo]
        destinos = {(c["implicitas"][i]["col"]) for i in t["imp_out"]}
        for col in t["cols"]:
            if col["imp"] and col["n"] not in destinos:
                col["imp"] = None
    return c


def cargar_alcance(ruta):
    if not ruta:
        return None
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def aplicar_alcance(m, alcance):
    """Modelo restringido a un alcance (p. ej. la Fase 2): esquemas completos más tablas elegidas de otros esquemas.
    Las tablas de fuera del alcance a las que apuntan sus FK quedan en m["contexto"]: el Modelo ER las muestra como
    «otro dominio», pero no entran al catálogo, a las cifras ni a los indicadores."""
    import copy
    if not alcance:
        return m
    completos = set(alcance.get("esquemas", []))
    parciales = alcance.get("parciales", {})

    def en_alcance(t):
        if t["s"] in completos:
            return True
        p = parciales.get(t["s"])
        return bool(p) and (t["t"] in p.get("tablas", []) or any(t["t"].startswith(x) for x in p.get("prefijos", [])))

    c = copy.deepcopy(m)
    dentro = {k for k, t in m["tablas"].items() if en_alcance(t)}
    c["tablas"] = collections.OrderedDict((k, t) for k, t in c["tablas"].items() if k in dentro)
    c["fks"] = [f for f in c["fks"] if f["c"] in dentro]
    c["contexto"] = {f["p"]: m["tablas"][f["p"]] for f in c["fks"] if f["p"] not in dentro and f["p"] in m["tablas"]}
    viejas = c["implicitas"]
    conservar = [i for i, x in enumerate(viejas) if x["c"] in dentro and (x["p"] in dentro or x["p"] in c["contexto"])]
    nuevo = {v: n for n, v in enumerate(conservar)}
    c["implicitas"] = [viejas[i] for i in conservar]
    nombres_fk = {(f["c"], f["n"]) for f in c["fks"]}
    for k, t in c["tablas"].items():
        t["fk_in"] = [n for n in t["fk_in"] if any((f["c"], f["n"]) in nombres_fk and f["n"] == n and f["p"] == k for f in c["fks"])]
        t["imp_out"] = [nuevo[i] for i in t["imp_out"] if i in nuevo]
        t["imp_in"] = [nuevo[i] for i in t["imp_in"] if i in nuevo]
        t["usada_por"] = [v for v in t["usada_por"] if v in dentro]
        for col in t["cols"]:
            if col["imp"] and col["imp"].rsplit(".", 1)[0] not in dentro and col["imp"].rsplit(".", 1)[0] not in c["contexto"]:
                col["imp"] = None
    esquemas_dentro = {t["s"] for t in c["tablas"].values()}
    c["programables"] = [p for p in c["programables"] if p["s"] in completos or set(p["usa"]) & dentro or set(p["escribe"]) & dentro]
    c["triggers"] = [g for g in c["triggers"] if g["tabla"] in dentro]
    fn_trigger = {g["fn"] for g in c["triggers"]}
    ya = {f'{p["s"]}.{p["n"]}' for p in c["programables"]}
    c["programables"] += [p for p in m["programables"] if f'{p["s"]}.{p["n"]}' in fn_trigger and f'{p["s"]}.{p["n"]}' not in ya]
    for t in c["tablas"].values():
        t["prog"] = [x for x in t["prog"] if x in {f'{p["s"]}.{p["n"]}' for p in c["programables"]}]
    c["vistas"] = [v for v in c["vistas"] if v["v"] in dentro or (v["v"].split(".")[0] in completos)]
    c["tipos"] = [x for x in c["tipos"] if x["s"] in completos]
    c["identidad"] = [i for i in c["identidad"] if i["tabla"] in dentro or i["es_maestro"]]
    orden = {s: n for n, s in enumerate(alcance.get("orden", []))}
    esquemas = []
    for e in c["esquemas"]:
        if e["s"] not in esquemas_dentro:
            continue
        ts = [t for t in c["tablas"].values() if t["s"] == e["s"]]
        e = dict(e)
        if e["s"] in parciales:
            p = parciales[e["s"]]
            e.update({"nombre": p.get("nombre", e["nombre"]), "d": p.get("descripcion", e["d"]), "de": "base" if p.get("descripcion") else e.get("de")})
        e.update({"orden": orden.get(e["s"], 999),
                  "tablas": sum(1 for t in ts if t["k"] in "rpf" and not t["particion"]), "vistas": sum(1 for t in ts if t["k"] in "vm"),
                  "columnas": sum(len(t["cols"]) for t in ts if t["k"] in "rpf" and not t["particion"]),
                  "filas": sum(t["filas"] or 0 for t in ts if t["k"] in "rpf" and not t["particion"]),
                  "vacias": sum(1 for t in ts if t["k"] in "rp" and not t["particion"] and t["filas"] == 0),
                  "apoyo": sum(1 for t in ts if t["k"] in "rp" and not t["particion"] and t["apoyo"]),
                  "bytes": sum(t["bytes"] for t in ts), "prog": sum(1 for p in c["programables"] if p["s"] == e["s"])})
        esquemas.append(e)
    c["esquemas"] = sorted(esquemas, key=lambda e: (e["orden"], e["s"]))
    c["alcance"] = alcance
    c["kpi"] = indicadores(c)
    return c
