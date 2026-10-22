# -*- coding: utf-8 -*-
r"""
Genera el Resumen Ejecutivo de la base de datos ESAP (Word) para el CLIENTE.

Es un documento de entrega: describe la base (alcance, dominios, contenido del modelo, datos personales)
y remite al Portal de Datos y al repositorio para el detalle. No incluye hallazgos, indicadores con meta
ni recomendaciones; eso va en el informe interno (generar_informe_interno.py).

Uso:
  python herramientas/generar_resumen.py --extraccion extracciones/2026-10-21 --version v1.0 \
      --url-portal "https://…/Portal_de_Datos_ESAP_v1.0.html" --repo "https://github.com/…"
Salida: informe/Resumen_Ejecutivo_BD_ESAP_<version>.docx
"""
import argparse
import collections
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402
from docx_util import documento, fecha_larga, hipervinculo, n, pie, portada, tabla, vineta  # noqa: E402


def construir_doc(m, version, url_portal, repo, entorno):
    ctx = m["ctx"]
    op = [t for t in m["tablas"].values() if t["k"] in "rp" and not t["particion"]]
    apoyo = [t for t in op if t["apoyo"]]
    cols = [c for t in op for c in t["cols"]]
    vistas = sum(1 for t in m["tablas"].values() if t["k"] in "vm")
    fecha = fecha_larga(ctx["fecha"])
    enlace = lambda vista: (url_portal + "#" + vista) if url_portal else ""
    alc = m.get("alcance")
    sufijo, sub = (f"_{alc['id']}", alc["id"].lower() + "/") if alc else ("", "")
    nombre_alc = f" · {alc['nombre']}" if alc else ""

    doc = documento()
    portada(doc, "Escuela Superior de Administración Pública · SuperApp ESAP" + nombre_alc, "Resumen ejecutivo de la base de datos",
            f"Entorno {entorno} · base {ctx['db']} · corte del {fecha} · versión {version}")
    if url_portal:
        p = doc.add_paragraph("Portal de Datos ESAP: ")
        hipervinculo(p, url_portal, url_portal)

    doc.add_heading("1. Propósito", level=1)
    doc.add_paragraph(
        "Este documento presenta la base de datos de la SuperApp ESAP: su alcance, su organización por dominios y el contenido "
        "de su modelo. El detalle de cada tabla, columna y relación se consulta en el Portal de Datos ESAP. Las consultas, los archivos "
        "CSV y la documentación en Markdown que respaldan el portal están en el repositorio técnico (sección 6).")
    if alc:
        doc.add_paragraph(f"Esta versión cubre solo la {alc['nombre']} del proyecto. {alc['descripcion']} Las cifras de este documento "
                          "se limitan a esas tablas. Las tablas de otros dominios a las que hacen referencia se muestran en el Modelo ER del portal "
                          "como «otro dominio».")

    doc.add_heading("2. Fuente y alcance", level=1)
    doc.add_paragraph(
        f"La información proviene de una extracción de solo lectura de la base {ctx['db']} en el entorno {entorno}, realizada el {fecha}. "
        "La extracción consulta el catálogo de PostgreSQL, las estadísticas del motor y conteos agregados. "
        "No incluye valores de los registros.")
    tabla(doc, ["Elemento", "Valor"], [
        ["Motor", ctx["version"].split(" on ")[0].split(" (")[0]],
        ["Tamaño de la base" + (" (completa)" if alc else ""), n(ctx["bytes"] / 1048576) + " MB"],
        ["Dominios (esquemas)", n(len(m["esquemas"]))],
        ["Tablas", n(len(op)) + ((", de las cuales 1 es de apoyo (respaldo, copia o migración)" if len(apoyo) == 1 else
                                  f", de las cuales {n(len(apoyo))} son de apoyo (respaldos, copias o migraciones)") if apoyo else "")],
        ["Vistas", n(vistas)],
        ["Columnas", n(len(cols))],
        ["Filas (conteo exacto)", n(sum(t["filas"] or 0 for t in op))],
    ], anchos=[5.5, 10.5])

    doc.add_heading("3. Organización por dominios", level=1)
    doc.add_paragraph("Cada esquema de la base agrupa las tablas de un dominio funcional de la SuperApp.")
    tabla(doc, ["Dominio", "Esquema", "Tablas", "Columnas", "Filas"],
          [[e["nombre"], e["s"], n(e["tablas"]), n(e["columnas"]), n(e["filas"])] for e in m["esquemas"]],
          anchos=[5.4, 4.6, 1.8, 2, 2.6], derecha=(2, 3, 4))

    doc.add_heading("4. Contenido del modelo", level=1)
    con_desc_t = sum(1 for t in op if t["de"] == "base")
    con_desc_c = sum(1 for c in cols if c["de"] == "base")
    val_t = sum(1 for t in op if t["de"] == "validada")
    val_c = sum(1 for c in cols if c["de"] == "validada")
    tabla(doc, ["Componente", "Cantidad", "Dónde se consulta"], [
        ["Relaciones declaradas (llaves foráneas)", n(len(m["fks"])), "Portal › Modelo ER y ficha de cada tabla"],
        ["Relaciones lógicas sin FK, confirmadas con los datos", n(len(m["implicitas"])), "Portal › Modelo ER (relaciones lógicas) y ficha de tabla"],
        ["Funciones y procedimientos", n(len(m["programables"])), "Portal › Inventario de programables"],
        ["Triggers", n(len(m["triggers"])), "Portal › Inventario de programables"],
        ["Vistas", n(vistas), "Portal › Inventario de programables"],
        ["Tipos enumerados", n(len(m["tipos"])), "Repositorio › docs/csv"],
        ["Tablas con descripción registrada en la base", f"{n(con_desc_t)} de {n(len(op))}", "Portal › Inicio (indicadores) y ficha de tabla"],
        ["Columnas con descripción registrada en la base", f"{n(con_desc_c)} de {n(len(cols))}", "Portal › ficha de tabla"],
    ] + ([["Tablas con descripción validada, por registrar en la base", n(val_t), "Portal › ficha de tabla (etiqueta «validada»)"]] if val_t else []) + (
        [["Columnas con descripción validada, por registrar en la base", n(val_c), "Portal › ficha de tabla (etiqueta «validada»)"]] if val_c else []) + [
    ], anchos=[7.5, 2.8, 5.7], derecha=(1,))
    doc.add_paragraph(
        "Las relaciones se documentan con su multiplicidad UML (por ejemplo, 0..* → 1), medida con los datos del entorno. "
        "El modelo entidad-relación se presenta por dominio y muestra también las relaciones con tablas de otros dominios.")

    doc.add_heading("5. Datos personales", level=1)
    pii = [c for t in op for c in t["cols"] if c["pii"]]
    por_cat = collections.Counter(c["pii"]["cat"] for c in pii)
    doc.add_paragraph(
        f"El portal identifica {n(len(pii))} columnas que, por su nombre, contienen datos personales, clasificadas según las categorías "
        "de la Ley 1581 de 2012. La clasificación se hace por nombre y tipo de columna, sin revisar valores, se muestra en la ficha "
        "de cada tabla y sirve de insumo para el responsable del tratamiento de datos.")
    if por_cat:
        tabla(doc, ["Categoría", "Columnas"], [[k, n(v)] for k, v in por_cat.most_common()], anchos=[8, 3], derecha=(1,))

    doc.add_heading("6. Dónde consultar el detalle", level=1)
    p = doc.add_paragraph(f"Portal de Datos ESAP{nombre_alc} {version}: ")
    if url_portal:
        hipervinculo(p, url_portal, url_portal)
    else:
        p.add_run(f"portal/{sub}Portal_de_Datos_ESAP{sufijo}_{version}.html. Es un archivo HTML autónomo que se abre en cualquier navegador, sin conexión.")
    secciones = [("Inicio", "welcome", "Cifras del catálogo, indicadores del modelo de datos (ISO/IEC 25012) y dominios funcionales"),
                 ("Buscador y fichas de tabla", "auth.personas" if not alc else next(iter(sorted(m["tablas"]))), "Menú por esquema y buscador de tablas, columnas y programables. Cada ficha muestra "
                  "propósito, campos, restricciones, datos personales, relaciones, vista enfocada del Modelo ER y lógica relacionada"),
                 ("Modelo ER", "modelo", "Diagrama entidad-relación por dominio, con cardinalidad UML y relaciones lógicas; exportable a SVG y PNG"),
                 ("Inventario de programables", "inventario", "Funciones, procedimientos, vistas y triggers, con las tablas que usan, a quién invocan y quién los invoca")]
    t = tabla(doc, ["Sección del portal", "Contenido", "Enlace"],
              [[s, d, "" if url_portal else f"#{v}"] for s, v, d in secciones], anchos=[3.3, 9.7, 3])
    if url_portal:
        for fila, (s, v, d) in zip(t.rows[1:], secciones):
            hipervinculo(fila.cells[2].paragraphs[0], enlace(v), "Abrir sección")
    p = doc.add_paragraph("Repositorio técnico: ")
    if repo:
        hipervinculo(p, repo, repo)
    else:
        p.add_run("(ubicación por definir)")
    for ruta, d in [(f"docs/{sub}csv/", "catálogo, columnas, relaciones, programables y datos personales en formato CSV"),
                    (f"docs/{sub}catalogo/", "un documento Markdown por dominio con todas sus tablas y columnas"),
                    (f"docs/{sub}informe_extraccion{sufijo}_{version}.md", "cifras de la extracción y cambios frente al corte anterior"),
                    ("sql/extraccion/", "consultas de solo lectura que producen esta información y permiten regenerarla")]:
        vineta(doc, f" {d}.", ruta)

    doc.add_heading("Anexo · Términos", level=1)
    for a, b in [("Llave foránea (FK): ", "restricción que obliga a que un valor exista en la tabla referenciada."),
                 ("Relación lógica: ", "columna que, por su nombre, corresponde a la clave de otra tabla y no tiene FK declarada."),
                 ("Multiplicidad UML: ", "número de registros de cada lado que participan en una relación (0..1, 1, 0..*, 1..*)."),
                 ("Tabla de apoyo: ", "tabla de respaldo, copia, migración o temporal, identificada por su nombre."),
                 ("Fuente maestra: ", "tabla de referencia de un dato, como los datos de identificación de una persona.")]:
        vineta(doc, b, a)
    pie(doc, f"Generado el {datetime.date.today():%Y-%m-%d} con herramientas/generar_resumen.py a partir de la extracción del {ctx['fecha'][:10]}.")
    return doc


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extraccion", required=True)
    ap.add_argument("--version", default="v1.0")
    ap.add_argument("--entorno", default="QA")
    ap.add_argument("--url-portal", default="", help="URL donde quedará publicado el portal")
    ap.add_argument("--repo", default="", help="URL del repositorio técnico")
    ap.add_argument("--alcance", help="versión Lite: JSON de config/alcances/ con los esquemas y tablas incluidos")
    ap.add_argument("--salida")
    a = ap.parse_args()
    alcance = M.cargar_alcance(a.alcance) if a.alcance else None
    try:
        m = M.vista_cliente(M.aplicar_alcance(M.construir(os.path.abspath(a.extraccion)), alcance))
    except M.ErrorExtraccion as e:
        sys.exit(f"No se generó el resumen: {e}")
    doc = construir_doc(m, a.version, a.url_portal, a.repo, a.entorno)
    sufijo, sub = (f"_{alcance['id']}", alcance["id"].lower()) if alcance else ("", "")
    destino = a.salida or os.path.join(M.RAIZ, "informe", sub, f"Resumen_Ejecutivo_BD_ESAP{sufijo}_{a.version}.docx")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    doc.save(destino)
    print("Resumen ejecutivo (cliente):", os.path.relpath(destino, M.RAIZ))


if __name__ == "__main__":
    main()
