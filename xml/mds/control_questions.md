## Control Questions

1. **Name advantages and disadvantages of XML**

   Advantages:

   - does not dictate what metadata is allowed

   - strict but simple format rules
   - Recreation of corrupted files
   - Interoperability
   - well-suited for data-centric and document-centric uses
   - good for parsing
   - readable

   Disadvantages:

   - metadata warrants bigger files

2. **What is a markup language in general?**

   - Separation of metadata from content (auf Syntaxebene)

3. **Why is metadata so important that it could motivate the design and specification of a new markup language?**

   - information of information

   - XML does not dictate metadata, so language could be created for new use-case

4. **Explain the difference between data and document-centric XML**

   - Hierarchische Struktur (Data)
   - small data items that follow a specific structure
   - Dokumentenzentrisch: "wildes Gemisch"

5. **Name five different application fields of XML in practice**

   - Configuration and Logging 
   - Web Services
   - Web Content and Type Setting
   - Business Interoperability
   - Data Carrier

6. **In which field does XML apparently have the biggest success?**

   - Business Interoperability

7. **What are XML-RPC and SOAP, and how do they distinguish ?**

   - RPC: geht durch Middleware (man bekommt vom XML nicht viel mit)
   - SOAP: Erhält einen XML-Knoten (erweiterbar)

8. **Which other XML concept is used for web services ?**

   - WSDL (beschreiben Klassen, was Service macht, wie Request/Response aussieht)
   - IDE kann Informationen aus XML parsen

9. **Which information does the XML prolog contain ?**

   - encoding, version, standalone (falls man auf DTDs verweisen wollen)
   - muss zu Beginn des Dokumentes sein
   - optional

10. **What are CDATA sections good for ?**

    - für code-snippets

    - used to avoid repetitive escaping of characters

11. **What is a processing instruction used for ?**

    - after prolog

    - give processing instructions to the application that opens the XML
    - e.g. styling

12. **When are two XML documents logically equivalent ?**

    - if they have the same in-memory representation after parsing
    - wenn sie also das gleiche bit-pattern haben

13. **Which of the following statements are true ?**

    a) Equivalent XML documents are equal.

    b) Equal XML documents are equivalent. <-- (können aber unterschiedliches bit-pattern haben)

14. **Name two reasons why namespaces are important**

    - Name clashing / Zugehörigkeit
    - Für Interpretation (z.B. für content-spezifisches rendering $\to$ z.B. SVG)

15. **Explain the difference between URLs, URNs and URIs**

    - URI
    - URL: wo?
    - URN: wer?

16. **Explain the difference between a default and a prefix namespace.**

    - default sucht alle Elemente darunter und das Element wo es selbst definiert ist
    - Präfix, dann passiert noch nichts. jedes Element muss dieses Präfix verwenden

17. **In which regard are attributes special with respect to namespaces ?**

    - nicht qualifiert
    - bei einem default namespace werden die Attribute nicht automatisch im Namespace gesucht

18. **What is the XML namespace and why is it special ?**

    - Muss nicht immer importiert werden

19. **What makes JSON human readable?**
    * plain text
    * structured only with textual characters
20. **For what is JSON mainly used?**
    * data interchange / exchange
    * data storing
    * web services / AJAX
21. **How can elements be nested in JSON?**
    * JSON objects / arrays are valid value types
    * `{"element": {"nestedElement": "nestedValue"}}`
    * `[["nestedValue1", "nestedValue2"], "element": {"key", "value"}]`
    * can be nested infinitely
22. **How does JSON differ from JavaScript Objects?**
    - JSON close to JS objects but not identical
    - JSON used for data interchange between all languages, not just in JS
    - JSON not part of JS
    - have differences (e.g. JSON keys need to be double-quoted)
    - most JSON data are valid JS objects literals, JSON is not a JS subset
23. **Why is JSON often used in SPA and mobile applications?**
    * lightweight
    * platform/language independant
    * human-readable format