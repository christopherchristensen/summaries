# Scheme 02



> Scheme kennt Iteration, gehört aber nicht zur funktionalen Programmierung. Behandeln wir also nicht. Scheme löst Iteration eigentlich anders.



## Was sind elementare Prädikate in Scheme?

* `#t` (wahr, true)
* `#f` (falsch, false)
* Ist ein Ausdruck, der zu `true` oder `false` ausgewertet wird
* Vergleichsoperationen: `=` , `<` , `<=` , `>` , `>=` 



## Boolesche Verknüpfungen

* `and` 

  * Ist keine Funktion,

  * aber man kann als Operanden `<expressions>` einer Form mit `and` hinzufügen

  * Beispiel:

    ```scheme
    > (and (= 23.3 23.3) (< 5 7))
    true
    ```

* `or`

  * Ist keine Funktion

  * aber man kann als Operanden einer Form `<expressions>` mit `and` hinzufügen

  * Pseudo-Beispiel:

    ```scheme
    (or <expr1> <expr2> ... <exprN>)
    ```



> * Ausdrücke von links nach rechts ausgewertet
> * Sequenzielle Auswertung
> * Es gibt einen Fehler falls einer der Ausdrücke weder `true` noch `false` ergibt
> * Es wird `false` zurückgegeben, falls alle Ausdrücke zu `false` ausgewertet werden



## Wie kann man in Scheme nach boolescher Gleichheit prüfen?

* `(boolean=? <expr1> <expr2>)` 
* Von links nach rechts ausgewertet
* Es wird `true` zurückgegeben, wenn beide Ausdrücke zu `true` oder zu `false` auswerten.
* Es wird `false` zurückgegeben, falls beide Ausdrücke unterschiedlich ausgewertet werden.
* Es gibt einen Fehler falls ein Ausdruck weder `true` noch `false`  ergibt.



## Was sind Prädikatfunktionen?

* Funktionen, die einen Wahrheitswert zurückliefern
* Funktionsname endet mit einem `?`
* Beispiele: `integer?` , `boolean?` , `char=?` 
* Testen, ob Objekte von bestimmten Datentypen, Zahlen oder Gleichheit sind
* Muss einen booleschen Wert zurückliefern



## Wie definiert man eigene Prädikatfunktionen?

* Frage nach `<identifier>` angeben
* `(define <identifier?> <expression>)` 
* Beispiel:

```scheme
(define (squarenumber? num) 
  (integer? (sqrt num)))
```



## Was sind Symbole?

* Sequenz von Zeichen angeführt von einem einfachen Anführungszeichen `'` 
* Mit einem Leerzeichen oder einem `'` (mit Anführungszeichen wird ein neues Symbol definiert) werden die Symbole voneinander getrennt
  $\to$ Leerzeichen als Symbole also nicht erlaubt
* um symbolische Informationen zu speichern (Name, Wörter, Richtungen)
* atomar
* können nicht zerlegt werden
* Ob Objekte gleiche (Gleichheit) Symbole sind, kann mit der Prädikatfunktion `symbol=?`  getestet werden.



## Was sind die Unterschiede zwischen Symbole und Strings?

* **TODO**



## Fallunterscheidung

* Schlüsselwort `cond`
* Bessere universelle Art Fallunterscheidung zu machen (als `if` )

```scheme
(cond (<condition clause1> <expr1>) 
      (<condition clause2> <expr2>) 
      ; Jede Klausel in Klammerpaar eingeschlossen
      ; Beliebig viele Klauseln erlaubt
      ...
(else <last-expr>)) ; else ist optional
```



## Wie wird `cond` ausgewertet?

* `<condition clauses>` der Reihe nach (oben nach unten) ausgewertet
  $\to$ Reihenfolge wichtig!
* Bei der ersten Bedingung, die zu `true`  führt, wird der zugehörige Ausdruck ausgewertet und zurückgegeben. 
* Wenn keine Bedingung zutrifft, wird eine Fehlermeldung ausgegeben!
  $\to$ mind. ein Fall muss zu `true`  ausgewertet werden
* `else` wird immer zu `true` ausgewertet



## Selektion

* Schlüsselwort `if` 
* muss immer eine `then` und `else` - Klausel enthalten
  $\to$ nicht optional
* Deshalb verwenden wir die Fallunterscheidung und nicht Selektion 



**// TODO BEISPIEL (SLIDES 20&21)**



##Struktur Datentyp

* Die Daten sind häufig nicht ein einzelner atomarer Wert (Zahl, Boolean, Symbol), sondern eine höhere Einheit mit vielen Eigenschaften.
* In Scheme spricht man von einem Strukturtyp genannt `struct`, oder auch von einem Verbund oder Record.
* Struktur Datentypen müssen im Gegensatz zu einfachen Datentypen selbst definiert werden.



## Wie definiert man eine Struktur?

```scheme
(define-struct <typename>
               (<field1> ... <fieldN>))
```

* `typename` : Bezeichnung der Struktur
* Damit hat man aber lediglich eine Typendefinition, aber noch kein Exemplar dieses Typs



## Implizite Struktur Definitionen

* **TODO**



## Namen für Strukturen

* **TODO**







## Kontrollfragen

#### Was sind elementare Prädikate?

* Ausdruck, der zu `true` oder `false` ausgewertet wird
* selbstauswertende Werte



#### Welche elementare Prädikate kennen Sie?

* `true` oder `false` 
* Vergleichsoperationen: `=` , `<` , `<=` , `>` , `>=` 



#### Wie werden boolesche Verknüpfungen (`and`, `or` ) ausgewertet?

* Von links nach rechts
* sequentielle Auswertung
  $\to$ Kurzschlussverfahren



#### Was sind Prädikatfunktionen?

* Funktionen, die einen Wahrheitswert zurückliefern



#### Woran erkennt man Prädikatfunktionen?

* Am Anführungszeichen nach dem `<identifier>`
* Beispiel: `(define <identifier?> <expression>)` 



####  Welche Arten von Prädikatfunktionen kennen Sie?

* Test auf Zahlen, Basistypen und Gleichheit



#### Wie wird `cond`-Anweisung ausgewertet?

* Der Reihe nach (von oben nach unten)
* Beim ersten `true` wird ausgewertet



#### Was passiert, wenn keine Bedingungender `cond`-Anweisung zutrifft?

* Gibt einen Fehler (deswegen `else`  verwenden)



#### Was ist das besondere an der `if`-Anweisung, gegenüber anderen Programmiersprachen (z.B. Java)?

* Es braucht dringend eine `else` - Klausel



#### Welche impliziten Funktionen gibt es zu der `define-struct` Anweisung?

* Prädikatsfunktion `?`
* Zugriff aufs Feld
* Selektor
* Erstellen `make`



#### Wie wird ein Objekt einer `define-struct` erzeugt?

* Mit dem Konstruktor
* `make`



#### Wie werden die Datentypen der Felder festgelegt?

* Sie werden gar nicht festgelegt
* Sie werden dynamisch typisiert



#### Erweitern Sie die Point Scaling Funktion mit dem Check auf die korrekten Datentypen. Fehlermeldung kann mit error ausgegeben werden.

* **TODO**
* möchte man verhindern (mit **cond** erweitern?)