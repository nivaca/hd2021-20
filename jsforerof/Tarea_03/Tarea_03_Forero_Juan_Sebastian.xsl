<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tei="http://www.tei-c.org/ns/1.0"  
    exclude-result-prefixes="tei"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    version="3.0">
    
<xsl:output method="text"/>
<!--Espacios en blanco-->
<xsl:template match="text()">
<xsl:value-of select="replace(., '\s+', ' ')"/>
</xsl:template>
    
<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>
 
<!--Quitar información del publicationStmt-->
 <xsl:template match="publicationStmt">
<!--<xsl:apply-templates/>-->
</xsl:template>

<!--Eliminar contenido de "author" texto-->
<xsl:template match="author">
<!--<xsl:apply-templates/> -->
</xsl:template>
    
<!--"sourceDesc"-->
<xsl:template match="sourceDesc">
<xsl:text>
    
</xsl:text>
    
<xsl:apply-templates/> 
</xsl:template>
      
<!--Colocar el título -->
<xsl:template match="title[parent::titleStmt]">
#<xsl:apply-templates/>
</xsl:template>
    
<!--Quitar la etiqueta "text" y mantener el texto-->
<xsl:template match="text">
<xsl:apply-templates/>
</xsl:template>

<!--Quitar la etiqueta body y mantener el texto-->
<xsl:template match="body">
<xsl:apply-templates/>
</xsl:template>
    
<!--Eliminar la etiqueta "foreing" y colocar el contenido en itálicas-->
<xsl:template match="foreign">
<xsl:text>*</xsl:text>
<xsl:apply-templates/>
<xsl:text>*</xsl:text>
</xsl:template>
    
<!--Seleccionar "div", recuperar el texto y separar cada div con un salto de línea.-->
<xsl:template match="div"> 
<xsl:text>
</xsl:text>
<xsl:apply-templates/>
</xsl:template> 
    
<!--Seleccionar "lb", recuperar el texto y separar cada salto de línea con espacios.-->
<xsl:template match="lb"> 
 <xsl:text>
 </xsl:text>
<xsl:apply-templates/>
</xsl:template> 

<!--Cambiar el marcado "q" por las comillas "«»"-->
<xsl:template match="q">
<xsl:text>«</xsl:text>
<xsl:apply-templates/>
<xsl:text>»</xsl:text>
</xsl:template>

<!--mantener el contenido de la etiqueta "persName"-->
<xsl:template match="persName">
<xsl:apply-templates/>
</xsl:template>
 
<!--Eliminar el contenido que está entre los marcadores TEI de "expan"-->
<xsl:template match="expan"> 
<!--<xsl:apply-templates/>-->
</xsl:template>
    
 
<!--Mantener la palabra "tiene" y tachar la palabra "tuvo"-->
<xsl:template match="del"> 
<xsl:text>~~</xsl:text>
<xsl:apply-templates/>
<xsl:text>~~ </xsl:text>  
</xsl:template>  
    
<!--Seleccionar "div type="impreso", recuperar el texto y separar cada div con un salto de línea.-->
<xsl:template match="div [@type='impreso']"> 
<xsl:text>

</xsl:text>
<xsl:apply-templates/>
</xsl:template> 
    
</xsl:stylesheet>