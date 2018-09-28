# 03 Logische Programmierung

* beschreibt was wir wollen
* **nicht** wie wir es berechnen
* *Prolog*



## Was sind die wichtigsten Mechanismen in Prolog?

* Matching 
* automatisches Backtracking

> Prolog geht davon aus, das alles was er nicht kennt, falsch ist



## Was versteht man unter der Wissensdatenbank?

* Zentral ist die Wissensdatenbank, worin alle Fakten & Regeln stecken. 
* Die Wissensdatenbank kann angefragt werden, wobei Prolog darauf entsprechend antwortet.

![wissensdatenbank](/Users/christopher/Development/studies/github/summaries-me/pcp/mds/imgs/wissensdatenbank.png)



## Anwendungsbeispiel I von Prolog

```erlang
% Drei Fakten sind in Wissensdatenbank enthalten. 
% Bigger definiert, dass erstes Element grösser als zweites Element ist.

bigger(elephant , horse).
bigger(horse , dog).
bigger(horse , sheep).

% Gegen die Wissensdatenbank kann eine Anfrage gemacht werden. Prolog prüft ob es für die Anfrage einen Match gibt. Jedoch existiert aber keine Match dafür. Nirgends ist definiert, dass ein Hund grösser als ein Elefant ist.

?- bigger(dog, elephant).
false.

% Für folgende Anfrage ist ein Match vorhanden. Fakt 1 in der Wissensdatenbank 
% matched die Anfrage.

?- bigger(elephant , horse).
true.

% Bei Anfragen können auch Variabeln definiert werden. Alle gross geschriebenen Wörter sind Variabeln. Prolog sucht nun nach allen Matches, welche als erstes Element horse haben. Als Resultat werden alle möglichen X Werte geliefert (Prolog liefert immer nur ein Resultat - möchte man weitere Resultate ansehen, muss Semikolon gedrückt werden).

?- bigger(horse, X).
X = dog ;
X = sheep ;
false.
```



## Anwendungsbeispiel II von Prolog

```erlang
% Wir wissen implizit, dass der Elefant grösser ist als der Hund. Da der Elefant grösser als das Pferd ist und das Pferd grösser als der Hund. Aber eine Anfrage ob der Elefant nun grösser als der Hund ist, würde false liefern. Es müssen Regeln definiert werden, welche diese Beziehung unter den Fakten abbilden. Wir definieren für bigger/2 eine transitive Hülle.

is_bigger(X, Y) :- bigger(X, Y).
is_bigger(X, Y) :- bigger(X, Z), is_bigger(Z, Y).
?- is_bigger(elephant , dog). true.

% Selbstverständlich können nun auch Anfragen mit Variabeln über die transitive Hülle durchgeführt werden.

?- is_bigger(X, dog).
X = horse ;
X = elephant ; false.

% Es können auch verknüpfte Anfragen (UND) ausgeführt werden.

?- is_bigger(elephant , X), is_bigger(X, dog). X = horse ;
false.

% Eine is_smaller/2-Regel ist schnell implementiert.

is_smaller(X, Y) :- is_bigger(Y, X).
```



##Was sind die verschiedenen Typen von Termen in Prolog?

* Terme
  * Einfache Terme
    * Atomare Terme (Atome, Zahlen)
    * Variable
  * Zusammengesetzte Terme



## Begriffe in Bezug auf Prologs Syntax

* **Zahlen**: Gelten auch als atomare Terme: 123, 4657.8, -9
* **Atome**: Beginnen mit Kleinbuchstaben oder sind in einfachen Anführungszeichen eingeschlossen. Gelten auch als atomare Terme: `elephant`, `’Mein Text’` 
* **Zusammengesetzte Terme**: Bestehen aus dem Funktor und Argumenten. Der Funktor ist ein Atom (`is_bigger`) und die Argumente sind Terme: `is_bigger(horse, X)` 
* **Variablen**: Beginnen mit Grossbuchstaben oder einem Unterstrich: `X`, `Elephant`, `_elephant`
* **Anonyme Variable**: Die Variable `_` (Unterstrich) heisst anonyme Variable. Diese dient als Platzhalter, dessen Wert nicht interessiert. Jedes auftreten repräsentiert eine neue Variable.
* **Grundterme**: Terme ohne Variablen. Diese sind als sogenannte Fakten bekannt: `bigger(you, me)`, `write(’hello’)`
* **Prädikate**: Atome und zusammengesetzte Terme. Treten sie als Atome auf sind es Fakten (`bigger`) sonst sind es Regeln `is_bigger(X, Y) :- bigger(X, Y)`.
* **Stelligkeit**: Die Stelligkeit eines Prädikats zeigt auf wie viele Argumente das Prädikat entgegennimmt. Die Stelligkeit wird am Schluss des Prädikats angegeben: `is_bigger/2`
* **Anfragen**: sind Prädikate oder Sequenzen von Prädikaten gefolgt von einem Punkt. Der Punkt ver- anlasst Prolog zu antworten.
* **Klauseln**: sind Fakten und Regeln (zusammengesetzte Terme).
* **Prozedur**: Alle Klauseln zum gleichen Prädikat (d.h alle Relationen mit gleichem Name (Funktor) &
  Stelligkeit).
* **Prolog-Programm**: Liste aller Klauseln.
* **Fakten**: Typischerweise Grundterme.
* **Regeln**: Bestehen aus einem Kopf (head) und einem Hauptteil (body), welche durch `:-` getrennt sind. Der Kopf einer Regel ist wahr, wenn alle Ziele (**Prädikate**) im Hauptteil als wahr bewiesen werden. Ziele werden durch Komma getrennt, welches eine UND-Verknüpfung darstellt (**Konjunktion**).



## Was verwendet Prolog um Regeln auszuwerten?

* Hornklauseln
* Die Definition der Hornklausel ($p1 ∧ p2 ∧ ... ∧ pn ⇒ q$) kann auf die Prolog-Syntax `q :- p1, p2, ... pn`. übertragen werden.



## Was ist Matching

* Wenn Anfragen an das Prolog-System gestellt werden, führt Prolog eine Beweissuche mittels Back- tracking und Matching durch.
* Zwei Terme matchen, wenn sie identisch sind oder wenn sie durch ersetzen von Variabeln durch andere Terme identisch gemacht werden können. 
* Mittels dem Gleichheits- Prädikat `=/2` kann abgefragt werden, ob zwei Terme matchen.



## Was sind die 3 Matching Regeln?

1. Zwei atomare Terme matchen, wenn 

* Falls Term eine Variable ist, dann matchen beide Terme und die Variable wird mit Wert des zweiten Terms instanziiert.
* Zwei zusammengesetzte Terme matchen, wenn
  * gleicher Funktor, gleiche Stelligkeit (gleiche Anzahl Argumente) und
  * alle korrespondierende Argument matchen