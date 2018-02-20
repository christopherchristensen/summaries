# Dokument-Datenbanken

## Datenmanagement

**Dokument Stores**:

* verwalten einzelne Datensätze in "Dokumenten" (JSON)
* Hohe Flexibilität der Speicherung unterschiedlicher Strukturen
* Alternative zu relationalen Datenbanken in Anwendungsfällen mit heterogenen Datensätzen
* MongoDB/CouchDB

**Dokument**:

* Strukturierte Sammlung mehrerer Schlüssel-Wert-Paare (JSON/YAML/XML)

> JSON $\neq$ Markupsprache

**Datenbankmodell**:

TODO

## Datenmodellierung

Abbildung von Entitätsmengen (EM):

* EM können durch eine Collection abgebildet werden
* Innerhalb Collection werden einzelne Realweltobjekte durch ein Dokument repräsentiert

**Beziehungsmengen**:

* Keine Auflösung von Fremdschlüsselbeziehung
* Keine Sicherstellung der Integrität von Referenzen
*  Dokument-DBs stellen die komplexen Datentypen Array und Object bereit und eröffnen dadurch drei Mog̈ lichkeiten in der Abbildung von Beziehungen:


	Speicherung der ID‘s der referenzierten Datensätze 
	2. **Denormalisierung**<br>
	Speicherung einer Kopie des referenzierten Datensatzes
	Speicherung des referenzierten Datensatzes als Unterteile
	
> Ich als Entwickler entscheide, ob ich Referenzierung, Denormalisierung oder Aggregation verwende
	
<img src="img/img03.png" width="400">

> Ungelöstes Problem: Wie modelliert man MongoDB? <br>
> Viele zeichnen einfach Beispiel-JSON auf.

## Datenbanksprache

Dokument-Datenbanken sind relational unvollständig

<img src="img/img03.png" width="400">

**Anfrageverarbeitung MongoDB**:

`db.collectionName.find({<Selektion>, {<Projektion>})`

Collection: `collectionName`<br>
Operation: `find()` <br>
Parameter: `<Selektion>`, `<Projektion>`

// TODO


## Konsistenzsicherung

Bei Dokumentdatenbanken:

* kein festes Datenschema
* Struktur gespeicherter Dokument nicht zuvor definiert
* einzelne Dokumente unterscheiden sich innerhalb einer Collection nicht vollständig voneinander
* Definition/Prüfung der Datenintegrität auf Applikationsebene
* Ausnahme: CouchDB (optional Integrität durch Träger, die bei jeder Schreiboperation auf entsprechenden Dokument ausgeführt wird)

**Transaktionsmanagement**:

MongoDB unterstützt keine Transaktionen!

• Operationen müssen einzeln ausgeführt werden


## Systemarchitektur

// TODO Indizes zur Anfrageoptimierung

**Replica Sets**: 1..n Knoten, welche zu verarbeitende Dokumente speichern. (Prio: hohe Verfügbarkeit)

**Router**: "Mongos", bilden Schnittstelle für client-Anfragen.

**Config Server**: // TODO


// TODO

