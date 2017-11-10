# Anfrageoptimierung
> Bezieht sich alles auf SQL-Datenbanken

**Wo sehen sie die grösste Quelle von Leistungsengpässen bei Datenbankanfragen?**

* Speicher-Typ
* Menge
* Fragmentierung (Joins)
* Rechenintensive Operationen
* Fehlende Indexe 
* Query nicht optimiert

**Wie sieht die Speicherhierarchie aus?**

* 1-10ns Register* 10-100ns Cache* 100-1000ns Hauptspeicher* 10 ms Plattenspeicher (SSD: 1ms)* 10 sec Archivspeicher

**Paging**: Methode der Speicherverwaltung per Seitenadressierung durch Betriebssysteme. Beim Paging wird der virtuelle Adressraum in gleich große Stücke unterteilt, die man als Seiten (engl. pages) bezeichnet. Die Seiten werden in der sogenannten Seitentabelle (engl. page table) verwaltet, die Informationen darüber enthält, wo für eine (virtuelle) Seite der entsprechende (reale) Seitenrahmen im Arbeitsspeicher tatsächlich zu finden ist, sowie meistens Zusatzinformationen zum Beispiel zu Gültigkeit, Schreibrechten oder ob (sowie evtl. wohin) die Seite ausgelagert wurde.

> sehr langsam zu lesen

**Caching**: Wenn ein BS Ressourcen (Funktionsbibliotheken, Schriftarten, etc.) vorerst im Arbeitsspeicher belässt, obwohl sie nach Ende ihrer Benutzung nicht mehr gebraucht werden. Solange kein Speichermangel herrscht, können sie im Arbeitsspeicher verbleiben, um dann ohne Nachladen von der Festplatte sofort zur Verfügung zu stehen, wenn sie wieder gebraucht werden. Wenn allerdings die Speicherverwaltung des Betriebssystems einen Speichermangel feststellt, werden diese Ressourcen als erste gelöscht.

> schnell zu lesen, hat aber nur wenig Platz


**Wie wird eine deklarative Anfrage ausgeführt?** 
<br> // TODO

## Anfrage logisch optimieren
 **Grundsätze**:
 
* Mehrere Selektionen auf gleiche Tabelle vereinigen* Zwischenresultate klein halten (Selektion, Projektion)	* Nicht verwendete Zeilen/Spalten aus Anfrage entfernen (so weit unten im Baum wie möglich) $\to$ Selektionen früh ausführen
* Projektionen so früh wie möglich ausführen.* Verbundsoperatoren (join) im Wurzelknoten des Anfragebaums verwenden.

**Wie programmieren Sie einen “Join” zwischen zwei HashMaps in Java?**

* Quadratischer Aufwand: Mit einem doppelten Loop und der Komplexität $O(n^2)$. Alle Tupel aus R1 werden mit allen Tupeln aus R2 auf Join-Kompatibilität geprüft (Nested Join)
* Linearer Aufwand nach Sortierung: Tupel werden in Sortierreihenfolge des Joinattributs Xdurchlaufen

**Was hat ein Telefonbuch und eine Datenbank gemeinsam?**

* Zugriffspfade
* Datensätze
* Telefonbuch ist eine DB (ohne DBMS)

**Baumstrukturen und binäre Bäume (B-Baum)**

* Eine Baumstruktur ermöglicht ein schnelles Finden vonDatensätzen
* B-Bäume = ausbalancierte Bäume (Breite n)
	* alle Pfade von Wurzel zu Blatt gleich lang
	* jeder Knoten hat mindestens n
	* höchstens 2n Teilbäume

**Bulk Load vs Indexe**

* Indexe sind optimiert für Lesen $\to$ Schreibaufwand erhöht (Index-Aktualisierung)
* Deswegen bei grossen Datenmengen (Bulk Load):
	* Indexe löschen (oder ausschalten)
	* Nach laden neu erstellen

**Wie sieht die nicht-algebraische Optimierung aus?**

In SQL:

```MySQL
explainselect * from moreStudenten sjoin morehoeren h on (s.MatrNr = h.MatrNr)join moreVorlesungen v on (h.VorlNr = v.VorlNr)join moreProfessoren p on (p.PersNr = v.gelesenVon) where s.Name = 'Studentin_12401';

```