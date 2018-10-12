# Prolog 6



## Wie könnte man mit Prolog ein Sudoku lösen?

* alle Anforderungen deklarieren (in Prädikaten modellieren)
* mit CLP-FD
* `sudoku/1`  wird mit einer Liste (Puzzle) von Listen aufgerufen. Diese Liste enthält je eine Liste mit 9 Elementen (Feldern) für jede der 9 vorgegebenen Zeilen

```erlang
:- use_module(library(clpfd)).

% Anforderungen deklarieren
sudoku(Rows) :-

	% Alle Listen in Rows in Liste Vs zusammenfassen (append)
	% Wertebereich 1 bis 9 festlegen (finite Domäne, Vs ins 1...9)
	append(Rows, Vs), Vs ins 1..9,
    
  	maplist(all_distinct, Rows), % jede Ziffer exakt einmal pro Zeile
   
  	transpose(Rows, Columns), % transponiert Rows in neue Liste Columns
    
  	maplist(all_distinct, Columns), % jede Ziffer exakt einmal pro Spalte
    
    % die 9 Zeilen in Rows den Variablen A bis I zuweisen
  	Rows = [A, B, C, D, E, F, G, H, I], 
    
    % überprüft ob für Zeilen Z1, Z2 und Z3 Block-Anforderungen 
    % erfüllt sind
  	blocks(A, B, C), blocks(D, E, F), blocks(G, H, I),
  	maplist(label, Rows).

% Vorgehen rekursiv
blocks([], [], []). % Einfacher Fall: die drei Zeilen sind leer

% Allgemeiner Fall: Ersten 3 Elemente auf Verschiedenheit der 3 Zeilen 
% prüfen. Danach rekursiv Rest prüfen (Listenschwänze Bs1, Bs2, Bs3).
blocks([A, B, C|Bs1], [D, E, F|Bs2], [G, H, I|Bs3]) :-
  	all_distinct([A, B, C, D, E, F, G, H, I]),
  	blocks(Bs1, Bs2, Bs3).
```

```erlang
% Programm aufrufen, freie Felder als anonyme Variablen _
?- Puzzle = [
	[5, 3, _, _, 7, _, _, _, _],
	[6, _, _, 1, 9, 5, _, _, _],
	[_, 9, 8, _, _, _, _, 6, _],
	[8, _, _, _, 6, _, _, _, 3],
	[4, _, _, 8, _, 3, _, _, 1],
	[7, _, _, _, 2, _, _, _, 6],
	[_, 6, _, _, _, _, 2, 8, _],
	[_, _, _, 4, 1, 9, _, _, _],
	[_, _, _, _, 8, _, _, 7, 9]
	],
	Puzzle = [A, B, C, D, E, F, G, H, I], 
    sudoku([A, B, C, D, E, F, G, H, I]).
```



## Was macht das Prädikat `label/1`  im Sudoku-Beispiel?

* Weist den Variablen von `Rows` Werte zu,
* so dass die angegebenen Constraints alle erfüllt sind.

> Damit beginnt im Sudoku-Beispiel die eigentliche Lösungssuche an!



