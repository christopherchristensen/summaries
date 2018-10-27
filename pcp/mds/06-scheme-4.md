# Scheme 4

> Typen von Rekursionen



## Was ist strukturelle Rekursion?

* strukturelle Rekursion (bisher verwendet)
  * Eingabedaten in ihre direkten strukturellen Komponenten zerlegt
  * rekursive Funktion einmal per Anzahl Elemente der Liste aufgerufen
  * Funktionsschema (ohne Spezialfall):
    * behandle erstes Element
    * **mache-etwas-mit** Rest
  * kann nicht alle Probleme lösen
  * nicht immer beste Lösung



## Was sind die Grenzen der strukturellen Rekursion?

* Sobald zwei Rekursionen in einer Funktion benötigt werden
* Das sind zwei strukturelle Rekursionen mit der Länge $n-1$, wobei n die Anzahl Eingabedaten ist
* Die Rekursionsaufrufe verdoppeln sich



## Akkumulative Rekursion

* Variable oder Parameter sammelt Resultat der bisherigen Berechnung (Zwischenspeichern)



## Was ist der Euklidische Algorithmus?

* eine der ältesten bekannten Algorithmen mit folgender Form:
  * `gcd(n, m) = gcd (m, n mod m) ; für m > 0`
  * `gcd (n, 0) = n ; Trivialfall`

* Implementation:

```scheme
(define (gcd-euclid n m)
  (cond
	[(zero? m) n]
	[else (gcd-euclid m (remainder n m))] 
   ))
```

* basiert auf generativer Rekursion
* trivialer (lösbarer) Fall: `m = 0` 
* generativer Schritt ruft `gcd-euclid` mit `m` und `(remainder n m)` als Argument auf
  * Die Argumente basieren auf keinem rekursiven Datentypen
  * Die Argumente werden bei jeden Aufruf neu berechnet -
    generiert aus $n$ und $m$ 
* auch mit grossen Zahlen effizient

> Scheme kennt die vordefinierte Funktion gcd



## Was ist der Ansatz der generativen Rekursion?

* Teile und herrsche (divide & conquer)
  * wenn Problem trivial lösbar, entsprechende Lösung zurückliefern
  * Ansonsten:
    * **Teile** Problem in kleine Teilprobleme
    * **Herrsche**: kleineren Probleme werden gelöst
    * **Kombiniere** Lösung der kleineren Probleme zu einer Lösung für das Ursprungsproblem

>  Design von generativ rekursiven Funktionen (Algorithmen) ist eine kreative Aktivität



## Was sind die Unterschiede zwischen struktureller, akkumulativer und generativer Rekursion?

- **strukturelle Rekursion**
  - Parameter bei einem Aufruf entweder unverändert oder eine Stufe näher zum Basisfall
- **strukturelle Rekursion mit Akkumulator** (akkumulative Rekursion)
  - Parameter wie bei struktureller Rekursion aber haben einen oder mehrere Akkumulator (Sammler-) Parameter
  - hat Hilfs- und Hüllfunktion (wrapper), welche Akkumulatoren initialisiert
  - können auch endrekursiv sein
    $\to$ wenn rekursive Funktionsaufruf die letzte Aktion zur Berechnung ist und mit dem letzten rekursiven Aufruf auch das Ergebnis der Berechnung vorliegt

* **generative Rekursion**
  * Parameter bei jedem Aufruf neu berechnet (generiert)
  * Es ist auf korrekte Parameter und die Terminierung der generativen Rekursion zu achten



## Was sind Funktionen erster Ordnung?

* machen Berechnungen unabhängig von Werten bestimmter Daten (Zahlen, Symbole)



## Was sind Funktionen höherer Ordnung?

* drücken allgemeine Berechnungsmethoden unabhängig von den jeweiligen beteiligten Funktionen aus
* z.B. könnten Relationszeichen `<` , `>` als Parameter übergeben werden
  $\to$ hier müsste man aber beachten dass die Parameter immer boolesche Argumente sein müssten



## Objekte erster Klasse

* In Scheme können Funktionen
  * als Parameter von anderen Funktionen dienen
  * Rückgabewerte von anderen Funktionen sein
  * an Namen gebunden werden
  * in Listen und Strukturen aufgenommen werden
* Funktionen sind auch Daten
  * diese Eigenschaft ist von zentraler Bedeutung für funktionale Programmiersprachen
  * Man spricht auch von **Werte erster Klasse** $\to$ first-class-citizen



## Wann werden Funktionen als Werte erster Klasse behandelt?

* Wenn man sie
  * als Parameter an andere Funktionen übergeben kann
  * zur Laufzeit erzeugen kann
  * als Resultate von Funktionen zurückgeben kann



## Wann heissen Funktionen "Funktionen höherer Ordnung"?

* wenn diese Funktionen andere Funktionen als Parameter und / oder Resultate haben (higher-order functions)



## Was ist der Vorteil von Funktionen höherer Ordnung?

* verbessern Expressivität einer Programmiersprache, also die Fähigkeit komplexe Sachverhalte möglichst klar und einfach auszudrücken



## `filter` Funktion

* Die Funktion «Prädikate auf Listen anwenden» ist vordefiniert:
  `(filter <function> <list>)`
* `filter` wendet `<function>` auf jedes Element von `<list>` an und filter liefert eine neue Liste von Elementen zurück, auf die `<function>` zutrifft.
*  `<function>` darf nur ein Argument besitzen.
*  `<function>` muss einen booleschen Wert zurückliefern.
* Beispiel:

```scheme
; eigene Prädikatfunktion
define (squarenumber? value) (integer? (sqrt value)))

; zur Laufzeit
> (filter squarenumber? (list 1 2 4 8 16 32 64))
(list 1 4 16 64)
```



## `map` Funktion

* wenn ein allgemeiner Operator bzw. eine Funktion auf alle Listenelemente angewendet wird: `(map <function> <list1>...<listN>)`

* map wendet `<function>` auf jedes Element von `<list1>...<listN>` an und map liefert eine neue Liste von Elementen zurück, auf die `<function>` zutrifft
* `<function>` muss soviel Argumente besitzen, wie es `<list1>...<listN>` gibt.
* Alle Listen `<list1>...<listN>` müssen die gleiche Anzahl Elemente besitzen.
* `<function>` darf `<list1>...<listN>` nicht verändern.
* Beispiel:

```scheme
; eigene Prädikatfunktion
(define my-list (list 3 5 -6 -23 37 2))

; zur Laufzeit
> (map sqr my-list)
(list 9 25 36 529 1369 4)

; ACHTUNG!
> (map + (list 1 2 3) my-list)
; map: all lists must have same size 
; arguments were: + (list 1 2 3) (list 3 5 -6 -23 37 2)
```



## `apply` Funktion

* betrachtet die Elemente der Liste als Operanden für die Funktion und liefert einen Funktionswert zurück (Werte und/oder Listen als Argumente möglich):
  `(apply <function> <value>...<list>)`
* apply wendet `<function>` auf jedes Element von `<val>...<list>` an und apply liefert einen Wert vom Datentyp, auf den `<function>` zutrifft
* `<function>` muss soviel Argumente besitzen, wie es `<value>...<list>` gibt!
* Das letzte Argument muss eine Liste sein!
* Beispiel:

```scheme
; Die als Argument übergebene allgemeine Funktion oder der Operator muss
; in jeder Weise mit dem/den Wert(en) und/oder Liste(n) korrespondieren.
> (apply + (list 1 -2 22 4 -5 1 76)) 
97
```



## Was ist zu beachten bei booleschen Operatoren `AND`, `OR` und `NOT` als Argumente?

* `no` ist ein Objekt erster Klasse (also eine **echte** Funktion)

```scheme
> (map not (list #true #false)) 
(list #false #true)
```

* Hingegen sind **and** und **or** nur Operatoren bzw. Scheme-Schlüsselbegriffe, aber keine echten Funktionen

```scheme
> (apply and (list #true #false))
; and: expected an open parenthesis before and, but found none
```







## Kontrollfragen



#### Welche Randbedingung muss erfüllt sein, damit Sie eine strukturelle Rekursion einsetzten können?
* Spezialfall muss existieren
* Rekursive Funktion und Basisfall
* muss terminieren
* Die Daten müssen von rekursiver Struktur sein (induktiv)



#### Was ist der Vorteil einer akkumulativen Rekursion gegenüber einer normalen strukturellen Rekursion?

* Zwischenresultate werden gespeichert $\to$ Schritte sparen
* Performanter, weniger Aufrufe, weniger Stack (viel kleiner)



#### Wann spricht man von einer generativen Rekursion?

* Wenn die Parameter bei jedem Aufruf neu generiert werden müssen



#### Was ist bei einer generativen Rekursion besonders zu beachten?

* auf die korrekten Parameter
* auf die Terminierung der generativen Rekursion
  $\to$  z.B. wenns nicht schön aufgeht und ich keine leere Liste erhalte am Ende



#### Nach welchem Prinzip gehen Sie beim Entwurf einer generativen Rekursion vor?

* Teile und Herrsche



#### Nennen Sie den Unterschied zwischen Funktionen erster Ordnung und Funktionen höherer Ordnung.

* **Funktionen erster Klasse**
  * machen Berechnungen unabhängig von Werten bestimmter Daten (Zahlen, Symbole) $\to$ Berechnen immer das gleiche
* **Funktionen höherer Ordnung**
  * drücken allgemeine Berechnungsmethoden unabhängig von den jeweiligen beteiligten Funktionen aus
  * wenn diese Funktionen andere Funktionen als Parameter und / oder Resultate haben (higher-order functions)



#### Wann werden Funktionen in einer Programmiersprache als «Werte erster Klasse» behandelt?

* wenn man sie
  - als Parameter an andere Funktionen übergeben kann
  - zur Laufzeit erzeugen kann
  - als Resultate von Funktionen zurückgeben kann



#### «Higher-Order Functions» verbessern die Expressivität einer Programmiersprache. Was bedeutet dies?

* komplexe Sachverhalte möglichst klar und einfach ausdrücken



#### Wenn Sie eine eigene Funktion / Operator für die vordefinierte Funktion `filter` schreiben, auf welche Randbedingungen müssen Sie achten?

*  `<function>` darf nur ein Argument besitzen
*  `<function>` muss einen booleschen Wert zurückliefern