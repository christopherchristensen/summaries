:- dynamic add_tail/3.

add_tail(ELEMENT, [], [ELEMENT]).                   % Für die letzte Rekursion, wenn x das Element und der Tail nur noch [] ist.
add_tail(ELEMENT, [HEAD | TAIL], NEUE_LISTE_1) :-   % (Element zum hinzufügen, Liste wird gesplittet in Head und Tail, Neue Liste)
    add_tail(ELEMENT, TAIL, NEUE_LISTE_2),          % Selbe Funktion wieder aufgerufen nur mit Tail (so wird x immer weiter nach hinten verschoben [a,x,b,c] -> [a,b,x,c])
    NEUE_LISTE_1 = [HEAD | NEUE_LISTE_2].           % Danach wird [a | [b,c,x]] gerechnet.

:- dynamic del/3.


del([HEAD, TAIL], ELEMENT, NEUE_LISTE_1):-
    del(TAIL, ELEMENT, NEUE_LISTE_2),
    NEUE_LISTE_1 = [HEAD | NEUE_LISTE_2].