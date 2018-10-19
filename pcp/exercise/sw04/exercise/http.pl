:- use_module(library(http/json_convert)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_client)).


% http_get('http://localhost:16316/problem/relationship/765', Reply, []).
% http_post('http://localhost:16316/test',json(['say hi to http post']),SolutionResponse,[]).


% Aus Übung SW02 --- RELATIONSHIPS
female(mary). female(liz). female(mia). female(tina). female(ann). female(sue). female(inge).
male(mike). male(jack). male(fred). male(tom). male(joe). male(jim). male(per).
parent(mary, mia). parent(mary, fred). parent(mary, tina). 
parent(mike, mia). parent(mike, fred). parent(mike, tina). 
parent(liz, tom). parent(liz, joe).
parent(jack, tom). parent(jack, joe). 
parent(mia, ann).
parent(tina, sue). parent(tina, jim). 
parent(tom, sue). parent(tom, jim).
parent(inge, mary). parent(per, mary).

mother(MOM, KID) :- 
    parent(MOM, KID), female(MOM).

is_mother(MOM, KID) :- mother(MOM, KID).

father(DAD, KID) :-
    parent(DAD, KID), male(DAD).

% Um alle Kinder von Mary zu bekommen, kann man mother(mary, X). ausführen

sibling(KID, SIBLING) :-
    parent(PARENT, KID), parent(PARENT, SIBLING).

grandmother(GRANDMOTHER, GRANDKID) :-
    parent(GRANDMOTHER, MOTHER), parent(MOTHER, GRANDKID), female(GRANDMOTHER).

% Um alle Grossmütter von jim auszugeben, kann man grandmother(X, jim). ausführen

% Zwei Möglichkeiten
% 1. Möglichkeit:
% offspring(ANCESTOR, OFFSPRING) :-
%     parent(ANCESTOR, OFFSPRING).
% 
% offspring(ANCESTOR, OFFSPRING) :-
%     parent(ANCESTOR, PARENT), parent(PARENT, OFFSPRING).
% Aber nur über zwei Generationen

% 2. Möglichkeit:
offspring(OFFSPRING, ANCESTOR) :-
    parent(ANCESTOR, OFFSPRING).

offspring(OFFSPRING, ANCESTOR) :-
    parent(ANCESTOR, PARENT), offspring(OFFSPRING, PARENT).

is_offspring(OFFSPRING, ANCESTOR) :- offspring(OFFSPRING, ANCESTOR).
% Funktioniert über mehrere Generationen

% 5. Eigener Familien-Operator

?- op(1150, xfx, is_mother).
?- op(1150, xfx, is_offspring).

% --- SUDOKU aus den Folien
:- use_module(library(clpfd)).

sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9, maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [A, B, C, D, E, F, G, H, I],
    blocks(A, B, C), blocks(D, E, F), blocks(G, H, I), maplist(label, Rows),
    RESULT = Rows.

blocks([], [], []).

blocks([A, B, C|Bs1], [D, E, F|Bs2], [G, H, I|Bs3]) :-
    all_distinct([A, B, C, D, E, F, G, H, I]),
    blocks(Bs1, Bs2, Bs3).

% ---

% JSON TO PROLOG
% :- json_object
%         point(x:integer, y:integer).
% http://www.swi-prolog.org/pldoc/man?section=jsonconvert

% HTTP --- Übergebene Prädikat aufrufen
:- json_object
    % JSON Objekte definieren, um von und nach JSON parsen zu können
    relationship(problemKey: integer, relationship: atom, firstPerson: atom, secondPerson: atom),
    relationship_solution(solution: atom, problemKey: integer),
    sudoku_object(problemKey: integer, sudoku: list),
    sudoku_solution(problemKey: integer, solution: list).


% Prädikate definieren
solve_relationship(RELATIONSHIP, FIRST_PERSON, SECOND_PERSON, RESULT) :-
    call(RELATIONSHIP, FIRST_PERSON, SECOND_PERSON),
    RESULT = true, !.

solve_relationship(RELATIONSHIP, FIRST_PERSON, SECOND_PERSON, RESULT) :-
    not(call(RELATIONSHIP, FIRST_PERSON, SECOND_PERSON)),
    RESULT = false, !.

solve_sudoku(PUZZLE, RESULT) :-
    maplist(replace_0, PUZZLE, RESULT),
	RESULT = [A, B, C, D, E, F, G, H, I],
	sudoku([A, B, C, D, E, F, G, H, I]).
    
    

% solve(relationship, ).
solve(relationship, PROBLEM_ID) :-

    atom_concat("http://localhost:16316/problem/relationship/", PROBLEM_ID, URL),
    http_get(URL, REPLY, []),

    % Von JSON nach prolog convertieren in das zuvor definierte JSON Objekt
    json_to_prolog(REPLY, relationship(PROBLEM_ID, RELATIONSHIP, FIRST_PERSON, SECOND_PERSON)),

    % Prädikat aufrufen, um RESULT zu erhalten 
    solve_relationship(RELATIONSHIP, FIRST_PERSON, SECOND_PERSON, RESULT),

    % Prolog zu JSON umwandeln mit zuvor definiertem JSON Objekt
    prolog_to_json(relationship_solution(RESULT, PROBLEM_ID), JSON_OBJECT),

    % POST mit RESULT und PROBLEM
    http_post("http://localhost:16316/problem/relationship", json(JSON_OBJECT), _, []),
    !. % CUT


% solve(sudoku, ).
solve(sudoku, PROBLEM_ID) :-

    atom_concat("http://localhost:16316/problem/sudoku/", PROBLEM_ID, URL),
    
    http_get(URL, REPLY, []),

    % Von JSON nach prolog convertieren in das zuvor definierte JSON Objekt
    json_to_prolog(REPLY, sudoku_object(PROBLEM_ID, PUZZLE)),

    % Prädikat aufrufen, um RESULT zu erhalten 
    solve_sudoku(PUZZLE, RESULT),

    % Prolog zu JSON umwandeln mit zuvor definiertem JSON Objekt
    prolog_to_json(sudoku_solution(PROBLEM_ID, RESULT), JSON_OBJECT),

    % POST mit RESULT und PROBLEM
    http_post("http://localhost:16316/problem/sudoku", json(JSON_OBJECT), _, []),
    !. % CUT


% ABGESCHAUT
replace_0(L1, L2) :-
    maplist(replace_help, L1, L2),
    !.
replace_help(0, _).
replace_help(X, X).