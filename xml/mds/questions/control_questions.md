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

24. **Explain the difference between the following two queries:***

    * > `/bond_movies/movie/*`

    * > `/bond_movies/movie/node()`

25. **Make a prediction what the following expression returns and verify***

    * > `/descendant::title[text() = "Dr. No"]/../regie`

26. **Which number does the bond movie with Maud Adams have?***

    1. Solve the exercise <u>knowing</u> she played a bond girl

       Solution: `//bond_girl[text()="Maud Adams"]/../@number`

    2. Solve the exercise <u>without knowing</u> she played a bond girl

       Solution: `//*[text() = "Maud Adams"]/../[@number]`

27. **How many times (`count()`) did Sean Connery play bond?***

    * `count(//*[text() = "Sean Connery"])`

28. **How much time (`sum()`) will it take to watch all bond movies?***

    * `sum(//duration)` 

29. **List all movies over 120min***

    * `//title[../duration > 120]`
    * or: `//duration[text() > 120]/../title`

30. **List all bond actors without double naming (`distinct-values()`)***

    * `distinct-values(//bond)` 

31. **Formulate an XPath query that produces the following output***

    * Output:

    > Terence Young produced 3 movies.
    > Guy Hamilton produced 4 movies.
    > Lewis Gilbert produced 3 movies. 
    > Peter R. Hunt produced 1 movies.
    > John Glen produced 5 movies.
    > Martin Campbell produced 2 movies. 
    > Roger Spottiswoode produced 1 movies. 
    > Michael Apted produced 1 movies.
    > Lee Tamahori produced 1 movies. 
    > Marc Forster produced 1 movies. 
    > Sam Mendes produced 2 movies.

    * Solution:

    ```xml
    for $i in distinct-values(//regie)
    return concat($i, " produced ", 
    			count(//regie[text() = $i]), "movies")
    ```

32. **Modify the query to show only successful producers (> 1 movie)***

    * Output:

    > Terence Young produced 3 movies. 
    > Guy Hamilton produced 4 movies. 
    > Lewis Gilbert produced 3 movies. 
    > John Glen produced 5 movies. 
    > Martin Campbell produced 2 movies. 
    > Sam Mendes produced 2 movies.

    * Solution:

    ```xml
    for $i in distinct-values(//regie)
    return
    if(count(//regie[text() = $i]) gt 1)
    then concat($i, " produced ", count(//regie[text() = $i]), " movies")
    else()
    ```

33. **List all countries with population less than Switzerland*\***

34. **List all codes of countries with population less than Switzerland*\***

35. **List all countries whose average life expectance between men and women does not differ by more than 4.5 years*\***

36. **Find the country with the fewest people*\***

37. **List all countries with less than 1.5M people under 15 years*\***

38. **Find all countries with at least 50% more young than old people*\***

39. **With the JSONPath evaluator (https://jsonpath.herokuapp.com/)  create an expression with the following output*\*\***

    * Output:

    > [ "Sean Connery" ]

    * Solution:





***** can only be solved with the bond data provided in the lecture

***\*** can only be solved with the `countries.xml` data provided in the lecture

***\*\*** can only be solved with the `bond_movies.json` data provided in the lecture

