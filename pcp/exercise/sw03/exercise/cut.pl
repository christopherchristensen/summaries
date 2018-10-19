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



warn1(T) :- 
    T < 80, 
    write('Temperatur ok'), !.

warn1(T) :- 
    T < 100, 
    write('Temperatur sehr warm'), !. 

warn1(_) :- 
    write('Temperatur zu heiss').



warn2(T) :- 
    T < 80, 
    write('Temperatur ok').

warn2(T) :- 
    T > 80,
    T < 100, 
    write('Temperatur sehr warm'). 

warn2(_) :- 
    write('Temperatur zu heiss').


mem(X, [X | _]):- !. % tail doesn’t matter 
mem(X, [_| Tail]) :- % head doesn’t matter
    mem(X, Tail). 