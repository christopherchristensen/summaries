# Extracting Data from XML



## Representing XML in Memory

* XML is text-based
* once XML doc has been read into memory it is usually represented as a tree
* ways to access tree: DOM, XPath, XQuery, XSLT, ...
* W3C document object model (**DOM**):
  * known tool for storing and processing XML trees
  * widely supported
* XQuery and XPath data model (**XDM**):
  * more powerful than DOM
  * e.g. supports object with types described by XML Schema
  * XPath, XQuery and XSLT all use this model
* Post-Schema Validation information set (**PSVI**):
  * XML Schema's own model
  * result of validating an XML document against a Schema and
  * augmenting the XML document with type information



## Limitations of DOM

* low-level API for accessing a tree in memory
* only has some basic object-oriented features
* certain implementations known to be memory inefficient



## XPath Language





## Exercises

