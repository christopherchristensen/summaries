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
