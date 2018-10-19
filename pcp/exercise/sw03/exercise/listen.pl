% a.)
add_tail(ELEMENT, [], [ELEMENT]).                   % Für die letzte Rekursion, wenn x das Element und der Tail nur noch [] ist.
add_tail(ELEMENT, [HEAD | TAIL], NEUE_LISTE_1) :-   % (Element zum hinzufügen, Liste wird gesplittet in Head und Tail, Neue Liste)
    add_tail(ELEMENT, TAIL, NEUE_LISTE_2),          % Bis TAIL eine leere Liste ist
    NEUE_LISTE_1 = [HEAD | NEUE_LISTE_2].           % Danach wird [a | [b,c,x]] gerechnet.

% b.)
del([ELEMENT], ELEMENT, []). % Wenn in der Liste nur noch zu löschende Element vorhanden ist. -> Rekursionsbasis 2
                             % Tritt ein wenn Element am Ende der Liste ist.
del([], _, []).              % Gibt eine leere Liste zurück, wenn leere Liste übergeben wird -> Rekursionsbasis 1


del([HEAD | TAIL], ELEMENT, LISTE_1) :- % Liste, Element, Neue Liste
    HEAD = ELEMENT,                     % Wenn Kopf gleich dem übergebenen Element entspricht (wenn nicht, dann Abbruch)
    del(TAIL, ELEMENT, LISTE_2),        % Tail wird weitergegeben (bis zur Rekursionsbasis)
    LISTE_1 = LISTE_2.


del([HEAD | TAIL], ELEMENT, LISTE_1) :- % Fügt den HEAD der neuen Liste hinzu
    del(TAIL, ELEMENT, LISTE_2),
    LISTE_1 = [HEAD | LISTE_2].     

% c.)
mem(X, [X | _]).     % tail doesn’t matter 
mem(X, [_| Tail]) :- % head doesn’t matter
    mem(X, Tail). 

mem_d(ELEMENT, LISTE) :-
    del(LISTE, ELEMENT, LISTE_1),
    not(LISTE = LISTE_1). % Wenn die Listen nicht mehr gleich sind nachdem ein Element entfernt wurde, dann war das Element in der Liste!

% d.)
rev_acc([ELEMENT], [], [ELEMENT]). % Falls die Liste nur ein Element enthält (kann nicht in Teile gesplittet werden)

rev_acc([], A, A). % Rekursionsbasis (Sobald Tail der ursprünglichen Liste leer ist wird einfach Akkumulater zurückgegeben)

rev_acc([HEAD | TAIL], AKKUM , NEUE_LISTE_1) :-
    AKKUM_TEMP = [HEAD | AKKUM],
    rev_acc(TAIL, AKKUM_TEMP, NEUE_LISTE_1).

% e.)
rev(LISTE, REVERSE_LISTE) :-
    rev_acc(LISTE, [], REVERSE_LISTE).