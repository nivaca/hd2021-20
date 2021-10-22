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
        
        # Eliminar head (reemplazar por nada)
         (r"<head>.+</head>", r"", re.DOTALL),
        
        # Eliminar span y dejar el segundo grupo de captura
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),       
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),       
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),       


        (r"</?html.+?>", r"", 0),
        (r"</?body.+?>", r"", 0),
        (r"</?article.+?>", r"", 0),
        (r"</?section.+?>", r"", 0),
        (r"</?header>", r"", 0),
        
        # Eliminar h1 y h2 y dejar el contenido 
        (r"<h1 .+?>(.+?)</h1>", r"\n# \1\n", 0),
        (r"<h2 .+?>(.+?)</h2>", r"\n## \1\n", 0),

        # Eliminar algunas etiquetas y dejar el contenido del grupo de captura
        (r'<div role="paragraph">(.+?)</div>', r"\n\1\n", 0),
        (r'<div class="logo">.+?</div>', r"", 0),
        (r'<div id="masthead">(.+?)</div>', r"\n\1\n", re.DOTALL),       
        (r'<div class="masthead-info">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="citation long">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),
        
        # Salir de itálicas y negritas
        (r'<i>(.+?)</i>', r"*\1*", 0),
        (r'<b>(.+?)</b>', r"**\1**", 0),

        # Salir de doctype
        (r"<!DOCTYPE.+?>", r"", 0),

        (r" *\n", r"\n", 0),
        (r"\n{3,}", r"\n\n\n", 0),
              
        # Eliminar todas las etiquetas
        (r"</?.*?>", r"", 0),
        (r"<\?.+?\?>", r"", 0),

        
        #ELIMINAR ESPACIO EN BLANCO Y REEMPLAZAR POR SALTO DE LÍNEA        
        # (r"< *\n", r"\n", r"", 0),
        (r"<\n{1,}", r"\n\n\n\n", 0),

        # Cambiar autor, eliminar otras etiquetas y dejar contenido
        (r'<div property="author" typeof="sa:ContributorRole">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="authors">(.+?)</div>', r"\1", re.DOTALL),
        # (r'<sup class="xref">(.+?)</sup>, r"\n\1", 0),
        (r'<div property="authors">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="core-affiliations>"(.+?)</div>', r"\1", 0),
        (r'</section>', r"", 0),
        #(r'<div class="core-exomatter">(.+?)</div>, r"\1", re.DOTALL),

        # Bibliografía
        (r'<h2>(.+?)</h2>', r"\1", 0),
        (r'<div role.+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<div id.+?>(.+?)</div>', r"-\1", re.DOTALL),

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

    with open(archivo_de_entrada, encoding="utf8") as f:
        datos_originales = f.read()

    datos_nuevos = reemplazar(datos_originales)

    with open(archivo_de_salida, "w", encoding="utf8") as f:
        f.write(datos_nuevos)


if __name__ == "__main__":
    main()
