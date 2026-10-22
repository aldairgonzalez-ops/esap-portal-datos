# -*- coding: utf-8 -*-
r"""
Propone descripciones para las columnas que no tienen COMMENT en la base, a partir de la estructura:
clave primaria, llaves foráneas, relaciones lógicas confirmadas, tipo de dato y convenciones de nombre
(created_at, *_por, fecha_*, is_*, motivo_*…). No usa valores de los registros.

Cada propuesta queda con estado «propuesta» y la regla que la produjo. Las columnas que ninguna regla
cubre quedan con la descripción vacía («por documentar») para que el equipo funcional las complete.

Flujo:
  1. python herramientas/proponer_descripciones.py --extraccion extracciones/2026-10-21 --alcance config/alcances/fase2.json
       -> config/propuestas/<id>_columnas.csv  (hoja de trabajo; se abre en Excel, separador ;)
  2. El equipo revisa la hoja: corrige o completa «descripcion» y cambia «estado» a «validada».
  3. python herramientas/proponer_descripciones.py --incorporar config/propuestas/<id>_columnas.csv [--estados validada,propuesta]
       -> agrega o actualiza esas filas en config/descripciones.csv (el portal las muestra con su estado)
  4. python herramientas/generar_comentarios.py --extraccion … --lote L001   (solo las validadas; COMMENT ON con reversa)
"""
import argparse
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402

CAMPOS = ["esquema", "tabla", "columna", "tipo", "restricciones", "descripcion", "estado", "regla"]

# participio o raíz del nombre -> sustantivo de la acción (anulado_at -> «anulación»)
ACCION = {
    "anulad": "anulación", "revisad": "revisión", "publicad": "publicación", "aprobad": "aprobación", "firmad": "firma",
    "cargad": "carga", "registrad": "registro", "enviad": "envío", "eliminad": "eliminación", "deleted": "eliminación",
    "confirmad": "confirmación", "rechazad": "rechazo", "revocad": "revocación", "cerrad": "cierre", "leid": "lectura",
    "read": "lectura", "creat": "creación", "cread": "creación", "updat": "actualización", "actualizad": "actualización",
    "modificad": "modificación", "asignad": "asignación", "notificad": "notificación", "radicad": "radicación",
    "generad": "generación", "finalizad": "finalización", "iniciad": "inicio", "solicitad": "solicitud",
    "verificad": "verificación", "validad": "validación", "suspendid": "suspensión", "cancelad": "cancelación",
    "archivad": "archivo", "expirad": "vencimiento", "expires": "vencimiento", "vencid": "vencimiento", "pagad": "pago",
    "legalizad": "legalización", "liquidad": "liquidación", "subid": "carga", "uploaded": "carga", "sent": "envío",
    "started": "inicio", "finished": "finalización", "ended": "finalización", "closed": "cierre", "approved": "aprobación",
    "rejected": "rechazo", "reviewed": "revisión", "signed": "firma", "assigned": "asignación", "last_login": "último ingreso",
    "used": "uso", "usad": "uso", "processed": "procesamiento", "procesad": "procesamiento",
}
SIMPLE = {
    "observaciones": "Observaciones registradas sobre el registro.", "observacion": "Observación registrada sobre el registro.",
    "email": "Correo electrónico.", "correo": "Correo electrónico.", "telefono": "Número de teléfono.", "celular": "Número de celular.",
    "identificacion": "Número de identificación.", "num_identificacion": "Número de identificación.",
    "tamano_bytes": "Tamaño del archivo en bytes.", "size_bytes": "Tamaño del archivo en bytes.", "mime_type": "Tipo MIME del archivo.",
    "url": "Dirección web (URL).", "ip": "Dirección IP registrada.", "user_agent": "Agente de usuario (navegador) registrado.",
    "orden": "Posición del registro para su ordenamiento.", "version": "Número de versión del registro.",
    "fecha_inicio": "Fecha de inicio.", "fecha_fin": "Fecha de finalización.", "anio": "Año.", "vigencia": "Vigencia (año).",
    "plazo_dias_habiles": "Plazo en días hábiles.", "dias_habiles": "Número de días hábiles.", "numero": "Número asignado al registro.",
    "metadata": "Metadatos adicionales en formato JSON.", "metadatos": "Metadatos adicionales en formato JSON.",
}
PARTICIPIO = re.compile(r"^(is_|es_|tiene_|has_)?(.+?)$")


TILDES = {"limite": "límite", "electrico": "eléctrico", "electrica": "eléctrica", "numero": "número", "codigo": "código",
          "anio": "año", "dias": "días", "habiles": "hábiles", "titulo": "título", "telefono": "teléfono", "pagina": "página",
          "academico": "académico", "academica": "académica", "tecnico": "técnico", "tecnica": "técnica", "juridico": "jurídico",
          "juridica": "jurídica", "basico": "básico", "minimo": "mínimo", "maximo": "máximo", "ultimo": "último", "ultima": "última",
          "publico": "público", "publica": "pública", "economico": "económico", "medico": "médico", "electronico": "electrónico"}


def tildes(palabra):
    if palabra in TILDES:
        return TILDES[palabra]
    return re.sub(r"(c|s)ion$", r"\1ión", re.sub(r"(c|s)iones$", r"\1iones", palabra))


def humano(x):
    x = re.sub(r"\s+", " ", re.sub(r"(?<=[a-záéíóú])(?=[A-Z])", " ", x).replace("_", " ")).strip().lower()
    return " ".join(tildes(w) for w in x.split())


def accion(raiz):
    # coincidencia exacta con la raíz más su terminación (anulado, anulada, anulados): no se adivinan compuestos
    r = raiz.lower()
    for k, v in ACCION.items():
        if r in (k, k + "o", k + "a", k + "os", k + "as", k + "e", k + "ed"):
            return v
    return None


MASCULINOS = {"registro", "envío", "rechazo", "cierre", "archivo", "inicio", "pago", "uso", "procesamiento", "vencimiento", "último ingreso"}


def art(sust):
    return "el" if sust in MASCULINOS else "la"


def de(sust):
    return "del " + sust if art(sust) == "el" else "de la " + sust


def es_fecha(ty):
    return ty.startswith(("timestamp", "date", "time"))


def proponer(t, c, fk_col, imp_col):
    """Devuelve (descripción, regla) o ("", "") si ninguna regla aplica."""
    n, nl, ty = c["n"], c["n"].lower(), c["ty"]
    tabla = f"{t['s']}.{t['t']}"
    auto = c["ident"] or bool(re.search(r"nextval|gen_random_uuid|uuid_generate", c.get("def") or ""))
    if c["pk"]:
        if nl in ("id", "id_" + t["t"].lower(), t["t"].lower() + "_id") or nl.startswith("id_") or ty == "uuid":
            return (f"Identificador único del registro en la tabla {t['t']}." + (" Se genera automáticamente." if auto else ""), "clave primaria")
        return (f"Clave primaria de la tabla {t['t']}: {humano(n)}.", "clave primaria")
    if (tabla, n) in fk_col:
        p, pc = fk_col[(tabla, n)]
        return (f"Referencia al registro de {p} ({pc}).", "llave foránea")
    if (tabla, n) in imp_col:
        p, pc = imp_col[(tabla, n)]
        return (f"Referencia al registro de {p} ({pc}); relación sin llave foránea declarada.", "relación lógica confirmada")
    if nl in ("created_at", "creado_en", "createdat", "fecha_creacion", "creada_en", "created_on", "fecha_registro") and es_fecha(ty):
        return ("Fecha y hora de creación del registro.", "auditoría")
    if nl in ("updated_at", "actualizado_en", "updatedat", "fecha_actualizacion", "modificado_en", "fecha_modificacion", "updated_on") and es_fecha(ty):
        return ("Fecha y hora de la última actualización del registro.", "auditoría")
    if nl in ("created_by", "creado_por", "createdby"):
        return ("Usuario que creó el registro.", "auditoría")
    if nl in ("updated_by", "actualizado_por", "modificado_por", "updatedby"):
        return ("Usuario que realizó la última actualización del registro.", "auditoría")
    if nl in SIMPLE:
        return (SIMPLE[nl], "nombre de la columna")
    m = re.match(r"^(.+?)_(at|en|on)$", nl)
    if m and es_fecha(ty):
        a = accion(m.group(1))
        if a:
            return (f"Fecha y hora {de(a)}.", "fecha de acción")
    m = re.match(r"^fecha_(.+)$", nl)
    if m and es_fecha(ty):
        a = accion(m.group(1))
        resto = humano(m.group(1))
        if a:
            return (f"Fecha {de(a)}.", "fecha")
        if resto.startswith("límite") or re.fullmatch(r"\w+(ado|ada|ido|ida)", resto):
            return (f"Fecha {resto}.", "fecha")
        return (f"Fecha de {resto}.", "fecha")
    m = re.match(r"^(.+?)_por$", nl)
    if m:
        a = accion(m.group(1))
        if a:
            return (f"Usuario que realizó {art(a)} {a}.", "responsable de acción")
    m = re.match(r"^motivo_(.+)$", nl)
    if m:
        resto = humano(m.group(1))
        return (f"Motivo de la {resto}." if resto.endswith(("ción", "sión")) else f"Motivo del {resto}.", "motivo")
    if ty == "boolean":
        if nl in ("activo", "is_activo", "is_active", "activa", "active", "habilitado", "enabled"):
            return ("Indica si el registro está activo.", "bandera")
        base = PARTICIPIO.match(nl).group(2)
        if re.search(r"(ado|ada|ido|ida)$", base):
            return (f"Indica si el registro está {humano(base)}.", "bandera")
        m = re.match(r"^(requiere|tiene|permite|incluye|aplica|acepta|genera|usa)_(.+)$", base)
        if m:
            return (f"Indica si {m.group(1)} {humano(m.group(2))}.", "bandera")
        return (f"Indica si aplica: {humano(base)}.", "bandera")
    if nl in ("nombre", "name"):
        return (f"Nombre del registro de {t['t']}.", "nombre de la columna")
    if nl in ("descripcion", "description"):
        return (f"Descripción del registro de {t['t']}.", "nombre de la columna")
    if nl in ("codigo", "code"):
        return (f"Código del registro de {t['t']}." + (" Único en la tabla." if c["uq"] else ""), "nombre de la columna")
    if nl in ("estado", "status"):
        return (f"Estado del registro de {t['t']}.", "nombre de la columna")
    if nl in ("tipo", "type"):
        return (f"Tipo del registro de {t['t']}.", "nombre de la columna")
    return ("", "")


def restricciones(t, c, fk_col):
    r = (["PK"] if c["pk"] else []) + (["FK"] if (f"{t['s']}.{t['t']}", c["n"]) in fk_col else []) + (["Unique"] if c["uq"] and not c["pk"] else [])
    return ", ".join(r + (["Null"] if c["nul"] else ["Not Null"]))


def generar(a):
    alcance = M.cargar_alcance(a.alcance) if a.alcance else None
    m = M.aplicar_alcance(M.construir(os.path.abspath(a.extraccion)), alcance)
    fk_col = {}
    for f in m["fks"]:
        if len(f["cols"]) == 1:
            fk_col[(f["c"], f["cols"][0])] = (f["p"], f["pcols"][0])
    imp_col = {(i["c"], i["col"]): (i["p"], i["pcol"]) for i in m["implicitas"] if i["estado"] == "confirmada por datos"}
    validar = {x.strip() for x in (a.validar_reglas or "").split(",") if x.strip()}
    filas, cuenta = [], {}
    for k, t in m["tablas"].items():
        if t["k"] not in "rp" or t["particion"]:
            continue
        for c in t["cols"]:
            if c["de"] == "base":
                continue
            if c["de"] in ("propuesta", "validada"):       # ya está en config/descripciones.csv
                d, estado = c["d"], c["de"]
                sug, r = proponer(t, c, fk_col, imp_col)
                regla = r if sug == d else "config/descripciones.csv"
            else:
                d, regla = proponer(t, c, fk_col, imp_col)
                estado = "propuesta" if d else "por documentar"
                regla = regla or "sin regla"
            cuenta[regla or "por documentar"] = cuenta.get(regla or "por documentar", 0) + 1
            if estado == "propuesta" and regla in validar:
                estado = "validada"
            filas.append({"esquema": t["s"], "tabla": t["t"], "columna": c["n"], "tipo": c["ty"],
                          "restricciones": restricciones(t, c, fk_col), "descripcion": d, "estado": estado, "regla": regla})
    sufijo = alcance["id"].lower() if alcance else "completa"
    destino = a.salida or os.path.join(M.CONFIG, "propuestas", f"{sufijo}_columnas.csv")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    if os.path.exists(destino) and not a.sobrescribir:
        # la hoja puede tener revisiones del equipo que aún no se incorporaron: se conservan
        with open(destino, encoding="utf-8-sig", newline="") as f:
            previas = {(r["esquema"], r["tabla"], r["columna"]): r for r in csv.DictReader(f, delimiter=";")}
        for r in filas:
            p = previas.get((r["esquema"], r["tabla"], r["columna"]))
            editada = p and (p["estado"] not in ("propuesta", "por documentar") or p["descripcion"] != r["descripcion"])
            if editada and r["estado"] not in ("validada",):
                r["descripcion"], r["estado"] = p["descripcion"], p["estado"]
    with open(destino, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, CAMPOS, delimiter=";")
        w.writeheader()
        w.writerows(filas)
    total = sum(len(t["cols"]) for t in m["tablas"].values() if t["k"] in "rp" and not t["particion"])
    base = total - len(filas)
    con = sum(1 for r in filas if r["descripcion"])
    print(f"Hoja de trabajo: {os.path.relpath(destino, M.RAIZ)}")
    print(f"Columnas: {total} · con COMMENT en la base: {base} · propuestas: {con} · por documentar: {len(filas) - con}")
    print(f"Cobertura si se validan todas las propuestas: {M.pct(base + con, total)} %")
    for r, v in sorted(cuenta.items(), key=lambda x: -x[1]):
        print(f"  {v:5d}  {r}")


def incorporar(a):
    estados = {e.strip().lower() for e in a.estados.split(",")}
    with open(a.incorporar, encoding="utf-8-sig", newline="") as f:
        nuevas = [r for r in csv.DictReader(f, delimiter=";")
                  if (r.get("descripcion") or "").strip() and (r.get("estado") or "").strip().lower() in estados]
    ruta = os.path.join(M.CONFIG, "descripciones.csv")
    actuales = M.leer_csv("descripciones.csv")
    clave = lambda r: (r["esquema"].strip(), r["tabla"].strip(), (r.get("columna") or "").strip())
    por_clave = {clave(r): r for r in actuales}
    agregadas = actualizadas = 0
    for r in nuevas:
        k = clave(r)
        fila = {"esquema": k[0], "tabla": k[1], "columna": k[2], "descripcion": r["descripcion"].strip(), "estado": r["estado"].strip().lower()}
        if k in por_clave:
            if (por_clave[k]["descripcion"], por_clave[k]["estado"]) != (fila["descripcion"], fila["estado"]):
                actualizadas += 1
        else:
            agregadas += 1
        por_clave[k] = fila
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, ["esquema", "tabla", "columna", "descripcion", "estado"], delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(por_clave.values(), key=clave))
    print(f"config/descripciones.csv: {agregadas} agregadas · {actualizadas} actualizadas · {len(por_clave)} en total (estados {sorted(estados)})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extraccion")
    ap.add_argument("--alcance", help="JSON de config/alcances/ (versión Lite)")
    ap.add_argument("--salida")
    ap.add_argument("--sobrescribir", action="store_true", help="regenera la hoja sin conservar las revisiones que tenga")
    ap.add_argument("--validar-reglas", help="marca como validadas las propuestas de estas reglas (separadas por coma)")
    ap.add_argument("--incorporar", help="hoja de trabajo revisada que se lleva a config/descripciones.csv")
    ap.add_argument("--estados", default="validada", help="estados de la hoja que se incorporan (separados por coma)")
    a = ap.parse_args()
    if a.incorporar:
        incorporar(a)
    elif a.extraccion:
        generar(a)
    else:
        ap.error("indica --extraccion (generar la hoja) o --incorporar (llevar la hoja revisada a config/descripciones.csv)")


if __name__ == "__main__":
    main()
