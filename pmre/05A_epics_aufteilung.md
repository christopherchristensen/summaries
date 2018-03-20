# Aufgabe Epics Aufteilen

## Ausgangslage / Fragestellung

Es soll ein Dokumentenmanagementsystem (DMS) entwickelt werden. Bisher wurde ein rudimentärer Anforderungskatalog entwickelt.Splitten Sie diese (zum Teil noch rudimentären) Epics auf!1. Als Benutzerdes DMS will ich neue Dokumente erfassen und für einem von mir definierten Benutzerkreis zur Bearbeitung freigeben.2. Als berechtigter Benutzer will ich Dokumente bearbeiten können. Wenn ich als berechtigter Benutzer ein Dokument ändere soll eine neue Version erstellt werden.3. Als berechtigter Benutzer will ich Dokumente mit Hilfe einer Suchfunktion schnell finden können. Dazu sollen die Dokumente indexiert abgelegt werden.

## Unsere Musterlösung

1. Epic
	1. Operation (beide Funktionen)
	2. Simple/Complex (Benutzerfreigabe Einschränken)
2. Epic
	1. Operation (bearbeiten, neue Version)
	2. Business Rule (Authentifizierung)
3. Epic
	1. Operation (Suche, Indexierung)
	2. Defer Performance (schnelle Suche)