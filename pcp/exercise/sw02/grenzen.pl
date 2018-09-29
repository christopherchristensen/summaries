% Es gibt eine Lösung zu diesem Problem

n(red, green).
n(red, yellow).
n(green, yellow).
n(green, red).
n(yellow, green).
n(yellow, red).

colors(LU, NW, OW, SZ, UR, ZG) :-
    UR = yellow,
    SZ = red,
    n(LU, ZG),
    n(LU, SZ),
    n(LU, NW),
    n(LU, OW),
    n(ZG, SZ),
    n(ZG, LU),
    n(SZ, ZG),
    n(SZ, LU),
    n(SZ, NW),
    n(SZ, UR),
    n(UR, SZ),
    n(UR, NW),
    n(NW, UR),
    n(NW, SZ),
    n(NW, OW),
    n(NW, LU),
    n(OW, LU),
    n(OW, NW).