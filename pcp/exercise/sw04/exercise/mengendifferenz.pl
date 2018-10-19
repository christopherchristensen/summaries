mem(X, [X | _]).     % tail doesn’t matter 
mem(X, [_| Tail]) :- % head doesn’t matter
    mem(X, Tail). 


set_difference([], _, []). % Rekursionsbasis, wenn Liste leer, dann gib eine leere Liste zurück
set_difference(LISTE, [], LISTE). % Fall, dass Liste mit einer leeren Liste abgeglichen wird

set_difference([HEAD | TAIL], LISTE, NEUE_LISTE) :- % Regel 1,
    not(mem(HEAD, LISTE)), % Head ist nicht Member der Liste
    !, % Ansonsten wird nicht in Regel 2 weitersuchen
    append(TEMP, [HEAD], NEUE_LISTE), % Head wird der neuen Liste angefügt
    set_difference(TAIL, LISTE, TEMP). % Aufruf mit dem Rest der Liste
    
set_difference([_ | TAIL], LISTE, NEUE_LISTE) :- % Head interessiert nicht
    set_difference(TAIL, LISTE, NEUE_LISTE).