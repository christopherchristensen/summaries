# Namespaces



## Why do we need namespaces?

* If two or more XML languages in same document $\to$ risk of name clashes of elements or attributes
* used to indicated which elements and attributes in the document belong to the same language



## Why not simply rename clashing elements?

* not always possible
* often two big of an effort needed



## Uniform Resources

* URL (Locator)
  * specifies location of a resource and 
  * how it can be retrieved
  * general format: `[Scheme]://[Domain]:[Port]/[Path]?[Query]#[Fragment]`
* URN (Name)
  * name that uniquely identifies a resource
  * can be registered at IANA
  * doesn't tell you where resource is nor how to retrieve it (just a unique name)
  * general format: `urn://[Namespace]:[Namespace specific String]`

* URI (Identifier)
  * umbrella term for both URLs and URNs
  * identifies a resource in some way (either by name or location)



## How do we declare namespaces?

* With URIs (URLs or URNs)
* e.g. `xmlns="http://www.w3.org/2000/svg"`



## Default Namespace

