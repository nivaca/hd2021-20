#!user/bin/env python3

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

        (r"<span .+?>(.+?)</span>", r"\1", 0),
        (r"<span .+?>(.+?)</span>", r"\1", 0),
        (r"<span .+?>(.+?)</span>", r"\1", 0),

        #-(r"</?article.+?>(.+?)</article>", r"", re.DOTALL),

        #-(r"<body .+?>", r"", 0),
        #-(r"</body>", r"", 0),

        (r"</?html.+?>", r"", 0),
        (r"</?body.+?>", r"", 0),
        (r"</?article.+?>", r"", 0),
        (r"</?section.+?>", r"", 0),
        (r"</?header>", r"", 0),
 
        #al final 
       
        (r"</?/html>", r"", 0),
        (r"</?/body>", r"", 0),
        (r"</article>", r"", 0),
        (r"</?/section>", r"", 0),
        

#------------------------------------------------ 

        (r'<i>(.+?)</i>', r"*\1*", 0),
        (r'<b>(.+?)</b>', r"**\1**", 0),
       

        (r"<\?.+?\?>", r"", 0),

        (r"<!DOCTYPE.+?>", r"", 0),

        #Espacios en blanco 
        (r" *\n", r"\n", 0),
        (r"\n{3,}",r"\n\n\n", 0),

        (r"<h1 .+?>(.+?)</h1>", r"\n#\1\n", 0),
        (r"<h2 .+?>(.+?)</h2>", r"\n##\1\n", 0),

        #bibliográfia - notas 
        (r"<h2>(.+?)</h2>", r"\n##\1\n", 0),
        
        (r'<div role="paragraph">(.+?)</div>', r"\n\1\n", 0), 

        (r'<div class="logo">.+?</div>', r"", 0),

        (r'<div id="masthead">(.+?)</div>', r"\n\1\n", re.DOTALL),
        (r'<div class="masthead-info">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="citation long">(.+?)</div>', r"\1", re.DOTALL),

        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),

        #autor
        (r'<div class="history".+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<sup class="xref".+?>()</sup>', r"", 0),

        (r'<div class="authors".+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="core-affiliations".+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="doi">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="article-notes">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="history">(.+?)</div>', r"\1", re.DOTALL),
        

        #palabras claves
        (r'<div id="keywords-en" .+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<div id="keywords" .+?>(.+?)</div>', r"\1", re.DOTALL),

        (r'<div property="name" .+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="core-exomatter" .+?>(.+?)</div>', r"\1", re.DOTALL),
        

        #bibliografia 
        (r'<div role="doc-biblioentry" .+?>(.+?)</div>', r"\1", re.DOTALL),

        (r'<em>(.+?)</em>', r"*\1*_", 0),
        (r'<a href=.+?>(.+?)</a>', r"(\1)", 0), 
        (r'<a href=.+?>(.+?)</a>', r"(\1)", 0), 
    

        #listas bibliografía:
        (r'<div id="R1" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R2" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R3" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R4" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R5" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R6" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R7" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R8" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R9" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R10" class="citations">(.+?)</div>', r"-\1", re.DOTALL),(r'<div id="R11" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R12" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R13" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R14" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R15" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R16" class="citations">(.+?)</div>', r"-\1", re.DOTALL),
        (r'<div id="R17" class="citations">(.+?)</div>', r"-\1", re.DOTALL),

        #nota
        (r'<div class="labeled" role="doc-footnote" .+?>(.+?)</div>', r"\1", re.DOTALL),

        (r'<div class="label".+?>(.+?)</div>', r"\1", re.DOTALL),

        
        #(r'div property="author" typeof="sa:ContributorRole">(.+?)</div>', r"\1", re.DOTALL),

        (r"<\?.+?\?>", r"", 0),
        (r"<!DOCTYPE.+?>", r"", 0),

        #Espacios en blanco 
        (r" *\n", r"\n", 0),
        (r"\n{2,}",r"\n\n", 0),


        #--------
        (r"</div>", r"", 0),



        #(r"<body .+?>(.+?)</body>", r"\1", re.DOTALL)


        #(r"(<span .+?>)(.+?)(</span>"), r"\2", 0),


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
