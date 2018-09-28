# Prolog 2



## Was ist die Grundidee von Prolog?

* ein Problem beschreiben (deklarativ)
* Prolog löst dann das Problem (prozedural)



## Was sind typische Prolog-Standardprobleme?

* Kreuzworträtsel lösen
* Karten färben
* Zahlenrätsel lösen
* Sudoku lösen
* Spracherkennung
* Expertensysteme



## Was sind zwei Nachteile von Prolog?

* Es verwendet Backtracking, deswegen für viele Anwendungen ineffizient
* Finden einer passenden Modellierung (Problem) ist nicht immer einfach



## Was ist ein Vorteil von Prolog

> Wenn Modell beschrieben, ist Problem (grundsätzlich) gelöst

* Problembeschreibung reicht
* Das Prologsystem "weiss" damit alles notwendige, um Lösungen zu finden
* Vorteil gegenüber imperativer Programmierung, wo Problemlösung schrittweise beschrieben werden muss



## Was passiert wenn Prolog keine Lösung findet?

* Prolog gibt `false.` zurück



## Kann Prolog rechnen?

* so nicht: `?- X = 1 + 2` , 
  * denn das ergibt `X = 1 + 2`
  * der `=/2` -Operator macht **nur ein Matching**
  * Ausdrücke werden nicht automatisch arithmetisch ausgewertet
* Auswertung mit `is/2` -Operator
  * `?- X is 1 + 2.` 
  * `X = 3` 



## Was mach der eingebaute `is/2` -Operator?

* erzwingt eine Auswertung,
* falls die Operanden Zahlen sind



## Gebundene / ungebundene Operanden

> In der Doku von SWI-Prolog stehen bei Prädikaten typischerweise vor jeden Operand  folgendes:

* `-` : 
  * Operand sollte **ungebunden** sein
  * eine Variable
* `+` : 
  * Operand sollte **gebunden** sein
  * eine Zahl, ein Atom oder gebundener zusammengesetzter Term
* `?` : 
  * Operand kann **gebunden** oder **ungebunden** sein



// TODO (slides 20/22)



## Welche vordefinierten arithmetischen Operatoren kennt Prolog?

> Wichtig: Operatoren sind in Prolog auch Prädikate

* `+` : Addition
* `-` : Subtraktion
* `*` : Multiplikation
* `/` : Division
* `**` : Potenz
* `//` : Ganzzahldivision
* `mod` : Modulo



## Welche vordefinierten arithmetischen Vergleichsoperatoren kennt Prolog?

> Hinweis: Diese Operatoren erzwingen die arithmetische Auswertung ihrer beiden Operatoren.

* `>` : grösser als
* `<` : kleiner als
* `>=` : grösser-gleich
* `=<` : kleiner-gleich
* `=:=` : Gleichheit
* `=\=` : Ungleichheit

> `=` macht nur Matching!



## Was ist der Unterschied zwischen Operatoren und Prädikaten?

* Operatoren und Prädikate sind dasselbe
* Zwei verschiedene Schreibweisen
* Gründsätzlich gibt es nur Prädikate,
* manche können jedoch auch als Operatoren verwendet werden



## Wie kann man aus Prädikaten Operatoren erstellen?

* mit dem eingebauten Prädikat `op/3` können Prädikate als Operatoren deklariert werden



## Vordefinierte Operatoren (Auswahl)

| Präzedenz | Typ  | Name        |
| --------- | ---- | ----------- |
| 1200      | xfx  | `—>` , `:-` |
| 1200      | fx   | `:-` , `?-` |
| // TODO   |      |             |
|           |      |             |
|           |      |             |
|           |      |             |



## Was macht die Präzedenz von Operatoren?

* gibt an, wie stark dieser Operator seine Operaden binden
* Tiefere Präzedenz = stärkere Bindung
* Operator mit höchster Präzedenz ist Haupt-Funktor von einem gegebenem Term
* 1 - 1200



## Welche Operator-Typen gibt es in Prolog?

> Typ gibt die relative Reihenfolge von Operator `f`​ und Operanden `x` , `y`  an

* Infix: `xfx` , `xfy` , `yfx`  (Operator `f` zwischen Operanden)
* Präfix: `fx` , `fy`  (Operator `f` vor Operand)
* Postfix: `xf` , `yf`  (Operator `f` nach Operand)



// TODO slide 35 - 40



## Wann ist ein Prädikat rekursiv definiert?

* Falls sich eine oder mehrere Regeln in ihrer Definition auf sich selber beziehen



## Einsatz von Rekursion

// TODO slide 43-52



> Berechnung von fibonacci (slide 48) ist überhaupt nicht effizient

