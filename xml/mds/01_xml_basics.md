# XML Basics



## Binary Files

* streams of bits
* Only application that created file knows meaning / interpretation



## Advantages of binary files

* concise representation 
* small space (e.g. hard disc)
* less bandwidth when transported across networks



## Text Files

* use standard encodings (e.g. UTF-8)



## Advantages of text files

* human and cross-application readable
* easier parsing (library functions)



## Disadvantages of text files

* space consuming (metadata needs separating from content)



## Metadata

* information about information
* such as encoding, version, author, etc.
* needs separating from content



## SGML

* Predecessor of XML
* advantages of text files are due to standard character encoding
* standardize separation of metadata

* concept good, but too complicated
* only dominant survivor: HTML 
  (is a SGML language)





> * Zip eliminiert Redundanz
> * ein Bit kann komprimiertes Files beschädigen
> * Backups nicht zippen



## XML

> Extensive Markup Language

* subset of SGML by W3C (published 1996)
* only specifies the rules for adding metadata
* does not dictate what metadata is allowed



## What is a markup language?

* system for annotating a digital document 
* in a way that is syntactically distinguishable from the content



## Advantages of XML

1. Very strict but simple format rules (e.g. generic parsing)
2. Recreation of corrupted files
3. Interoperability
4. XML is well-suited for data-centric and document-centric uses



## Data-Centric Use of XML

* Data-centric XML documents:
  * have many small data items
  * that follow a specific structure
  * They may be extracted from a structured database and formatted as XML documents for exchange



## Document-Centric Use of XML

* Document-centric XML documents (e.g. XHTML):
  * contain large amounts of text (news, articles, books)
  * There is little or no structured data elements



## Hybrid Use of XML

* Hybrid XML documents: 
  * may have parts that contain structured data
  * other parts that are predominantly textual or unstructured



## Disadvantage of XML

* metadata warrants bigger files
* (zipping also has its trade-offs)



## What are different applications for XML?

* Configuration and Loggin
* Web Services
* Web Content and Type Setting (XHTML, MathML, SVG, ...)
* Business Interoperability (Probably biggest use of XML nowadays)
* Data Carrier (e.g. carrier for encrypted data)



## Main Designs for Web Service Requests

* XML-RPC Approach (**R**emote **P**rocedure **C**alls)
  * function name and parameters wrapped in XML
  * mimics traditional (local) function calls
* Document Approach
  * service expects XML document defined by an XML Schema
  * service processes document and carries out task
  * used by e.g. SOAP



## Simple Object Access Protocol

> SOAP

* messaging **protocol** 
* that allows programs that run on disparate operating systems (Windows, Linux, ...) 
* to communicate using HTTP and its XML



## Advantage of SOAP

* application gets access to XML node directly



## Structure of SOAP

* SOAP message = `<envelope>` containing `<header>` and `<body>`
* Header contains information about request, body and XML node
* SOAP collaborates well with XML encryption & signatures



## SOAP can transport any XML node, but how can we know what a SOAP request should look like ?

> Web Services Descripion Language

* XML language WSDL solves problem by providing a contract between web services and the outside world
* WSDL documents outline what messages the SOAP server expects and what messages it returns
* A programmer doesn't need to look at WSDL documents directly. There are tools that produce code for SOAP requests directly from WSDL files



## UDDI

> Universal Discovery, Description and Integration (UDDI) protocol

* "How to find Web Services in the Wild"
* allows to register web services such that they can be discovered by programmers and other web services.

* The global UDDI registry consists of several servers that all mirror each other: register once, find everywhere
* Along with your web service you register your contact information
* Another company therefore can use UDDI to find business partners that offer the sort of web service they are looking for

> "[...] UDDI has never really taken off"



## JSON

> Javascript Object Notation

* Lightweight data interchange format
* compact, but easy to read / write for humans



## JSON vs XML

| JSON                                                         | XML                                                          |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| - more compact<br />- easier read-/writeable                 | - less compact<br />- harder read-/writeable                 |
| - data exchange format                                       | - markup language                                            |
| - better suited for data-centric use                         | equally well suited for <br />- data-centric<br />- document-centric<br />- hybrid use <br />- (but mainly document-centric) |
| - JSON Schema allows to define own languages<br />- but doesn't know complex data types and references | - XML Schema allows to define own languages. <br />- But knows complex data types and references |
| - JSONPath                                                   | XPATH and XQuery extract info efficiently from deeply nested XML documents |
| - No equivalent in JSON world                                | - XSLT enables autom. transformation of XML into different output formats <br />- not necessarily XML <br />- biggest XML success? |

* XML also contains almost too many possibilities



## XML Prolog

* option
* if does exist, then must come first in XML document
* version always 1.0 or 1.1*
* XML allows the use of any Unicode subset. But encodings other than UTF-8
  and UTF-16 will not necessarily be recognized by every parser
* Standalone applies only to documents that specify a DTD

* Example:

```xml
<?xml version="1.0"?>
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml version="1.0" encoding="UTF-16"?>
<?xml version="1.0" encoding="EUC-JP" standalone="yes"?>
```



## Elements and Attributes

* Elements without attributes:
  `<author>`Marc Pouly`</author>`
* Element with three attributes (key-value pairs)
  `<note day="10" month="1" year="2014">`Get beer for weekend`</note>`
* Self-closing element (no content) without attributes: 
  `<br />` (short-hand notation for `<br></br>`)
* Self-closing element with two attributes:
  `<img href="../test.png" border="0" />`



## Root and Nested Element

* Each XML document must have exactly one root element embracing all other elements
* All other elements are nested underneath the root element



## Important Naming Rules for Elements

* Names can begin with either underscore or an uppercase or lowercase letter
* Digits, hyphen, etc. can appear as subsequent characters
* Names are case-sensitive (`<AUTHOR>` ≠ `<author>` ≠ `<Author>`)
* Names must not contain spaces
* Names must not start with XML (either lowercase or uppercase)
* Don't use colon as name, since conflicts with namespaces



## Important Naming Rules for Attributes

* naming follows same rules as elements
* values must be in single-quotes or double-quotes
* single-quotes / double-quotes can be mixed in same document, not in same attribute
* If you use (single-quotes) double-quotes as delimiter you cannot use them inside the value
* There must be a value part, even if it is an empty pair of quotes
* Attribute names must be unique per element



## Comments and Entities

* Comments: `<!-- -->`
* Problem: Code below will generate an XML error
  `<message>if salary < 1000 then</message>`
* Solution: replace "<" with entity reference (`&lt;`)



## CDATA Sections

* Means that no markup is present
* Can be used to avoid repetitive escaping of characters
* Often used for embedding script code (e.g. Javascript into XHTML)

```xml
<conversion>
<![CDATA[
1 kilometer < 1 mile
1 pint < 1 liter
1 pound < 1 kilogram
]]>
</conversion>
```



## Processing Instructions

* follow immediately after the prolog
* used to give processing instructions to the application that opens the XML document

```xml
<?xml-stylesheet type="text/xsl" href="transformer.xslt" ?>
<?xml-stylesheet type="text/css" href="style.css" ?>
```



## Well-Formed XML / Error Handling

* If XML document satisfies all these rules, it is called well-formed
* Browsers often accept HTML code that is not well-formed (good?)
* XML is as strict as programming languages
  * The XML specification defines whether a broken syntax rule is fatal
  * XML processor may recover from errors and continue, but must stop on fatal errors



## Equivalence

* XML documents are equivalent, if same in-memory representation after parsing



 