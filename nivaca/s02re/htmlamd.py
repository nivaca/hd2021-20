#!/usr/bin/env python3

import re
import sys
import os


def reemplazar(datos: str) -> str:
    patrones: list[tuple[str, str, int]] = [

        # Vamos a trabajar desde aquí: ------------------------
        # formato: ( r"<patrón de búsqueda>",
        #            r"<patrón de reemplazo>",
        #            <bandera de re>)

        (r"Perífrasis", r"Semana", 0),
        # (r"", r"", 0),
        # (r"", r"", 0),
        # (r"", r"", 0),
        # (r"", r"", 0),
        # (r"", r"", 0),
        # (r"", r"", 0),
        # (r"", r"", re.MULTILINE | re.DOTALL),

        # hasta aquí: ------------------------
    ]

    # for i in range(2):
    for patron, reemplazo, bandera in patrones:
        patroncomp = re.compile(patron, bandera)
        datos = re.sub(patroncomp, reemplazo, datos)

    return datos


def main():
    num_args = len(sys.argv)
    archivo_de_entrada = ""

    if num_args > 1:
        archivo_de_entrada = sys.argv[1]
    else:
        print("Uso: python3 htmlamd.py <archivo.[x]htm[l]>")
        exit(1)

    archivo, extension = os.path.splitext(archivo_de_entrada)

    if extension.lower() not in [".xhtml", ".html", ".htm"]:
        print("Uso: python3 htmlamd.py <archivo.[x]htm[l]>")
        exit(1)

    archivo_de_salida = archivo + ".md"

    with open(archivo_de_entrada) as f:
        datos_originales = f.read()

    datos_nuevos = reemplazar(datos_originales)

    with open(archivo_de_salida, "w") as f:
        f.write(datos_nuevos)


if __name__ == "__main__":
    main()
