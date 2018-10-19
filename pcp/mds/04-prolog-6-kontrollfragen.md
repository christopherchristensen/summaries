## Kontrollfragen

#### Was bewirkt das eingebaute Prädikat `all_distinct/1` ?

- Dass jeder Wert nicht zweimal vorkommt



#### Was bewirkt das eingebaute Prädikat `maplist/2 ` ? Erläutere die Anwendung an einem eigenen Beispiel.

- Bildet jedes Prädikat auf jedes Element der Liste ab
- `NaturalNumber = [], maplist(not(0), NaturalNumbers).` 



#### Was bewirkt `transpose/2` auf eine Liste von Listen? Machen Sie zur Illustration ein Beispiel dazu.

- Matrixoperation "transponieren"
- Zeilen auf Spalten abbilden



#### Was passiert, wenn `sudoku/1` mit einer Liste von 9 Listen mit je 9 anonymen Variablen aufgerufen wird? Was ist also die von Prolog ermittelte Lösung zu einer Sudoku-Instanz ohne vorgegebene Zahlen?

- Gibt alle möglichen Lösungen aus, 
- da wir keine Werte vorgegeben haben



#### Mit welchen beiden Prädikaten werden aus Prolog GET- resp. POST-Anfragen gestellt?

- `http_get/3`
- `http_post/4`



#### Welche Antwort erwartet man bei einer GET- Anfrage auf die nicht-existente URL „http://www.invalid-url.net/“?

- Error (Socket Error)



#### Aus welchen Elementen sind JSON-Objekte grundsätzlich aufgebaut? Machen sie je ein Beispiel für jeden Element-Typ.

- Listen,
- Key/Value Pairs
- Atom und 
- Nummern



#### Was können Sie mit dem eingebauten Prädikat `call/2` tun? Illustrieren Sie an einem Beispiel.

- Prädikate generisch aufrufen
- Erstes Argument ist das Prädikat, danach Variablen
- `call(is_bigger, mary, john)` .



#### Wie kann `maplist/3` eingesetzt werden? (inkl.Beispiel)

- Führt Prädikat auf gesamte List aus

```erlang
?- maplist(sqrt, [4, 9, 16], X).
X = [2.0, 3.0, 4.0].
```





