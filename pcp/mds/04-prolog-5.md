# Prolog 5



## Wie kann man etwas falsches in Prolog ausdrücken?

* Dass etwas nicht stimmt, also falsch (false) ist, kann in Prolog mit dem Prädikat fail/0 ausgedrückt werden.

```erlang
snake(snake).
animal(snake).
animal(horse).
animal(dog).
likes(mary, X) :- snake(X), !, fail. % Mary mag keine Schlangen
likes(mary, X) :- animal(X).
```



## Welche Alternativen gibt es um etwas falschen in Prolog auszudrücken?

* `not(:Goal)`
  * Schwache Negation 
  * korrespondiert nicht exakt zu Negation in mathematischer Logik $\to$  basiert auf Closed World Assumption (CWA)
* `\+ :Goal` 

* Beispiel:

```erlang
?- not(likes(mary, snakes)).
true.

?- \+ likes(mary, snakes).
true.

% Weitere Beispiele
likes_with_not(mary, X) :- animal(X), not(snake(X)).
different_with_not(X, Y) :- not(X = Y).

?- likes_with_not (mary, snake).
false.

?- different_with_not(tom, mary).
true.
```



## Was ist der Unterschied zwischen den Prädikaten `not` und `\+` ?

* Kein Unterschied
* Beide Notationen sind äquivalent



## Was ist die Closed-World-Assumption (CWA)?

* Es wird angenommen, dass jedes Programm **alles** Wahre über die Welt beschreibt.
* Umgekehrt: alles, was nicht im Programm beschrieben ist, oder sich aus dem Programm nicht ableiten lässt, wird als falsch angenommen.
* Negierte Aussagen über Dinge, über welche ein Prolog-Programm nichts "weiss", werden als wahr angenommen.

> Die CWA in Prolog verdient spezielle Aufmerksamkeit, da wir im Alltagsleben nicht von einer „geschlossenen“ Welt ausgehen. Da können uns Prolog-Programme sonst „komische“ Resultate produzieren...



## Zeige ein Beispiel wo das Prädikat `not` komische Lösungen aufweist

```erlang
great_food(creaBeck).
great_food(novartis).
limited_seating(novartis).
good_place(Restaurant) :-
	not(limited_seating(Restaurant)).
```

```erlang
?- great_food(X), good_place(X). % query 1
X = creaBeck. % as expected

?- good_place(X), great_food(X). % query 2
false. % what went wrong?
```



* Bei Anfrage 1 ist das X schon instanziert
* Wenn „good_place(X)“ aufgerufen wird, bei Anfrage 2 jedoch nicht



> „not Goal“ funktioniert zuverlässig wenn die Variablen in „Goal“ instanziiert sind in dem Moment wenn, „not Goal“ aufgerufen wird. Andernfalls können unerwartete Resultate auftreten. Entsprechend sollte Negation nur bei Zielen verwenden, bei welchen die Variablen bereits instanziiert wurden



// TODO Slides 20 - 22



## Was ist die Motivation von Constraint Logic Programming (CLP)?

* Um arithmetische Berechnungen durchführen zu können

```erlang
% Ohne CLP
?- X + 1 = 5.
false.

% Mit CLP
?- { X + 1 = 5 }.
X = 4.
```



## Was ist notwendig um CLP verwenden zu können?

* Man muss die CLP-Library einbinden

```erlang
% Zur Laufzeit
?- use_module(library(clpr)).
% library(clpr) compiled into clpr 0.07 sec, 1,304 clauses
true.

% Vor Kompilierung
:- use_module(library(clpr)). 
convert_clp(Celsius, Fahrenheit) :-
{ Celsius = (Fahrenheit - 32) * 5 / 9 }.
```



## Was sind Constraint-Satisfaction-Probleme (CSP)?

* mathematische Probleme definiert durch
  * Eine Menge von Variablen
  * Domänen, aus welchen die Variablen Wert annehmen können
  * Constraints (Bedingungen) welche die Variablen erfüllen müssen

> Gesucht ist eine Zuweisung von Werten zu den Variablen, so dass diese Werte alle vorgegebenen Constraints erfüllen.



## Wie kann man CSPs lösen?

* Mit Hilfe von CLP
  * CLP-Bibliotheken geben die Domänen (Wertebereiche) für Variablen vor
  * CLP-R: reelle Zahlen
  * CLP-Q: rationale Zahlen
  * CLP-FD: finite Domänen



## Ist das folgende Beispiel ein CSP?

* Beispiel:

```erlang
:- use_module(library(clpr)). 
convert_clp(Celsius, Fahrenheit) :-
	{ Celsius = (Fahrenheit - 32)*5/9 }.
```

* Ja, es ist ein CSP, denn es hat die drei notwendigen Zutaten dafür:
  * Variablen: Celsius, Fahrenheit
  * Eine Domäne: reelle Zahlen
  * Constraints: Celsius = ( Fahrenheit - 32 ) * 5 / 9



// TODO Slide 32 ff.