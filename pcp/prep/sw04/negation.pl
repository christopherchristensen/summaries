object(car).

have(X) :- object(X).
dont_have(X) :- \+(object(X)).


snake(snake).
animal(snake).
animal(bird).

likes(mary, X) :- snake(X), !, fail.
likes(mary, X) :- animal(X).

not(P) :- P, !, fail.
not(_P) :- true.

