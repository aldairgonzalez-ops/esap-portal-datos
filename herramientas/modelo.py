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
    ("Credencial de acceso", "alta", r"(password|passwd|contrasena|clave_acceso|pass_hash|secret|(^|_)token)"),
    ("Dato sensible", "alta", r"(salud|enfermedad|diagnost|discapacidad|etnia|etnic|raza|religion|orientacion_sexual|"
                              r"biometr|huella|rostro|(^|_)foto|fotografia|sindical|politic)"),
    ("Identificación", "alta", r"(num_identificacion|identificacion|document_number|num_documento|nro_documento|"
                                r"numero_documento|(^|_)documento$|cedula|(^|_)dni|pasaporte|passport)"),
    ("Contacto", "media", r"(e_?mail|correo|(^|_)tel(_|$)|telefono|phone|celular|movil|mobile|whatsapp|"
                          r"direccion|dir_residencia|address)"),
    ("Nombre de persona", "media", r"(first_name|last_name|full_name|middle_name|(^|_)nombres$|nombre_completo|nombre_persona|"
                                   r"apellido|nom_tercero|nom_largo|primer_nombre|segundo_nombre)"),
    ("Dato personal", "media", r"(nacimiento|birth|(^|_)edad|genero|gender|(^|_)sexo|estado_civil|gen_tercero)"),
]
# Columnas de contacto institucional (sede, seccional, empresa): no se tratan como dato personal.
INSTITUCIONAL = re.compile(r"(sede|seccional|empresa|institucion|entidad|dependencia|oficina|soporte|"
                           r"remitente|sender|smtp|from_)", re.I)
TIPO_DOC = re.compile(r"^(tip|tipo|type)_", re.I)

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


def clasificar_pii(col, tabla):
    if TIPO_DOC.search(col):
        return None
    for nombre, nivel, patron in CATEGORIAS_PII:
        if re.search(patron, col, re.I):
            if nombre == "Contacto" and (INSTITUCIONAL.search(col) or INSTITUCIONAL.search(tabla)):
                return None
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
            "s": r["s"], "t": r["t"], "k": r["k"], "tipo": KIND_TABLA.get(r["k"], r["k"]),
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
        pii = clasificar_pii(r["c"], r["t"])
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
    por_col = collections.defaultdict(list)
    for r in ex["12_relaciones_implicitas"]:
        por_col[(f'{r["s"]}.{r["t"]}', r["col"])].append(r)
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
             "trg_fn": (r.get("ret") or "") == "trigger"}
        programables.append(p)
        for k in usa:
            tablas[k]["prog"].append(f'{r["s"]}.{r["n"]}')
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
        if INSTITUCIONAL.search(r["col"]) or INSTITUCIONAL.search(r["t"]):
            continue
        identidad.append({"tipo": r["tipo"], "tabla": f'{r["s"]}.{r["t"]}', "col": r["col"], "maestro": r["maestro"],
                          "es_maestro": r["es_maestro"], "nn": r["nn"], "dist": r["dist"], "en_maestro": r["en_maestro"],
                          "fuera": r["dist"] - r["en_maestro"], "apoyo": bool(APOYO.search(r["t"]))})

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
            "tablas": sum(1 for t in ts if t["k"] in "rpf"), "vistas": sum(1 for t in ts if t["k"] in "vm"),
            "columnas": sum(len(t["cols"]) for t in ts if t["k"] in "rpf"),
            "filas": sum(t["filas"] or 0 for t in ts if t["k"] in "rpf"),
            "vacias": sum(1 for t in ts if t["k"] in "rp" and t["filas"] == 0),
            "apoyo": sum(1 for t in ts if t["k"] in "rp" and t["apoyo"]),
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
    ident = [i for i in m["identidad"] if not i["es_maestro"] and not i["apoyo"] and i["nn"]]
    pii = [c for t in oper for c in t["cols"] if c["pii"]]
    huerf = sum(f.get("huerf") or 0 for f in fks)

    def k(id_, nombre, dim, v, meta, detalle, ok, vista):
        return {"id": id_, "nombre": nombre, "dim": dim, "valor": v, "meta": meta, "detalle": detalle, "ok": ok, "vista": vista}

    con_desc_t = sum(1 for t in oper if t["d"])
    con_desc_c = sum(1 for c in cols if c["d"])
    con_pk = sum(1 for t in oper if t["pk"])
    con_datos = sum(1 for t in oper if t["filas"])
    idx_fk = sum(1 for f in fks if f["indexada"])
    decl = len(fk1) + len(imp_conf)
    return [
        k("K01", "Tablas con descripción", "Comprensibilidad", pct(con_desc_t, len(oper)), "≥ 95 %",
          f"{con_desc_t} de {len(oper)} tablas operativas tienen descripción registrada", pct(con_desc_t, len(oper)) >= 95, "catalogo"),
        k("K02", "Columnas con descripción", "Comprensibilidad", pct(con_desc_c, len(cols)), "≥ 95 %",
          f"{con_desc_c} de {len(cols)} columnas de tablas operativas tienen descripción", pct(con_desc_c, len(cols)) >= 95, "catalogo"),
        k("K03", "Tablas con clave primaria", "Unicidad", pct(con_pk, len(oper)), "100 %",
          f"{con_pk} de {len(oper)} tablas operativas declaran clave primaria", con_pk == len(oper), "calidad"),
        k("K04", "Relaciones declaradas como FK", "Integridad referencial", pct(len(fk1), decl), "≥ 95 %",
          f"{len(fk1)} FK declaradas y {len(imp_conf)} relaciones implícitas que los datos confirman total o parcialmente",
          pct(len(fk1), decl) >= 95, "relaciones"),
        k("K05", "FK con índice en la columna hija", "Eficiencia", pct(idx_fk, len(fks)), "100 %",
          f"{idx_fk} de {len(fks)} FK tienen un índice que empieza por sus columnas", idx_fk == len(fks), "relaciones"),
        k("K06", "Valores sin registro padre en FK", "Consistencia", huerf, "0",
          f"{huerf} valores en columnas FK sin fila correspondiente en la tabla padre", huerf == 0, "relaciones"),
        k("K07", "Tablas operativas con datos", "Actualidad", pct(con_datos, len(oper)), "referencia",
          f"{con_datos} de {len(oper)} tablas operativas tienen filas en QA; {len(oper) - con_datos} sin filas", None, "calidad"),
        k("K08", "Tablas de apoyo", "Mantenibilidad", len(ts) - len(oper), "referencia",
          f"{len(ts) - len(oper)} tablas de respaldo, copia, migración o temporales identificadas por su nombre", None, "calidad"),
        k("K09", "Copias de datos de identidad fuera de la fuente maestra", "Consistencia", len(ident), "referencia",
          f"{len(ident)} columnas de correo o documento con datos fuera de la fuente maestra", None, "identidad"),
        k("K10", "Columnas con datos personales identificadas", "Confidencialidad", len(pii), "referencia",
          f"{len(pii)} columnas clasificadas por su nombre (Ley 1581 de 2012); "
          f"{sum(1 for c in pii if c['pii']['nivel'] == 'alta')} de nivel alto", None, "personales"),
    ]
