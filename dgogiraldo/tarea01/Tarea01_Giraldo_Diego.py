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

        # Proyecto Herramientas digitales
        # Programa en Python por Nicolás Vaughan
        # Expresiones regulares por Diego Giraldo
        # d.giraldoo@uniandes.edu.co
        # Maestría en Humanidades digitales - Universidad de los Andes
        

        #Para eliminar
        (r"<head>.+</head>", r"", re.DOTALL),
        
        (r"<span .+?>(.+?)</span>", r"\1", 0),
        (r"<span .+?>(.+?)</span>", r"\1", 0),
        (r"<span .+?>(.+?)</span>", r"\1", 0),

        #Para títulos 
        (r"<h1 .+?>(.+?)</h1>", r"\n# \1\n", 0),
        (r"<h2 .+?>(.+?)</h2>", r"\n## \1\n", 0),
        
        #Para eliminar
        (r'<div role="paragraph">(.+?)</div>', r"\n\1  \n", 0),
        (r'<div class="logo">.+?</div>', r"", 0),
        (r'<div id="masthead">(.+?)</div>', r"\n\1\n", re.DOTALL),

        (r'<div class="masthead-info">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="citation long">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),

        #Ajustes Notas
        (r'<div class="label">(\*)</div>', r"\\\1", 0),
        (r'<div class="label">1.</div>', r"1", 0),

        #Para lista de bibliografía
        (r'<div role="doc-biblioentry" epub:type="biblioentry">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div id="R.+?" .+?>(.+?)</div>', r"- \1", re.DOTALL),

        (r"<div .+?>(.+?)</div>", r"\1", re.DOTALL),
        (r"<div .+?>(.+?)</div>", r"\1", re.DOTALL),
        (r"<div .+?>(.+?)</div>", r"\1", re.DOTALL),
        (r"<div .+?>(.+?)</div>", r"\1", re.DOTALL),

        #Para los otros títulos de segundo nivel
        (r"<h2>(.+?)</h2>", r"\n## \1\n", 0),

        #Para eliminar
        (r"</?html.+?>", r"", 0),
        (r"</?body.+?>", r"", 0),
        (r"</?article.+?>", r"", 0),
        (r"</?section.+?>", r"", 0),
        (r"</?header>", r"", 0),

        #Para eliminar
        (r"</html>", r"", 0),
        (r"</body>", r"", 0),
        (r"</article>", r"", 0),
        (r"</section>", r"", 0),
        
        #Para mentener el formato al texto
        (r'<i>(.+?)</i>', r"*\1*", 0),
        (r'<em>(.+?)</em>', r"*\1*", 0),
        (r'<b>(.+?)</b>', r"**\1**", 0),

        #Para eliminar
        (r"<\?.+?\?>", r"", 0),
        (r"<!DOCTYPE.+?>", r"", 0),

        #Para los links
        (r'<a href="https://doi.org/10.21670/ref.2016.34.a06">.+?</a>', r"<https://doi.org/10.21670/ref.2016.34.a06>", 0),
        (r'<a href="https://doi.org/10.5195/REVIBEROAMER.2010.6752">.+?</a>', r"<https://doi.org/10.5195/REVIBEROAMER.2010.6752>", 0),
        (r"<a href.+?>(.+?)</a>", r"<\1>", 0),

        #Para eliminar  
        (r'<sup class="xref">\<(.+?)\></sup>', r"\1", re.DOTALL),
        
        #Para los saltos de línea 
        (r" *\n", r"\n", 0),
        (r"\n{3,}", r"\n\n\n", 0),
        #(r"\n\n", r"<br/><br/>", 0),

        #Para los espacios
        (r" {2,}", r"", 0),

        #Transformaciones
            #Título
        (r"# VERSOS \*MIXTURADOS\* EN LA FRONTERA URUGUAYA: CONVERSACIÓN CON FABIÁN SEVERO", r"# Nuevos versos en la frontera de Uruguay: conversando con Fabián Severo", 0),
            #Autor
        (r"Lina Gabriela Cortés\*\n{1}", r"**Lina Gabriela Cortés** *\n", 0),
            #Datos revista
        (r"(Perífrasis). (Revista de Literatura,) (Teoría y Crítica), (Julio-Diciembre, PP. 132-146)", r"### \1\n**\2 \3**\n*Número 24, \4*\n", 0),
        (r"(ISSN 2145-8987), (E-ISSN 2145-9045)", r"1. \1\n2. \2\n", 0),
        (r"\nNúmero 24\n\n", r"", 0),


        #Para las citas, pero no aplica porque ninguna cita empieza en una línea aparte
        #(r"(“.+?” \(.+?\))", r"\n>\1", 0),
        
        #Plantillas
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

    with open(archivo_de_entrada, encoding="utf8") as f:
        datos_originales = f.read()

    datos_nuevos = reemplazar(datos_originales)

    with open(archivo_de_salida, "w", encoding="utf8") as f:
        f.write(datos_nuevos)


if __name__ == "__main__":
    main()
