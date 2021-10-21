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
        
                                        # Eliminar el marcado de HTML del documento
        
        # Eliminar la marca <head> 
        (r"<head>.+</head>", r"", re.DOTALL),

         
        # Eliminar las marcas <span>
        # Cambiar el número de la publicación
        (r'(<div property="isPartOf".+?>).+?(</div>)', r"Vol. 107, no. 2", re.DOTALL),    
            # Cambiar el nombre de la revista
        (r'<span property="isPartOf".+?>.+?</span>', r"International Journal of Cancer\n", re.DOTALL), 
            # Cambiar la fecha de publicación de la revista
        (r'<span property="datePublished">.+?</span>', r"                21 de Julio de 2003\n", re.DOTALL),  
            # Cambiar la páginación de la publicación
        (r'<span property="pagination">.+?</span>', r"                P.283-284", re.DOTALL), 
            # Cambiar el ISSN por el DOI de la publicación
        (r'<span class="printIssn">.+?</span>', r"DOI: 10.1002/ijc.11382", re.DOTALL), 
            # Eliminar el ISSN online
        (r'<span class="onlineIssn">.+?</span>', r"", 0),
            # Eliminar etiquetas de span que quedaron sueltas
        (r"(<span .+?>)(.+?)(</span>)", r"", 0),        
        (r"(</span>)(.+?)(</span>)", r"\2", 0), 
        (r"(</span>)(.+?)(</span>)", r"\2", 0),
        (r'</span>', r"", 0),
       

        # Eliminar las marcas <body>, <html>, <article>, <section> y <header>
        (r"</?html.+?>", r"", 0),
        (r"</?body.+?>", r"", 0),
        (r"</?article.+?>", r"", 0),
        (r"</?section.+?>", r"", 0),
        (r"</?header>", r"", 0),
        
        # Reemplazar los marcadores <h1> y <h2> por los marcadores en Markdown de título (#) y subtítulo (##)
        (r"<h1 .+?>.+?</h1>", r"Does Pizza Protect Against Cancer?\n", 0), # Modificar el título del artículo
        (r"<h2 .+?>(.+?)</h2>", r"## \1", 0),

        # Crear una lista no numerada usando viñetaas con las intervenciones que hay en el artículo
        (r'<div role="paragraph"><b>Lina Gabriela Cortés:</b>(.+?)</div>', r"-**Lina Gabriela Cortés:**\1\n", 0),
        (r'<div role="paragraph"><b>Fabián Severo:</b>(.+?)</div>', r"-**Fabián Severo:**\1\n", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Lauren Berlant(.+?)</div>', r"-**Cortés:** Lauren Berlant\1\n", 0),
        (r'<div role="paragraph"><b>Severo</b>: Arnaldo Antunes(.+?)</div>', r"-**Severo:** Arnaldo Antunes\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Y en ese universo(.+?)</div>', r"-**Cortes:** Y en ese universo\1\r", 0),
        (r'<div role="paragraph"><b>Severo</b>: Si iba a hablar(.+?)</div>', r"-**Severo:** Si iba a hablar\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Con relación(.+?)</div>', r"-**Cortes:** Con relación\1\r", 0),
        (r'<div role="paragraph"><b>Severo:</b> ¿Vos sabés(.+?)</div>', r"-**Severo:** ¿Vos sabés\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Sobre este(.+?)</div>', r"-**Cortes:** Sobre este\1\r", 0),
        (r'<div role="paragraph"><b>Severo</b>: Mirá,(.+?)</div>', r"-**Severo:** Mirá,\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> La frontera(.+?)</div>', r"-**Cortes:** La frontera\1\r", 0),
        (r'<div role="paragraph"><b>Severo</b>: ¿Vos(.+?)</div>', r"-**Severo:** ¿Vos\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> ¿Podríamos(.+?)</div>', r"-**Cortés:** ¿Podríamos\1\r", 0),
        (r'<div role="paragraph"><b>Severo:</b> El portuñol es(.+?)</div>', r"-**Severo:** El portuñol es\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> El exilio(.+?)</div>', r"-**Cortés:** El exilio\1\r", 0),
        (r'<div role="paragraph"><b>Severo:</b> Claro, por(.+?)</div>', r"-**Severo:** Claro, por\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Frente(.+?)</div>', r"-**Cortés:** Frente\1\r", 0),
        (r'<div role="paragraph"><b>Severo</b>: Claro, sí,(.+?)</div>', r"-**Severo:** Claro, sí,\1\r", 0),
        (r'<div role="paragraph"><b>Cortés:</b> Esta influencia(.+?)</div>', r"-**Cortés:** Esta influencia\1\r", 0),
        (r'<div role="paragraph"><b>Severo:</b> Sí, a mí(.+?)</div>', r"-**Severo:** Sí, a mí\1\r", 0),


        # Convertir las citas en formato de citas de Markdown (>)
        #(r'\“(.+?)\”', r" \n >\1\n", re.DOTALL),
        
        (r'\“Hijo, no me hagas (.+?)\” \(28\).', r" \n> Hijo, no me hagas \1 (28).\n ", 0),
        (r'\“si yo vengo de (.+?)\”.', r" \n> si yo vengo de \1.\n", 0),
        (r'\“Vo iscrevé (.+?)\”', r" \n> Vo iscrevé \1", 0),
        (r'\“Voy a escribir (.+?)\”.', r" \n> Voy a escribir \1.\n", 0),      
        (r'\“Miséria (.+?)\”.', r" \n> Miséria \1.\n", 0),      
        (r'\“pensá en positivo que (.+?)\”.', r" \n> pensá en positivo que \1.\n", 0),      
        (r'\“Fabián Severo es el referente que reivindica el portuñol\”', r" \n> Fabián Severo es el referente que reivindica el portuñol", 0),
        (r'\“Mi madre (.+?)\” \(56\).', r" \n> Mi madre \1 (56).\n", 0),
        (r'\“En mi cuadra, lo que sobra es madre\”', r" \n> En mi cuadra, lo que sobra es madre\n", 0),
        (r'\“En mi cuadra, lo que falta es padre\”', r" \n> En mi cuadra, lo que falta es padre\n", 0),
        (r'\“Queim (.+?)\” \(15\),', r" \n> Queim \1 (15),\n", 0),
        (r'\“Artigas e uma (.+?)\” \(21\).', r" \n> Artigas e uma \1 (21).\n", 0),
        (r'\“el río me saco tres veces\”', r" \n> el río me saco tres veces", 0),
        (r'\“pero no me va a correr de acá\”', r" \n> pero no me va a correr de acá\n", 0),
        (r'\“Nací perdiendo (.+?)\”', r" \n> Nací perdiendo \1\n", 0),
        (r'\“Dios creó el mundo en Artigas. (.+?)”,', r" \n> Dios creó el mundo en Artigas. \1,", 0),
        (r'\“Para mí, (.+?)\” \(66\)', r" \n> Para mí, \1 (66).\n", 0),
        (r'\“Ah no, (.+?)\”,', r" \n> Ah no, \1,\n", 0),
        (r'\“Bueno, (.+?)\”,', r" \n> Bueno, \1,\n", 0),
        (r'\“Fabi, no encontré (.+?)\”,', r" \n> Fabi, no encontré \1,\n", 0),
        (r'\“Fabián, ¿por (.+?)\”,', r" \n> Fabián, ¿por \1,\n", 0),
        (r'\“¿A vos te parece (.+?)\”.', r" \n> ¿A vos te parece \1.\n", 0),
        (r'\“Artigas se enllenó (.+?)\”', r" \n> Artigas se enllenó \1", 0),
        (r'\“pará, este (.+?)\”.', r" \n> pará, este \1.\n", 0),
        (r'\“El río Cuareim (.+?)\” \(23\).', r" \n> El río Cuareim \1 (23).\n", 0),
        (r'\“Fabi, no llevés (.+?)\”.', r" \n> Fabi, no llevés \1.\n", 0),
        (r'\“No seré yo quien (.+?)\”.', r" \n> No seré yo quien \1.\n", 0),
        

        # Eliminar los marcadores de párrafos en marcado html para pasarlos a Markdown
        (r'<div role="paragraph">(.+?)</div>', r"\1\n", 0),
                    
                #Eliminar distintos marcadores html del documento y reemplazar datos y metadatos
        (r'<div class="logo">.+?</div>', r"", 0),
        (r'<div id="masthead">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="masthead-info">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div class="citation long">(.+?)</div>', r"\1", re.DOTALL),
        (r'<div property="isPartOf" .+?>(.+?)</div>', r"\1", re.DOTALL),
        (r"<\?.+?\?>", r"", 0),
        (r"<!DOCTYPE.+?>", r"", 0),
        (r" *\n", r"\n", 0),
        (r'<div property="organization">(.+?)</div>', r"\1", 0),
            # Cambiar el nombre de los autores
        (r'<div class="authors">.+?</div>', r"Silvano Gallus, Cristina Bosetti, Eva Negri, Renato Talamini, Maurizio Montella, Ettore Conti, Silvia Franceschi, Carlo La Vecchia", re.DOTALL),
        (r'<div class="core-affiliations">(.+?)</div>', r"\1", 0),
        (r'<div property="author" .+?>(.+?)</div>', r"\1", re.DOTALL),
        (r'<sup class="xref">.+?</sup>', r"", 0),
        (r'<div class="doi">(.+?)</div>', r"\1", 0),
        (r'<a href="https://doi.org/10.25025/perifrasis202112.24.07" .+?>(.+?)</a>', r"DOI: 10.1002/ijc.11382", 0),
        (r'</div>', r"", 0),
        (r'<div class="article-notes">', r"", 0),
        (r'<div class="history">', r"", 0),
            # Cambiar palabras clave en español
        (r'<div id="keywords".+?>', r"Digestive tract cancers; lycopene; pizza; risk factors.\n", 0),
        (r': , , , ,', r"", 0), #Elimina las comas que separan las palabras clave en el artículo original
        (r'<div class="core-exomatter" .+?>', r"", 0),
        (r'<div property="name" .+?>', r"", 0),
            # Cambiar palabras clave en inglés
        (r'<div id="keywords-en" .+?>', r"Digestive tract cancers; lycopene; pizza; risk factors.\n", 0),
        (r'</section>(.+?)</section>', r"\1", re.DOTALL),
                
                #Cambiar más de tres espacios en blanco por sólo uno
        (r"\n{3,}", r"\n", 0),
             
                #Cambiar el marcado hmtl de cursivas (i) y negritas (b) al marcado de estas en Markdown (cursivas: *; negritas: **)
        (r'<i>(.+?)</i>', r"*\1*", 0),
        (r'<b>(.+?)</b>', r"**\1**", 0),

        #Cambiar el título del abstract 
        (r"VERSES \*MIXTURADOS\* ON THE URUGUAYAN BORDER: A CONVERSATION WITH FABIÁN SEVERO", r"Does Pizza Protect Against Cancer?", re.DOTALL),
                                                                                    
                                            #TRABAJO CON LA BIBLIOGRAFÍA

        #Cambiar el marcador <h2> de la BIBLIOGRAFÍA
        (r"<h2>BIBLIOGRAFÍA</h2>", r"## REFERENCIAS", 0),
        
        (r'<div role="doc-biblioentry" .+?>', r"", re.DOTALL),

        # Referencia 1   
        (r'<div id="R1" .+?>', r"- Berlant, Lauren. “Intimidad”. Revista Transas. Letras y artes de América Latina, traducido por Julia Kratje y Mónica Szumurk, 2020, https://t.ly/F9P0.", 0), 

        # Referencia 2   
        (r'<div id="R2" .+?>', r"- “Brasileirinho - Maria Bethânia (Show Completo) hd”. Youtube, subido por Noandro Meneses, 1 de enero de 2014, https://t.ly/vEUf.", 0),
            
        # Referencia 3   
        (r'<div id="R3" .+?>', r"- “Caetano Veloso - Oração Ao Tempo (Ao Vivo)”. Youtube, subido por Caetano Veloso, 30 de mayo de 2018, https://t.ly/5Rqa.", 0),
        
        # Referencia 4
        (r'<div id="R4" .+?>', r"- Foffani, Enrique. “La frontera Uruguay-Brasil: Fabián Severo. El poeta sin gramática”. Katatay, año viii, núm. 10, 2012, pp. 43-67.", 0),

        # Referencia 5
        (r'<div id="R5" .+?>', r"- Gasparini, Pablo. “Néstor Perlongher. Una extraterritorialidad en gozoso portuñol”. Revista iberoaméricana, vol. lxxxvi, núm. 232-233, 2010, pp. 757-775. Crossref.", 0),

        # Referencia 6
        (r'<div id="R6" .+?>', r"- Johansson, Ellinor. “Antes, eu quería ser uruguaio, agora, quiero ser daqui. Un análisis sobre actitudes lingüísticas en poemas y canciones escritos en portuñol”. Institutionen för Språk Och Litteraturer, 2018, pp. 1-36.", 0),

        # Referencia 7
        (r'<div id="R7" .+?>', r"- “Miséria”. Youtube, subido por Titãs (Oficial), 14 de enero de 2017, https://youtu.be/SHwoxlD24zM.", 0),

        # Referencia 8
        (r'<div id="R8" .+?>', r"- “Onde Eu Nasci Passa Um Rio”. Youtube, subido por Gal Costa-Tema, 31 de julio 2018, https://t.ly/EkRD.", 0),

        # Referencia 9
        (r'<div id="R9" .+?>', r"- Perlongher, Néstor. “El portuñol en la poesía”. Tse Tse, núm. 7-8, 2000, pp. 254-259.", 0),

        # Referencia 10
        (r'<div id="R10" .+?>', r"- Peyrou, Rosario. “La frontera norte en el imaginario cultural”. Revista uruguaya de psicoanálisis, núm. 113, 2011, pp. 156-167.", 0),

        # Referencia 11
        (r'<div id="R11" .+?>', r"- Ribeiro, Djamila. O que é lugar de fala? Letramento, 2017.", 0),

        # Referencia 12
        (r'<div id="R12" .+?>', r"- Severo, Fabián. Noite nu Norte. Rumbo Editoria, 2011.", 0),

        # Referencia 13
        (r'<div id="R13" .+?>', r"- ---. Sepultura. La Canoa, 2020.", 0),

        # Referencia 14
        (r'<div id="R14" .+?>', r"- ---. Viento de Nadie. Rumbo Editorial, 2013.", 0),

        # Referencia 15
        (r'<div id="R15" .+?>', r"- ---. Viralata. Estuario, 2018.", 0),

        # Referencia 16
        (r'<div id="R16" .+?>', r"- Sturza, Eliana. “Línguas de fronteira: o desconhecido território das práticas linguisticas nas fronteiras brasileiras”. Revista ciencia e cultura, vol. 57, núm. 2, 2005, pp. 47-50.", 0),

        # Referencia 17
        (r'<div id="R17" .+?>', r"- Winikor, María. “Vivir la frontera. Prácticas sociales y culturales desde los márgenes”. Estudios fronterizos, nueva época, vol. 17, núm. 34, 2016, pp. 100-116. Crossref.", 0),
        (r'<a href="https.+?>.+?</a>', r"", 0),
     
        # Eliminar las marcas HTML de las notas del final
        (r"<h2>Notas</h2>", r"## NOTAS", 0),
        (r'<div .+?>', r"", re.DOTALL),
        (r'<a href=.+?>(.+?)</a>', r"Correo electrónico:\1", 0),
        (r'</section>', r"", 0),
        (r'</article>', r"", 0),
        (r'</body>', r"", 0),
        (r'</html>', r"", 0),
        # Eliminar espacios en blanco que entran en conflicto con el sistema de marcación MARKDOWN
        (r'/^\s+|\s+$|\s+(?=\s)/g', r"",re.DOTALL),
                   
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
