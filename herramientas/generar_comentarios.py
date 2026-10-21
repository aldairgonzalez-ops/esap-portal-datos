# -*- coding: utf-8 -*-
r"""
Genera el script que registra en la base las descripciones de config/descripciones.csv (COMMENT ON)
y su script de reversa, que restaura los comentarios tal como estaban en la extracción indicada.

Solo toca metadatos (comentarios); no cambia datos ni restricciones. Cumple la regla de simulación:
el script termina en ROLLBACK salvo que se lance con  -v aplicar=1 .

Uso:
  python herramientas/generar_comentarios.py --extraccion extracciones/2026-10-21 --lote L001
Salidas:
  sql/metadatos/<lote>_aplicar_comentarios.sql
  sql/metadatos/<lote>_reversa_comentarios.sql
Ejecución (primero simulación, luego aplicación con aprobación):
  psql "service=esap_qa dbname=esap_db" -X -v aplicar=0 -f sql/metadatos/L001_aplicar_comentarios.sql
  psql "service=esap_qa dbname=esap_db" -X -v aplicar=1 -f sql/metadatos/L001_aplicar_comentarios.sql
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402


def ident(x):
    return '"' + x.replace('"', '""') + '"'


def literal(x):
    return "NULL" if x is None or x == "" else "'" + x.replace("'", "''") + "'"


def objeto(s, t, c, kind):
    tipo = {"v": "VIEW", "m": "MATERIALIZED VIEW", "f": "FOREIGN TABLE"}.get(kind, "TABLE")
    return f"COLUMN {ident(s)}.{ident(t)}.{ident(c)}" if c else f"{tipo} {ident(s)}.{ident(t)}"


def cabecera(titulo, lote, db):
    return [f"/* {titulo} · lote {lote}", "   Solo metadatos (COMMENT ON). Termina en ROLLBACK salvo  -v aplicar=1 . */",
            "\\set ON_ERROR_STOP on", "\\if :{?aplicar}", "\\else", "  \\set aplicar 0", "\\endif",
            f"select current_database() = {literal(db)} as es_la_base \\gset",
            "\\if :es_la_base", "\\else", f"  \\echo 'ALTO: no estás conectado a {db}.'", "  \\quit", "\\endif",
            "begin;"]


def pie():
    return ["\\if :aplicar", "  commit;", "  \\echo 'APLICADO: cambios confirmados.'", "\\else", "  rollback;",
            "  \\echo 'SIMULACIÓN: todo se ejecutó y se revirtió. Para aplicar: -v aplicar=1'", "\\endif"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extraccion", required=True, help="extracción vigente: de ella se toma el comentario actual para la reversa")
    ap.add_argument("--lote", required=True)
    ap.add_argument("--estados", default="validada", help="estados de config/descripciones.csv que se registran (separados por coma)")
    a = ap.parse_args()

    m = M.construir(os.path.abspath(a.extraccion))
    estados = {e.strip().lower() for e in a.estados.split(",")}
    filas = [r for r in M.leer_csv("descripciones.csv") if (r.get("estado") or "").strip().lower() in estados and (r.get("descripcion") or "").strip()]
    if not filas:
        sys.exit(f"No hay descripciones con estado {sorted(estados)} en config/descripciones.csv.")

    # comentario actual en la base, tal como quedó en la extracción (para la reversa)
    actual = {}
    for k, t in m["tablas"].items():
        actual[(t["s"], t["t"], "")] = (t["d"] if t["de"] == "base" else "", t["k"])
        for c in t["cols"]:
            actual[(t["s"], t["t"], c["n"])] = (c["d"] if c["de"] == "base" else "", t["k"])

    aplicar = cabecera("Registrar descripciones de negocio", a.lote, m["ctx"]["db"])
    reversa = cabecera("Reversa: restaurar los comentarios previos", a.lote, m["ctx"]["db"])
    faltan, n = [], 0
    for r in filas:
        clave = (r["esquema"].strip(), r["tabla"].strip(), (r.get("columna") or "").strip())
        if clave not in actual:
            faltan.append(".".join(x for x in clave if x))
            continue
        previo, kind = actual[clave]
        aplicar.append(f"COMMENT ON {objeto(*clave, kind)} IS {literal(r['descripcion'].strip())};")
        reversa.append(f"COMMENT ON {objeto(*clave, kind)} IS {literal(previo)};")
        n += 1
    aplicar += pie()
    reversa += pie()
    destino = os.path.join(M.RAIZ, "sql", "metadatos")
    os.makedirs(destino, exist_ok=True)
    for nombre, lineas in (("aplicar", aplicar), ("reversa", reversa)):
        open(os.path.join(destino, f"{a.lote}_{nombre}_comentarios.sql"), "w", encoding="utf-8").write("\n".join(lineas) + "\n")
    print(f"{n} comentarios en sql/metadatos/{a.lote}_aplicar_comentarios.sql (y su reversa).")
    if faltan:
        print(f"Omitidos por no existir en la extracción ({len(faltan)}): " + ", ".join(faltan[:20]))


if __name__ == "__main__":
    main()
