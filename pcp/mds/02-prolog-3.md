# Prolog 3



## Wie optimiert man Prolog-Programme?

* Prolog verwendet grundsätzlich Backtracking, d.h. Tiefensuche zur Problemlösung
* grundsätzlich nicht effizient
* Zwei Methoden zur Optimierung
  * Endrekursion
  * Assertions



## Wann ist eine Prozedur endrekursiv?

Wenn,

* sie nur einen rekursiven Aufruf hat und
* dieser rekursive Aufruf ist der letzte Aufruf in der letzten Klausel von dieser Prozedur



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

