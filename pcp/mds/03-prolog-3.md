# Prolog 3



## Wie optimiert man Prolog-Programme?

* Prolog verwendet grundsätzlich Backtracking, d.h. Tiefensuche zur Problemlösung
* grundsätzlich nicht effizient
* Zwei Methoden zur Optimierung
  * Endrekursion
  * Assertions



## Was ist Endrekursion?

* rekursive Funktion, bei der
* der rekursive Funktionsaufruf die letzte Aktion zur Berechnung von *f* ist



## Wann ist eine Prozedur endrekursiv?

Wenn,

* sie nur einen rekursiven Aufruf hat und
* dieser rekursive Aufruf ist der letzte Aufruf in der letzten Klausel von dieser Prozedur
* Aufrufe vor dem rekursiven Aufruf alle deterministisch sein

> alle Punkte zusammen!



## Was ist der Vorteil von Endrekursion?

* kein zusätzlicher Speicherplatz zur Verwaltung der Rekursion notwendig
* kein Backtracking notwendig
* Endrekursion kann als Iteration ohne zusätzlichen
  Speicherplatz ausgeführt werden



## Beispiel Endrekursion

```erlang
p(...) :- ...  	% no recursive call in the body 
p(...) :- ...  	% no recursive call in the body
...
p(...) :- 
	..., 		% all deterministic and
	..., 		% no recursive calls until here. 
    p(...). 	% here: tail-recursive call
```

> Iteration (weniger Speicher benötigt)



## Was ist mit "last call optimization" gemeint?

* Endrekursion



## Definiere die Datenstruktur Liste

* endliche Sequenz von Elementen
* in Prolog mit Hilfe von [ ] (eckigen Klammern) dargestellt
* Elemente einer Liste werden in eckigen Klammern eingeschlossen und durch Komma getrennt

```erlang
?- Y = [d, e, f(X), [x, y]].
Y = [d, e, f(X), [x, y]].
```



## Wie sind Listen aufgebaut?

* rekursiv
* TODO

