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