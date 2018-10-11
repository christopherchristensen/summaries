/**
p(X):- 
    a(X). 

p(X):- 
    b(X), 
    c(X). 

p(X):- 
    d(X).

a(1).
b(2). 
b(3).
c(2). 
c(3).
d(4).

*/

p(X):- 
    a(X).

p(X):- 
    b(X), !, c(X). 

p(X):- 
    d(X).

a(1).
b(2). 
b(3).
c(2). 
c(3).
d(4).

/**

warn(T) :- 
    T < 80, 
    write('Temperatur ok'), !.

warn(T) :- 
    T < 100, 
    write('Temperatur sehr warm'), !. 

warn(_) :- 
    write('Temperatur zu heiss').

*/

warn(T) :- 
    T < 80, 
    write('Temperatur ok').

warn(T) :- 
    T > 80,
    T < 100, 
    write('Temperatur sehr warm'). 

warn(_) :- 
    write('Temperatur zu heiss').