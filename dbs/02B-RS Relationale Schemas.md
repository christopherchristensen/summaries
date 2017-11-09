# RS Relationale Schemas
## Tabellendefinition
* Tabellenname: eindeutig
* Merkmalsname: eindeutig und bezeichnet bestimmte Spalte mit gewünschten Eigenschaft
* Keine Spaltenordnung: Anzahl der Merkmale beliebig, Ordnung bedeutungslos
* Keine Zeilenordnung: Anzahl Tupel beliebig, Ordnung bedeutungslos
* Identifikationsschlüssel: identifiziert Tupel eindeutig

## Identifikationsschlüssel
* Eindeutigkeit
* Minimalität

## Relationenmodell
Relationale Datenbanken speichern Daten in Tabellen mit Zeilen und Spalten. Tabellen werden mathematisch als Relationen beschrieben.

Modell drückt Daten wie Beziehungen zwischen Daten tabellarisch aus.

## Redundanz und Anomalien
Redundanz kann zu *Anomalien* führen. Redundanzbeispiel: Zweimal den Namen "Meier" in einer Tabelle.

Ziel: *Analyse von Abhängigkeiten zur Vermeidung von Redundanz* (Normalformen)

Mutationsanomalien:

* Einfügeanomalie: Einfügen von Daten nicht möglich
* Löschanomalie: Ungewolltes Löschen
* Änderungsanomalie: Mehrfache Änderungen notwendig bei Änderung eines Objekts

### 1. Normalform (1NF)
Es dürfen **nur einfache Werte** vorliegen. Zusammengesetzte Werte, Mengen, Aufzählungen, Wiederholungsgruppen etc. sind verboten 

**Prüfung**: Falls die Tabelle nicht in 3. Normalform ist, wandle sie in 3. Normalform (mit Begründung weshalb nicht im 3NF)

**Achtung**: Unter der 1NF gibt es die Kategorie nicht-normalisierte Tabellen (falls Aufzählen beinhaltet etc.)

### 2. Normalform
Falls die Tabelle in 1NF ist und jedes Nichtschlüsselmerkmal **voll funktional abhängig von Schlüssel** ist.

### 3. Normalform
Falls die Tabelle in 2NF ist und **kein** Nichtschlüsselmerkmal von irgendeinem **Schlüssel** **transitiv abhängig** ist.

![transitiv abhängig](/Users/Christopher/MacDown/Images/DBS/image01.png)

### Primär-/Fremdschlüssel
Einer der Kandidatenschlüssel wird als Hauptschlüssel definiert undwird als **Primärschlüssel** bezeichnet.

Eine Tabelle kann Zeilen in einer anderen Tabelle referenzieren $\to$ **Fremdschlüssel**.

Bei **komplex-komplexen** Beziehungsmengen:
![komplex-komplex](/Users/Christopher/MacDown/Images/DBS/image02.png)

Bei **einfach-komplexen** Beziehungsmengen:
![einfach-komplex](/Users/Christopher/MacDown/Images/DBS/image03.png)

Bei **einfach-einfachen** Beziehungsmengen:
![eifach-einfach](/Users/Christopher/MacDown/Images/DBS/image04.png)

Generalisation in Tabellenform:
![eifach-einfach](/Users/Christopher/MacDown/Images/DBS/image05.png)

Netzwerkartige Firmenstruktur in Tabellenform:
![eifach-einfach](/Users/Christopher/MacDown/Images/DBS/image06.png)

Hierarchische Artikelstruktur in Tabellenform:
![eifach-einfach](/Users/Christopher/MacDown/Images/DBS/image07.png)



Diese Abbildung hat einen Fehler (schwächeres Glied), ich weiss nicht wo...sorry.

