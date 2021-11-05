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

<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="teiHeader">
</xsl:template>

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
<xsl:text>
</xsl:text>
</xsl:template>

<xsl:template match="lb">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="lb[@break='no']">
<xsl:text>⦑no-brake⦒</xsl:text>
</xsl:template>

<xsl:template match="persName | title">
<xsl:value-of select="upper-case(.)" />
</xsl:template>

<xsl:template match="persName[parent::signed]">
<xsl:text>--</xsl:text>
<xsl:value-of select="upper-case(.)" />
<xsl:text>--</xsl:text>
</xsl:template>

<xsl:template match="foreign">
<xsl:text>〘</xsl:text>
<xsl:value-of select="@xml:lang"/>
<xsl:text>〙</xsl:text>
<xsl:text>*</xsl:text>
<xsl:apply-templates/>
<xsl:text>*</xsl:text>
</xsl:template>

<xsl:template match="closer">
<xsl:text>

</xsl:text>
<xsl:apply-templates/>
<xsl:text>

</xsl:text>
</xsl:template>

<xsl:template match="signed">
<xsl:text>**</xsl:text>
<xsl:apply-templates/>
<xsl:text>**</xsl:text>
</xsl:template>

<xsl:template match="gap">
<xsl:text>᚜</xsl:text>
<xsl:value-of select="@reason "/>
<xsl:text>᚛ </xsl:text>
</xsl:template>

<xsl:template match="unclear">
<xsl:text>(¿)</xsl:text>
<xsl:apply-templates/>
<xsl:text>(?)</xsl:text>
</xsl:template>

<xsl:template match="q">
<xsl:text>«</xsl:text>
<xsl:apply-templates/>
<xsl:text>»</xsl:text>
</xsl:template>

<xsl:template match="choise">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="expan">
</xsl:template>

<xsl:template match="abbr">
<xsl:text>***</xsl:text>
<xsl:apply-templates/>
<xsl:text>***</xsl:text>
</xsl:template>

<xsl:template match="num">
<xsl:text>≈</xsl:text>
<xsl:apply-templates/>
<xsl:text>≈</xsl:text>
</xsl:template>
  
  <xsl:template match="num[@value='177']">
    <xsl:text>≔Valor: </xsl:text>
    <xsl:value-of select="@value"/>
    <xsl:text>≕ </xsl:text>
  </xsl:template>

<xsl:template match="del[@rend='tachado']">
</xsl:template>

<xsl:template match="subst">
<xsl:text>{subst}</xsl:text>
<xsl:apply-templates/>
<xsl:text>{/subst}</xsl:text>
</xsl:template>
  
  <xsl:template match="corr">
    <xsl:text>{corr}</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>{/corr}</xsl:text>
  </xsl:template>

</xsl:stylesheet>