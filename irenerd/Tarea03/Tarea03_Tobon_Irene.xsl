<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:tei="http://www.tei-c.org/ns/1.0"  
  exclude-result-prefixes="tei"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0"
  version="3.0">
  
  <xsl:output method="text"/>
  
  <xsl:template match="text()">
    <xsl:value-of select="replace(., '\s+', ' ')"/>
  </xsl:template>
  
  <!--acá empieza el proceso desde el inicio del documento para sacar el contenido de texto-->
  
  <xsl:template match="/">
    <xsl:apply-templates/>
  </xsl:template>
  
  <!--Acá voy a quitar el contenido del header -->
  <xsl:template match="teiHeader">
  </xsl:template>
  
  <!--Acá voy a modificar el contenido del Text -->
  
  <xsl:template match="text">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="body">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="div">
    <xsl:apply-templates/>
  </xsl:template>
  
  
  
  <xsl:template match="p">
    <xsl:text>
      
    </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>
  
  
  <xsl:template match="persName|name">
    <xsl:value-of select="upper-case(.)"/>
  </xsl:template>
  
  <!-- Títulos en itálicas y negrillas-->
  
  <xsl:template match="title">
    <xsl:text>***</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>***</xsl:text>
  </xsl:template>
  
  <xsl:template match="q">
    <xsl:text>"</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>"</xsl:text>
  </xsl:template>
  
  <xsl:template match="foreign"> 
    <xsl:text>*</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>*</xsl:text>
  </xsl:template>
  
  <!-- capturo los saltos de línea-->
  
  <xsl:template match="lb"> 
    <xsl:text>  &#xa;</xsl:text>
  </xsl:template>
  
  <!-- capturo los expan que son hijos de choice-->
  
  
  <xsl:template match="expan[parent::choice]">   
  </xsl:template>
  
  <!-- la firma en itálicas-->
  
  <xsl:template match="signed[parent::closer]">
    <xsl:text>*</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>*</xsl:text>
  </xsl:template>  
  
  
</xsl:stylesheet>
  