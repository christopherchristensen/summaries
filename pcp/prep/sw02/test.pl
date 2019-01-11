:- dynamic bigger/2.
bigger(man, tree). % Grundterme
bigger(tree, house).
bigger(tree, bird).
bigger('randomness', 'more-randomness').

'test print'(hallo).

elephant.

praedicate(5).

is_bigger(X, Y) :- bigger(X, Y).
is_bigger(X, Y) :- bigger(X, Z), is_bigger(Z, Y).

is_smaller(X, Y) :- bigger(Y, X).
is_smaller(X, Y) :- bigger(Y, Z), is_bigger(Z, X).