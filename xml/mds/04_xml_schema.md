# XML Schema & Validation



## When is a document well-formed?

* when it satisfies the basic XML syntax



## XML Validation

* DTDs and XML Schemas serve to define XML languages
* There are W3C Schemas and DTDs for standardized XML languages 
  (e.g. SVG, MathML)
* In order to be valid SVG document code must satisfy the corresponding DTD or XML Schema definition
* XML parsers can validate files against a DTD or XML Schema



## DTD vs. XSD

* XML Schema (XSD) is itself an XML language
* DTDs use a different syntax
* DTDs do not fully support namespaces; XML Schema does
* XML Schema allows validation of element and attribute content against built-in or user-defined data types
* With XML Schemas we can more easily create complex and reusable structures and types
* HTML is not XML and therefore still needs a DTD. Other than that I believe that DTDs are dying out



## 3 Good Reasons for XML Schemas

1. An XML processing application can validate an input file against a Schema using a standard parser. 
   * This directly separates out incorrect files. 
   * Syntax checking of input files reduces to typing 3 lines of code. 
   *  cheap, fast and produces less software bugs

2. If you need to specify a new data exchange format with your business partners, write an XML Schema. 
   * provides specification, documentation and validator at once

3. OOP languages (e.g. Java or C#) directly allow to construct type hierarchies from XML Schemas. The same works with XML databases



## Validating XML Files against XML Schemas

* If XML document adheres an XML Schema, it is called an instance of this Schema

* It is possible to directly embed a Schema definition into an XML document (e.g. if the document will remain the only instance)



## Different ways to validate XML

1. Online Schema Validator
2. IDEs with built-in validator
3. Use a parser in your favourite programming language



## XML Namespaces vs. Java Packages

* XML Schemas define new XML languages / vocabularies 
  (comparable to e.g. packages in Java defining new API)

* If a class belongs to a package in Java, then this package is declared in the source code and must be imported for usage
* Putting a class into a package in Java is not mandatory. 
* Putting a vocabulary into a namespace is not mandatory.

* In the same way, if some vocabulary is part of a namespace, this namespace must be declared in the source code (XML Schema) and imported for usage (XML document)
* A namespace assigned to a Schema is called target namespace



## Do I need a Target Namespace?

* No, just refer in your XML document to an XML schema, and your code can be validated
* Sometimes your XML Schema is distributed over multiple files. Then, using a target namespace, you can signal that all this vocabulary belongs to the same language
* If you want to combine several vocabularies in the same document there can be at most one vocabulary without a target namespace
* Web languages like XHTML, SVG and MathML are often combined in the same document. Fortunately, they all have target namespaces



## Binding without Target Namespaces 1



## Binding without Target Namespaces 2



## Binding with Target Namespaces 1



## Binding with Target Namespaces 2







## Skeleton Extension 