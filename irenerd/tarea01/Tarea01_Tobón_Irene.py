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

        (r"<head>.+</head>", r"", re.DOTALL),
        
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),        # (r"", r"", 0),
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),        # (r"", r"", 0),
        (r"(<span .+?>)(.+?)(</span>)", r"\2", 0),        # (r"", r"", 0),


        (r"</?html.+?>", r"", 0),
        (r"</?body.+?>", r"", 0),
        (r"</?article.+?>", r"", 0),
        (r"</?section.+?>", r"", 0),
        (r"</?header>", r"", 0),
        
        (r"<h1 .+?>(.+?)</h1>", r"\n# \1\n", 0),
        (r"<h2 .+?>(.+?)</h2>", r"\n## \1\n", 0),

        (r'<div role="paragraph">(.+?)</div>', r"\n\1\n", 0),
        
        (r'<div class="logo">.+?</div>', r"", 0),

        (r'<div id="masthead">(.+?)</div>', r"\n\1\n", re.DOTALL),
       
        
        (r'<div class="masthead-info">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="citation long">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),
        

        (r'<i>(.+?)</i>', r"*\1*", 0),
        (r'<b>(.+?)</b>', r"**\1**", 0),

        (r"<\?.+?\?>", r"", 0),

        (r"<!DOCTYPE.+?>", r"", 0),

        (r" *\n", r"\n", 0),
        (r"\n{3,}", r"\n\n\n", 0),

        #Hola Nicolás. Acá empieza mi tarea, dejé el código que llevábamos escrito arriba, sin tocarlo:

        #Primero: Limpiar el resto de etiquetas HTML

        (r"</section>", r"", 0),
        (r"</article>", r"", 0),
        (r"</body>", r"", 0),
        (r"</html>", r"", 0),

        (r'<div property="organization">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="authors">(.+?)</div>', r"\1", re.DOTALL),
        
        (r'<div class="doi">(.+?)</div>', r"\1", re.DOTALL),
        
        (r'<div class="core-affiliations">(.+?)</div>', r"\1", re.DOTALL),
        (r'<sup class="xref">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="core-exomatter" lang="en">', r"", re.DOTALL),
        (r'<a href="#corresp1-fn1" role="doc-noteref" epub:type="noteref">(.+?)</div>', r"\1", re.DOTALL),


        #Cambiar título, autores y datos de la revista

        (r"Número 24", r"Volúmen 1, capítulo 3", 0),
        (r"Perífrasis", r"Ideas y creaciones literarias en portugues y español", 0),
        (r"ISSN 2145-8987, E-ISSN 2145-9045", r"ISSN 3333-4444, E-ISSN 1111-999", 0),
        (r'<div property="author" typeof="sa:ContributorRole">(.+?)</div>', r"Autores: Dominguina Ritacuba, Paulina Perea, Alfonso Fernandez Prieto", re.DOTALL),
        

        #H2 de la parte inferior y énfasis
        (r"<h2>(.+?)</h2>", r"\n## \1\n", 0),

        (r'<em>(.+?)</em>', r"*\1*", 0),
        (r"\n{3,}", r"\n", 0),

        #Cuarto: Bibliografía

        (r"<div .+?>(.+?)</div>", r"\n- \1\n", 0),
        (r'<em>(.+?)</em>', r"*\1*", 0),

        (r"</?div>", r"", 0),
        (r'<div role="doc-biblioentry" epub:type="biblioentry">', r"", 0),
        (r"<a href=", r"\(", 0),
        (r"</a>", r"\)", 0),
        (r'<div class="labeled" role="doc-footnote" epub:type="footnote">', r"", 0),
       
     

        # (r"</?[body|header|article] .+?>", r"", 0),        # (r"", r"", 0),
        # (r"</?article .+?>", r"", 0),        # (r"", r"", 0),
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

    with open(archivo_de_entrada, encoding="utf8") as f:
        datos_originales = f.read()

    datos_nuevos = reemplazar(datos_originales)

    with open(archivo_de_salida, "w", encoding="utf8") as f:
        f.write(datos_nuevos)


if __name__ == "__main__":
    main()
