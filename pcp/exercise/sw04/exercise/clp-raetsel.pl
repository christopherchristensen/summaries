% a.) Ist auf mehrere Arten möglich!
:- use_module(library(clpr)).
:- use_module(library(clpfd)).

% Erste Möglichkeit mit einem Prädikat
double_age(DAUGHTER_AGE, MOTHER_AGE, YEARS) :-
    {DAUGHTER_AGE + YEARS = (MOTHER_AGE + YEARS) / 2}, !. % Wenn gewünschte Bedingung zutrifft.

double_age(DAUGHTER_AGE, MOTHER_AGE, YEARS) :-
    not(DAUGHTER_AGE = {MOTHER_AGE / 2}), % Wenn gewünschte Bedingung nicht zutrifft.
    YEARS = {YEARS + 1},
    double_age(DAUGHTER_AGE, MOTHER_AGE, YEARS).

% b.) 
donald_gerald_robert([D, O, N, A, L, D] + [G, E, R, A, L, D] = [R, O, B, E, R, T]) :-

    Vars = [D, O, N, A, L, G, E, R, B, T], 
    Vars ins 0..9, 

    all_distinct(Vars),
        D*100000 + O*10000 + N*1000 + A*100 + L*10 + D +
        G*100000 + E*10000 + R*1000 + A*100 + L*10 + D #= 

    R*100000 + O*10000 + B*1000 + E*100 + R*10 + T, 
    D #\= 0, G #\= 0, R #\=0,
    label(Vars).

% ?- donald_gerald_robert(A + B = C).
% A = [5, 2, 6, 4, 8, 5],
% B = [1, 9, 7, 4, 8, 5],
% C = [7, 2, 3, 9, 7, 0] ;
% false.