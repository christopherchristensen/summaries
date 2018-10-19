# Prolog 4



## Wie kann man das Backtracking von Prolog verfolgen?

* Mit `trace.` zur Programm-Laufzeit
* Graphischer Debugger von SWI-Prolog



## Weshalb reicht rein deklaratives Vorgehen bei Prolog-Programmen nicht?

* Weil durch Umordnen von Regeln und Zielen einer Klausel die Effizienz einer Prozedur verändert oder die Prozedur gar unbrauchbar macht
* Es braucht Wissen / Verständnis über wie Prolog funktioniert (deterministische Tiefensuche mit Backtracking)



## Wie sollte man Vorgehen beim Erstellen eines Prädikats oder Faktes?

* Zuerst immer einfache Dinge probieren
  * D.h. typischerweise Rekursionsbasis als erste Regel angeben (danach allgemeiner Fall)
  * D.h. auch bei einzelnen Zielen einer Regel zuerst die einfachen Ziele angeben (danach die komplizierteren)

​	

## Wie sind Regeln in Prolog aufgebaut?

* Aus 	
  * einem Kopf (head) und
  * einem Hauptteil (body) mit Zielen,
  * durch `:-` getrennt.
  * Ziele im Hauptteil mit `,` getrannt und `.` abgeschlossen
* Der Kopf einer Regel ist wahr, falls alle Ziele (Prädikate, Goals) im Hauptteil als wahr bewiesen werden können



## Was bedeutet das `,`  in Prolog?

* Logisches UND
* d.h. alle Ziele einer Regel werden ver-UND-et (Konjunktion)



## Was bedeutet Konjunktion von Anfragen?

* das ver-UND-en von Regeln, Termen oder (zur Laufzeit) einzelne Anfragen
* wird ermöglicht durch durch eingebautes Prädikat `,` 
* logisches UND

```erlang
?- X = Y, X = pia.
X = Y, Y = pia.

?- X = Y, X = pia, Y = tom.
false.
```



## Was bedeutet Disjunktion von Zielen?

* Das ver-ODER-n von Zielen
* wird ermöglicht durch eingebautes Prädikat `;` 

```erlang
rich(tom). 
nice(mary). 
interesting(X) :-
            rich(X); % rich ODER nice
            nice(X).
```

```erlang
% zur Laufzeit
?- interesting(tom).
true.

?- interesting(mary).
true.
```

> Anfragen können ebenfalls ver-ODER-t werden.



## Wie würde man eine Regel mit einer Disjunktion in eine Regel ohne Disjunktion umwandeln?

* Zwei Regeln erstellen
* Eine Regel mit einer Disjunktion ist äquivalent zu zwei Regeln mit den beiden Operanden der Disjunktion



## Was ist der Nachteil von Disjunktion?

* schlechter lesbar $\to$ nicht gleich verständlich



## Was ist der Cut-Operator?

* Ein eingebautes Prädikat von Prolog `!/0` 

  * Nimmt keine Argumente entgegen
  * Ist immer erfüllt
  * Bindet bisherige Wahl innerhalb der aktuellen Klausen

* Nach einem Cut-Prädikat kann kein Backtracking in der betroffen Regel mehr ausgeführt werden


 ## Weshalb ist ein Cut-Operator sinnvoll?

* Backtracking kann zu Ineffizienz führen
* Prolog kann Zeit und Speicher verschwenden um Möglichkeiten zu erkunden, die nirgens hinführen
* Der Cut-Operator bietet die Möglichkeit Backtracking zu beinflussen



## Inwiefern verändert der Cut-Operator die Bedeutung von Prolog?

* Nicht mehr rein deklarativ
* Dazu ist auch eine prozedurale Betrachtung notwendig







## Kontrollfragen



#### Spielt die Reihenfolge der Regeln und die Reihenfolge der Ziele einer Regel in der Wissensdatenbank eine Rolle?

* Ja, sie hat einen Einfluss auf die Programm-Ausführung.

```erlang
bigger(elephant, horse). 
bigger(horse, dog). 
bigger(horse, sheep). 

ib_1(X, Y) :- 
	bigger(X, Z),
	ib_1(Z, Y). 
	
ib_1(X, Y) :- bigger(X, Y).
```

* Liefert dieselben Resultate wie das ursprüngliche `is_bigger/2` - Prädikat, nur ist der Suchbaum jeweils anders.
* Ausführung ist in diesem Beispiel weniger effizient.
* In anderen Variationen kann das Verändern der Reihenfolge das Programm zu Errors führen und somit unbrauchbar machen.

* Verwende `trace.` zur Programm-Laufzeit, um die Programm-Ausführung zu verfolgen.



#### Eine Wissensdatenbank enthält die Fakten `f(a). f(b). g(c).` und die Regel `g(X) :- f(X).` . Welche Resultate werden auf die Anfrage `g(G)` in welcher Reihenfolge geliefert?

1. `X = c,`
2. `X = a,` 
3. `X = b.`

* Zuerst wird der Fakt `g(c)` gefunden, erst danach die Regel.
* Die Reihenfolge in der die Fakten / Regeln deklariert sind spielt hier also eine Rolle auf die Reihenfolge der Antworten.



#### Zeichne den Suchbaum zu obigem Beispiel mit der Anfrage `g(G)` 

![suchbaum-prolog-4](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/suchbaum-prolog-4.png)

#### Welches Resultat wird in obigem Beispiel auf `?- g(a).` geliefert?

* `true.` 
* Es findet den Fakt.



#### Was für Konsequenzen kann das Ändern der Reihenfolge von Regeln und der Reihenfolge der Ziele von einzelnen Klauseln für eine Prozedur haben?

* Kann die Effizienz des Programms verbessern oder verschlechtern
* Kann dazu führen, dass das Programm nicht mehr ausgeführt werden kann (zum Beispiel bei transitiven Regeln!)
* Der Suchbaum wird auch verändert



#### Gegeben ist eine Wissensdatenbank (siehe unten). Was für Lösungen findet Prolog auf die Anfrage `?- u(X)` .

* Gegeben:

```erlang
u(1).
u(X) :- v(X).
u(2).
v(_X) :- !, write("CUT").
```

* Lösung: // TODO

```
?- u(X).
X = 1,
"CUT".

```

