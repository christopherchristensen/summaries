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
    efib_clp(N1, F1),
    fib_clp(N2, F2).