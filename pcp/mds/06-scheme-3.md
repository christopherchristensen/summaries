# Scheme 3

> Rekursive Datentypen



## Listen

* Mit Strukturen können Datenobjekte mit einer festen Zahl von Daten gespeichert werden
* Häufig wissen wir nicht, aus wie vielen Datenelementen eine Datenstruktur besteht (oder Struktur ist rekursiv, so können beliebig grosse Datenobjekte strukturiert abgespeichert werden)
* **Idee**: Ein Element der Datenstruktur speichert (direkt oder indirekt) ein Exemplar der Datenstruktur (rekursive Datenstruktur mit Rekursionsanker/-basis)



## Was ist die Definition einer Liste in Scheme?

* leer oder
* besteht aus
  * einem ersten Element
  * einem Rest (Liste) $\to$ rekursive Definition
* In Scheme:
  * `empty` : leere Liste
  * `cons` : Konstruktor
  * `first` : Funktion für das erste Element
  * `rest` : für das "zweite" Element (Restliste)
  * Prädikatfunktionen: `cons?` , `empty?` , `list?` 
  * `<element>` : erste Element (beliebiger Datentyp)
  * `<rest of the list>` : entweder `empty` oder `cons` 

```scheme
empty ; oder
(cons <element> <rest of the list>)

; Fehler, denn zweites Element ist keine Liste
(cons 1 2)

; Listendefinition: Eine Liste mit 2 Elementen
(define list2 (cons 'a (cons 'b empty)))
```

![zeigerdarstellung](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/zeigerdarstellung.png)



## Wie greift man auf die Elemente einer Liste zu?

* `(first <list>)`
* `(rest <list>)`
* `(first (first <list>))` , etc.
* Früher mit `car` und `cdr` 



## Welche weitere Funktionen gibt es für Listen?

* `(reverse <list>)` : dreht Reihenfolge um
* `(length <list>)` : gibt Länge einer Liste zurück
* `(append <list1> <list2>)` : fügt Listen zusammen



##Welcher Datentyp kann ein Element einer Liste haben?

* beliebiger Datentyp
* Listenelemente müssen auch innerhalb einer Liste nicht vom gleichen Datentyp sein 



## Kann man Listen einfacher konstruieren als mit `cons` ?

* Ja, mit `list` :

```scheme
(list <element1> ... <elementN>) 
; ist äquivalent zu:
(cons <element1> (cons ... (cons <elementN> empty)))

; Beispiel:
<list 1 2 3 'a 'b 'c>
```

* oder mit dem Quote-Konstruktor `'` :

```scheme
'((1 2) (3 4) (5 6)) ; statt : (list 1 2 3)
'(a b c) ; statt : (list 'a 'b 'c)
```



## Was ist der Unterschied zwischen `list` und dem Quote-Konstruktor `'` ?

* `list` wertet alle Argument aus
* Quote nicht!

```scheme
> (list (+ 1 2))
(list 3)

> '(+ 1 2)
(list '+ 1 2)
```





## Was sind strukturierte Listen?

* Listen und einfache Typen (Baumstruktur)
* sequentielle Listen gleicher Länge
* Strukturen vom gleichen Typ:

```scheme
(define-struct person (name number))
(define phone-book
  (list
   (make-person "Meier" 2051)
   (make-person "Müller" 3352)))
```

> Kann trotzdem beliebige Datentypen enthalten...



## Welches Funktionsschema haben Listen in Scheme?

* **mache-etwas-mit** Liste

  * ist leer: Spezialfall

  * ist nicht leer:

    $\to$ behandle erstes Element

    $\to$ **mache-etwas-mit** dem Rest der Liste



> Rekursion



## Wohldefinierte Rekursion

* Die Auswertung der Funktion terminiert
* Nicht jede rekursive Definition ist wohldefiniert
  $\to$ z .B. `(define (f a-bool) (f (not a-bool)))`

* Unser Funktionsschema für rekursive Definition ist ein Beispiel für strukturelle Rekursion.
  * Die Struktur der Funktion folgt der (rekursiven) Struktur der Daten.
  * Solche rekursiven Definitionen sind stets wohldefiniert, weil die Schachtelungstiefe der Daten in jedem rekursiven Aufruf strikt abnimmt.



## Sortieren von Zahlen

* Sortieren durch Einfügen (Funktionsschema):

```scheme
(define (sort-by-insert num-list)
  (cond
   ((empty? num-list) empty)
   (else <einfügen an geeigneter Stelle> (first num-list)
         <sortieren> (rest num-list))
   ))
```



## Einfügen in sortierte Liste

* Hilfsfunktion `insert`
* Funktionsschema:

```scheme
(define (insert value a-list) 
  ((wenn value <= <erstes Element> a-list
         <erzeuge neue Liste mit value und a-list>)
   (<sonst erzeuge neue Liste mit erstem Element und a-list>
           füge value in (rest a-list) ein))
```

* Implementierung:

```
(define (insert value a-list) (cond
((empty? a-list) (list value))
((<= value (first a-list)) (cons value a-list)) (else (cons (first a-list)
                (insert value (rest a-list))))
))
```

//TODO





## Kontrollfragen



#### Beschreibe was eine Liste ist in Scheme

* rekursive Datenstruktur
* mit Rekursionsbasis
* Mit einem ersten Element und einer Liste

> Verkettung von Listen



#### Welche Art von Elementen (Datentypen) kann eine Liste enthalten?

* Als erstes Element irgendeinen Datentypen (dynamisch typisiert)
* Als zweites Element eine Liste (auch `empty`)
* Listenelemente müssen nicht vom gleichen Datentyp sein



#### Mit welchen Funktionen kann man eine Liste erstellen (konstruieren)?

* Mit `cons` 
  $\to$  plus `<element>` und `<rest of the list>`
* Mit `list` 
* Mit Quote `'`



#### Mit welchen vordefinierten Funktionen kann man auf Elemente einer Liste zugreifen?

* `first`
* `rest` 



#### Was erhält man als Ausgabe mit folgender Anweisung?

* **Anweisung**: `(rest (rest (list 1 2 3 4))` 
* **Lösung**:
  * Fehler, denn es fehlt eine Klammer
  * Mit zusätzlicher Klammer erhält man: 
    `(cons 3 (cons 4 '()))`



#### Wie greift man auf das zweite Element einer Liste zu?

* `(rest list1)` : so erhält man das zweite Element als Restliste
* `(first (rest list1))` : so erhält man effektiv das zweite Element

> Oder: `second` 



#### Wie sieht das Funktionsschema für Operationen auf Listen aus?

* **mache-etwas-mit** Liste
  * ist leer: Spezialfall

  * ist nicht leer:

    $\to$ behandle erstes Element

    $\to$ **mache-etwas-mit** dem Rest der Liste


#### Bei welchen Listen oder Operationen auf Listen kann man das Funktionsschema nicht anwenden?

* mit `list` und
* mit `'` 
* wenn das Funktionsschema erweitert werden muss



#### Was bedeutet wohl definierte Rekursion?

* Sie terminiert



#### Schreibe eine Rekursion, die nicht wohldefiniert ist

* `(define (f a-bool) (f (not a-bool)))`



