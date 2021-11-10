Está muy bien. Sin embargo, no entiendo el propósito de esta plantilla:

    <xsl:template match="lb[@break='no']">
    <xsl:text>⦑no-brake⦒</xsl:text>
    </xsl:template>

En el TEI:

    sospecho<lb break="no"/>samente

produce:

   sospecho⦑no-brake⦒samente

que es precisamente lo que que se quería evitar (eso es lo que "no-break" codifica).

Nota: 4.8