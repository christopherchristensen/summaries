# Semesterprojekt

## Recherche

### Vorhandene Sharing-Systeme

* WeeShare: https://www.weeshare.com/?gclid=EAIaIQobChMI-tiqpu3G2QIVTLftCh0cngepEAAYAyAAEgJYrvD_BwE
* Sharoo: https://www.sharoo.com/
* Catch a car: https://www.catch-a-car.ch/en/home/
* Vulog: http://www.vulog.com/technology/#front-end
* DriveMyCar: www.drivemycar.com.au

### Carpooling-Systeme

* BlaBlaCar: https://www.blablacar.co.uk/ride-sharing/basel/

### Andere Sharing-Systeme

* GanzSharing: https://www.ganzsharing.ch/ganz-sharing
* Airbnb: https://www.airbnb.com/

## Definition Ausdrücke

* Car-Sharing: Privatfahrzeuge ausleihen oder verleihen
* Car-Pooling: Firmenfahrzeuge ausleihen oder verleihen
* Car Borrower: Person, welche Autos **von** anderen ausleiht
* Car Lender: Person, welche sein Auto **an** andere ausleiht

## Erste Ideen für Features

### Car Borrower
* Kann Preise bestimmen
* Bekommt Preisvorschläge
* Bekommt Punkte (Öko, etc.)
* Übersicht von Ausleihstatistiken
* Will Sicherheit vor Schaden an Fahrzeug
* Will im Falle von verunreinigungen eine Reinigung erhalten

### Car Lender
* Man erkennt beim Start direkt die Location und gibt nur noch an wohin man gehen will (Current Location $\to$ _________ )
* Will Sicherheit haben, dass er das Auto erhält
* Übersicht von Ausgaben

### Sicht Beide
* Man kann Ratings vergeben
* Kommunikation mit der Gegenseite möglich

## UI Wünsche

### Erster Seitenbesuch

* Einfache und übersichtliche Benutzeroberfläche
* Navigation ist intuitiv (Ich finde schnell was ich möchte, der Nutzer wird geführt)
* Funktionalität ist intuitiv
* Wenig, aber nutzbare/relevante Informationen darstellen (weniger ist mehr!)
* Klare Unterteilung der UI gemäss Nutzer (Borrower / Lender)
* Responsive
* Als eingeschränkter Nutzer (Sehbehinderung, etc.) schnell zum Ziel kommen
* Attraktive/Sinnvolle Farbenkombinationen
* Moderne Design-Features
* Gute Performance beim Ausführen von Funktionen (Wartezeit gering)
* "Poweruser-Shortcuts"
* Kann Inhalt betrachten, ohne Registrierung (gibt es Angebote für Autos, die mich interessieren)
* Finde aber Registrierung schnell

### Borrower

#### Neuer Car Borrower (Registrierung)

* Navigation zur Registrierung
* Einfache Registrierung
* Kurzer Registrierungsprozess (Nur Daten, die absolut notwendig sind)
* Geführte Navigation (keine Unklarheiten, Entscheidungswege)
* Bei Unklarheiten $\to$ Forum? (Übersichtliche, relevante FAQ)

#### Registrierter Car Borrower

##### Autosuche

* Ich finde **schnell** und **ohne Aufwand** ein Auto zum gewünschten Zeitpunkt, Preis und am richtigen Ort
* Gute Autovorschläge
* Filter für Custom-Wünsche (manuel / automatisch, teuer / billig, etc.)
* Einfaches Scheduling (Kalender)

##### Abschluss

* Einfache Buchung eines Autos
* Klare Richtlinien
* Kommunikation mit Lender
* Quittung

##### Generelle Funktionen

* Update über Autozustand hinzufügen (Meilenstand, Gute Qualität, Innenaustattung)
* Beschwerdeplattform
* Statistiken über Buchungen
* Profil mit Bewertungen (+ Anfechtungsmöglichkeiten)

### Lender

#### Neuer Car Lender

* Soll sicher wirken (Versicherung)
* Soll sich und Auto einfach registrieren können
* Richtlinien klar und übersichtlich
* Möglichkeit Konto ohne Registrierung
* Bilderupload einfach
* Autobeschreib hinzufügen einfach
* Hilfe bei Kategorisierung (Auswahl bei Modell, etc.)

#### Registrierter Car Lender

##### Generelle Funktionen
* Beschwerdeplattform
* Statistiken über Auto, etc.
* Einfaches Scheduling (Kalender)
* Profil mit Bewertungen (+ Anfechtungsmöglichkeiten)

##### Abschluss

* (Scheduling)
* Bestrafung des Borrowers bei Überziehung
* Quittung

## Mentales Modell

**Was sind Erwartungen an das System?**

* Wenn ich auf ein Auto clicke, bekomme ich zuerst Infos über das Auto, bevor ich es mieten kann (vor Bestellung, Frage, ob ich sicher bin)
* Meldung für erfolgreiche Buchung
* Meldung bei Stornierungen
* Ladebalken, wenn ich warten muss
* Preis inklusive Mwst. angeben
* Antwortzeiten werden mitgeteilt
* Klare Infos über Verfügbarkeit der Autos

**Welche Erfahrungen haben Sie mit dem System oder mit ähnlichen?**

* Airbnb ermöglicht das Buchen von Appartment/Wohnungen mit demselben Prinzip, wie unser CarPooling-System
* Realität / Bilder sind nicht immer ein und dasselbe
* Streitigkeiten zwischen Borrower und Lender
* (Airbnb) Schlüsselübergabestelle nicht immer klar
* Verspätungen einer Partie (Uber)
* Effizientes, einfaches System (Uber)
* Vertrauen muss bei vielen solchen Systemen vorhanden sein

**Welche Funktionen muss das System aus ihrer Sicht unbedingt haben?**

* Begeisterungsfunktionen, die intrinsisches Handeln fördern (Erlebnis)
* Extrinsisches Handeln fördern durch Belohnung an Stammkunden
* Bei Suchfunktion verschiedene Alternativen
* Bei Suche schon adäquate Anzahl Attribute anzeigen (im Gleichgewicht mit Heuristiken)

**Welche Ansprüche haben sie an die Gestaltung des Systems?**

* Die Cognitive Load reduzieren durch Heuristiken (nur die wichtigsten, relevanten Infos anzeigen)
* UserInterface ist wirkt beruhigend (Farben), professionell und sicher (Gestaltgesetze)
* Das System kann sowohl via App als auch Website benutzt werden

**Was muss beim System erfüllt sein, damit sie damit zufrieden sind/wären?**

* Borrower und Lender vertrauen unserem App und hinterfragen Sicherheit und Zuverlässigkeit nicht
* Flow muss angenehm sein
* Buchung und Vermietung des Autos geschieht intuitiv in einem Process
* keine redundanten Dateneingaben bei Funktionen, wie Buchung, Vermietung, Erstellen von Angeboten, Erstellen von Profilen
* Ein gutes Gleichgewicht zwischen UserControl und Lenkung (vorallem beim Buchungsabschluss)