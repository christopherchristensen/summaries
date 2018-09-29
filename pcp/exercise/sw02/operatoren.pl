add(X, Y, Z) :-
    Z is X + Y.

mult(X, Y, Z) :-

    X =:= 0 ->
    Z is X ;

    Y =:= 0 ->
    Z is Y ;

    X1 = X - 1,
    mult(X1, Y, XY), add(XY, Y, Z). % X = 0