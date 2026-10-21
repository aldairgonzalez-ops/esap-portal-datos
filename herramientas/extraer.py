# -*- coding: utf-8 -*-
r"""
Lanza la extracción del catálogo de la base ESAP (QA) con psql, en SOLO LECTURA.

Crea extracciones/<AAAA-MM-DD> (o la carpeta que se indique) y deja allí un JSONL por consulta.
La contraseña no pasa por aquí: psql la toma de pgpass.conf o la pide en pantalla.

Uso (desde la raíz del repositorio):
  python herramientas/extraer.py                         # usa el servicio "esap_qa" de pg_service.conf
  python herramientas/extraer.py --servicio esap_qa --bd esap_db
  python herramientas/extraer.py --host 100.x.y.z --puerto 5432 --usuario lector --bd esap_db

Busca psql en el PATH y, en Windows, también en las carpetas de pgAdmin 4 y de PostgreSQL.
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SCRIPT = os.path.join("sql", "extraccion", "extraer_todo.sql")
ESPERADOS = ["00_contexto", "01_esquemas", "02_tablas", "03_columnas", "04_restricciones", "05_indices",
             "06_programables", "07_triggers", "08_vistas", "09_tipos", "10_conteo_filas",
             "11_cardinalidad_fk", "12_relaciones_implicitas", "13_identidad"]


def buscar_psql(indicado):
    if indicado:
        return indicado
    en_path = shutil.which("psql")
    if en_path:
        return en_path
    patrones = [r"C:\Program Files\pgAdmin 4\runtime\psql.exe",
                r"C:\Program Files\pgAdmin 4\v*\runtime\psql.exe",
                r"C:\Program Files\PostgreSQL\*\bin\psql.exe",
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\pgAdmin 4\runtime\psql.exe")]
    for p in patrones:
        hallados = sorted(glob.glob(p))
        if hallados:
            return hallados[-1]
    sys.exit("No se encontró psql. Instálalo o indica la ruta con --psql (pgAdmin 4 lo trae en su carpeta runtime).")


def verificar(salida):
    """Cada JSONL debe existir y cerrar con su fila de control {"_fin": n} que cuadre con las filas."""
    problemas = []
    for nombre in ESPERADOS:
        ruta = os.path.join(salida, nombre + ".jsonl")
        if not os.path.isfile(ruta):
            problemas.append(f"falta {nombre}.jsonl")
            continue
        lineas = [l for l in open(ruta, encoding="utf-8").read().splitlines() if l.strip()]
        try:
            fin = json.loads(lineas[-1]).get("_fin")
        except (IndexError, ValueError):
            fin = None
        if fin is None or fin != len(lineas) - 1:
            problemas.append(f"{nombre}.jsonl sin fila de control válida")
        else:
            print(f"  {nombre:<28} {fin:>7} filas")
    return problemas


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--servicio", default="esap_qa", help="servicio de pg_service.conf (por defecto esap_qa)")
    ap.add_argument("--host")
    ap.add_argument("--puerto")
    ap.add_argument("--usuario")
    ap.add_argument("--bd", default="esap_db", help="base que debe estar conectada (por defecto esap_db)")
    ap.add_argument("--salida", help="carpeta relativa a la raíz; por defecto extracciones/<fecha>")
    ap.add_argument("--maestro-email", default="auth.personas.dir_email")
    ap.add_argument("--maestro-doc", default="auth.personas.num_identificacion")
    ap.add_argument("--psql")
    ap.add_argument("--solo-verificar", metavar="CARPETA",
                    help="no extrae: solo revisa una extracción ya hecha (por ejemplo desde la PSQL Tool de pgAdmin)")
    a = ap.parse_args()

    if a.solo_verificar:
        print(f"Verificación de {a.solo_verificar}:")
        problemas = verificar(os.path.join(RAIZ, a.solo_verificar))
        if problemas:
            sys.exit("Extracción incompleta: " + "; ".join(problemas))
        print(f"\nOK. Siguiente paso:\n  python herramientas/generar_portal.py --extraccion {a.solo_verificar.replace(os.sep, '/')}")
        return

    salida = (a.salida or f"extracciones/{datetime.date.today().isoformat()}").replace("\\", "/")
    if " " in salida:
        sys.exit("La carpeta de salida no puede tener espacios (psql la recibe como variable).")
    os.makedirs(os.path.join(RAIZ, salida), exist_ok=True)

    psql = buscar_psql(a.psql)
    cmd = [psql, "-X", "-q", "-d", a.bd if a.host else f"service={a.servicio} dbname={a.bd}"]
    if a.host:
        cmd += ["-h", a.host] + (["-p", a.puerto] if a.puerto else []) + (["-U", a.usuario] if a.usuario else [])
    cmd += ["-v", f"salida={salida}", "-v", f"bd_esperada={a.bd}",
            "-v", f"maestro_email={a.maestro_email}", "-v", f"maestro_doc={a.maestro_doc}",
            "-f", SCRIPT]
    entorno = dict(os.environ, PGCLIENTENCODING="UTF8", PGAPPNAME="portal_datos_esap_extraccion")
    print("Ejecutando:", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    r = subprocess.run(cmd, cwd=RAIZ, env=entorno)
    if r.returncode != 0:
        sys.exit(f"psql terminó con código {r.returncode}. Revisa el mensaje anterior.")

    print(f"\nVerificación de {salida}:")
    problemas = verificar(os.path.join(RAIZ, salida))
    if problemas:
        sys.exit("Extracción incompleta: " + "; ".join(problemas))
    print(f"\nOK. Siguiente paso:\n  python herramientas/generar_portal.py --extraccion {salida}")


if __name__ == "__main__":
    main()
