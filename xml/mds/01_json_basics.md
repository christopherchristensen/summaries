# JSON Basics



## What is JSON?

> JavaScript Object Notation

* simple, text-based data format
* derived from JS literals
* quasi-subset of JS
* designed for human-readable data interchange
* language independant
* most programming languages can generate and read JSON format
* today's standard data format for web application / services



## Advantages of JSON

* lightweight (low verbosity)
* format is easy to read / write
  * libraries implementing the data model are also lightweight
  * fast rendering, parsing, processing
* independant
  * can be processed in many prog. languages
* human-readable
* Algorithms to process JSON remain efficient and simple
* Can represent important data structures for computer science such as lists and trees
* JSON data types are the same as in most programming languages
* JSON maps directly to object models



## Disadvantages of JSON

> compared with XML

* JSON is not a document markup language
* Namespaces not supported, respectively each object forms a namespace
* Data validation officially not supported (spec in status “draft”)
* JSONPath not as powerful as XPath



## Applications of JSON

* Data Exchange (JSON = domain independent)
* Data Storing
* JSON-RPC
* JSON-WSP
* Web Services and AJAX



## JSON-RPC

> JSON Remote Procedure Call
>
> * Request / Response are JSON objects



## JSON-WSP

> JSON Web Service Protocol

* Same purpose as WSDL for SOAP
* uses JSON to describe how given service can be consumed and what will be returned
* with JSON-WSP code to communicate with service can be generated automatically
* specification (draft!) defines four elements:
  * description: Service description specification. How to communicate with the service.
  * request: the method that is to be invoked and the arguments.
  * response: the result of a service method invocation.
  * fault: fault information in case of an error.



## Web Services and AJAX

* designed for machine-to-machine interaction
* Different types of web services: 
  * SOAP, used to be the standard approach
  * but it has been dominated by REST in recent years
* use machine-readable formats to communicate, such as XML and JSON
* As JSON can easily be processed in JS, it is often a preferred data format for mobile and web applications
* In modern front-end development, AJAX has become an important term. 
  * offers ability to exchange data with a web service in the background
  * without interfering with the currently displayed page



## In which two compositions can JSON data be structured?

* JSON **object**
  * unordered collection of key/value pairs
  * `{ "KeyA": "ValueA", "KeyB", "ValueB" }`
* JSON **array**
  * ordered list of values
  * `[ "arrayItem0", "arrayItem1" ]`

* JSON is case sensitive!



## JSON Objects

* begin and end with `{ }` 
* unordered collections of key/value  pairs, separated by `:`
* pairs separated by commas `,` 
* keys always in double quotes `"`
* value syntax depends on the type (string, number, object, etc.)



## JSON Arrays

* begin and end with `[]`
* ordered lists of values, separated by commas `,`
* can contain mixed types
* value syntax depends on the type (string, number, object, etc.)



## JSON Values

* 4 primitive and 2 structured types
  * string, number, object, array, boolean, null
* objects / arrays are valid value types



## JSON Strings

* Unicode (default: UTF8)
* support escaping for 
  * double quotes
  * control characters
  * hexadecimal-encoded characters



## JSON Numbers

* base10 literals
* supports real number literals
* allows various types of numerical values: `[4, -4, 0.1, -0.33, 1.2e-1, -2.7e-1]`



## How many times can JSON Objects be nested?

* infinitely (good practice?)



## Nested Compositions

* JSON array can be nested in a JSON object and vice versa
* JSON array can be nested in a JSON array
* JSON object can be nested in a JSON object



## JSON- vs. JS-Objects

* JSON close to JS objects but not identical
* JSON used for data interchange between all languages, not just in JS
* JSON not part of JS
* have differences (e.g. JSON keys need to be double-quoted)
* most JSON data are valid JS objects literals, JSON is not a JS subset