<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:tei="http://www.tei-c.org/ns/1.0"  
exclude-result-prefixes="tei"
xpath-default-namespace="http://www.tei-c.org/ns/1.0"
version="3.0">

<xsl:output method="text"/>
  
<!-- Mi intención no fue presentar el texto original de la manera más fiel posible, sino intentar replicar la forma en que uso LaTeX más frecuentemente. Tuve unos problemas con los metadatos y aunque se me ocurrieron algunas soluciones, dudo que sean las más elegantes. -->

<xsl:template match="text()">
<xsl:value-of select="replace(., '\s+', ' ')"/>
</xsl:template>

<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="teiHeader">
<xsl:text>
\documentclass[12pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{comment}
\usepackage{graphicx}
\usepackage{glossaries}
\usepackage{afterpage}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{enumerate}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage{setspace}
\doublespacing
\usepackage{etoolbox}
\AtBeginEnvironment{quote}{\singlespacing\small}
\usepackage{cleveref}
\crefformat{section}{\S#2#1#3} % see manual of cleveref, section 8.2.1
\crefformat{subsection}{\S#2#1#3}
\crefformat{subsubsection}{\S#2#1#3}
% https://tex.stackexchange.com/questions/208933/how-to-show-symbol-when-i-refer-a-chapter&#xa;
</xsl:text>
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="titleStmt">
<xsl:text>&#xa;\title{Dedicatoria de un libro de Alejandra Pizarnik a Julio Cortázar}&#xa;</xsl:text>
<xsl:text>&#xa;\author{Alejandra Pizarnik}&#xa;</xsl:text>
</xsl:template>

<xsl:template match="persName">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="author">
<xsl:text>&#xa;\author{</xsl:text>
<xsl:apply-templates/>
<xsl:text>}&#xa;</xsl:text>
</xsl:template>

<xsl:template match="publicationStmt">
</xsl:template>

<xsl:template match="sourceDesc">
<xsl:text>
&#xa;\date{Septiembre de 1972}&#xa;
</xsl:text>
</xsl:template>

<xsl:template match="text">
<xsl:text>&#xa;\begin{document}&#xa;</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;\end{document}&#xa;</xsl:text>
</xsl:template>

<xsl:template match="body">
<xsl:text>
\maketitle&#xa; \newpage&#xa;
</xsl:text>
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="div[@type='manuscrito']">
<xsl:text>&#xa;\section{Manuscrito}</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="div[@type='impreso']">
<xsl:text>&#xa;\section{Impreso}</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="p">
<xsl:text>&#xa;</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="lb">
<xsl:text>&#xa;</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;</xsl:text>
</xsl:template>


<xsl:template match="foreign">
<xsl:text>\textit{</xsl:text>
<xsl:apply-templates/>
<xsl:text>}</xsl:text>
</xsl:template>

<xsl:template match="title">
<xsl:text>\textit{</xsl:text>
<xsl:apply-templates/>
<xsl:text>}</xsl:text>
</xsl:template>

<xsl:template match="closer">
<xsl:text>&#xa;</xsl:text>
<xsl:apply-templates/>
<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="corr">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="signed">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="gap">
<xsl:text>[ilegible] </xsl:text>
</xsl:template>

<!-- <xsl:template match="q">
<xsl:text>\begin{quote}</xsl:text>
<xsl:apply-templates/>
<xsl:text>\end{quote}</xsl:text>
</xsl:template> --> 

<xsl:template match="q">
<xsl:text>"</xsl:text>
<xsl:apply-templates/>
<xsl:text>"</xsl:text>
</xsl:template>

<xsl:template match="unclear">
<xsl:text>[</xsl:text>
<xsl:apply-templates/>
<xsl:text>]</xsl:text>
</xsl:template>

<xsl:template match="choice">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="abbr">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="expan">
</xsl:template>

<xsl:template match="num">
<xsl:text>$</xsl:text>
<xsl:apply-templates/>
<xsl:text>$</xsl:text>
</xsl:template>

<xsl:template match="subst">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="add">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="del">
</xsl:template>

</xsl:stylesheet>