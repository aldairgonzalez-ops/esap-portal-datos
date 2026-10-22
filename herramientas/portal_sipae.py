# -*- coding: utf-8 -*-
"""
Portal de Datos ESAP sobre la interfaz del Portal de Datos SIPAE v2.3 (UAPA).

Toma herramientas/plantilla_sipae/portal_base.html (la interfaz SIPAE sin datos, ver preparar_plantilla_sipae.py)
y le inyecta el catálogo de ESAP en los mismos bloques y con la misma forma que producían los generadores de la UAPA:
  db-json   fichas de tablas y de programables
  sm-json   Modelo ER: dominios, tablas, FK con estado y cardinalidad
  rel-json  relaciones lógicas validadas con datos y cardinalidad medida
  pii-json  (nuevo) clasificación de datos personales de ESAP, que reemplaza las reglas por nombre de SIPAE
Además reemplaza los textos y las reglas propias de SIPAE / SQL Server. Cada reemplazo debe encontrarse
exactamente una vez (o las veces indicadas); si la plantilla cambia, el generador se detiene en lugar de
producir un portal a medias.
"""
import collections
import html as H
import json
import os
import re

import modelo as M

PLANTILLA = os.path.join(M.RAIZ, "herramientas", "plantilla_sipae", "portal_base.html")

TIPO_PROG = {"p": "Stored Procedure", "a": "Funcion Agregada", "w": "Funcion de Ventana"}
# Misma idea que REGLAS_VERBO de Generar_Portal_v2_3.py, con verbos en español e inglés de ESAP. El orden importa.
REGLAS_VERBO = [
    ("Notificación", r"notific|alerta|correo|mail|outbox|recordatorio"),
    ("Validación", r"validar|validacion|verificar|confirmar|validate|check"),
    ("Carga", r"cargue|carga(?!r)|importar|import|sincroniz|sync|migrar"),
    ("Alta", r"(add|insert|create|crear|registrar|guardar|agregar|generar|emitir|issue)(_|$|[A-Z])|(add|insert)$"),
    ("Baja", r"(delete|eliminar|borrar|remove|anular|purge|limpiar)"),
    ("Cambio", r"(update|actualizar|modificar|cambiar|editar|set_|asignar|vincular|configurar|recalcular|calcular)"),
    ("Consulta", r"(get|consulta|listar|buscar|obtener|select|search|filter|resumen|vw_|stats|reporte)"),
]


def verbo(nombre, escribe):
    for v, patron in REGLAS_VERBO:
        if re.search(patron, nombre, re.I):
            return v
    return "Cambio" if escribe else "Otro"


def tipo_funcion(p):
    if p["k"] in TIPO_PROG:
        return TIPO_PROG[p["k"]]
    ret = (p.get("ret") or "").lower()
    if ret == "trigger":
        return "Funcion de Trigger"
    if ret.startswith("setof") or ret.startswith("table"):
        return "Funcion de Tabla"
    return "Funcion Escalar"


def parametros(args):
    """'p_email text, OUT total integer' -> [[nombre, tipo, IN/OUT, '']]"""
    salida, nivel, actual, partes = [], 0, "", []
    for ch in args or "":
        if ch == "(":
            nivel += 1
        elif ch == ")":
            nivel -= 1
        if ch == "," and nivel == 0:
            partes.append(actual)
            actual = ""
        else:
            actual += ch
    if actual.strip():
        partes.append(actual)
    for i, parte in enumerate(partes, 1):
        tokens = parte.strip().split()
        modo = "IN"
        if tokens and tokens[0].upper() in ("IN", "OUT", "INOUT", "VARIADIC"):
            modo = "OUT" if tokens[0].upper() in ("OUT", "INOUT") else "IN"
            tokens = tokens[1:]
        if len(tokens) >= 2:
            nombre, tipo = tokens[0], " ".join(tokens[1:])
        else:
            nombre, tipo = f"${i}", " ".join(tokens)
        salida.append([nombre, tipo, modo, ""])
    return salida


def bloques(m, version, entorno):
    T = {k: t for k, t in m["tablas"].items() if t["k"] in "rpf" and not t["particion"]}
    ctx = m["ctx"]

    # ---- programables (funciones, procedimientos, vistas y triggers), como en el inventario SIPAE v2.2
    procs, usa_tabla = {}, collections.defaultdict(set)
    nombres = collections.Counter(f'{p["s"]}.{p["n"]}' for p in m["programables"])
    clave_de = {}
    for p in m["programables"]:
        k = f'{p["s"]}.{p["n"]}' if nombres[f'{p["s"]}.{p["n"]}'] == 1 else f'{p["s"]}.{p["n"]}({p["args"]})'
        clave_de[f'{p["s"]}.{p["n"]}'] = clave_de.get(f'{p["s"]}.{p["n"]}', k)
        prm = parametros(p["args"])
        procs[k] = {"fullname": k, "schema": p["s"], "name": p["n"] if k.endswith(p["n"]) else k.split(".", 1)[1],
                    "type": tipo_funcion(p), "purpose": p["d"], "tables": p["usa"], "params": prm,
                    "verbo": verbo(p["n"], p["escribe"]), "n_params": len(prm), "n_salida": sum(1 for x in prm if x[2] == "OUT"),
                    "n_tablas": len(p["usa"]), "escribe": p["escribe"], "llama": p["llama"]}
        for t in p["usa"]:
            usa_tabla[t].add(k)
    for v in m["vistas"]:
        t = m["tablas"].get(v["v"], {})
        procs[v["v"]] = {"fullname": v["v"], "schema": t.get("s", v["v"].split(".")[0]), "name": t.get("t", v["v"].split(".", 1)[1]),
                         "type": "Vista", "purpose": t.get("d", ""), "tables": [u for u in v["usa"] if u in T], "params": [],
                         "verbo": "Consulta", "n_params": 0, "n_salida": 0, "n_tablas": len(v["usa"])}
        for u in v["usa"]:
            usa_tabla[u].add(v["v"])
    trg_nombres = collections.Counter(f'{g["tabla"].split(".")[0]}.{g["n"]}' for g in m["triggers"])
    for g in m["triggers"]:
        esquema = g["tabla"].split(".")[0]
        k = f'{esquema}.{g["n"]}' if trg_nombres[f'{esquema}.{g["n"]}'] == 1 else f'{esquema}.{g["n"]} · {g["tabla"].split(".", 1)[1]}'
        fn = clave_de.get(g["fn"], g["fn"])
        procs[k] = {"fullname": k, "schema": esquema, "name": k.split(".", 1)[1], "type": "Trigger",
                    "purpose": f"Trigger {g['estado']} sobre {g['tabla']}: {g['def']}", "tables": [g["tabla"]], "params": [],
                    "verbo": "Cambio", "n_params": 0, "n_salida": 0, "n_tablas": 1, "llama": [fn] if fn in procs else []}
        usa_tabla[g["tabla"]].add(k)
    invocado = collections.defaultdict(set)
    for k, p in procs.items():
        for x in p.get("llama", []):
            invocado[x].add(k)
    for k, xs in invocado.items():
        if k in procs:
            procs[k]["invocado_por"] = sorted(xs)

    # ---- tablas
    fk_col, fk_pares = collections.defaultdict(list), collections.defaultdict(list)
    for f in m["fks"]:
        for a, b in zip(f["cols"], f["pcols"]):
            fk_col[(f["c"], a)].append(f"FK -> {f['p']}({b})")
            fk_pares[f["c"]].append([a, f["p"], b])
    tablas_db, tablas_sm = {}, {}
    for k, t in T.items():
        lista, lista_sm = [], []
        for c in t["cols"]:
            partes = (["PK"] if c["pk"] else []) + (["Identity"] if c["ident"] else []) + fk_col.get((k, c["n"]), [])
            if c["uq"] and not c["pk"]:
                partes.append("Unique")
            if c["gen"]:
                partes.append("Calculada")
            partes.append("Null" if c["nul"] else "Not Null")
            estado = "propuesta" if c["de"] in ("propuesta", "validada") else ""
            lista.append([c["n"], c["ty"], ", ".join(partes), c["d"], estado])
            sc = {"n": c["n"], "t": c["ty"], "nn": not c["nul"], "pk": c["pk"]}
            if c["ident"]:
                sc["id"] = 1
            if c["d"]:
                sc["d"] = c["d"]
            lista_sm.append(sc)
        sp = sorted(usa_tabla.get(k, []))
        tablas_db[k] = {"fullname": k, "schema": t["s"], "name": t["t"], "desc": t["d"], "cols": lista,
                        "fks": fk_pares.get(k, []), "procs": sp}
        tablas_sm[k] = {"rows": int(t["filas"] or 0), "ncol": len(lista), "d": t["d"] or None, "cols": lista_sm, "sp": sp}

    esquemas = [e for e in m["esquemas"] if e["tablas"]]
    dominios = [{"name": e["s"], "tables": sorted(t["t"] for t in T.values() if t["s"] == e["s"]), "main": True} for e in esquemas]
    # versión Lite: las tablas de fuera del alcance a las que apuntan sus FK se dibujan como «otro dominio»
    contexto = {k: t for k, t in m.get("contexto", {}).items() if k not in T}
    for k, t in contexto.items():
        tablas_sm[k] = {"rows": int(t["filas"] or 0), "ncol": len(t["cols"]), "d": t["d"] or None,
                        "cols": [dict({"n": c["n"], "t": c["ty"], "nn": not c["nul"], "pk": c["pk"]}, **({"d": c["d"]} if c["d"] else {}))
                                 for c in t["cols"]], "sp": []}
    fks = [{"fk": f["n"], "c": f["c"], "p": f["p"], "cc": f["cols"], "pc": f["pcols"], "dis": False,
            "unt": not f["validada"], "one": bool(f["unica"])} for f in m["fks"] if f["c"] in T and (f["p"] in T or f["p"] in contexto)]
    fecha = ctx["fecha"].replace("T", " ")[:16]
    smap = {e["s"]: e["nombre"] for e in esquemas}
    dominios_cfg = {r["esquema"]: r for r in M.leer_csv("dominios.csv")}
    for k in contexto:
        sch = k.split(".")[0]
        smap.setdefault(sch, (dominios_cfg.get(sch) or {}).get("nombre") or sch)
    sm = {"ctx": {"db": ctx["db"], "srv": ctx.get("host_conexion") or ctx["srv"], "fecha": fecha},
          "domains": dominios, "tables": tablas_sm, "fks": fks, "smap": smap, "rotas": {}}

    def veredicto(i):
        if not i["nn"]:
            return "SIN DATOS"
        if i["cob"] >= 95:
            return "CONFIRMADA" if not i["sin_padre"] else "CONFIRMADA CON HUERFANOS"
        return "DUDOSA" if i["ok"] else "DESCARTADA"
    inferidas = [{"c": i["c"], "col": i["col"], "p": i["p"] if (i["p"] in T or i["p"] in contexto) else None, "pc": i["pcol"], "amb": bool(i["alternativas"]),
                  "pct": i["cob"], "orf": i["sin_padre"], "ver": veredicto(i),
                  "msg": None if i["ok"] else ("Sin valores para validar" if not i["nn"] else "Ningún valor coincide con la tabla candidata"),
                  "nat": "Auditoría / histórico" if M.es_bitacora(*i["c"].split(".", 1)) else "Negocio", "src": "bd"}
                 for i in m["implicitas"] if i["c"] in T]
    tablas_por_nombre = {f["n"]: f for f in m["fks"]}
    cardinalidad = [{"fk": f["n"], "c": f["c"], "opt": 0 if f["oblig"] else 1, "uni": 1 if f["unica"] else 0} for f in m["fks"] if f["c"] in T]
    rel = {"generado": ctx["fecha"][:10], "fuente": f"{ctx['db']} ({entorno})", "inferidas": inferidas, "cardinalidad": cardinalidad}

    pii = {f"{k}|{c['n']}": {"cat": c["pii"]["cat"], "alto": c["pii"]["nivel"] == "alta"}
           for k, t in T.items() for c in t["cols"] if c["pii"]}
    db = {"tables": tablas_db, "procedures": dict(sorted(procs.items()))}
    del tablas_por_nombre
    return db, sm, rel, pii, esquemas


def tarjetas_dominios(esquemas):
    """Bloque «Arquitectura Conceptual de Módulos» con los dominios de ESAP (mismas clases de la plantilla)."""
    filas = []
    for e in esquemas:
        desc = H.escape(e["d"]) if e["d"] else "Descripción del dominio por documentar."
        marca = (' <span class="ml-1.5 px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-600 dark:text-amber-400 font-semibold '
                 'text-[9px] not-italic border border-amber-500/20" title="Descripción propuesta; pendiente de validar con el equipo funcional">'
                 'propuesta</span>') if e["d"] and e.get("de") == "propuesta" else ""
        filas.append(f'''              <div class="space-y-1">
                <h4 class="font-semibold text-slate-800 dark:text-slate-200">{H.escape(e["nombre"])}</h4>
                <p class="text-slate-500">Esquema <code class="text-indigo-400">{H.escape(e["s"])}</code> · {e["tablas"]} tablas. {desc}{marca}</p>
              </div>''')
    return "\n".join(filas)


def construir_html(m, version, entorno):
    alc = m.get("alcance")
    etiqueta = f"{alc['nombre']} · {version}" if alc else version
    db, sm, rel, pii, esquemas = bloques(m, version, entorno)
    html = open(PLANTILLA, encoding="utf-8").read()
    ctx = m["ctx"]
    carga = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    i = html.index("Arquitectura Conceptual de Módulos (SIPAE)")
    ini = html.index('<div class="grid md:grid-cols-2 gap-4 text-xs">', i)
    fin = html.index('<div class="pt-4 border-t', ini)
    html = (html[:ini] + '<div class="grid md:grid-cols-2 gap-4 text-xs">\n' + tarjetas_dominios(esquemas)
            + "\n            </div>\n            \n            " + html[fin:])

    mapeo = ",\n".join(f"      {json.dumps(e['s'], ensure_ascii=False)}: {json.dumps(e['nombre'], ensure_ascii=False)}" for e in esquemas)
    ini = html.index("const SCHEMA_MAPPINGS = {")
    fin = html.index("};", ini) + 2
    html = html[:ini] + "const SCHEMA_MAPPINGS = {\n" + mapeo + "\n    };" + html[fin:]

    i = html.index("<!-- v2.3 · Catálogo regenerado desde PREPRODUCCIÓN")
    html = html[:i] + (f"<!-- Portal de Datos ESAP {version} · catálogo de {ctx['db']} ({entorno}, {ctx.get('host_conexion') or ctx['srv']}), "
                       f"extracción del {ctx['fecha'].replace('T', ' ')[:16]}. Generado por herramientas/generar_portal.py. "
                       "Funciona sin conexión: Tailwind CSS compilado, fuentes Inter y JetBrains Mono, íconos Lucide.") + html[html.index(" -->", i):]

    rep = [
        ("<title>Portal Interactivo de Datos - SIPAE v2.3</title>", f"<title>Portal Interactivo de Datos - ESAP {etiqueta}</title>"),
        (">SIPAE Data Portal</h1>", ">ESAP Data Portal</h1>"),
        (">v2.3 · Modelo ER + Inventario</p>", f">{etiqueta} · Modelo ER + Inventario</p>"),
        ('font-semibold">sqldb-sipae-pprd</span> <span class="ml-1 px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-500 text-[10px]">QA</span>',
         f'font-semibold">{H.escape(ctx["db"])}</span> <span class="ml-1 px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-500 text-[10px]">{H.escape(entorno)}</span>'),
        ("Sistema de Información de Alimentación Escolar (SIPAE)",
         f"SuperApp ESAP · {alc['nombre']}" if alc else "SuperApp ESAP · Escuela Superior de Administración Pública"),
        ("Arquitectura Conceptual de Módulos (SIPAE)", f"Arquitectura Conceptual de Módulos (ESAP · {alc['nombre']})" if alc else "Arquitectura Conceptual de Módulos (ESAP)"),
        ("La base de datos se encuentra estructurada en múltiples módulos funcionales e integrados para dar soporte a la Unidad Administrativa Especial de Alimentación Escolar (UAPA):",
         (f"Esta versión documenta solo la {alc['nombre']} del proyecto: {len(esquemas)} dominios funcionales de la SuperApp ESAP. "
          "Las tablas de otros dominios a las que se hace referencia aparecen en el Modelo ER como «otro dominio»:") if alc else
         f"La base de datos se organiza en {len(esquemas)} dominios funcionales que dan soporte a los módulos de la SuperApp ESAP:"),
        (">Maestros, tránsito y staging</span>", ">Maestras, transaccionales y catálogos</span>"),
        (">Lógica T-SQL compilada</span>", ">Lógica SQL y PL/pgSQL en la base</span>"),
        ("<!-- v2.0: datos del Modelo ER (catálogo sqldb-sipae-pprd, extraído 2026-09-25 14:03) -->",
         f"<!-- datos del Modelo ER (catálogo {ctx['db']}, extraído {ctx['fecha'].replace('T', ' ')[:16]}) -->"),
        ("(ctx.db || 'sqldb-sipae-pprd')", f"(ctx.db || '{ctx['db']}')"),
        # reglas de SIPAE -> ESAP
        ("return /^(Bkp_|Snapshot_|tmp)|Respaldo|BACKUP|20\\d{2}[01]\\d[0-3]\\d|Cuarentena|^usuariosPAE/i.test(name);",
         "return /(bkp|backup|respaldo|_old$|^old_|_tmp$|^tmp_|^temp_|_temp$|copia|_copy$|(^|_)20\\d{2}_?\\d{2}_?\\d{2}|deprecated|_test$|^test_|prueba|migrations?(_|$)|flyway)/i.test(name);"),
        ("return sch === 'Auditoria' || /^(TA_|DM)|Auditoria|Historico|Historial|_Log|^Log_|AuditLog|Outbox/i.test(name);",
         "return sch === 'audit' || /(^log_|_logs?$|^logs?$|auditlog|^audit_|_audit$|historial|historico|bitacora)/i.test(name);"),
        ("fuente: r ? 'BD (script 02)' : 'catálogo',", "fuente: r ? 'BD (conteo de la extracción)' : 'catálogo',"),
        ("d: `${conPK} de ${neg.length} (sin Staging ni tablas de apoyo)`", "d: `${conPK} de ${neg.length} (sin tablas de apoyo)`"),
        ("'se confirman con el script 01 v2.1'", "'se confirman con la extracción'"),
        ("'Relaciones lógicas y cardinalidad calculadas desde el catálogo embebido; se confirman con los scripts 01 y 02 de v2.1. Los indicadores acompañan la evolución del modelo en cada ciclo de refactorización.'",
         "'Relaciones lógicas y cardinalidad calculadas desde el catálogo embebido. Los indicadores acompañan la evolución del modelo en cada corte.'"),
        ("Los indicadores acompañan la evolución del modelo en cada ciclo de refactorización.`", "Los indicadores acompañan la evolución del modelo en cada corte.`"),
        ("'Resuelto del catalogo del sistema. No incluye las llamadas desde la capa de aplicacion en C#.'",
         "'Resuelto del código fuente almacenado en la base. No incluye las llamadas desde la capa de aplicación.'"),
        ("'Detectado en el texto capturado en el repositorio de despliegue. Cobertura parcial: ausencia no significa que no escriba.'",
         "'Detectado en el código fuente almacenado en la base (INSERT, UPDATE, DELETE). Cobertura parcial: ausencia no significa que no escriba.'"),
        ("llamadas desde la capa de aplicación en C#: que un procedimiento no tenga invocadores", "llamadas desde la capa de aplicación: que un procedimiento no tenga invocadores"),
        ("«Escribe» se detecta en el texto capturado en el\n          repositorio de despliegue, con cobertura parcial.",
         "«Escribe» se detecta en el código fuente almacenado en la\n          base, con cobertura parcial."),
        ("Definición propuesta en Glosario v2.1 (ISO/IEC 11179-4); pendiente de aplicar como MS_Description en BD",
         "Definición propuesta (ISO/IEC 11179-4); pendiente de registrar como COMMENT en la base"),
        ("Definición validada y registrada en preproducción", "Definición registrada en la base"),
        ("const AUD = /^(auditoria|usuario(creacion|modificacion)?|fecha(creacion|modificacion|registro))$/i;",
         "const AUD = /^(auditoria|usuario(creacion|modificacion)?|fecha(creacion|modificacion|registro)|created_(at|by)|updated_(at|by)|deleted_at|"
         "creado_(en|por)|actualizado_(en|por)|fec_(creacion|modificacion|ult_act)|usu_(creacion|modificacion|actualizacion)|fecha_(creacion|actualizacion))$/i;"),
        ("if (/^(Sub)?Tipos?|^Estados?|^TipoEstado/i.test(n) || (!outDeg[k] && (t.ncol||0) <= 6)) return 'cat';",
         "if (/^(Sub)?Tipos?|^Estados?|^TipoEstado|^tipos?_|^estados?_|^cat_|^catalogo|_tipos?$|_estados?$/i.test(n) || (!outDeg[k] && (t.ncol||0) <= 6)) return 'cat';"),
        ("Cardinalidad (v2.1): lado padre", "Cardinalidad: lado padre"),
        # ficha de tabla: una FK hacia una tabla que no está en el catálogo (fuera del alcance) se muestra sin enlace
        ("          const card = document.createElement('a');\n          card.href = `#${encodeURIComponent(fk[1])}`;",
         "          const enCatalogo = !!DB_DATA.tables[fk[1]];\n"
         "          const card = document.createElement(enCatalogo ? 'a' : 'div');\n"
         "          if (enCatalogo) card.href = `#${encodeURIComponent(fk[1])}`; else card.title = 'Tabla de otro dominio, fuera del alcance de esta versión';"),
        # Modelo ER: un dominio sin relaciones dibuja sus tablas como tarjetas independientes en lugar de quedar vacío
        ("        edges.push({p:f.p, c:f.c, f});\n      });\n    return {nodes, edges};\n  }\n  function focusGraph(k){",
         "        edges.push({p:f.p, c:f.c, f});\n      });\n"
         "    if(!nodes.size){ const d=D.domains.find(x=>x.name===dom); (d?d.tables:[]).forEach(t=>{ const k=dom+'.'+t; if(T[k]) nodes.set(k, tableNode(k,false)); }); }\n"
         "    return {nodes, edges};\n  }\n  function focusGraph(k){"),
        # inventario: «Frente» y «Captura» eran del contrato SIPAE (frentes de trabajo y repositorio de despliegue)
        ("        { k: '_esc',         t: 'Escribe',    num: true },\n        { k: '_frente',      t: 'Frente',     num: false },\n"
         "        { k: '_capt',        t: 'Captura',    num: false }\n",
         "        { k: '_esc',         t: 'Escribe',    num: true }\n"),
        ("          <td class=\"p-1.5\">${fr}</td>\n          <td class=\"p-1.5 text-[10px] text-slate-400\">${Q21.esc(d._capt) || '·'}</td>\n", ""),
        ('<label class="flex items-center gap-1.5 text-xs text-slate-600 dark:text-slate-300 pb-1.5">\n            <input id="inv-fr"',
         '<label class="hidden">\n            <input id="inv-fr"'),
        ("con su grafo de\n            llamadas, su traza al despliegue y su frente de trabajo.",
         "con su grafo de\n            llamadas y las tablas que usan y escriben."),
    ]
    for viejo, nuevo in rep:
        if html.count(viejo) != 1:
            raise SystemExit(f"Plantilla SIPAE: no se encontró exactamente una vez: {viejo[:90]}")
        html = html.replace(viejo, nuevo)
    n_v23 = html.count('font-mono">v2.3</span>')
    if n_v23 < 2:
        raise SystemExit("Plantilla SIPAE: no se encontraron las etiquetas de versión v2.3")
    html = html.replace('font-mono">v2.3</span>', f'font-mono">{version}</span>')

    # datos personales: se reemplazan las reglas por nombre de SIPAE por la clasificación de ESAP (modelo.py)
    ini = html.index("      piiRules: [")
    fin = html.index("      // --- Relaciones inferidas:", ini)
    html = html[:ini] + '''      // Clasificación de ESAP (herramientas/modelo.py, Ley 1581 de 2012): tipo de dato y contexto, no solo el nombre
      piiMap: (() => { try { return JSON.parse(document.getElementById('pii-json').textContent); } catch (e) { return {}; } })(),
      pii(table, c) {
        const r = this.piiMap[table.fullname + '|' + c[0]];
        return r ? { cat: r.cat, nna: false, alto: !!r.alto } : null;
      },

''' + html[fin:]

    for id_, obj in (("db-json", db), ("rel-json", rel), ("sm-json", sm)):
        a = html.index(f'<script id="{id_}" type="application/json">')
        a = html.index(">", a) + 1
        b = html.index("</script>", a)
        html = html[:a] + carga(obj) + html[b:]
    i = html.index('<script id="rel-json" type="application/json">')
    html = html[:i] + f'<script id="pii-json" type="application/json">{carga(pii)}</script>\n  ' + html[i:]

    restos = [l.strip()[:120] for l in html.splitlines() if re.search(r"SIPAE|SISPAE|UApA|\bUAPA\b|sqldb-sipae|sql-uapa|Alimentaci[oó]n Escolar", l)]
    return html, restos, {"tablas": len(db["tables"]), "programables": len(db["procedures"]), "fks": len(sm["fks"]),
                          "inferidas": len(rel["inferidas"]), "pii": len(pii), "dominios": len(sm["domains"])}
