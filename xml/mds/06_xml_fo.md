# Formatting Objects



## What are FOs?

> Formatting Objects

* HTML / XHTML are document formats designed for being displayed in browser
* not made for paper print
* XSL-FO
  * page description language 
  * used for producing e.g. printer or e-book reader optimized documents
  * part of W3C XSL spec



## 2-Phase Process Model

* XSL-FO works in 2 phases with 3 types of docs involved:
  1. XML docs are transformed into FO docs using  a standard XSL processor
  2. FO docs are then converted into printable (or page- optimized) format like PDF or RTF using an FO processor



## Producing an FO Document Skeleton with XSLT

```xml
<?xml version="1.0" ?> 
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 			
    xmlns:fo="http://www.w3.org/1999/XSL/Format">
    
	<xsl:template match="/">
		<fo:root>
			<!–- FO page description-->
		</fo:root>
  	</xsl:template>
</xsl:stylesheet>
```



