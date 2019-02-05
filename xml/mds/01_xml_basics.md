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





## Control Questions

1. **Name advantages and disadvantages of XML**

   Advantages:

   * does not dictate what metadata is allowed

   * strict but simple format rules
   * Recreation of corrupted files
   * Interoperability
   * well-suited for data-centric and document-centric uses
   * good for parsing
   * readable

   Disadvantages:

   * metadata warrants bigger files

2. **What is a markup language in general?**

   * Separation of metadata from content (auf Syntaxebene)

3. **Why is metadata so important that it could motivate the design and specification of a new markup language?**

   * information of information

   * XML does not dictate metadata, so language could be created for new use-case

4. **Explain the difference between data and document-centric XML**

   * Hierarchische Struktur (Data)
   * small data items that follow a specific structure
   * Dokumentenzentrisch: "wildes Gemisch"

5. **Name five different application fields of XML in practice**

   * Configuration and Logging 
   * Web Services
   * Web Content and Type Setting
   * Business Interoperability
   * Data Carrier

6. **In which field does XML apparently have the biggest success?**

   * Business Interoperability

7. **What are XML-RPC and SOAP, and how do they distinguish ?**

   * RPC: geht durch Middleware (man bekommt vom XML nicht viel mit)
   * SOAP: Erhält einen XML-Knoten (erweiterbar)

8. **Which other XML concept is used for web services ?**

   * WSDL (beschreiben Klassen, was Service macht, wie Request/Response aussieht)
   * IDE kann Informationen aus XML parsen

9. **Which information does the XML prolog contain ?**

   * encoding, version, standalone (falls man auf DTDs verweisen wollen)
   * muss zu Beginn des Dokumentes sein
   * optional

10. **What are CDATA sections good for ?**

    * für code-snippets

    * used to avoid repetitive escaping of characters

11. **What is a processing instruction used for ?**

    * after prolog

    * give processing instructions to the application that opens the XML
    * e.g. styling

12. **When are two XML documents logically equivalent ?**

    * if they have the same in-memory representation after parsing
    * wenn sie also das gleiche bit-pattern haben

13. **Which of the following statements are true ?**

    a) Equivalent XML documents are equal.

    b) Equal XML documents are equivalent. <-- (können aber unterschiedliches bit-pattern haben)

14. **Name two reasons why namespaces are important**

    * Name clashing / Zugehörigkeit
    * Für Interpretation (z.B. für content-spezifisches rendering $\to$ z.B. SVG)

15. **Explain the difference between URLs, URNs and URIs**

    * URI
    * URL: wo?
    * URN: wer?

16. **Explain the difference between a default and a prefix namespace.**

    * default sucht alle Elemente darunter und das Element wo es selbst definiert ist
    * Präfix, dann passiert noch nichts. jedes Element muss dieses Präfix verwenden

17. **In which regard are attributes special with respect to namespaces ?**

    * nicht qualifiert
    * bei einem default namespace werden die Attribute nicht automatisch im Namespace gesucht

18. **What is the XML namespace and why is it special ?**

    * Muss nicht immer importiert werden



