:- dynamic fak_as/2.
:- dynamic fak_clear/0.

fak(0, 1).

fak(N, F) :-
    fak_as(N, F), % Sucht zuerst hier nach gespeichertem Wert
    write("Hinweis: Fakultät von "),
    write(N),
    write(" war gespeichert").

fak(N, F) :-
    N > 0,
    N1 is N - 1,
    fak(N1, F1),
    F is N * F1,
    asserta(fak_as(N, F)). % Speichert Resultat ins Prädikat fak_as/2 => z.B. asserta(fak_as(5, 120)).

fak_clear :-
    retractall(fak_as(_,_)), % Lösche alle gespeicherten Einträge vom Prädikat fak_as/2.
    write("Hinweis: Alle gespeicherten Werte wurden gelöscht").