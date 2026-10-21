# -*- coding: utf-8 -*-
r"""
Genera el Informe interno de hallazgos y oportunidades de mejora de la base de datos ESAP (Word).

Documento de USO INTERNO (no se entrega al cliente). Reúne lo que el entregable no incluye:
indicadores con meta, hallazgos con su evidencia, oportunidades de mejora priorizadas y listas de detalle.
Cada hallazgo y cada oportunidad aparece solo si los datos de la extracción lo sustentan.

Uso:
  python herramientas/generar_informe_interno.py --extraccion extracciones/2026-10-21 --version v1.0
Salida: interno/Informe_Interno_Hallazgos_BD_ESAP_<version>.docx
"""
import argparse
import collections
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402
from docx_util import campo, documento, fecha_larga, n, pie, portada, tabla, vineta  # noqa: E402

TOPE = 25  # filas por lista en los anexos; la lista completa queda en interno/csv/


def hallazgos(m, entorno):
    T, k = m["tablas"], {x["id"]: x for x in m["kpi"]}
    op = [t for t in T.values() if t["k"] in "rp" and not t["particion"]]
    oper = [t for t in op if not t["apoyo"]]
    clave = lambda t: f"{t['s']}.{t['t']}"
    H = []

    ident = sorted([i for i in m["identidad"] if not i["es_maestro"] and not i["apoyo"] and i["nn"]], key=lambda i: -i["fuera"])
    if ident:
        esq = sorted({i["tabla"].split(".")[0] for i in ident})
        maestros = sorted({i["maestro"] for i in m["identidad"]})
        fuera = sum(i["fuera"] for i in ident)
        H.append({"id": "H01", "tema": "Identidad", "prioridad": "Alta",
                  "titulo": "Datos de identidad replicados fuera de la fuente maestra",
                  "observado": f"{n(len(ident))} columnas de correo o documento en {n(len(esq))} esquemas ({', '.join(esq)}) almacenan el dato "
                               f"en lugar de referenciar a la persona en {', '.join(maestros)}. En conjunto suman {n(fuera)} valores distintos "
                               "que no existen en la fuente maestra.",
                  "importa": "Una misma persona puede tener datos distintos en cada módulo. Una actualización en un módulo no llega a los demás, "
                             "y los reportes por persona requieren cruces por correo o documento.",
                  "evidencia": [f"{i['tabla']}.{i['col']}: {n(i['fuera'])} de {n(i['dist'])} valores fuera de la maestra" for i in ident[:6]],
                  "donde": "Portal interno › Identidad · interno/csv/identidad.csv"})

    imp = [i for i in m["implicitas"] if i["nn"]]
    if imp:
        sin_padre = sum(i["sin_padre"] for i in imp)
        conf = sum(1 for i in imp if i["estado"] == "confirmada por datos")
        parc = sum(1 for i in imp if i["estado"] == "parcial")
        H.append({"id": "H02", "tema": "Integridad referencial", "prioridad": "Alta" if sin_padre else "Media",
                  "titulo": "Relaciones lógicas sin llave foránea declarada",
                  "observado": f"{n(len(imp))} columnas con datos apuntan por su nombre a la clave de otra tabla sin una FK. "
                               f"{n(conf)} se confirman con el 95 % o más de los valores, {n(parc)} de forma parcial, y {n(sin_padre)} valores "
                               "no encuentran su registro padre.",
                  "importa": "Sin la FK, la base acepta valores que apuntan a registros inexistentes. Los valores sin padre ya presentes "
                             "deben depurarse antes de declarar la restricción.",
                  "evidencia": [f"{i['c']}.{i['col']} → {i['p']}.{i['pcol']}: {n(i['ok'])} de {n(i['nn'])} con padre ({n(i['cob'])} %)"
                                for i in sorted(imp, key=lambda i: -i["sin_padre"])[:6]],
                  "donde": "Portal interno › Relaciones · docs/csv/relaciones_implicitas.csv"})

    huerf = [f for f in m["fks"] if f.get("huerf")]
    if huerf:
        H.append({"id": "H03", "tema": "Integridad referencial", "prioridad": "Alta",
                  "titulo": "Valores sin registro padre en llaves foráneas declaradas",
                  "observado": f"{n(len(huerf))} FK tienen en total {n(sum(f['huerf'] for f in huerf))} valores sin fila correspondiente en la tabla padre.",
                  "importa": "Indica FK creadas sin validar (NOT VALID) o datos cargados con las restricciones desactivadas. "
                             "Las consultas que unen esas tablas omiten esos registros.",
                  "evidencia": [f"{f['c']} ({', '.join(f['cols'])}) → {f['p']}: {n(f['huerf'])}" for f in huerf[:6]],
                  "donde": "interno/csv/fk_diagnostico.csv"})

    novalid = [f for f in m["fks"] if not f["validada"]]
    if novalid:
        H.append({"id": "H04", "tema": "Integridad referencial", "prioridad": "Media",
                  "titulo": "Llaves foráneas sin validar",
                  "observado": f"{n(len(novalid))} FK están declaradas como NOT VALID: aplican a los registros nuevos, no a los existentes.",
                  "importa": "Los datos anteriores a la restricción no están verificados.",
                  "evidencia": [f"{f['n']} ({f['c']})" for f in novalid[:6]], "donde": "interno/csv/fk_diagnostico.csv"})

    sin_pk = [t for t in oper if not t["pk"]]
    if sin_pk:
        con_uq = sum(1 for t in sin_pk if t["uq"])
        nota_uq = f"; {n(con_uq)} tienen al menos una restricción UNIQUE" if con_uq else ""
        H.append({"id": "H05", "tema": "Unicidad", "prioridad": "Media",
                  "titulo": "Tablas operativas sin clave primaria",
                  "observado": f"{n(len(sin_pk))} de {n(len(oper))} tablas operativas no declaran clave primaria{nota_uq}.",
                  "importa": "No hay garantía de que cada fila sea única. La replicación lógica, varios ORM y las herramientas de "
                             "sincronización requieren una clave primaria.",
                  "evidencia": [f"{clave(t)} ({n(t['filas'])} filas)" for t in sin_pk[:8]], "donde": "Portal interno › Calidad · interno/csv/tablas_sin_pk.csv"})

    sin_idx = [f for f in m["fks"] if not f["indexada"]]
    if sin_idx:
        H.append({"id": "H06", "tema": "Eficiencia", "prioridad": "Media",
                  "titulo": "Llaves foráneas sin índice en la columna hija",
                  "observado": f"{n(len(sin_idx))} de {n(len(m['fks']))} FK no tienen un índice que empiece por sus columnas.",
                  "importa": "Las uniones por esa relación y los borrados o actualizaciones en la tabla padre recorren la tabla hija completa; "
                             "el costo crece con el volumen de producción.",
                  "evidencia": [f"{f['c']} ({', '.join(f['cols'])}) → {f['p']}: {n(f.get('filas'))} filas" for f in sorted(sin_idx, key=lambda f: -(f.get('filas') or 0))[:6]],
                  "donde": "Portal interno › Calidad · interno/csv/fk_diagnostico.csv"})

    if k["K01"]["valor"] < 95 or k["K02"]["valor"] < 95:
        H.append({"id": "H07", "tema": "Comprensibilidad", "prioridad": "Media",
                  "titulo": "Diccionario de datos incompleto en la base",
                  "observado": f"{k['K01']['detalle']}; {k['K02']['detalle']}. Meta de referencia: 95 %.",
                  "importa": "El significado de tablas y columnas depende de conocimiento que no está registrado en la base. "
                             "En el portal de entrega estos elementos aparecen como «por documentar».",
                  "evidencia": [f"{e['nombre']}: {n(sum(1 for t in oper if t['s'] == e['s'] and t['d']))} de "
                                f"{n(sum(1 for t in oper if t['s'] == e['s']))} tablas con descripción" for e in m["esquemas"]][:8],
                  "donde": "Portal interno › Catálogo · docs/csv/tablas.csv y columnas.csv"})

    cred = [(t, c) for t in op for c in t["cols"] if c["pii"] and c["pii"]["cat"] == "Credencial de acceso"]
    if cred:
        H.append({"id": "H08", "tema": "Confidencialidad", "prioridad": "Alta",
                  "titulo": "Columnas con credenciales o tokens de acceso",
                  "observado": f"{n(len(cred))} columnas guardan, por su nombre, contraseñas, hashes o tokens.",
                  "importa": "Deben almacenar solo hashes con algoritmo adaptativo (bcrypt, Argon2) o tokens cifrados, con acceso restringido "
                             "y sin copias en entornos de prueba. La extracción no revisa valores: el formato debe verificarse con desarrollo.",
                  "evidencia": [f"{clave(t)}.{c['n']} ({c['ty']})" for t, c in cred[:8]], "donde": "Portal › Datos personales · docs/csv/datos_personales.csv"})

    vacias = [t for t in oper if t["filas"] == 0]
    if vacias:
        por_esq = collections.Counter(t["s"] for t in vacias)
        H.append({"id": "H09", "tema": "Actualidad", "prioridad": "Baja",
                  "titulo": f"Tablas operativas sin filas en {entorno}",
                  "observado": f"{n(len(vacias))} de {n(len(oper))} tablas operativas no tienen filas. Por esquema: "
                               + ", ".join(f"{s} {n(c)}" for s, c in por_esq.most_common()) + ".",
                  "importa": "Pueden ser módulos aún sin uso en este entorno o estructuras sin uso. Amplían el modelo que se entrega y se mantiene, "
                             "y su estado debe confirmarse con desarrollo.",
                  "evidencia": [f"{clave(t)} (relaciones: {len(t['fk_out']) + len(t['fk_in'])}, funciones que la mencionan: {len(t['prog'])})" for t in vacias[:8]],
                  "donde": "Portal interno › Calidad · interno/csv/tablas_sin_filas.csv"})

    apoyo = [t for t in op if t["apoyo"]]
    if apoyo:
        con_pii = [t for t in apoyo if any(c["pii"] for c in t["cols"]) and t["filas"]]
        H.append({"id": "H10", "tema": "Mantenibilidad", "prioridad": "Media" if con_pii else "Baja",
                  "titulo": "Tablas de apoyo dentro de los esquemas operativos",
                  "observado": f"{n(len(apoyo))} tablas de respaldo, copia, migración o temporales ({n(sum(t['bytes'] for t in apoyo) / 1048576)} MB)"
                               + (f"; {n(len(con_pii))} contienen columnas con datos personales y tienen filas." if con_pii else "."),
                  "importa": "Aparecen en el diccionario junto a las tablas operativas, ocupan espacio y, si copian datos personales, "
                             "amplían el alcance del tratamiento.",
                  "evidencia": [f"{clave(t)} ({n(t['filas'])} filas)" for t in apoyo[:8]], "donde": "Portal interno › Calidad · interno/csv/tablas_apoyo.csv"})

    trg_off = [g for g in m["triggers"] if g["estado"] != "activo"]
    if trg_off:
        H.append({"id": "H11", "tema": "Consistencia", "prioridad": "Media",
                  "titulo": "Triggers deshabilitados",
                  "observado": f"{n(len(trg_off))} triggers están deshabilitados.",
                  "importa": "La lógica que implementan (auditoría, fechas, validaciones) no se ejecuta.",
                  "evidencia": [f"{g['tabla']}: {g['n']}" for g in trg_off[:8]], "donde": "Portal › Programables · docs/csv/triggers.csv"})

    secdef = [p for p in m["programables"] if p["secdef"]]
    if secdef:
        H.append({"id": "H12", "tema": "Seguridad", "prioridad": "Baja",
                  "titulo": "Funciones con SECURITY DEFINER",
                  "observado": f"{n(len(secdef))} funciones se ejecutan con los permisos de su propietario.",
                  "importa": "Deben fijar search_path y limitar EXECUTE a los roles que las requieren.",
                  "evidencia": [f"{p['s']}.{p['n']}" for p in secdef[:8]], "donde": "docs/csv/programables.csv"})
    return H


OPORTUNIDADES = [
    ("OM01", "Fuente única de identidad", ["H01"], "Alta", "Arquitectura de datos y desarrollo",
     "Usar la fuente maestra de personas como único origen de correo y documento. Los módulos guardan solo el identificador "
     "de la persona y resuelven sus datos al consultar. Se requiere un plan de migración y la conciliación de los valores que hoy "
     "están fuera de la maestra."),
    ("OM02", "Declarar las relaciones confirmadas", ["H02", "H03", "H04"], "Alta", "DBA y desarrollo",
     "Depurar los valores sin padre, declarar como FK las relaciones lógicas confirmadas y validar las FK existentes (VALIDATE CONSTRAINT)."),
    ("OM03", "Controles de calidad en la entrada", ["H01", "H02"], "Alta", "Desarrollo",
     "Validar formato, obligatoriedad y referencias antes de guardar. Los registros que no cumplan se rechazan o se envían a cuarentena."),
    ("OM04", "Protección de credenciales", ["H08"], "Alta", "Desarrollo y seguridad",
     "Verificar que contraseñas y tokens se guarden con hash adaptativo o cifrados, restringir su lectura y excluirlos de las copias a entornos de prueba."),
    ("OM05", "Índices en llaves foráneas", ["H06"], "Media", "DBA",
     "Crear índices en las columnas hijas de las FK, empezando por las tablas con más filas. En producción, crearlos con CREATE INDEX CONCURRENTLY."),
    ("OM06", "Claves primarias", ["H05"], "Media", "DBA y desarrollo",
     "Definir clave primaria en cada tabla operativa; donde exista una restricción UNIQUE NOT NULL, promoverla a PK."),
    ("OM07", "Completar el diccionario", ["H07"], "Media", "Líder de datos y equipo funcional",
     "Registrar las descripciones de negocio con COMMENT ON mediante lotes con simulación y reversa (herramientas/generar_comentarios.py). "
     "El portal se actualiza al regenerarlo."),
    ("OM08", "Depuración preventiva", ["H09", "H10"], "Baja", "Desarrollo y DBA",
     "Confirmar con desarrollo el uso de las tablas sin filas y de apoyo. Renombrar las que no se usen con el sufijo _deprecated "
     "durante un periodo de observación y retirarlas si ninguna aplicación falla."),
    ("OM09", "Revisión de lógica en la base", ["H11", "H12"], "Baja", "DBA",
     "Confirmar si los triggers deshabilitados deben activarse o retirarse, y revisar search_path y permisos de las funciones SECURITY DEFINER."),
]


def construir_doc(m, version, entorno):
    ctx = m["ctx"]
    H = hallazgos(m, entorno)
    ids = {h["id"] for h in H}
    OM = [o for o in OPORTUNIDADES if ids & set(o[2])]
    T = m["tablas"]
    oper = [t for t in T.values() if t["k"] in "rp" and not t["particion"] and not t["apoyo"]]

    doc = documento()
    portada(doc, "SuperApp ESAP · Base de datos", "Informe interno de hallazgos y oportunidades de mejora",
            f"Entorno {entorno} · base {ctx['db']} · corte del {fecha_larga(ctx['fecha'])} · versión {version}", marca="USO INTERNO · NO ENTREGABLE")

    doc.add_heading("1. Objetivo y alcance", level=1)
    doc.add_paragraph(
        "Este informe reúne los hallazgos sobre la estructura y la consistencia de la base de datos, y las oportunidades de mejora "
        "que se derivan de ellos. Complementa el Portal de Datos y el resumen ejecutivo que se entregan al cliente, que son descriptivos.")
    doc.add_paragraph(
        f"Fuente: extracción de solo lectura de {ctx['db']} ({entorno}) del {fecha_larga(ctx['fecha'])}, servidor {ctx['srv']}. "
        "Cada cifra sale de la extracción; no se revisaron valores de registros.")

    doc.add_heading("2. Resumen", level=1)
    if H:
        tabla(doc, ["Id", "Hallazgo", "Tema", "Prioridad"], [[h["id"], h["titulo"], h["tema"], h["prioridad"]] for h in H], anchos=[1.3, 9.2, 3.5, 2])
    else:
        doc.add_paragraph("La extracción no sustenta hallazgos.")

    doc.add_heading("3. Indicadores", level=1)
    estado = lambda x: "Referencia" if x["ok"] is None else ("Cumple" if x["ok"] else "No cumple")
    tabla(doc, ["Id", "Indicador", "Dimensión", "Valor", "Meta", "Estado"],
          [[x["id"], x["nombre"], x["dim"], n(x["valor"]) + (" %" if "%" in x["meta"] else ""), x["meta"], estado(x)] for x in m["kpi"]],
          anchos=[1.1, 5.6, 3.3, 1.9, 2, 2.1], derecha=(3,))

    doc.add_heading("4. Hallazgos", level=1)
    for h in H:
        doc.add_heading(f"{h['id']} · {h['titulo']}", level=2)
        campo(doc, "Prioridad:", f"{h['prioridad']} · {h['tema']}")
        campo(doc, "Qué se observó:", h["observado"])
        campo(doc, "Por qué importa:", h["importa"])
        if h["evidencia"]:
            doc.add_paragraph().add_run("Evidencia:").bold = True
            for e in h["evidencia"]:
                vineta(doc, e)
        campo(doc, "Dónde verlo:", h["donde"])

    doc.add_heading("5. Oportunidades de mejora", level=1)
    tabla(doc, ["Id", "Oportunidad", "Atiende", "Prioridad", "Responsable sugerido"],
          [[o[0], o[1], ", ".join(x for x in o[2] if x in ids), o[3], o[4]] for o in OM], anchos=[1.3, 5, 2.4, 2, 5.3])
    for o in OM:
        doc.add_heading(f"{o[0]} · {o[1]}", level=3)
        doc.add_paragraph(o[5])

    doc.add_heading("6. Condiciones de la intervención", level=1)
    for a, b in [("Sin cambios de datos ni restricciones en QA ", "mientras desarrollo y pruebas trabajen sobre la base. Las oportunidades OM02, "
                  "OM05, OM06 y OM08 se planean con desarrollo y se ejecutan en una ventana acordada."),
                 ("Solo metadatos de inmediato: ", "las descripciones (COMMENT ON) se aplican por lotes, con simulación previa, aprobación y reversa."),
                 ("Producción: ", "toda mejora estructural se prueba primero en QA y se despliega con migraciones versionadas del equipo de desarrollo.")]:
        vineta(doc, b, a)

    doc.add_heading("7. Próximos pasos", level=1)
    for i, txt in enumerate([
            "Revisar este informe con el líder técnico y el equipo de desarrollo, y confirmar prioridades y responsables.",
            "Validar con el equipo funcional los nombres de dominio y las descripciones propuestas, y aplicarlas por lotes (OM07).",
            "Acordar con desarrollo el plan para identidad (OM01) y relaciones (OM02), con fechas y criterios de aceptación.",
            "Repetir la extracción después de cada intervención y comparar los indicadores (generar_portal.py --anterior)."], 1):
        doc.add_paragraph(txt, style="List Number")

    doc.add_heading("Anexo A · Listas de detalle", level=1)
    doc.add_paragraph(f"Se muestran hasta {TOPE} filas por lista. Las listas completas están en interno/csv/.")
    sin_pk = [t for t in oper if not t["pk"]]
    if sin_pk:
        doc.add_heading("Tablas operativas sin clave primaria", level=3)
        tabla(doc, ["Tabla", "Filas"], [[f"{t['s']}.{t['t']}", n(t["filas"])] for t in sin_pk[:TOPE]], anchos=[12, 3], derecha=(1,))
    vacias = [t for t in oper if t["filas"] == 0]
    if vacias:
        doc.add_heading(f"Tablas operativas sin filas en {entorno}", level=3)
        tabla(doc, ["Tabla", "Relaciones", "Funciones que la mencionan"],
              [[f"{t['s']}.{t['t']}", n(len(t["fk_out"]) + len(t["fk_in"])), n(len(t["prog"]))] for t in vacias[:TOPE]], anchos=[10, 2.5, 3.5], derecha=(1, 2))
    sin_idx = sorted([f for f in m["fks"] if not f["indexada"]], key=lambda f: -(f.get("filas") or 0))
    if sin_idx:
        doc.add_heading("Llaves foráneas sin índice en la columna hija", level=3)
        tabla(doc, ["Tabla hija", "Columnas", "Tabla padre", "Filas"],
              [[f["c"], ", ".join(f["cols"]), f["p"], n(f.get("filas"))] for f in sin_idx[:TOPE]], anchos=[5.5, 3.5, 5, 2], derecha=(3,))
    ident = [i for i in m["identidad"] if not i["es_maestro"] and i["nn"]]
    if ident:
        doc.add_heading("Identidad frente a la fuente maestra", level=3)
        tabla(doc, ["Tabla.columna", "Distintos", "En maestra", "Fuera"],
              [[f"{i['tabla']}.{i['col']}" + (" (apoyo)" if i["apoyo"] else ""), n(i["dist"]), n(i["en_maestro"]), n(i["fuera"])]
               for i in sorted(ident, key=lambda i: -i["fuera"])[:TOPE]], anchos=[9, 2.3, 2.3, 2.3], derecha=(1, 2, 3))
    pie(doc, f"Generado el {datetime.date.today():%Y-%m-%d} con herramientas/generar_informe_interno.py a partir de la extracción del {ctx['fecha'][:10]}.")
    return doc, H, OM


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extraccion", required=True)
    ap.add_argument("--version", default="v1.0")
    ap.add_argument("--entorno", default="QA")
    ap.add_argument("--salida")
    a = ap.parse_args()
    try:
        m = M.construir(os.path.abspath(a.extraccion))
    except M.ErrorExtraccion as e:
        sys.exit(f"No se generó el informe: {e}")
    doc, H, OM = construir_doc(m, a.version, a.entorno)
    destino = a.salida or os.path.join(M.RAIZ, "interno", f"Informe_Interno_Hallazgos_BD_ESAP_{a.version}.docx")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    doc.save(destino)
    print(f"Informe interno: {os.path.relpath(destino, M.RAIZ)} · {len(H)} hallazgos · {len(OM)} oportunidades de mejora")


if __name__ == "__main__":
    main()
