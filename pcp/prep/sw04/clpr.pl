:- use_module(library(clpr)).
fib(N, F) :- { N = 0, F = 0 }.
fib(N, F) :- { N = 1, F = 1 }.
fib(N, F) :-
    { N > 0 },
    { N1 = N - 1 },
    { N2 = N - 2 },
    fib(N1, F1), fib(N2, F2),
    { F = F1 + F2 }.


