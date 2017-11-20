# Message Passing

**Message passing**: Ein Beispiel der Kommunikation bei der Nachrichten vom Sender zu einem oder mehreren Empfängern gesendet werden $\to$ invocation, signals, data packets

Eigenschaften der Versandsarten:

* verlässliche Übertragung
* garantierte Übertragung
* unicast, multi-/broadcast, client-server, all-to-all
* synchron, asynchron

--

**Persistente Kommunikation**: <br>
Nachricht solange gespeichert bis Empfänger bereit (z.B. E-Mail). 

$\to$ asynchron oder synchron

**Transiente Kommunikation**: <br>
Nachricht gespeichert, solange sendende und empfangene Applikation ausgeführt werden (z.B. Router, Socket). 

$\to$ asynchron oder synchron

**Asynchrone Kommunikation**: <br>
Sender wird fortgesetzt nach dem er seine Nachricht zur Übertragung weitergegeben hat (z.B. E-Mail, Diskussionsforum).

**Synchrone Kommunikation**: <br>
Sender wird blockiert bis Nachricht an Empfänger übermittelt wurde oder Puffer des Empfängers die Nachricht übernommen hat (z.B. Telefonie, Instant Messaging, Internet-Videokonferenz).

**Weitere transiente Kommunikationsformen**: <br> Auslieferungsbasierte und antwortbasierte transiente synchrone Kommunikation.

--

**Message Passing Interface (MPI)**: Standard, der Nachrichtenaustausch bei parallelen Berechnungen auf verteilten Computersystemen beschreibt $\to$ kein konkretes Protokoll

## Nachrichtenverarbeitung

Nachricht enthält:

* **ID**, <br>
identifiziert Nachricht (z.B. GET, POST) $\to$ nicht immer benötigt
* **Argumente**, <br>
können Datentypen sein (Int, String, etc.) $\to$ Vorteil ist Argumente können direkt über `DataInputStream` und `DataOutputStream`gelesen und geschrieben werden $\to$ können zusätzliche Infos enthalten

--

Prinzipien der Nachrichtenverarbeitung:

* Trennung zw. Kommunikations- und Applikationsdetail
* Verknüpfung von Nachrichten mit Methoden der Applikationsobjekte

--

**Fabrikmethode**, <br>

> **Zweck**: Erzeugung von Objekten an Unterklasse delegieren <br>
> **Nachrichtenverarbeitung mit Fabrikmethode**: Basic Message definiert Protokoll (Klassenstruktur) und sorgt für Senden und Empfangen. Basic Message Handler erzeugt Nachricht $\to$ Alle Netzwerkteilnehmer benötigen diese Struktur

**Basic Message**,

* besitzt Methoden: `messageId`, `argList`, `readArgs`, `writeArgs`
* hat Getter/Setter für ID und Argumente
* beinhaltet abstrakte Methode `operate`

**Basic Message Handler**,

* besitzt Methoden: `sendMsg`, `readMsg`, `buildMessage`
* sendet/empfängt Nachrichten an/von Netzteilnehmern
* stellt das globale Message-Handler Objekt `current`zur Verfügung

**Message**,

* besitzt Methoden: `messageId`, `argList`, `readArgs`, `writeArgs`
* hat Getter/Setter für ID und Argumente
* beinhaltet abstrakte Methode `operate`, `handles` und `newCopy`


## Protokolle

**Fixe Protokolle**: <br>
Menge der möglichen Kennung (IDs), die möglichen Argument (Anzahl + Typ) **vor** einer Kommunikationssitzung bekannt $\to$ keine Änderungen während Kommunikation

**Adaptive Protokolle**: <br>
Nachrichten können während Laufzeit ändern.

* Änderung Länge der Argumentliste
* Änderung der Argumenttypen
* Änderung des Nachrichtentyps

$\to$ häufiger als fixe Protokolle

## Prototyp

Durch `Prototype`werden eine Menge von Objekten zur Verfügung gestellt, die durch Aufruf von `clone` wieder zur Objekterzeugung herangezogen werden können.

* Message definiert das Protokoll
* Message Handler erzeugt die Nachricht anhand einer Liste der Nachrichtentypen

 

