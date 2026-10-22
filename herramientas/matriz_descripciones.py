# -*- coding: utf-8 -*-
r"""
Matriz de validación de descripciones de columnas (Excel) para revisar con el equipo de desarrollo.

Incluye las columnas sin descripción registrada en la base ni validada: las que tienen una propuesta por regla
(config/propuestas/<id>_columnas.csv) y las que estaban por documentar, con la propuesta semántica de
config/propuestas/<id>_semanticas.csv. Para cada una muestra el tipo de dato, las restricciones, los valores
permitidos (CHECK o tipo enumerado), si apunta a un catálogo y en qué lógica de la base se usa (funciones,
procedimientos, triggers, vistas, índices). No usa valores de los registros.

Uso:
  python herramientas/matriz_descripciones.py contexto --extraccion extracciones/2026-10-22 --alcance config/alcances/fase2.json
      -> config/propuestas/<id>_contexto.jsonl  (insumo para redactar las propuestas semánticas)
  python herramientas/matriz_descripciones.py matriz --extraccion extracciones/2026-10-22 --alcance config/alcances/fase2.json
      -> config/propuestas/Matriz_Validacion_Descripciones_<Id>.xlsx
  python herramientas/matriz_descripciones.py incorporar --matriz config/propuestas/Matriz_Validacion_Descripciones_<Id>.xlsx
      -> lleva a config/descripciones.csv las filas con decisión «Aprobada» o «Aprobada con ajuste» (estado validada)
  python herramientas/matriz_descripciones.py incorporar --tablas config/propuestas/<id>_tablas.csv
      -> lo mismo para las descripciones de tabla (decisión «Aprobada»)
"""
import argparse
import csv
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402

CATALOGO = re.compile(r"^(Sub)?Tipos?|^Estados?|^TipoEstado|^tipos?_|^estados?_|^cat_|^catalogo|_tipos?$|_estados?$|^config_|^parametros?_", re.I)
DECISIONES = ["Pendiente", "Aprobada", "Aprobada con ajuste", "Rechazada", "Requiere aclaración"]


def palabra(col):
    return re.compile(r'(?<![\w"])"?' + re.escape(col) + r'"?(?![\w"])', re.I)


def es_catalogo(m, k):
    t = m["tablas"].get(k) or m.get("contexto", {}).get(k)
    if not t:
        return False
    return bool(CATALOGO.search(t["t"])) or (not t["fk_out"] and len(t["cols"]) <= 6)


def valores_check(defn, col):
    # solo CHECK que restringen la propia columna: (col)::text = ANY (ARRAY['a'::text, …])  o  col IN ('a', …)
    c = r'\(*"?' + re.escape(col) + r'"?\)*(?:::[\w ]+)?\)*'
    m = re.search(c + r"\s*=\s*ANY\s*\(+\s*ARRAY\[(.*?)\]", defn, re.I) or re.search(c + r"\s+IN\s*\((.*?)\)", defn, re.I)
    if not m:
        return []
    return [v.replace("''", "'") for v in re.findall(r"'((?:[^']|'')*)'", m.group(1))]


def contexto(ext, alcance):
    m = M.aplicar_alcance(M.construir(ext), alcance)
    fuentes = {(r["s"], r["n"]): r.get("src") or "" for r in M.leer_jsonl(ext, "06_programables")}
    tipos = {f'{t["s"]}.{t["n"]}': t["vals"] for t in m["tipos"]}
    tipos.update({t["n"]: t["vals"] for t in m["tipos"]})
    fk_col = {}
    for f in m["fks"]:
        for c, pc in zip(f["cols"], f["pcols"]):
            fk_col[(f["c"], c)] = (f["p"], pc)
    sufijo = alcance["id"].lower() if alcance else "completa"
    hoja = {}
    ruta_hoja = os.path.join(M.CONFIG, "propuestas", f"{sufijo}_columnas.csv")
    if os.path.isfile(ruta_hoja):
        with open(ruta_hoja, encoding="utf-8-sig", newline="") as f:
            hoja = {(r["esquema"], r["tabla"], r["columna"]): r for r in csv.DictReader(f, delimiter=";")}
    filas = []
    for k, t in m["tablas"].items():
        if t["k"] not in "rp" or t["particion"]:
            continue
        nombre_t = re.compile(r'(?<![\w])"?' + re.escape(t["t"]) + r'"?(?![\w])', re.I)
        progs = [p for p in m["programables"] if nombre_t.search(fuentes.get((p["s"], p["n"]), ""))]
        vistas = [v for v in m["vistas"] if k in (v.get("usa") or []) or nombre_t.search(v.get("def") or "")]
        for c in t["cols"]:
            if c["de"] in ("base", "validada"):
                continue
            pal = palabra(c["n"])
            uso = []
            for p in progs:
                src = fuentes.get((p["s"], p["n"]), "")
                lineas = [x.strip() for x in src.splitlines() if pal.search(x)]
                if lineas:
                    uso.append({"obj": f'{p["s"]}.{p["n"]}', "tipo": p["tipo"], "lineas": lineas[:3]})
            trg = [g["n"] for g in t["trg"] if pal.search(g["def"].split(" ON ")[0])]
            vis = [f'{v["v"]}' if "." in v["v"] else v["v"] for v in vistas if pal.search(v["def"] or "")]
            idx = [i["n"] for i in t["idx"] if c["n"] in i["cols"] and not i["pk"]]
            checks = [x["def"] for x in t["ck"] if pal.search(x["def"])]
            vals = sorted({v for x in checks for v in valores_check(x, c["n"])})
            ty_base = c["ty"].split("(")[0].replace('"', "")
            enum = tipos.get(ty_base) or tipos.get(ty_base.split(".")[-1])
            ref = fk_col.get((k, c["n"]))
            filas.append({
                "esquema": t["s"], "tabla": t["t"], "desc_tabla": t["d"], "filas_tabla": t["filas"], "columna": c["n"], "tipo": c["ty"],
                "nulo": c["nul"], "defecto": c["def"], "pk": c["pk"], "unica": bool(c["uq"]),
                "fk": f"{ref[0]}.{ref[1]}" if ref else "", "fk_catalogo": bool(ref and es_catalogo(m, ref[0])),
                "tabla_catalogo": es_catalogo(m, k), "check": checks, "valores": vals or (enum or []), "enum": bool(enum),
                "uso_programables": uso, "triggers": trg, "vistas": vis, "indices": idx,
                "propuesta_regla": c["d"] if c["de"] == "propuesta" else (h["descripcion"] if (h := hoja.get((t["s"], t["t"], c["n"]))) and h["estado"] == "propuesta" else ""),
                "regla": (hoja.get((t["s"], t["t"], c["n"])) or {}).get("regla", ""), "estado": c["de"] or "por documentar",
                "columnas_tabla": [x["n"] for x in t["cols"]],
            })
    return m, filas


def cmd_contexto(a):
    alcance = M.cargar_alcance(a.alcance)
    _, filas = contexto(os.path.abspath(a.extraccion), alcance)
    sufijo = alcance["id"].lower() if alcance else "completa"
    destino = os.path.join(M.CONFIG, "propuestas", f"{sufijo}_contexto.jsonl")
    with open(destino, "w", encoding="utf-8") as f:
        for r in filas:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{os.path.relpath(destino, M.RAIZ)}: {len(filas)} columnas "
          f"({sum(1 for r in filas if r['propuesta_regla'])} con propuesta por regla, {sum(1 for r in filas if not r['propuesta_regla'])} por documentar)")


def texto_evidencia(x):
    if not x:
        return ""
    partes = []
    for e in x["evidencias"]:
        t = e.get("comentario") or e.get("comment_typeorm")
        if t:
            partes.append(f'{e["fuente"].replace("backend/", "")}: {t[:300]}')
    ent = next((e for e in x["evidencias"] if e["tipo"] == "entidad"), None)
    if ent:
        if not partes:
            partes.append(f'Mapeada en {ent["fuente"].replace("backend/", "")} ({ent["entidad"]}.{ent["propiedad"]})')
        if ent.get("enum"):
            partes.append("Enum: " + ", ".join(ent["enum"]))
    vals = sorted(set(x.get("validaciones_dto") or []) | {v for e in x["evidencias"] for v in e.get("validaciones", [])})
    if vals:
        partes.append("Validación: " + ", ".join(vals[:6]))
    return " | ".join(partes)


def leer_semanticas(sufijo, tipo="semanticas"):
    ruta = os.path.join(M.CONFIG, "propuestas", f"{sufijo}_{tipo}.csv")
    if not os.path.isfile(ruta):
        return {}
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return {(r["esquema"], r["tabla"], r["columna"]): r for r in csv.DictReader(f, delimiter=";")}


def texto_uso(r):
    partes = []
    for u in r["uso_programables"]:
        partes.append(f'{u["tipo"]} {u["obj"]}')
    partes += [f"Trigger {x}" for x in r["triggers"]] + [f"Vista {x}" for x in r["vistas"]]
    return "; ".join(partes)


def cmd_matriz(a):
    from openpyxl import Workbook
    from openpyxl.formatting.rule import CellIsRule, FormulaRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    alcance = M.cargar_alcance(a.alcance)
    m, filas = contexto(os.path.abspath(a.extraccion), alcance)
    sufijo = alcance["id"].lower() if alcance else "completa"
    etiqueta = alcance["nombre"] if alcance else "Base completa"
    if not filas:
        print(f"No hay columnas pendientes de descripción en {etiqueta}: no se genera la matriz (se conserva la anterior, si existe).")
        return
    sem = leer_semanticas(sufijo)
    cod = leer_semanticas(sufijo, "codigo")        # propuestas afinadas con el código de la aplicación
    aju = leer_semanticas(sufijo, "ajustes")       # propuestas reescritas o verificadas contra el código (tienen prioridad)
    dec = leer_semanticas(sufijo, "decisiones")    # decisiones ya tomadas (aprobaciones en bloque); se precargan en la matriz
    evid = {}
    ruta_ev = os.path.join(M.CONFIG, "propuestas", f"{sufijo}_evidencia_codigo.jsonl")
    if os.path.isfile(ruta_ev):
        for linea in open(ruta_ev, encoding="utf-8"):
            x = json.loads(linea)
            evid[(x["esquema"], x["tabla"], x["columna"])] = x
    dominios = {e["s"]: e["nombre"] for e in m["esquemas"]}
    cols_todas = [c for t in m["tablas"].values() if t["k"] in "rp" and not t["particion"] for c in t["cols"]]
    total_cols = len(cols_todas)
    base = sum(1 for c in cols_todas if c["de"] == "base")
    validadas = sum(1 for c in cols_todas if c["de"] == "validada")

    F = "Arial"
    fino = Side(style="thin", color="D0D5DD")
    borde = Border(left=fino, right=fino, top=fino, bottom=fino)
    cab = PatternFill("solid", fgColor="1F3A5F")
    cab_rev = PatternFill("solid", fgColor="7A4E00")
    editable = PatternFill("solid", fgColor="FFF7D6")
    ajuste = Alignment(wrap_text=True, vertical="top")

    wb = Workbook()
    # ---------------- Instrucciones
    ins = wb.active
    ins.title = "Instrucciones"
    ins.sheet_view.showGridLines = False
    lineas = [
        (f"Matriz de validación de descripciones de columnas · SuperApp ESAP · {etiqueta}", Font(name=F, bold=True, size=14, color="1F3A5F")),
        (f"Base {m['ctx']['db']} (QA) · extracción del {m['ctx']['fecha'][:10]} · generada el {datetime.date.today():%Y-%m-%d}", Font(name=F, size=10, color="555555")),
        ("", None),
        ("Objetivo", Font(name=F, bold=True, size=11)),
        ("Revisar con el equipo de desarrollo la descripción de cada columna que aún no tiene descripción registrada en la base ni validada.", Font(name=F, size=10)),
        ("Las propuestas se redactaron a partir de la estructura (nombre, tipo, restricciones, valores permitidos, relaciones) y del código de las "
         "funciones, triggers y vistas que usan la columna, y del código fuente de la aplicación (entidades y migraciones). No se revisaron valores de los registros. Son propuestas: no reemplazan el conocimiento del equipo.", Font(name=F, size=10)),
        ("", None),
        ("Cómo revisar (hoja «Matriz»)", Font(name=F, bold=True, size=11)),
        ("1. Lea la propuesta, su fundamento y, si la hay, la pregunta para desarrollo.", Font(name=F, size=10)),
        ("2. Elija la decisión en la lista desplegable (celdas amarillas):", Font(name=F, size=10)),
        ("     Aprobada: la propuesta se registra tal cual.", Font(name=F, size=10)),
        ("     Aprobada con ajuste: escriba el texto correcto en «Descripción final».", Font(name=F, size=10)),
        ("     Rechazada: la propuesta no corresponde; escriba la descripción correcta en «Descripción final» o explique en «Observaciones».", Font(name=F, size=10)),
        ("     Requiere aclaración: falta información; anote la duda en «Observaciones».", Font(name=F, size=10)),
        ("3. Registre quién revisó y la fecha. «Descripción a registrar» se calcula sola.", Font(name=F, size=10)),
        ("     Ejemplo: Decisión = Aprobada con ajuste · Descripción final = «Valor de los viáticos de la comisión, en pesos colombianos, "
         "calculado como la suma de días pernoctados y no pernoctados.» · Revisado por = Equipo Viáticos · Fecha de revisión = 2026-10-23.", Font(name=F, size=10, italic=True)),
        ("4. La hoja «Métricas» muestra el avance por dominio, por confianza y por uso en la lógica.", Font(name=F, size=10)),
        ("Las decisiones que ya vienen diligenciadas salen de config/propuestas/<alcance>_decisiones.csv (por ejemplo, aprobaciones en bloque); se pueden cambiar en la matriz.", Font(name=F, size=10)),
        ("", None),
        ("Columnas de la matriz", Font(name=F, bold=True, size=11)),
        ("Confianza: Alta (el nombre, el tipo y la lógica coinciden) · Media (el nombre es claro pero falta confirmar el uso) · Baja (el nombre es ambiguo; revisar con prioridad).", Font(name=F, size=10)),
        ("Origen: «Código fuente (verificado)» (contrastada con entidades, servicios y migraciones), «Regla estructural (redacción revisada)», «Código fuente» (redactada a partir del comentario del desarrollador en la entidad o la migración), «Regla estructural» (convención de nombre) "
         "o «Propuesta semántica» (redactada a partir del contexto de la base).", Font(name=F, size=10)),
        ("Evidencia en código: archivo y línea del repositorio de la aplicación (rama micro-frontend) donde se define la columna, con el comentario del "
         "desarrollador, los valores del enum y las validaciones declaradas.", Font(name=F, size=10)),
        ("Uso en lógica: funciones, procedimientos, triggers y vistas de la base que mencionan la columna. La lógica de la aplicación se resume en «Evidencia en código».", Font(name=F, size=10)),
        ("Catálogo: la columna apunta a una tabla de catálogo, tiene valores permitidos (CHECK o tipo enumerado) o pertenece a una tabla de catálogo.", Font(name=F, size=10)),
        ("", None),
        ("Después de la revisión", Font(name=F, bold=True, size=11)),
        ("python herramientas/matriz_descripciones.py incorporar --matriz <este archivo>  → lleva las aprobadas a config/descripciones.csv (estado validada).", Font(name="Consolas", size=9)),
        ("Las validadas se publican en el portal y quedan listas para registrarse en la base con un lote COMMENT ON (con reversa), cuando haya autorización.", Font(name=F, size=10)),
    ]
    for i, (txt, fnt) in enumerate(lineas, 1):
        c = ins.cell(row=i, column=1, value=txt)
        if fnt:
            c.font = fnt
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ins.column_dimensions["A"].width = 150

    # ---------------- Matriz
    ws = wb.create_sheet("Matriz")
    enc = ["ID", "Dominio", "Esquema", "Tabla", "Filas en QA", "Columna", "Tipo de dato", "Admite nulos", "Restricciones",
           "Valores permitidos", "Referencia (FK)", "Catálogo", "Uso en lógica", "Detalle del uso", "Índices", "Evidencia en código",
           "Origen", "Propuesta de descripción", "Confianza", "Fundamento", "Pregunta para desarrollo",
           "Decisión", "Descripción final", "Revisado por", "Fecha de revisión", "Observaciones", "Descripción a registrar"]
    anchos = [9, 18, 18, 24, 9, 24, 18, 8, 16, 26, 26, 9, 9, 40, 18, 50, 13, 46, 10, 34, 34, 18, 40, 16, 12, 30, 40]
    ws.append(enc)
    for i, w in enumerate(anchos, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
        h = ws.cell(row=1, column=i)
        h.font = Font(name=F, bold=True, color="FFFFFF", size=10)
        h.fill = cab_rev if i >= 22 else cab
        h.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        h.border = borde
    ws.row_dimensions[1].height = 34
    orden = {s: i for i, s in enumerate((alcance or {}).get("orden") or [e["s"] for e in m["esquemas"]])}
    filas.sort(key=lambda r: (orden.get(r["esquema"], 99), r["tabla"].lower(), r["columnas_tabla"].index(r["columna"])))
    sin_sem = 0
    for n, r in enumerate(filas, 2):
        clave = (r["esquema"], r["tabla"], r["columna"])
        s = sem.get(clave, {})
        if clave in aju:
            s = aju[clave]
            origen, prop, conf, fund = s["origen"], s["propuesta"], s["confianza"], s["fundamento"]
        elif clave in cod:
            s = cod[clave]
            origen, prop, conf, fund = "Código fuente", s["propuesta"], s["confianza"], s["fundamento"]
        elif r["propuesta_regla"]:
            origen, prop = "Regla estructural", r["propuesta_regla"]
            conf = s.get("confianza") or "Media"
            fund = s.get("fundamento") or "Convención de nombre de la columna."
        else:
            origen, prop = "Propuesta semántica", s.get("propuesta", "")
            conf, fund = s.get("confianza", ""), s.get("fundamento", "")
            if not prop:
                sin_sem += 1
        restr = ", ".join(x for x in ["PK" if r["pk"] else "", "FK" if r["fk"] else "", "Única" if r["unica"] else "",
                                       "CHECK" if r["check"] else "", "Enumerado" if r["enum"] else ""] if x)
        catal = r["fk_catalogo"] or r["tabla_catalogo"] or bool(r["valores"])
        uso = texto_uso(r)
        detalle = " | ".join(f'{u["obj"]}: {u["lineas"][0][:120]}' for u in r["uso_programables"][:3])
        valores = ", ".join(r["valores"][:15]) + (" …" if len(r["valores"]) > 15 else "")
        ev_txt = texto_evidencia(evid.get(clave))
        fila = [f"C{n - 1:04d}", dominios.get(r["esquema"], r["esquema"]), r["esquema"], r["tabla"], r["filas_tabla"], r["columna"], r["tipo"],
                "Sí" if r["nulo"] else "No", restr, valores, r["fk"], "Sí" if catal else "No", "Sí" if uso else "No",
                (uso + (" — " + detalle if detalle else "")) if uso else "", ", ".join(r["indices"]), ev_txt,
                origen, prop, conf, fund, s.get("pregunta", ""),
                (d := dec.get(clave, {})).get("decision") or "Pendiente", d.get("descripcion_final", ""), d.get("revisado_por", ""),
                datetime.date.fromisoformat(d["fecha"]) if d.get("fecha") else None, d.get("observaciones", ""),
                f'=IF(OR(V{n}="Aprobada"),R{n},IF(AND(OR(V{n}="Aprobada con ajuste",V{n}="Rechazada"),W{n}<>""),W{n},""))']
        ws.append(fila)
        for i in range(1, len(enc) + 1):
            c = ws.cell(row=n, column=i)
            c.font = Font(name=F, size=9)
            c.alignment = ajuste
            c.border = borde
            if 22 <= i <= 26:
                c.fill = editable
        ws.cell(row=n, column=25).number_format = "yyyy-mm-dd"
    ult = len(filas) + 1
    ws.freeze_panes = "G2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(enc))}{ult}"
    dv = DataValidation(type="list", formula1='"' + ",".join(DECISIONES) + '"', allow_blank=False, showDropDown=False,
                        errorTitle="Decisión", error="Elija un valor de la lista.", promptTitle="Decisión", prompt="Elija la decisión de la revisión")
    ws.add_data_validation(dv)
    dv.add(f"V2:V{ult}")
    dvf = DataValidation(type="date", operator="greaterThan", formula1="DATE(2026,1,1)", allow_blank=True,
                         error="Escriba una fecha (aaaa-mm-dd).", errorTitle="Fecha")
    ws.add_data_validation(dvf)
    dvf.add(f"Y2:Y{ult}")
    colores = {"Aprobada": "D1FADF", "Aprobada con ajuste": "D1E9FF", "Rechazada": "FEE4E2", "Requiere aclaración": "FEF0C7"}
    for k, col in colores.items():
        ws.conditional_formatting.add(f"V2:V{ult}", CellIsRule(operator="equal", formula=[f'"{k}"'], fill=PatternFill("solid", fgColor=col)))
    ws.conditional_formatting.add(f"S2:S{ult}", CellIsRule(operator="equal", formula=['"Baja"'], font=Font(name=F, size=9, bold=True, color="B42318")))
    # ajuste sin texto: se marca para completar
    ws.conditional_formatting.add(f"W2:W{ult}", FormulaRule(formula=[f'AND(OR($V2="Aprobada con ajuste",$V2="Rechazada"),$W2="")'],
                                                             fill=PatternFill("solid", fgColor="FDA29B")))

    # ---------------- Métricas
    mt = wb.create_sheet("Métricas")
    mt.sheet_view.showGridLines = False
    R = f"Matriz!$V$2:$V${ult}"
    rng = lambda col: f"Matriz!${col}$2:${col}${ult}"
    titulo = lambda c, t: (mt.cell(row=c, column=1, value=t).__setattr__("font", Font(name=F, bold=True, size=12, color="1F3A5F")))
    mt.cell(row=1, column=1, value=f"Métricas de la revisión · {etiqueta}").font = Font(name=F, bold=True, size=14, color="1F3A5F")

    def tabla_m(fila0, cab_, filas_):
        for j, h in enumerate(cab_, 1):
            c = mt.cell(row=fila0, column=j, value=h)
            c.font = Font(name=F, bold=True, color="FFFFFF", size=10)
            c.fill = cab
            c.border = borde
            c.alignment = Alignment(horizontal="center", wrap_text=True)
        for i, fila in enumerate(filas_, fila0 + 1):
            for j, v in enumerate(fila, 1):
                c = mt.cell(row=i, column=j, value=v)
                c.font = Font(name=F, size=10, bold=(fila[0] == "Total"))
                c.border = borde
                if isinstance(v, str) and v.startswith("=") and "/" in v:
                    c.number_format = "0.0%"
        return fila0 + len(filas_) + 2

    # 1. avance general
    titulo(3, "Avance general")
    f0 = 4
    filas_av = [["Columnas en la matriz", f"=COUNTA({rng('A')})"]]
    for d in DECISIONES:
        filas_av.append([d, f'=COUNTIF({R},"{d}")'])
    filas_av.append(["Revisadas (decisión distinta de Pendiente)", f'=B5-B6'])
    filas_av.append(["% revisado", "=IF(B5=0,0,B11/B5)"])
    filas_av.append(["Con descripción a registrar", f'=SUMPRODUCT(--({rng("AA")}<>""))'])
    filas_av.append(["Ajustes sin texto en «Descripción final»", f'=SUMPRODUCT((({R}="Aprobada con ajuste")+({R}="Rechazada"))*({rng("W")}=""))'])
    sig = tabla_m(f0, ["Indicador", "Valor"], filas_av)
    # 2. indicador de cobertura
    titulo(sig, "Cobertura de descripciones de columnas (indicador K02, meta ≥ 95 %)")
    k0 = sig + 1
    filas_k = [["Columnas del alcance", total_cols],
               ["Con descripción registrada en la base (COMMENT)", base],
               ["Validadas antes de esta matriz (config/descripciones.csv)", validadas],
               ["Con descripción a registrar en esta matriz", "=B13"],
               ["Cobertura actual", f"=(B{k0 + 2}+B{k0 + 3})/B{k0 + 1}"],
               ["Cobertura al incorporar la matriz", f"=(B{k0 + 2}+B{k0 + 3}+B{k0 + 4})/B{k0 + 1}"],
               ["Columnas que faltan para la meta de 95 %", f"=MAX(0,ROUNDUP(0.95*B{k0 + 1},0)-(B{k0 + 2}+B{k0 + 3}+B{k0 + 4}))"]]
    sig = tabla_m(k0, ["Concepto", "Valor"], filas_k)
    nota = mt.cell(row=sig - 1, column=1, value=f"Columnas del alcance, base y validadas: cifras fijas de la extracción del {m['ctx']['fecha'][:10]} y de config/descripciones.csv.")
    nota.font = Font(name=F, size=8, italic=True, color="666666")
    sig += 1
    # 3. por dominio
    titulo(sig, "Avance por dominio")
    doms = sorted({r["esquema"] for r in filas}, key=lambda s: orden.get(s, 99))
    D = rng("C")
    filas_d = []
    for s in doms:
        i = sig + 2 + len(filas_d)
        filas_d.append([dominios.get(s, s), s, f'=COUNTIF({D},B{i})', f'=COUNTIFS({D},B{i},{R},"Aprobada")+COUNTIFS({D},B{i},{R},"Aprobada con ajuste")',
                        f'=COUNTIFS({D},B{i},{R},"Rechazada")', f'=COUNTIFS({D},B{i},{R},"Requiere aclaración")',
                        f'=COUNTIFS({D},B{i},{R},"Pendiente")', f"=IF(C{i}=0,0,(C{i}-G{i})/C{i})"])
    a0, a1 = sig + 2, sig + 1 + len(filas_d)
    filas_d.append(["Total", "", f"=SUM(C{a0}:C{a1})", f"=SUM(D{a0}:D{a1})", f"=SUM(E{a0}:E{a1})", f"=SUM(F{a0}:F{a1})", f"=SUM(G{a0}:G{a1})",
                    f"=IF(C{a1 + 1}=0,0,(C{a1 + 1}-G{a1 + 1})/C{a1 + 1})"])
    sig = tabla_m(sig + 1, ["Dominio", "Esquema", "Columnas", "Aprobadas", "Rechazadas", "Por aclarar", "Pendientes", "% revisado"], filas_d)
    # 4. por confianza y origen
    titulo(sig, "Avance por confianza y origen de la propuesta")
    filas_c = []
    for etiqueta_c, col, val in [("Confianza Alta", "S", "Alta"), ("Confianza Media", "S", "Media"), ("Confianza Baja", "S", "Baja"),
                                 ("Origen: Código fuente", "Q", "Código fuente"), ("Origen: Regla estructural", "Q", "Regla estructural"),
                                 ("Origen: Propuesta semántica", "Q", "Propuesta semántica"), ("Con evidencia en código", "P", "?*"),
                                 ("Usadas en lógica de la base", "M", "Sí"), ("Relacionadas con catálogo", "L", "Sí")]:
        i = sig + 2 + len(filas_c)
        filas_c.append([etiqueta_c, f'=COUNTIF({rng(col)},"{val}")',
                        f'=COUNTIFS({rng(col)},"{val}",{R},"Aprobada")+COUNTIFS({rng(col)},"{val}",{R},"Aprobada con ajuste")',
                        f'=COUNTIFS({rng(col)},"{val}",{R},"Pendiente")', f"=IF(B{i}=0,0,(B{i}-D{i})/B{i})"])
    sig = tabla_m(sig + 1, ["Grupo", "Columnas", "Aprobadas", "Pendientes", "% revisado"], filas_c)
    for col, w in zip("ABCDEFGH", [52, 22, 12, 12, 12, 12, 12, 12]):
        mt.column_dimensions[col].width = w

    # ---------------- Lógica de la base (detalle del uso)
    lg = wb.create_sheet("Uso en lógica")
    lg.append(["Esquema", "Tabla", "Columna", "Objeto", "Tipo de objeto", "Líneas donde aparece la columna"])
    for r in filas:
        for u in r["uso_programables"]:
            lg.append([r["esquema"], r["tabla"], r["columna"], u["obj"], u["tipo"], "\n".join(u["lineas"])])
        for x in r["triggers"]:
            lg.append([r["esquema"], r["tabla"], r["columna"], x, "Trigger (UPDATE OF)", ""])
        for x in r["vistas"]:
            lg.append([r["esquema"], r["tabla"], r["columna"], x, "Vista", ""])
    for i, w in enumerate([18, 26, 26, 44, 16, 90], 1):
        lg.column_dimensions[get_column_letter(i)].width = w
        lg.cell(row=1, column=i).font = Font(name=F, bold=True, color="FFFFFF", size=10)
        lg.cell(row=1, column=i).fill = cab
    for row in lg.iter_rows(min_row=2):
        for c in row:
            c.font = Font(name=F, size=9)
            c.alignment = ajuste
    lg.freeze_panes = "A2"
    lg.auto_filter.ref = f"A1:F{lg.max_row}"

    wb.move_sheet("Métricas", offset=-1)
    destino = a.salida or os.path.join(M.CONFIG, "propuestas", f"Matriz_Validacion_Descripciones_{alcance['id'] if alcance else 'Completa'}.xlsx")
    wb.save(destino)
    print(f"{os.path.relpath(destino, M.RAIZ)}: {len(filas)} columnas · {sum(1 for r in filas if texto_uso(r))} usadas en lógica · "
          f"sin propuesta semántica: {sin_sem}")


def cmd_incorporar(a):
    from openpyxl import load_workbook
    nuevas = []
    if a.tablas:   # hoja de descripciones de tabla (config/propuestas/<id>_tablas.csv): las de decisión «Aprobada»
        with open(a.tablas, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f, delimiter=";"):
                texto = (r.get("descripcion_final") or "").strip() or (r.get("propuesta") or "").strip()
                if (r.get("decision") or "").strip() in ("Aprobada", "Aprobada con ajuste") and texto:
                    nuevas.append({"esquema": r["esquema"], "tabla": r["tabla"], "columna": "", "descripcion": texto, "estado": "validada"})
    filas = load_workbook(a.matriz)["Matriz"].iter_rows(values_only=True) if a.matriz else iter([])
    enc = list(next(filas, []))   # se leen los valores escritos, no fórmulas
    ix = {h: i for i, h in enumerate(enc)}
    for row in filas:
        dec = (row[ix["Decisión"]] or "").strip()
        final = (row[ix["Descripción final"]] or "").strip()
        prop = (row[ix["Propuesta de descripción"]] or "").strip()
        texto = prop if dec == "Aprobada" else (final if dec in ("Aprobada con ajuste", "Rechazada") else "")
        if texto:
            nuevas.append({"esquema": row[ix["Esquema"]], "tabla": row[ix["Tabla"]], "columna": row[ix["Columna"]], "descripcion": texto, "estado": "validada"})
    actuales = M.leer_csv("descripciones.csv")
    clave = lambda r: (r["esquema"], r["tabla"], r.get("columna") or "")
    por = {clave(r): r for r in actuales}
    antes = len(por)
    for r in nuevas:
        por[clave(r)] = r
    with open(os.path.join(M.CONFIG, "descripciones.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, ["esquema", "tabla", "columna", "descripcion", "estado"], delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(por.values(), key=clave))
    print(f"config/descripciones.csv: {len(nuevas)} descripciones validadas desde la matriz y la hoja de tablas · {len(por) - antes} nuevas · {len(por)} en total")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("accion", choices=["contexto", "matriz", "incorporar"])
    ap.add_argument("--extraccion")
    ap.add_argument("--alcance")
    ap.add_argument("--matriz")
    ap.add_argument("--tablas", help="incorporar: hoja de descripciones de tabla (config/propuestas/<id>_tablas.csv)")
    ap.add_argument("--salida")
    a = ap.parse_args()
    {"contexto": cmd_contexto, "matriz": cmd_matriz, "incorporar": cmd_incorporar}[a.accion](a)


if __name__ == "__main__":
    main()
