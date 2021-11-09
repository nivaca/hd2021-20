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
  
  <xsl:template match="teiheader">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="fileDesc">  
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="titleStmt">  
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="title[parent::p]">  
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="persName">  
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="author">  
    <xsl:text>
      ##</xsl:text>
    <xsl:apply-templates/>
    <xsl:text></xsl:text>
  </xsl:template>
  
  <xsl:template match="publicationStmt">
    <xsl:text> 
</xsl:text>
    <xsl:apply-templates/>
    <xsl:text> 
</xsl:text>
  </xsl:template>
  
  <xsl:template match="p">
    <xsl:text>

    </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="name">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="date[@when-iso='2021-10-29']">
    <xsl:text>

    </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="sourceDesc">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="ref">
    <xsl:text>[</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>]</xsl:text>
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
    <xsl:text> &#xa; 
    </xsl:text>
    
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="lb">
    <xsl:text>
    </xsl:text>
    <xsl:apply-templates/>
    <xsl:text></xsl:text>
  </xsl:template>
  
  <xsl:template match="foreign[@xml:lang='fra']">
    <xsl:text>*</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>*</xsl:text>
  </xsl:template>
  
  <xsl:template match="closer">
    <xsl:text>
    </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="del">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="add">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="corr">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="signed">
    <xsl:text>
    </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="q">
    <xsl:text>"</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>"</xsl:text>
  </xsl:template>
  
  <xsl:template match="gap[@reason='illegible']">
    <xsl:text>\{?</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>\} </xsl:text>
  </xsl:template>
  
  <xsl:template match="abbr">
    <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="expam">
    <xsl:apply-templates/>
  </xsl:template>
 
  <xsl:template match="num">
    <xsl:apply-templates/>
  </xsl:template>

</xsl:stylesheet>