# Datenbankprogrammierung

Wann braucht man Datenbankprogrammierung:

* einfacher
* mehr mögliche Abfragen
* Schnittstellen
* Prüfungen
* Fallunterscheidungen:</br>Ist Benutzer berechtigt Daten einzusehen
* Logik

$\to$ Praktisch alle Apps sind heute mit Datenbankprogrammierung aufgesetzt

DB-Anfragen sind satzorientiert und nicht mengenorientiert.

**Cursor** = Zeiger, der in einer vom Datenbanksystem vorgegebenen Reihenfolge eine Menge von Tupeln durchlaufen kann $\to$ tabellenzeilenweises Vorgehen

> **Stored Procedures** = Programme, welche direkt mit Datenbankserver in einer an SQL angelehnten, um prozedurale Konstrukte erweiterten Sprache definiert werden

> **Stored Functions** = gespeicherte Prozeduren

> Unterschied zwischen Stored Procedures (SP) und Stored Functions (SF): 

> * SP haben keinen Rückgabewert 
> * SF haben einen Rückgabewert

**Java Database Connectivity (JDBC)**: Kann mit meinem Java-Programm verschiedene Datenbanken mit JDBC-Standard ansprechen

