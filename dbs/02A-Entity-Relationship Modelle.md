# Entity-Relationship Modelle

Müssen den Sachverhalt im echten Leben irgendwie modellieren können.

Graphdatenbanken besteht nur aus Knoten und Kanten.

Relationale Datenbanken sind deshalb schwieriger verständlich (sehr strikt). Man muss einiges an Wissen haben, damit man sie richtig verwenden kann.

## Entitäten
Generische Werte verwenden:
(Person) --> [mag] --> (Games)

[mag] ist hier die Beziehung

Falsche wäre:
(Alex) --> [mag] --> (Games)
Problem: Wenn es jemand gibt die Sandra heisst, die Games mag, dann geht die Entität nicht auf.

Beispiele zu Entitäten, etc.

**Entität**: Mitarbeiter Meier, wohnhaft in der Lindenstrasse in Liestal

**Entitätsmenge**: Menger aller Mitarbeiter mit Merkmalen Name, Strasse und Ort

**Identifikationsschlüssel**: Mitarbeiternummer als künstlicher Schlüssel

Zu viele Attribute bedeutet eine grössere Datenbank und erzeugt Probleme später mit den Queries.

Man braucht Schlüssel um Entitäten mit selben Bezeichnungen voneinander unterscheiden zu können (z.B. 3 Personen heissen Alex)

**Künstlicher Schlüssel**: Erfundener Schlüssel

**Natürlicher Schlüssel**: Aus relevanten Werten erstellt.

Die Entitäten müssen im Relationship-Modell nicht in beide Richtungen lesbar sein (Mitarbeiter gehört zu Projekt, Projekt gehört zu Mitarbeiter).

Ziel von Identifikationsschlüssel: Eindeutigkeit

Je kleiner der Identifikationsschlüssel ist, desto weniger Rechenleistung braucht die Suche

## Generalisation

Das Verallgemeinern von Entitäten und somit auch von Entitätsmengen.

**Spezialisierung**: Die in einer Generalisationshierarchie abhängigen Entitäsmengen oder Subentitätsmengen

Bei der Generalisation von Entitätsmengen treten folgende Fälle auf:

* Überlappende Subentitätsmengen
* Überlappend-vollständige Subentitätsmengen
* Disjunkte Subentitätsmengen
* Disjunkt-vollständige Subentitätsmengen

**Aggregation**: Zusammenfügen von Entitäten zu einem übergeordneten Ganzen (netzwerkartige und hierarchische Strukturen)

$\to$ netzwerkartig: Facebook, ich kenne jemand der jemand kennt der jemand kennt

$\to$ hierarchische Strukturen
