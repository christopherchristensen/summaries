a(a).
b(a).
b(b).

f(X) :- a(X), !, b(X).

g(X) :- a(X), b(X).

u(1).
u(x) :- v(x).
u(2).
v(x) :- write('CUT').

max(X, Y, X) :- X >= Y, !.
max(X, Y, Y) :- X < Y.