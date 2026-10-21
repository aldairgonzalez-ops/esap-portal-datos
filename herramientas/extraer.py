# -*- coding: utf-8 -*-
r"""
Lanza la extracción del catálogo de la base ESAP (QA) con psql, en SOLO LECTURA.

Crea extracciones/<AAAA-MM-DD> (o la carpeta que se indique) y deja allí un JSONL por consulta.
La contraseña no pasa por aquí ni se guarda: psql la pide en pantalla en cada ejecución.

Uso (desde la raíz del repositorio; por defecto se conecta a QA 100.127.140.5 / esap_db / postgres):
  python herramientas/extraer.py --verificar-conexion    # evidencia CSV en evidencias/<fecha>/
  python herramientas/extraer.py                         # extracción completa en extracciones/<fecha>/
  python herramientas/extraer.py --servicio esap_qa      # con un servicio de pg_service.conf
psql pide la contraseña en pantalla una vez por comando (no se guarda en pgpass.conf ni en PGPASSWORD).

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


QA_HOST = "100.127.140.5"   # servidor de QA en Tailscale (confirmado el 2026-10-21)


def comando_psql(a, script, variables):
    psql = buscar_psql(a.psql)
    if a.servicio:
        cmd = [psql, "-X", "-q", "-d", f"service={a.servicio} dbname={a.bd}"]
    else:
        cmd = [psql, "-X", "-q", "-h", a.host, "-p", a.puerto, "-U", a.usuario, "-d", a.bd]
    for k, v in variables.items():
        cmd += ["-v", f"{k}={v}"]
    return cmd + ["-f", script]


def ejecutar(cmd):
    entorno = dict(os.environ, PGCLIENTENCODING="UTF8", PGAPPNAME="portal_datos_esap_extraccion")
    print("Ejecutando:", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    r = subprocess.run(cmd, cwd=RAIZ, env=entorno)
    if r.returncode != 0:
        sys.exit(f"psql terminó con código {r.returncode}. Revisa el mensaje anterior.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verificar-conexion", action="store_true",
                    help="no extrae: corre la verificación previa y deja evidencias/<fecha>/verificacion_conexion.csv")
    ap.add_argument("--host", default=QA_HOST, help=f"servidor (por defecto QA: {QA_HOST})")
    ap.add_argument("--puerto", default="5432")
    ap.add_argument("--usuario", default="postgres")
    ap.add_argument("--bd", default="esap_db", help="base que debe estar conectada (por defecto esap_db)")
    ap.add_argument("--servicio", help="usar un servicio de pg_service.conf en lugar de --host/--puerto/--usuario")
    ap.add_argument("--servidor-esperado", default=QA_HOST,
                    help="IP que debe reportar el servidor; la extracción se detiene si es otra ('' para no comprobar)")
    ap.add_argument("--salida", help="carpeta relativa a la raíz; por defecto extracciones/<fecha> (o evidencias/<fecha>)")
    ap.add_argument("--maestro-email", default="auth.personas.dir_email")
    ap.add_argument("--maestro-doc", default="auth.personas.num_identificacion")
    ap.add_argument("--psql")
    ap.add_argument("--solo-verificar", metavar="CARPETA",
                    help="no extrae: solo revisa una extracción ya hecha (por ejemplo desde la PSQL Tool de pgAdmin)")
    a = ap.parse_args()
    hoy = datetime.date.today().isoformat()

    if a.solo_verificar:
        print(f"Verificación de {a.solo_verificar}:")
        problemas = verificar(os.path.join(RAIZ, a.solo_verificar))
        if problemas:
            sys.exit("Extracción incompleta: " + "; ".join(problemas))
        print(f"\nOK. Siguiente paso:\n  python herramientas/generar_portal.py --extraccion {a.solo_verificar.replace(os.sep, '/')}")
        return

    if a.verificar_conexion:
        salida = (a.salida or f"evidencias/{hoy}").replace("\\", "/")
        os.makedirs(os.path.join(RAIZ, salida), exist_ok=True)
        ejecutar(comando_psql(a, os.path.join("sql", "verificar_conexion_csv.sql"), {"salida": salida}))
        ruta = os.path.join(RAIZ, salida, "verificacion_conexion.csv")
        print("\n" + open(ruta, encoding="utf-8").read())
        print(f"Evidencia: {salida}/verificacion_conexion.csv\n"
              f"Para compartirla:  git add {salida} && git commit -m \"Verificación de conexión QA {hoy}\" && git push")
        return

    salida = (a.salida or f"extracciones/{hoy}").replace("\\", "/")
    if " " in salida:
        sys.exit("La carpeta de salida no puede tener espacios (psql la recibe como variable).")
    os.makedirs(os.path.join(RAIZ, salida), exist_ok=True)
    ejecutar(comando_psql(a, SCRIPT, {"salida": salida, "bd_esperada": a.bd, "srv_esperado": a.servidor_esperado,
                                      "maestro_email": a.maestro_email, "maestro_doc": a.maestro_doc}))

    print(f"\nVerificación de {salida}:")
    problemas = verificar(os.path.join(RAIZ, salida))
    if problemas:
        sys.exit("Extracción incompleta: " + "; ".join(problemas))
    print(f"\nOK. Para compartirla:\n  git add {salida} && git commit -m \"Extracción QA {hoy}\" && git push"
          f"\nSiguiente paso:\n  python herramientas/generar_portal.py --extraccion {salida}")


if __name__ == "__main__":
    main()
