Muy bien. Sin embargo, debe tener cuidado en todos los XPath usados en las plantillas de las líneas 60, 68, 72 y 76: cuando usa una sola barra (/) en la expresión está estipulando que debe ser el hijo inmediato. En lugar de:

<xsl:template match="div[@type='impreso']/abbr">

sería mejor usar:

<xsl:template match="div[@type='impreso']//abbr">

(note la doble barra). Así se asegura de que sea un descendiente y no un hijo inmediato.

Por otro lado, una expresión tan específica como:

<xsl:template match="div[@type='impreso']/p/num[@value='14']">

es poco eficiente (y así sucede con otras en su stylesheet). Entre más generales (entre más casos abarquen), tanto mejor.


Nota: 4.8