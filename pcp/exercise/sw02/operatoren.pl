add(X, Y, Z) :-
    Z is X + Y.

mult(_,0,0).
mult(0,_,0).
mult(A,1,A).
mult(1,B,B).

mult(A, B, X) :-
    A > 0,
    B > 0,
    B2 is B - 1,
    mult(A, B2, X2),
    X is X2 + A.