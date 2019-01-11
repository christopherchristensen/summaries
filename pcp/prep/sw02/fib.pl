fib(0, 0).
fib(1, 1).

fib(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, F1), fib(N2, F2),
    F is F1 + F2.


fib_tr(N, F) :- fib_tr(N, 0, 1, F).
fib_tr(0, A, _, A).
fib_tr(N, A, B, F) :-
    N1 is N - 1,
    N1 >= 0,
    Sum is A + B,
    fib_tr(N1, B, Sum, F).