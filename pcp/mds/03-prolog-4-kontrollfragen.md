## Kontrollfragen



#### Spielt die Reihenfolge der Regeln und die Reihenfolge der Ziele einer Regel in der Wissensdatenbank eine Rolle?

- Ja, sie hat einen Einfluss auf die Programm-Ausführung.

```erlang
bigger(elephant, horse). 
bigger(horse, dog). 
bigger(horse, sheep). 

ib_1(X, Y) :- 
	bigger(X, Z),
	ib_1(Z, Y). 
	
ib_1(X, Y) :- bigger(X, Y).
```

- Liefert dieselben Resultate wie das ursprüngliche `is_bigger/2` - Prädikat, nur ist der Suchbaum jeweils anders.
- Ausführung ist in diesem Beispiel weniger effizient.
- In anderen Variationen kann das Verändern der Reihenfolge das Programm zu Errors führen und somit unbrauchbar machen.
- Verwende `trace.` zur Programm-Laufzeit, um die Programm-Ausführung zu verfolgen.



#### Eine Wissensdatenbank enthält die Fakten `f(a). f(b). g(c).` und die Regel `g(X) :- f(X).` . Welche Resultate werden auf die Anfrage `g(G)` in welcher Reihenfolge geliefert?

1. `X = c,`
2. `X = a,` 
3. `X = b.`

- Zuerst wird der Fakt `g(c)` gefunden, erst danach die Regel.
- Die Reihenfolge in der die Fakten / Regeln deklariert sind spielt hier also eine Rolle auf die Reihenfolge der Antworten.



#### Zeichne den Suchbaum zu obigem Beispiel mit der Anfrage `g(G)` 

![suchbaum-prolog-4](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/suchbaum-prolog-4.png)

#### Welches Resultat wird in obigem Beispiel auf `?- g(a).` geliefert?

- `true.` 
- Es findet den Fakt.



#### Was für Konsequenzen kann das Ändern der Reihenfolge von Regeln und der Reihenfolge der Ziele von einzelnen Klauseln für eine Prozedur haben?

- Kann die Effizienz des Programms verbessern oder verschlechtern
- Kann dazu führen, dass das Programm nicht mehr ausgeführt werden kann (zum Beispiel bei transitiven Regeln!)
- Der Suchbaum wird auch verändert



#### Gegeben ist eine Wissensdatenbank (siehe unten). Was für Lösungen findet Prolog auf die Anfrage `?- u(X)` .

- Gegeben:

```erlang
u(1).
u(X) :- v(X).
u(2).
v(_X) :- !, write("CUT").
```

- Lösung: // TODO

```
?- u(X).
X = 1,
"CUT".
```

