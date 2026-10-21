# -*- coding: utf-8 -*-
r"""
Genera el Portal de Datos ESAP y el detalle técnico del repositorio a partir de una extracción.

Salidas (rutas relativas a la raíz del repositorio):
  ENTREGABLE (cliente) · lenguaje descriptivo, sin hallazgos ni recomendaciones
    portal/Portal_de_Datos_ESAP_<version>.html     HTML autónomo, sin conexión ni CDN
    docs/csv/*.csv                                 catálogo, columnas, relaciones, programables… (separador ;, UTF-8 con BOM)
    docs/catalogo/*.md                             un Markdown por esquema y un índice
    docs/informe_extraccion_<version>.md           cifras de la extracción y, con --anterior, cambios frente a ella
  USO INTERNO · hallazgos e indicadores con meta
    interno/Portal_de_Datos_ESAP_<version>_interno.html   portal con las vistas Calidad e Identidad
    interno/csv/*.csv                                      indicadores, identidad, FK con diagnóstico y listas de hallazgos

Uso:
  python herramientas/generar_portal.py --extraccion extracciones/2026-10-21 --version v1.0
  python herramientas/generar_portal.py --extraccion extracciones/2026-10-21 --version v1.1 --anterior extracciones/2026-10-14
Opciones: --entorno QA · --repo <url del repositorio> · --simular (no escribe nada)
"""
import argparse
import csv
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402

RAIZ = M.RAIZ
PLANTILLA = os.path.join(RAIZ, "herramientas", "plantilla_portal.html")


def escribir_csv(ruta, cab, filas):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(cab)
        w.writerows(filas)


def md_celda(v):
    return str("" if v is None else v).replace("|", "\\|").replace("\n", " ")


def generar_csv(m, carpeta):
    T = m["tablas"]
    escribir_csv(os.path.join(carpeta, "esquemas.csv"),
                 ["esquema", "dominio", "descripcion", "tablas", "vistas", "columnas", "filas", "tablas_sin_filas", "tablas_apoyo", "programables", "bytes"],
                 [[e["s"], e["nombre"], e["d"], e["tablas"], e["vistas"], e["columnas"], e["filas"], e["vacias"], e["apoyo"], e["prog"], e["bytes"]] for e in m["esquemas"]])
    escribir_csv(os.path.join(carpeta, "tablas.csv"),
                 ["esquema", "tabla", "tipo", "descripcion", "estado_descripcion", "filas", "columnas", "clave_primaria", "fk_salida", "fk_entrada",
                  "implicitas_salida", "implicitas_entrada", "indices", "triggers", "apoyo", "bytes"],
                 [[t["s"], t["t"], t["tipo"], t["d"], t["de"], t["filas"], len(t["cols"]), ",".join(t["pk"]), len(t["fk_out"]), len(t["fk_in"]),
                   len(t["imp_out"]), len(t["imp_in"]), len(t["idx"]), len(t["trg"]), "sí" if t["apoyo"] else "no", t["bytes"]] for t in T.values()])
    escribir_csv(os.path.join(carpeta, "columnas.csv"),
                 ["esquema", "tabla", "posicion", "columna", "tipo", "admite_nulos", "valor_defecto", "descripcion", "estado_descripcion",
                  "pk", "unica", "fk_a", "implicita_a", "fraccion_nulos", "dato_personal", "nivel"],
                 [[t["s"], t["t"], i + 1, c["n"], c["ty"], "sí" if c["nul"] else "no", c["def"], c["d"], c["de"], "sí" if c["pk"] else "",
                   "sí" if c["uq"] else "", c["fk"] or "", c["imp"] or "", c["nf"], (c["pii"] or {}).get("cat", ""), (c["pii"] or {}).get("nivel", "")]
                  for t in T.values() for i, c in enumerate(t["cols"])])
    escribir_csv(os.path.join(carpeta, "relaciones_fk.csv"),
                 ["tabla_hija", "columnas", "tabla_padre", "columnas_padre", "fk", "multiplicidad_hijo", "multiplicidad_padre", "obligatoria",
                  "filas_hija", "con_valor", "padres_distintos", "max_hijos_por_padre", "filas_padre", "on_delete", "on_update"],
                 [[f["c"], ",".join(f["cols"]), f["p"], ",".join(f["pcols"]), f["n"], f["mh"], f["mp"], "sí" if f["oblig"] else "no",
                   f.get("filas"), f.get("nn"), f.get("dist"), f.get("maxh"), f.get("padres"), f["del"], f["upd"]] for f in m["fks"]])
    escribir_csv(os.path.join(carpeta, "relaciones_implicitas.csv"),
                 ["tabla", "columna", "tabla_destino", "columna_destino", "regla", "valores", "con_padre", "sin_padre", "cobertura_pct", "estado", "otros_destinos_posibles"],
                 [[i["c"], i["col"], i["p"], i["pcol"], i["regla"], i["nn"], i["ok"], i["sin_padre"], i["cob"], i["estado"], ", ".join(i["alternativas"])] for i in m["implicitas"]])
    escribir_csv(os.path.join(carpeta, "programables.csv"),
                 ["esquema", "nombre", "tipo", "lenguaje", "parametros", "devuelve", "usa", "escribe_en", "descripcion", "security_definer"],
                 [[p["s"], p["n"], p["tipo"], p["lang"], p["args"], p["ret"], ", ".join(p["usa"]), ", ".join(p["escribe"]), p["d"], "sí" if p["secdef"] else "no"]
                  for p in m["programables"]])
    escribir_csv(os.path.join(carpeta, "datos_personales.csv"), ["esquema", "tabla", "columna", "tipo", "categoria", "nivel", "tabla_apoyo"],
                 [[t["s"], t["t"], c["n"], c["ty"], c["pii"]["cat"], c["pii"]["nivel"], "sí" if t["apoyo"] else "no"]
                  for t in T.values() if t["k"] in "rp" for c in t["cols"] if c["pii"]])
    escribir_csv(os.path.join(carpeta, "triggers.csv"), ["tabla", "trigger", "funcion", "estado", "definicion"],
                 [[g["tabla"], g["n"], g["fn"], g["estado"], g["def"]] for g in m["triggers"]])


def generar_csv_interno(m, carpeta):
    """Diagnóstico para el equipo interno: indicadores con meta, identidad y listas de hallazgos."""
    T = m["tablas"]
    oper = [t for t in T.values() if t["k"] in "rp" and not t["particion"] and not t["apoyo"]]
    escribir_csv(os.path.join(carpeta, "fk_diagnostico.csv"),
                 ["tabla_hija", "columnas", "tabla_padre", "fk", "filas_hija", "sin_padre", "indice_en_hija", "validada"],
                 [[f["c"], ",".join(f["cols"]), f["p"], f["n"], f.get("filas"), f.get("huerf"), "sí" if f["indexada"] else "no",
                   "sí" if f["validada"] else "no"] for f in m["fks"]])
    escribir_csv(os.path.join(carpeta, "tablas_sin_pk.csv"), ["esquema", "tabla", "filas", "claves_unicas"],
                 [[t["s"], t["t"], t["filas"], " | ".join(",".join(u["cols"]) for u in t["uq"])] for t in oper if not t["pk"]])
    escribir_csv(os.path.join(carpeta, "tablas_sin_filas.csv"), ["esquema", "tabla", "fk_salida", "fk_entrada", "mencionada_por_funciones"],
                 [[t["s"], t["t"], len(t["fk_out"]), len(t["fk_in"]), len(t["prog"])] for t in oper if t["filas"] == 0])
    escribir_csv(os.path.join(carpeta, "tablas_apoyo.csv"), ["esquema", "tabla", "filas", "bytes"],
                 [[t["s"], t["t"], t["filas"], t["bytes"]] for t in T.values() if t["k"] in "rp" and t["apoyo"]])
    escribir_csv(os.path.join(carpeta, "identidad.csv"),
                 ["tipo", "tabla", "columna", "fuente_maestra", "es_maestra", "con_valor", "distintos", "en_maestra", "fuera_de_maestra", "tabla_apoyo"],
                 [[i["tipo"], i["tabla"], i["col"], i["maestro"], "sí" if i["es_maestro"] else "no", i["nn"], i["dist"], i["en_maestro"], i["fuera"],
                   "sí" if i["apoyo"] else "no"] for i in m["identidad"]])
    escribir_csv(os.path.join(carpeta, "indicadores.csv"), ["id", "indicador", "dimension", "valor", "meta", "detalle"],
                 [[k["id"], k["nombre"], k["dim"], k["valor"], k["meta"], k["detalle"]] for k in m["kpi"]])


def generar_md(m, carpeta, nombre_portal):
    os.makedirs(carpeta, exist_ok=True)
    T, ctx = m["tablas"], m["ctx"]
    indice = [f"# Catálogo de la base {ctx['db']}", "",
              f"Extracción de solo lectura del {ctx['fecha'][:10]} · {ctx['version']}. La vista navegable está en el portal "
              f"(`portal/{nombre_portal}`); aquí queda la misma información en texto para consulta y control de versiones.", "",
              "| Dominio | Esquema | Tablas | Columnas | Filas | Programables |", "|---|---|--:|--:|--:|--:|"]
    for e in m["esquemas"]:
        indice.append(f"| [{md_celda(e['nombre'])}]({e['s']}.md) | `{e['s']}` | {e['tablas']} | {e['columnas']} | {e['filas']:,} | {e['prog']} |".replace(",", "."))
        L = [f"# {e['nombre']} (`{e['s']}`)", "", e["d"] or "_Descripción del dominio por documentar._", "",
             f"{e['tablas']} tablas · {e['vistas']} vistas · {e['columnas']} columnas · {e['filas']:,} filas · {e['prog']} funciones o procedimientos".replace(",", "."), ""]
        ts = [t for t in T.values() if t["s"] == e["s"]]
        L += ["| Tabla | Tipo | Filas | Descripción |", "|---|---|--:|---|"]
        L += [f"| [`{t['t']}`](#{t['t'].lower()}) | {t['tipo']}{' · apoyo' if t['apoyo'] else ''} | {'' if t['filas'] is None else t['filas']} | {md_celda(t['d']) or '_Por documentar_'} |" for t in ts]
        for t in ts:
            L += ["", f"## {t['t']}", "", md_celda(t["d"]) or "_Por documentar._", "",
                  f"- Clave primaria: {', '.join(f'`{c}`' for c in t['pk']) or 'no declarada'}",
                  f"- Filas: {'—' if t['filas'] is None else t['filas']}"]
            fks = [f for f in m["fks"] if f["c"] == f"{t['s']}.{t['t']}"]
            if fks:
                L.append("- Referencia a: " + "; ".join(f"`{', '.join(f['cols'])}` → `{f['p']}` ({f['mh']} → {f['mp']})" for f in fks))
            imps = [m["implicitas"][i] for i in t["imp_out"]]
            if imps:
                L.append("- Relaciones implícitas: " + "; ".join(f"`{i['col']}` ↝ `{i['p']}` ({i['cob']} % con padre)" for i in imps))
            if t.get("vusa"):
                L.append("- Vista que usa: " + ", ".join(f"`{u}`" for u in t["vusa"]))
            L += ["", "| # | Columna | Tipo | Nulos | Descripción | Marcas |", "|--:|---|---|---|---|---|"]
            for i, c in enumerate(t["cols"]):
                marcas = " ".join(x for x in ["PK" if c["pk"] else "", "única" if c["uq"] else "", f"FK→{c['fk']}" if c["fk"] else "",
                                              f"↝{c['imp']}" if c["imp"] else "", c["pii"]["cat"] if c["pii"] else ""] if x)
                L.append(f"| {i + 1} | `{c['n']}` | `{md_celda(c['ty'])}` | {'sí' if c['nul'] else 'no'} | {md_celda(c['d']) or '_Por documentar_'} | {md_celda(marcas)} |")
        open(os.path.join(carpeta, f"{e['s']}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    open(os.path.join(carpeta, "README.md"), "w", encoding="utf-8").write("\n".join(indice) + "\n")


def comparar(m, anterior):
    """Cambios de estructura frente a una extracción anterior (tablas, columnas, FK, programables, filas)."""
    a = M.construir(anterior)
    ta, tn = set(a["tablas"]), set(m["tablas"])
    ca = {(k, c["n"]): c["ty"] for k, t in a["tablas"].items() for c in t["cols"]}
    cn = {(k, c["n"]): c["ty"] for k, t in m["tablas"].items() for c in t["cols"]}
    fa, fn = {(f["c"], f["n"]) for f in a["fks"]}, {(f["c"], f["n"]) for f in m["fks"]}
    pa = {f"{p['s']}.{p['n']}({p['args']})" for p in a["programables"]}
    pn = {f"{p['s']}.{p['n']}({p['args']})" for p in m["programables"]}
    filas = sorted(((k, a["tablas"][k]["filas"], m["tablas"][k]["filas"]) for k in ta & tn
                    if a["tablas"][k]["filas"] != m["tablas"][k]["filas"]), key=lambda x: -abs((x[2] or 0) - (x[1] or 0)))
    col_n = sorted(f"{k}.{c}" for k, c in set(cn) - set(ca) if k in ta)
    col_r = sorted(f"{k}.{c}" for k, c in set(ca) - set(cn) if k in tn)
    lista = lambda xs: ", ".join(f"`{x}`" for x in xs[:60]) + (f" … y {len(xs) - 60} más" if len(xs) > 60 else "") if xs else "ninguna"
    L = ["", f"## Cambios frente a la extracción del {a['ctx']['fecha'][:10]}", "",
         f"- **Tablas nuevas ({len(tn - ta)}):** {lista(sorted(tn - ta))}",
         f"- **Tablas que ya no están ({len(ta - tn)}):** {lista(sorted(ta - tn))}",
         f"- **Columnas nuevas en tablas que ya existían ({len(col_n)}):** {lista(col_n)}",
         f"- **Columnas retiradas de tablas que siguen ({len(col_r)}):** {lista(col_r)}",
         f"- **Columnas con otro tipo:** {lista(sorted(f'{k}.{c} {ca[(k, c)]} → {cn[(k, c)]}' for k, c in set(ca) & set(cn) if ca[(k, c)] != cn[(k, c)]))}",
         f"- **FK nuevas ({len(fn - fa)}):** {lista(sorted(n for _, n in fn - fa))}",
         f"- **FK retiradas ({len(fa - fn)}):** {lista(sorted(n for _, n in fa - fn))}",
         f"- **Programables nuevos ({len(pn - pa)}):** {lista(sorted(pn - pa))}",
         f"- **Programables retirados ({len(pa - pn)}):** {lista(sorted(pa - pn))}",
         f"- **Tablas con otro número de filas:** {len(filas)}", ""]
    if filas:
        L += ["| Tabla | Antes | Ahora |", "|---|--:|--:|"] + [f"| `{k}` | {x} | {y} |" for k, x, y in filas[:15]]
    return L


def informe(m, version, nombre_portal, anterior):
    ctx, k = m["ctx"], m["kpi"]
    op = [t for t in m["tablas"].values() if t["k"] in "rp" and not t["particion"]]
    L = [f"# Informe de la extracción · Portal de Datos ESAP {version}", "",
         "| | |", "|---|---|", f"| Base | `{ctx['db']}` |", f"| Servidor | `{ctx['srv']}:{ctx['puerto']}` |", f"| Motor | {ctx['version']} |",
         f"| Usuario de extracción | `{ctx['usuario']}` |", f"| Fecha de extracción | {ctx['fecha'].replace('T', ' ')} |",
         f"| Portal generado | `portal/{nombre_portal}` · {datetime.datetime.now():%Y-%m-%d %H:%M} |", "",
         "## Cifras", "",
         f"- Esquemas: {len(m['esquemas'])} · tablas: {len(op)} ({sum(1 for t in op if t['apoyo'])} de apoyo) · vistas: {sum(1 for t in m['tablas'].values() if t['k'] in 'vm')}",
         f"- Columnas: {sum(len(t['cols']) for t in op)} · FK: {len(m['fks'])} · relaciones implícitas: {len(m['implicitas'])}",
         f"- Funciones y procedimientos: {len(m['programables'])} · triggers: {len(m['triggers'])} · tipos enumerados: {len(m['tipos'])}",
         f"- Filas totales: {sum(t['filas'] or 0 for t in op):,}".replace(",", "."),
         f"- Tablas y columnas con descripción registrada: {sum(1 for t in op if t['d'])} de {len(op)} tablas · "
         f"{sum(1 for t in op for c in t['cols'] if c['d'])} de {sum(len(t['cols']) for t in op)} columnas"]
    if anterior:
        L += comparar(m, anterior)
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extraccion", required=True)
    ap.add_argument("--version", default="v1.0")
    ap.add_argument("--entorno", default="QA")
    ap.add_argument("--repo", default="", help="URL del repositorio con el detalle técnico (se cita en el portal)")
    ap.add_argument("--anterior", help="extracción anterior para listar cambios en el informe")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()

    ext = os.path.abspath(a.extraccion)
    try:
        m = M.construir(ext)
    except M.ErrorExtraccion as e:
        sys.exit(f"No se generó el portal: {e}")

    nombre = f"Portal_de_Datos_ESAP_{a.version}.html"
    nombre_int = f"Portal_de_Datos_ESAP_{a.version}_interno.html"
    base = {k: m[k] for k in ("ctx", "esquemas", "tablas", "fks", "implicitas", "programables", "triggers", "tipos")}
    base["vistas"] = [{"v": v["v"], "usa": v["usa"]} for v in m["vistas"]]
    base.update({"version": a.version, "entorno": a.entorno, "repo": a.repo, "generado": f"{datetime.datetime.now():%Y-%m-%d %H:%M}"})
    interna = dict(base, edicion="interna", identidad=m["identidad"], kpi=m["kpi"])
    # La edición para el cliente no lleva diagnóstico: ni indicadores con meta, ni identidad, ni conteos de valores sin padre.
    cliente = dict(base, edicion="cliente", identidad=[], kpi=[],
                   fks=[{k: v for k, v in f.items() if k not in ("huerf", "indexada", "validada")} for f in m["fks"]])
    texto_inf = informe(m, a.version, nombre, os.path.abspath(a.anterior) if a.anterior else None)
    print(texto_inf[:3000])
    if a.simular:
        print("Simulación: no se escribió nada.")
        return

    plantilla = open(PLANTILLA, encoding="utf-8").read()
    if plantilla.count("/*__DATOS__*/") != 1:
        sys.exit("La plantilla no tiene exactamente un marcador /*__DATOS__*/")
    for datos, carpeta, archivo in ((cliente, "portal", nombre), (interna, "interno", nombre_int)):
        carga = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        html = plantilla.replace("/*__DATOS__*/", carga).replace("__VERSION__", a.version)
        destino = os.path.join(RAIZ, carpeta, archivo)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        if os.path.exists(destino):
            print(f"Aviso: {archivo} ya existía y se reemplaza. Para conservar versiones anteriores usa otra --version.")
        open(destino, "w", encoding="utf-8", newline="\n").write(html)
        print(f"Portal {datos['edicion']}: {carpeta}/{archivo} ({len(html) / 1048576:.2f} MB)")

    generar_csv(m, os.path.join(RAIZ, "docs", "csv"))
    generar_csv_interno(m, os.path.join(RAIZ, "interno", "csv"))
    generar_md(m, os.path.join(RAIZ, "docs", "catalogo"), nombre)
    ruta_inf = os.path.join(RAIZ, "docs", f"informe_extraccion_{a.version}.md")
    open(ruta_inf, "w", encoding="utf-8").write(texto_inf)
    print("Detalle: docs/csv/, docs/catalogo/ y", os.path.relpath(ruta_inf, RAIZ), "· uso interno: interno/csv/")


if __name__ == "__main__":
    main()
