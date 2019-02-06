# XSLT



## What is XSLT?

> Extensible Stylesheet Language Transformations

* one of the big success stories of XML technologies
* transforms documents from a source format to a target format
* source format must be an XML language, target format can be anything
* typical target languages are XHTML, SVG or FO
* declarative-functional programming language



## XSLT Principles

* An XSLT file is a set of templates

* Each template specifies an XPath-like expression

* The XSLT processor 

  1. builds an optimized DOM tree from the input XML document

  2. It then starts from the root of the source tree, finds the best-matching template and executes this template (only one)

