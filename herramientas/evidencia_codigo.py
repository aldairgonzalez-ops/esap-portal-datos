# -*- coding: utf-8 -*-
r"""
Busca en el código fuente de la SuperApp (repositorio de la aplicación, solo lectura) la evidencia que documenta
cada columna pendiente de la matriz: comentarios JSDoc o // sobre la propiedad de la entidad TypeORM, COMMENT ON
y comentarios -- en las migraciones SQL, y la validación declarada (class-validator) en la entidad o en los DTO.

No ejecuta nada del repositorio: solo lee archivos de texto .ts y .sql.

Uso:
  python herramientas/evidencia_codigo.py --repo C:\ruta\al\repositorio --rama micro-frontend --alcance config/alcances/fase2.json
      -> config/propuestas/<id>_evidencia_codigo.jsonl   (una línea por columna con evidencia)
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modelo as M  # noqa: E402

# servicio -> esquema por defecto (para @Entity('tabla') sin schema)
SERVICIO_ESQUEMA = {
    "hiring-service": "hiring", "travel-expenses-service": "travel_expenses", "academic-schedule-service": "academic-schedule",
    "infrastructure-management-service": "infrastructure-management", "chatbot-service": "chatbot",
    "academic-work-plan-service": "academic_work_plan", "academic-registration-service": "academic_registration",
    "auth-service": "auth", "certification-service": "certification", "legal-management-service": "legal_management",
    "internal-disciplinary-control-service": "internal_disciplinary_control", "internal-institutional-control-service": "control_interno",
    "notifications-service": "notifications", "audit-service": "audit",
}
OMITIR = {"node_modules", ".git", "dist", "build", "coverage"}
DECOR_COL = re.compile(r"@(Column|PrimaryColumn|PrimaryGeneratedColumn|CreateDateColumn|UpdateDateColumn|DeleteDateColumn|VersionColumn|JoinColumn)\s*\(", re.S)
VALIDADORES = re.compile(r"@(Is\w+|Min|Max|MinLength|MaxLength|Length|Matches|ArrayMinSize|ArrayMaxSize|ValidateIf)\s*\(([^)]*)\)")


def norm(x):
    return re.sub(r"[^a-z0-9]", "", (x or "").lower())


def limpiar_jsdoc(t):
    t = re.sub(r"^/\*\*?|\*/$", "", t.strip())
    lineas = [re.sub(r"^\s*\*\s?", "", l).rstrip() for l in t.splitlines()]
    return re.sub(r"\s+", " ", " ".join(l for l in lineas if l.strip())).strip()


def archivos(raiz, ext):
    for d, subdirs, fs in os.walk(raiz):
        subdirs[:] = [s for s in subdirs if s not in OMITIR]
        for f in fs:
            if f.endswith(ext):
                yield os.path.join(d, f)


def servicio_de(ruta, raiz):
    partes = os.path.relpath(ruta, raiz).replace("\\", "/").split("/")
    return partes[1] if len(partes) > 2 and partes[0] == "backend" else ""


def leer(p):
    with open(p, encoding="utf-8", errors="ignore") as f:
        return f.read()


def entidades(raiz):
    """(esquema, tabla, columna) -> lista de evidencias de las entidades TypeORM."""
    ev = {}
    props = {}   # (servicio, propiedad normalizada) -> validadores de DTO
    for p in archivos(os.path.join(raiz, "backend"), ".ts"):
        if p.endswith(".spec.ts"):
            continue
        s = leer(p)
        rel = os.path.relpath(p, raiz).replace("\\", "/")
        serv = servicio_de(p, raiz)
        if "@Entity" not in s:
            if "class-validator" in s:   # DTO: validaciones por propiedad
                for m in re.finditer(r"((?:\s*@\w+\([^)]*\)\s*)+)\s*(?:readonly\s+)?(\w+)\??!?\s*:", s):
                    vals = [f"{a}({b.strip()})" if b.strip() else a for a, b in VALIDADORES.findall(m.group(1))]
                    if vals:
                        props.setdefault((serv, norm(m.group(2))), set()).update(vals)
            continue
        for me in re.finditer(r"@Entity\s*\(([^)]*)\)\s*(?:@\w+\([^)]*\)\s*)*export\s+class\s+(\w+)", s, re.S):
            args = me.group(1)
            nombre = re.search(r"name\s*:\s*['\"]([^'\"]+)", args) or re.match(r"\s*['\"]([^'\"]+)", args)
            esquema = re.search(r"schema\s*:\s*['\"]([^'\"]+)", args)
            tabla = nombre.group(1) if nombre else me.group(2)
            esq = esquema.group(1) if esquema else SERVICIO_ESQUEMA.get(serv, "")
            # doc de la clase
            previo = s[:me.start()]
            doc_clase = re.search(r"/\*\*((?:(?!\*/).)*)\*/\s*$", previo, re.S)
            cuerpo_ini = s.index("{", me.end())
            fin = len(s)
            sig = re.search(r"@Entity\s*\(", s[me.end():])
            if sig:
                fin = me.end() + sig.start()
            cuerpo = s[cuerpo_ini:fin]
            for mc in DECOR_COL.finditer(cuerpo):
                # argumentos del decorador (paréntesis balanceados)
                i, nivel = mc.end(), 1
                while i < len(cuerpo) and nivel:
                    nivel += {"(": 1, ")": -1}.get(cuerpo[i], 0)
                    i += 1
                arg = cuerpo[mc.end():i - 1]
                resto = cuerpo[i:]
                mp = re.match(r"((?:\s*@\w+\s*\((?:[^()]|\([^()]*\))*\))*)\s*(?:readonly\s+)?(\w+)\??!?\s*:", resto, re.S)
                if not mp:
                    continue
                prop = mp.group(2)
                col = re.search(r"name\s*:\s*['\"]([^'\"]+)", arg) if mc.group(1) != "JoinColumn" or "name" in arg else None
                colname = col.group(1) if col else prop
                # comentarios inmediatamente antes de los decoradores de esta propiedad
                antes = cuerpo[:mc.start()]
                antes = re.sub(r"(\s*@\w+\s*\((?:[^()]|\([^()]*\))*\))+\s*$", "", antes)
                comentario = ""
                mj = re.search(r"/\*\*((?:(?!\*/).)*)\*/\s*$", antes, re.S)
                if mj:
                    comentario = limpiar_jsdoc(mj.group(0))
                else:
                    # solo líneas completas de comentario: un «// …» al final de la línea anterior es de esa propiedad
                    ml = re.search(r"(?m)((?:^[ \t]*//[^\n]*\n)+)\s*$", antes)
                    if ml:
                        comentario = " ".join(l.strip()[2:].strip() for l in ml.group(1).splitlines() if l.strip())
                # comentario al final de la línea de la propiedad: «contenido: string; // HTML»
                fin_prop = resto[mp.end():].split("\n", 1)[0]
                if "//" in fin_prop:
                    final = fin_prop.split("//", 1)[1].strip()
                    comentario = f"{comentario} {final}".strip() if comentario else final
                opc_coment = re.search(r"comment\s*:\s*['\"`]([^'\"`]+)", arg)
                enum = re.search(r"enum\s*:\s*\[([^\]]*)\]", arg)
                linea = s[:cuerpo_ini + mc.start()].count("\n") + 1
                vals = [f"{a}({b.strip()})" if b.strip() else a for a, b in VALIDADORES.findall(mp.group(1))]
                e = {"fuente": f"{rel}:{linea}", "tipo": "entidad", "entidad": me.group(2), "propiedad": prop,
                     "comentario": comentario, "comment_typeorm": opc_coment.group(1) if opc_coment else "",
                     "enum": re.findall(r"['\"]([^'\"]+)['\"]", enum.group(1)) if enum else [],
                     "validaciones": vals, "doc_tabla": limpiar_jsdoc(doc_clase.group(0)) if doc_clase else "", "servicio": serv}
                ev.setdefault((esq, tabla, colname), []).append(e)
    return ev, props


RE_CT = re.compile(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?((?:\"[^\"]+\"|\w+)\.)?(\"[^\"]+\"|\w+)\s*\(", re.I)
RE_AT = re.compile(r"ALTER\s+TABLE\s+(?:IF\s+EXISTS\s+)?(?:ONLY\s+)?((?:\"[^\"]+\"|\w+)\.)?(\"[^\"]+\"|\w+)", re.I)
RE_CO = re.compile(r"COMMENT\s+ON\s+COLUMN\s+((?:\"[^\"]+\"|[\w-]+)\.)?(\"[^\"]+\"|\w+)\.(\"[^\"]+\"|\w+)\s+IS\s+'((?:[^']|'')*)'", re.I)


def q(x):
    return (x or "").rstrip(".").strip('"')


def migraciones(raiz):
    """(esquema, tabla, columna) -> evidencias de SQL (COMMENT ON y comentarios -- en la definición de la columna)."""
    ev = {}
    fuentes = list(archivos(raiz, ".sql")) + [p for p in archivos(os.path.join(raiz, "backend"), ".ts")
                                               if not p.endswith(".spec.ts") and re.search(r"migration|migracion|schema|ddl", p, re.I)]
    for p in fuentes:
        rel = os.path.relpath(p, raiz).replace("\\", "/")
        if "backup" in rel.lower():
            continue
        s = leer(p)
        serv = servicio_de(p, raiz)
        for m in RE_CO.finditer(s):
            esq = q(m.group(1)) or SERVICIO_ESQUEMA.get(serv, "")
            ev.setdefault((esq, q(m.group(2)), q(m.group(3))), []).append(
                {"fuente": f"{rel}:{s[:m.start()].count(chr(10)) + 1}", "tipo": "COMMENT ON", "comentario": m.group(4).replace("''", "'")})
        # comentarios -- en líneas de definición de columnas (CREATE TABLE ... / ALTER TABLE ... ADD COLUMN ...)
        tabla_actual, esq_actual, pendiente = None, None, []
        for n, linea in enumerate(s.splitlines(), 1):
            mct = RE_CT.search(linea) or RE_AT.search(linea)
            if mct:
                esq_actual = q(mct.group(1)) or SERVICIO_ESQUEMA.get(serv, "")
                tabla_actual = q(mct.group(2))
                pendiente = []
            st = linea.strip()
            if st.startswith("--"):
                pendiente.append(st[2:].strip())
                continue
            if not tabla_actual:
                pendiente = []
                continue
            mcol = re.match(r"\s*(?:ADD\s+COLUMN\s+(?:IF\s+NOT\s+EXISTS\s+)?)?(\"[^\"]+\"|[a-zA-Z_]\w*)\s+[a-zA-Z]", linea, re.I)
            if mcol and mcol.group(1).upper() not in ("CONSTRAINT", "PRIMARY", "UNIQUE", "CHECK", "FOREIGN", "CREATE", "ALTER", "COMMENT", "INSERT", "UPDATE"):
                coment = linea.split("--", 1)[1].strip() if "--" in linea else ""
                texto = " ".join(x for x in pendiente + [coment] if x)
                if texto:
                    ev.setdefault((esq_actual, tabla_actual, q(mcol.group(1))), []).append(
                        {"fuente": f"{rel}:{n}", "tipo": "comentario SQL", "comentario": texto})
            pendiente = []
            if st.endswith(");"):
                tabla_actual = None
    return ev


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="carpeta del repositorio de la aplicación (solo lectura)")
    ap.add_argument("--rama", default="", help="rama revisada (se registra en la evidencia)")
    ap.add_argument("--alcance")
    a = ap.parse_args()
    alcance = M.cargar_alcance(a.alcance)
    sufijo = alcance["id"].lower() if alcance else "completa"
    ctx = [json.loads(l) for l in open(os.path.join(M.CONFIG, "propuestas", f"{sufijo}_contexto.jsonl"), encoding="utf-8")]
    try:
        commit = subprocess.run(["git", "-C", a.repo, "log", "-1", "--format=%h %ad", "--date=short"], capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = ""
    ent, props = entidades(a.repo)
    sql = migraciones(a.repo)
    ent_n = {(e, norm(t), norm(c)): v for (e, t, c), v in ent.items()}
    sql_n = {(e, norm(t), norm(c)): v for (e, t, c), v in sql.items()}
    destino = os.path.join(M.CONFIG, "propuestas", f"{sufijo}_evidencia_codigo.jsonl")
    n = con_coment = 0
    with open(destino, "w", encoding="utf-8") as f:
        for r in ctx:
            k = (r["esquema"], norm(r["tabla"]), norm(r["columna"]))
            evs = ent_n.get(k, []) + sql_n.get(k, [])
            if not evs:
                continue
            serv = next((e.get("servicio") for e in evs if e.get("servicio")), "")
            dto = sorted({v for e in evs if e.get("propiedad") for v in props.get((serv, norm(e["propiedad"])), set())})
            n += 1
            con_coment += any(e.get("comentario") or e.get("comment_typeorm") for e in evs)
            f.write(json.dumps({"esquema": r["esquema"], "tabla": r["tabla"], "columna": r["columna"], "repo_commit": f"{a.rama} {commit}".strip(),
                                "evidencias": evs, "validaciones_dto": dto}, ensure_ascii=False) + "\n")
    print(f"{os.path.relpath(destino, M.RAIZ)}: {n} de {len(ctx)} columnas con evidencia en el código · {con_coment} con comentario del desarrollador")


if __name__ == "__main__":
    main()
