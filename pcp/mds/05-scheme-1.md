# Scheme 01



## Welchem Progrqmmierparadigma wird Scheme zugeordnet?

* funktional (deklarativ)



## Durch was wurde LISP inspiriert?

* das Lambda Kalkül



## Was bedeutet homoikonisch?

* Homoikonizität: Selbst-Abbildbarkeit
* Eigenschaft von Programmiersprach, dass Programme gleichzeitig Datenstrukturen derselben Sprache sind.
* Es ist einfach, Programme zu schreiben, die Programme schreiben (Turingmaschine)

> In Lisp: jedes Programm eine Liste



## Prinzipien der funktionalen Programmierung

* Im Zentrum stehen Funktionen
  * Keine Seiteneffekte (referentielle Transparenz) 
    $\to$ *man kann in anderen Programmiersprachen **nicht** beweisen, dass ein Programm immer dasselbe Resultat liefert (z.B. in Java)*
  * Funktionen als gleichberechtigte Datenobjekte (Funktionen höherer Ordnung)
  * Verwendung von Funktions-Implementierung für verschiedene Typen
    $\to$ Polymorphismus
  * Programme sind kürzer, klarer, besser zu warten, zuverlässiger, schneller zu erstellen
* Lösen einer Aufgabe anhand von **Dekomposition** und **Komposition**



## DrRacket

* integrierte Entwicklungsumgebung (IDE) für den Scheme-Dialekt Racket
*  verschiedene, skalierbare Scheme-Dialekte
  $\to$ (Einsteiger / Fortgeschritten)
* direkte Rückmeldung und Kontrolle aller Prozeduraufrufe
* REPL Konsole (Read-Evaluate-Print Loop)
  * Einlesen des Ausdrucks, analysieren auf erlaubte Syntax
  * Auswerten des Ausdrucks
  * Ausgabe des Auswertungsresultats (falls keine Fehler auftreten)
* hat einen Stepper, durch den man schrittweise das Prinzip der Substitution beim Abarbeiten funktionaler Prozeduraufrufe verfolgen kann.
  $\to$ Debugging



## Zahlen in Scheme

* selbstauswertend 
  $\to$ die Werte der Ziffern sind die Zahlen, die sie bezeichnen, auch in der Genauigkeit
* primitive atomare Ausdrücke
* Scheme unterscheidet zwischen
* ganzen Zahlen (integer), Bsp. 23
  * rationalen Zahlen (rational), Bsp. - 3⁄4 oder -0.75
  * reellen Zahlen (real), Bsp. pos. Unendlich = +inf.0
  * irrationale Zahlen, Bsp. pi = #i3.141592653589793
  * komplexen Zahlen (complex), Bsp. -2 = #i0+1.4142135623i



## Boolesche Werte in Scheme

* true, false
* selbstauswertend
* alternative Darstellung `#t` und `#f` 



## Eingebaute Operaten in Scheme

* eine Auswertung ergibt den Wert einer derartigen Operation
* auch PRIM-OPS (primitive operations) genannt
* Operatoren für ganze Zahlen:

![ops-ganze-zahlen](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/ops-ganze-zahlen.png)

* Operatoren für reele und komplexe Zahlen:

![ops-komplexe-zahlen](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/ops-komplexe-zahlen.png)



## Form in Scheme

* Alles, was in Scheme eingegeben wird, ist eine Form:
  `(<operator> <operand1> <operand2> …)` 
* Eine Form wird durch runde Klammern eingeschlossen.
* Präfix-Schreibweise, zuerst der Operator (gilt auch für Funktionen), dann die Operanden (beliebig viele).
* Reihenfolge der Auswertung ist nicht festgelegt!
* Formen können geschachtelt werden.
* Klammern treten immer paarweise auf.
* Die Präfix-Schreibweise **kennt keine Punkt-vor-Strich-Regel**, da alles durch Klammern geregelt wird.



## Scheme Syntax - Klammern

* Vollständig geklammerte Präfix-Notation
  * **Vorteil**: eine Operatorrangfolge für alle Operatoren
  * **Nachteil**: hohe Zahl der Klammern
* Einige Scheme-Implementierungen (z.B. Racket) erlauben zusätzlich die Verwendung von eckigen Klammern.



## Wie kann man das Ausgabeformat im Interaktionsfenster von DrRacket ändern?

* In den Einstellungen $\to$ *Fraction Style*



## Welche Auswertungsregeln für Werte, Namen und Operationen gibt es in Scheme?

*  **Selbstauswertend**: gibt den Wert zurück, z.B. Zahlen und boolesche Werte.
* **Name**: gibt den Wert zurück, der in der Umgebung mit diesem Namen assoziiert wird.
* **Eingebauter Operator**: gibt die Sequenz der Instruktionen zurück, welche die entsprechende Operation durchführen.
* **Kombination der Auswertungsregeln**:
  * rechne die Unterausdrücke (in beliebiger Reihenfolge) aus,
  * wende die Funktion, die der Wert des links stehenden Unterausdruckes ist (der Operator), auf die Operanden an (die Werte der restlichen Unterausdrücke).
* **Form mit Schlüsselwort**: Wende die Funktion an, die mit einem der Scheme Schlüsselwörter ausgeführt wird.



## Auswertungsregeln für Formen

* rekursiv: Bei einer Form ruft die Regel sich selbst auf
* Jedes Element muss ausgewertet werden, bevor die Gesamtauswertung einer Form abgeschlossen werden kann



## Definition von Namen (Bezeichner)

* Buchstaben, Ziffern und Sonderzeichen erlaubt
* In funktionalen Sprachen wird der Bezeichner an einen Ausdruck oder Wert gebunden
* Für Definition `define` verwenden:

```scheme
(define <identifier> <expression>)
```

* `identifier` : Name
* `expression` : Ausdruck (Konstante, Variable, Funktionsaufruf, ...)



> Scheme unterscheidet Gross-/Kleinschreibung nicht $\to$ Case-Sensitivität in DrRacket  einstellen



## Wie definiert man in Scheme eine Funktion?

* mit `define`

```scheme
(define (<identifier> <formal parameters>) 
  			<expression>)
```

* Funktionsdefinitionen bilden das Programm (Applikation)
  $\to$ main-Funktion existiert nicht
* // TODO 



## Kontrollfragen

#### Was ist falsch an den folgenden Ausdrücken?

* Ausdrücke:

  1. `(5 * 14)`

  2. `(* (5) 3)` 
  3. `(+ (* 2 4)` 
  4. `(* + 3 5 2)`
  5. `(/ 25 0)` 

* Lösungen:

  1. Operator an falscher Stelle (sollte am Anfang in der Klammer stehen)
  2. Die `5` ist in einer eigenen Form, die einen Operator benötigt
  3. Es fehlt die Klammer ganz rechts
  4. Man kann nur ein Operator pro Klammer angeben, das `+` wird als Operand wahrgenommen $\to$ oder es fehlen zwei Klammern 
  5. Man kann nicht durch $0$ teilen, aber am Ausdruck gibt es nichts auszusetzen



#### Scheme ist dynamisch typisiert. Was bedeutet das?

* Es gibt keine Typen in Scheme. // TODO



#### Wie wird der Ausdruck `(* (- 6 4) (+ 3 2))` schrittweise ausgewertet?

* rekursiv
* egal ob von rechts nach links oder links nach rechts



#### Wie sehen die Auswertungsregeln für allgemeine Formen aus?

* Es muss ein Operator und ein Operand in einer Form vorhanden sein
* Ausgewertet wird die Form rekursiv



#### Wie sieht die Auswertungsregeln für die spezielle Form `define` aus?

* selbstauswertend
* Beide Operanden müssen zuerst ausgewertet werden, um zusammen berechnet zu werden
* Die Operanden werten sich selbst aus



