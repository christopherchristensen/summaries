# XML Processing in Java, PHP & .NET



## JAXP

> Java API for XML Processing

* Lightweight, standardized framework for validation, parsing, generation and transformation of XML docs
* Includes SAX, DOM and StAX parsers
* Can invoke XSL transformations and XML Schema validation



## Parsing XML

* many ways to access XML data (DOM, JDOM, XDM used by XPath, XQuery and XSLT and others)
* These methods require that whole XML doc loaded into memory prior to processing
* in-memory representation of an XML doc about 4 times bigger than its file size
* may want to avoid this way of treating XML docs in case of large files or limited memory
* Sequential processing doesn't load XML docs into memory but reads them sequentially from the beginning to the end and hands over the content to the programmer



## Sequential Processing

* Different stages for sequential processing:
  1. Doc is traversed and whenever a specific item is found, an event is fired off. Programmer decides to which events she wants to respond (SAX / Java)
  2. Programmer instructs XML reader in which part of the doc she is interested in. Reader moves to this place and sequentially returns the subsequent content (XmlReader in .NET, StAX in Java)

## Push vs. Pull

* SAX pushes data to applications by firing events
* Alternatively, pull data that is currently pointed at by a cursor that moves forward, never backward

> beides sequentiell



## Downsides Sequential Processing

* Can't go back!
* A consequence of the above is, you can't validate a doc against e.g. an XML Schema prior to processing
* cannot modify XML docs with SAX

> up to programmer to choose best method for each task
>
> * Upside weniger Speicherbedarf



[...]

## SAX API Summary

1. Create parser `XMLReader`
2. Give `DefaultHandler` extension to parser
3. Start reader on XML file





## JDOM

* a Java representation of an XML document 
  * based on an in-memory object tree similar to DOM
* straightforward, lightweight, fast API optimized for Java programmers

* alternative to DOM, SAX and StAX
* not a wrapper for W3C DOM, or an abstraction or an
  extension or another version of DOM
* serves same purpose as DOM, but easier to use and based on Java Collection Framework



## JDOM Core Classes

* uses Java Collection Framework
  (no list type similar to SAX `Attributes` necessary)

* 