# -*- coding: utf-8 -*-
r"""
Prepara la plantilla del Portal de Datos a partir del portal SIPAE (UAPA), SIN sus datos.

El portal ESAP reutiliza la interfaz del Portal de Datos SIPAE v2.3: el mismo HTML, estilos, vistas y lógica,
con los datos de ESAP. Este script se ejecuta UNA VEZ en el equipo que tiene el portal SIPAE:
  1. Copia el HTML y vacía cada bloque <script type="application/json"> (db-json, sm-json, rel-json…).
     Así el repositorio ESAP no guarda el catálogo ni ningún dato de SIPAE.
  2. Guarda la FORMA de cada bloque (nombres de campo y tipo de valor, sin valores) en forma.json,
     para que el generador ESAP produzca exactamente la estructura que espera cada vista.
  3. Lista los textos de la interfaz que mencionan SIPAE / UApA / PAE, que el generador ESAP reemplaza.

Uso:
  python herramientas/preparar_plantilla_sipae.py --portal "G:\Mi unidad\UAPA\Base de datos v2.0\Portal_de_Datos_SIPAE_v2.3.html"
Salidas (en herramientas/plantilla_sipae/):
  portal_base.html   interfaz del portal con los bloques de datos vacíos
  forma.json         estructura de cada bloque (sin valores)
  textos_sipae.txt   líneas de la interfaz que nombran SIPAE / UApA / PAE
"""
import argparse
import json
import os
import re
import sys

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DESTINO = os.path.join(RAIZ, "herramientas", "plantilla_sipae")
BLOQUE = re.compile(r'(<script\b[^>]*\bid="([^"]+)"[^>]*type="application/json"[^>]*>|<script\b[^>]*type="application/json"[^>]*\bid="([^"]+)"[^>]*>)(.*?)(</script>)', re.S)
MENCIONES = re.compile(r"(SIPAE|SISPAE|UApA|UAPA|Alimentaci[oó]n Escolar|\bPAE\b|sql-uapa|sqldb-sipae)", re.I)


def forma(v, profundidad=0, muestras=3):
    """Estructura sin valores: dict -> {clave: forma}, lista -> [forma de hasta 3 elementos fusionada], escalar -> tipo."""
    if isinstance(v, dict):
        # diccionarios indexados por nombre de objeto (tablas, procedimientos): se describe un valor típico
        if len(v) > 20 and all(isinstance(x, (dict, list)) for x in list(v.values())[:20]):
            valores = list(v.values())[:muestras]
            return {"<clave>": fusionar([forma(x, profundidad + 1) for x in valores]), "_n": len(v)}
        return {k: forma(x, profundidad + 1) for k, x in v.items()}
    if isinstance(v, list):
        if not v:
            return []
        return [fusionar([forma(x, profundidad + 1) for x in v[:50]]), {"_n": len(v)}]
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, (int, float)):
        return "num"
    if v is None:
        return "null"
    return "str"


def fusionar(formas):
    dicts = [f for f in formas if isinstance(f, dict)]
    if dicts and len(dicts) == len(formas):
        claves = {}
        for d in dicts:
            for k, x in d.items():
                claves.setdefault(k, []).append(x)
        return {k: fusionar(xs) for k, xs in claves.items()}
    tipos = sorted({json.dumps(f, sort_keys=True) for f in formas})
    return json.loads(tipos[0]) if len(tipos) == 1 else [json.loads(t) for t in tipos][:4]


CATEGORIAS = ("ver", "nat", "type", "verbo", "src", "estado", "tipo", "k")


def categorias(v, acumulado):
    """Valores distintos de los campos de categoría (veredictos, tipos de objeto…): vocabulario, no datos."""
    if isinstance(v, dict):
        for k, x in v.items():
            if k in CATEGORIAS and isinstance(x, str) and len(x) <= 40:
                acumulado.setdefault(k, set()).add(x)
            categorias(x, acumulado)
    elif isinstance(v, list):
        for x in v:
            categorias(x, acumulado)
    return acumulado


def vacio(v):
    if isinstance(v, dict):
        return {}
    if isinstance(v, list):
        return []
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--portal", required=True, help="ruta del Portal_de_Datos_SIPAE_v2.3.html")
    a = ap.parse_args()
    if not os.path.isfile(a.portal):
        sys.exit(f"No se encontró {a.portal}")
    html = open(a.portal, encoding="utf-8").read()
    formas, salida, pos, bloques = {}, [], 0, []
    for m in BLOQUE.finditer(html):
        id_ = m.group(2) or m.group(3)
        try:
            datos = json.loads(m.group(4))
        except ValueError as e:
            sys.exit(f"El bloque {id_} no es JSON válido: {e}")
        formas[id_] = forma(datos)
        cats = categorias(datos, {})
        if cats:
            formas[id_ + ":valores"] = {k: sorted(v)[:30] for k, v in cats.items()}
        # se conserva la forma mínima del bloque (claves de primer nivel vacías) para que la interfaz cargue
        minimo = {k: vacio(v) for k, v in datos.items()} if isinstance(datos, dict) else vacio(datos)
        salida.append(html[pos:m.start(4)])
        salida.append(json.dumps(minimo, ensure_ascii=False, separators=(",", ":")))
        pos = m.end(4)
        bloques.append((id_, len(m.group(4))))
    salida.append(html[pos:])
    base = "".join(salida)
    if not bloques:
        sys.exit("No se encontraron bloques <script type=\"application/json\">: ¿es el portal SIPAE v2.x?")

    os.makedirs(DESTINO, exist_ok=True)
    open(os.path.join(DESTINO, "portal_base.html"), "w", encoding="utf-8", newline="").write(base)
    json.dump(formas, open(os.path.join(DESTINO, "forma.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lineas = [f"{i}: {l.strip()[:220]}" for i, l in enumerate(base.splitlines(), 1) if MENCIONES.search(l)]
    open(os.path.join(DESTINO, "textos_sipae.txt"), "w", encoding="utf-8").write("\n".join(lineas) + "\n")

    print(f"Portal SIPAE: {len(html) / 1048576:.2f} MB  ->  plantilla sin datos: {len(base) / 1048576:.2f} MB")
    for id_, n in bloques:
        print(f"  bloque {id_:<14} {n / 1048576:6.2f} MB vaciado")
    print(f"  {len(lineas)} líneas de la interfaz mencionan SIPAE/UApA/PAE (ver textos_sipae.txt)")
    print("\nSiguiente paso:\n  git add herramientas/plantilla_sipae && git commit -m \"Plantilla del portal SIPAE sin datos\" && git push")


if __name__ == "__main__":
    main()
