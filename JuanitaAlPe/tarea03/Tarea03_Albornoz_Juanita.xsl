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
<xsl:apply-templates/>    </xsl:template>
  
<xsl:template match="text">
<xsl:apply-templates/>    </xsl:template>
  
<xsl:template match="body">
<xsl:apply-templates/>    </xsl:template>
  
<xsl:template match="div">
<xsl:apply-templates/> 
</xsl:template>

  
<xsl:template match="publicationStmt">
  </xsl:template>

<xsl:template match="author">
<xsl:text>
***</xsl:text> <xsl:apply-templates/>
<xsl:text>***</xsl:text>    </xsl:template>

<xsl:template match="sourceDesc">
  </xsl:template>
  
<xsl:template match="choice">
<xsl:apply-templates/> 
</xsl:template>

<xsl:template match="closer">
<xsl:text>
    
</xsl:text>
<xsl:apply-templates/>    
</xsl:template>

<xsl:template match="signed">
<xsl:text>*</xsl:text> <xsl:apply-templates/>
<xsl:text>*</xsl:text>    </xsl:template>
  
<xsl:template match="expan">
<xsl:text>*</xsl:text> <xsl:apply-templates/>
<xsl:text>*</xsl:text>    </xsl:template>
  
<xsl:template match="p">
<xsl:text>
      
</xsl:text>
<xsl:apply-templates/>
</xsl:template>
  
<xsl:template match="persName|name">
<xsl:value-of select="upper-case(.)"> </xsl:value-of>
</xsl:template>
  
<xsl:template match="lb">
<xsl:text></xsl:text>
<xsl:apply-templates/>
<xsl:text></xsl:text>
</xsl:template>
  
<xsl:template match="num">
<xsl:text>**</xsl:text> <xsl:apply-templates/>
<xsl:text>**</xsl:text>    </xsl:template>
  
<xsl:template match="foreign">
<xsl:text>*</xsl:text> <xsl:apply-templates/>
<xsl:text>*</xsl:text>    </xsl:template>
  
<xsl:template match="title">
<xsl:text>#</xsl:text> <xsl:apply-templates/>
<xsl:text>#</xsl:text> </xsl:template>
  
<xsl:template match="q">
<xsl:text>"</xsl:text> <xsl:apply-templates/>
<xsl:text>"</xsl:text>    </xsl:template>
  
<xsl:template match="del">
</xsl:template>
  
</xsl:stylesheet>