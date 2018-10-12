different(X,X):-
    !, fail.
different(_X, _Y).

snake(snake).
animal(snake).
animal(horse).
animal(dog).
likes(mary, X) :- snake(X), !, fail.
likes(mary, X) :- animal(X).

:- use_module(library(clpr)). 
:- use_module(library(clpfd)). 
fib_clp(N, F) :- 
    { N = 0, F = 0 }. 
fib_clp(N, F) :- 
    { N = 1, F = 1 }. 
fib_clp(N, F) :-
    { N >= 2, F = F1+F2, N1 = N-1, N2 = N-2 }, 
    fib_clp(N1, F1),
    fib_clp(N2, F2).


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

:- use_module(library(http/http_client)).
:- use_module(library(http/http_json)).