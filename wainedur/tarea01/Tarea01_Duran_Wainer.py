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

        (r"<head>.+</head>", r"\n", re.DOTALL),

        (r"(<span.+?>)(.+?)(</span>)", r"\2", 0),
        (r"(<span.+?>)(.+?)(</span>)", r"\2", 0),
        (r"(<span.+?>)(.+?)(</span>)", r"\2", 0),

        (r"</?html.*?>", r"", 0),
        (r"</?body.*?>", r"", 0),
        (r"</?article.*?>", r"", 0),
        (r"</?section.*?>", r"", 0),
        (r"</?header.*?>", r"", 0),

        (r"<h1 .+?>(.+?)</h1>", r"\n# \1\n", 0),
        (r"<h2 .+?>(.+?)</h2>", r"\n## \1\n", 0),

        (r'<div role="paragraph"(.+?)</div>', r"\n\1", 0),

        (r'<div class="logo">.+?</div>', r"", 0),

        (r'<div id="masthead">(.+?)</div>', r"\n\1\n", re.DOTALL),

        (r'<div class="masthead-info">(.+?)</div>', r"\n\1\n", re.DOTALL),

        (r'<div class="citation long">(.+?)</div>', r"\n\1\n", re.DOTALL),

        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),


        (r"<i>(.+?)</i>", r"*\1*", 0),
        (r"<b>(.+?)</b>", r"**\1**", 0),

        (r"<\?.+?\?>", r"", 0),
        (r"<!DOCTYPE.+?>", r"", 0),

        (r" *\n", r"\n", 0),
        (r"\n{3,}", r"\n\n\n", 0),
        
        
        # Tarea

        (r'<div class="authors">(.+?)</div>', r"\n\1\n", re.DOTALL),

        (r'<div property="author" typeof="sa:ContributorRole">(.+?)</div>', r"\1", re.DOTALL),

        (r'<sup class="xref">(.+?)</sup>', r"[^*]\1", re.DOTALL),

        (r'<a href="#corresp1-fn1" role="doc-noteref" epub:type="noteref">.+?</a>', r"", 0),

        (r'<div class="core-affiliations">(.+?)</div>', r"\n\1", re.DOTALL),
        
        (r'<div property="organization">(.+?)</div>', r"\n\1", re.DOTALL),

        (r'<div class="doi">(.+?)</div>', r"\n\1", re.DOTALL),

        (r'<div class="article-notes">(.+?)</div>', r"\n\1", re.DOTALL),
 
        (r'<div class="history">(.+?)</div>', r"\n\1", re.DOTALL),

        (r'<a href="https://doi.org/10.25025/perifrasis202112.24.07" property="sameAs">(.+?)</a>', r"\1", 0),

        (r'<div id="keywords" property="keywords" epub:type="keywords">(.+?)</div>', r"\n\1", re.DOTALL),
        
        (r'<div class="core-exomatter" lang="en">(.+?)</div>', r"\n\1", re.DOTALL),
        
        (r'<div property="name" epub:type="title">(.+?)</div>', r"\n\1", re.DOTALL),

        (r'<div id="keywords-en" property="keywords" epub:type="keywords">(.+?)</div>', r"\n\1", re.DOTALL),
        


        # Bibliografía

        (r'<h2>(.+?)</h2>', r"\1\n", 0),

        (r'<div role.+?>(.+?)</div>', r"\n\1\n", re.DOTALL),
        
        (r'<div id.+?>(.+?)</div>', r"-\1", re.DOTALL),

        (r"<em>(.+?)</em>", r"*\1*", 0),
                     

        # Notas

        (r'<div class="labeled" role="doc-footnote" epub:type="footnote">(.+?)</div>', r"\n\1\n", re.DOTALL),
        
        (r'<a.+?>(.+?)</a>', r"(\1)", 0),

        (r'<div class="label">*(.+?)</div>', r"\1", re.DOTALL),

        
        # Disposición  

        (r"\n\n\n", r"\n\n", 0),
        
        (r" {5,16}", r"", 0),

        (r"\n{3,8}", r"\n\n", 0),

        



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

    with open(archivo_de_entrada, encoding="utf8") as f:
        datos_originales = f.read()

    datos_nuevos = reemplazar(datos_originales)

    with open(archivo_de_salida, "w", encoding="utf8") as f:
        f.write(datos_nuevos)


if __name__ == "__main__":
    main()
