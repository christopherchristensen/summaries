% fib_tr(N, F) :- fib_tr(N, 0, 1, F).
% fib_tr(0, A, _, A).
% fib_tr(N, A, B, F) :-
%     N1 is N - 1,
%     N1 >= 0,
%     Sum is A + B,
%     fib_tr(N1, B, Sum, F).



:- dynamic bigger/2.
bigger(elephant, horse).
bigger(horse, dog).
bigger(horse, sheep).

% Assertion braucht mehr Speicher,
% und er nimmt zuerst den letzten Eintrag und wenn dies nicht
% die Assertion ist, die gesucht wird, wird wieder rekursiv im
% Speicher gesucht (wieder Rekursion, also wieder ineffizient)
% siehe: listing(fib_as), dann sieht man den gesammten Speicher
% nach Ausführung von fib_as. Plus manchmal werden Fakten mehrmals
% gespeichert.
:- dynamic fib_as/2.
fib_as(0, 0).
fib_as(1, 1).
fib_as(N, F) :-
    N > 1,
    N1 is N-1,
    N2 is N-2,
    fib_as(N1, F1),
    fib_as(N2, F2),
    F is F1+F2,
    asserta(fib_as(N, F)).

% Liste aus Vorlesung (S.34)
mem(X, [X | _]). % tail doesn’t matter 
mem(X, [_| Tail]) :- mem(X, Tail). % head doesn’t matter

% Listenkonkatenation
conc([], L, L).
conc([X | L1], L2, [X | L3]) :- conc(L1, L2, L3).

mem_c(X, L) :-
    conc(_, [X | _], L). % Ähnlich wie Kontrollfrage 2 (S. 43)

f(a).
f(b).
g(c).

g(X) :-
    f(X).

u(1).
u(X) :- 
    v(X).
u(2).
v(_X) :- 
    !, write("CUT").

max1(X, Y, Z) :- 
    X >= Y, !, X = Z. 

max1(_X, Y, Y).

r(a) :- !. 
r(b). 
r(c).

b(b). 
b(a) :- !. 
b(c).

fib_tr(N,F) :-
    fib_tr(N, 0, 1, F).

fib_tr(0,A,_,A).
fib_tr(N,A,B,F) :-
    N1 is N - 1,
    N1 >= 0,
    Sum is A + B,
    fib_tr(N1, B, Sum, F).