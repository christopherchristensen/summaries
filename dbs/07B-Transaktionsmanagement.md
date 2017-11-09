# Transaktionsmanagement

**Transaktionskonzept**,

* Abbildung von Transaktionen
* Änderung von Systemzuständen
* Datenbank-Transaktion
* Konsistenzbedingungen

**Ziel des Transaktionsmanagements** ist Inkonsistenzen vermeiden, <br>

* Recovery (Fehler/Systemabstürze)
* Synchronisierung (Mehrbenutzerbetrieb)

## ACID

* **Atomicity**:<br>
Alle oder keine Teilaktionen werden durchgeführt
* **Conistency**:<br>
Einhaltung der Integritätsbedingungen
* **Isolation**:<br>
Gleichzeitig laufende Transaktionen sind isoliert. Wenn mehrere Benutzer gleichzeitig Transaktionen durchführen werden diese nicht voneinander beeinflusst (Locking)
* **Durability**:<br>
Erhaltung der Systemzustände nach Abschluss der Transaktion  (Logging)

## Synchronisierung

> Ein Schedule von gleichzeitig ablaufenden Transaktionen heisst korrekt synchronisiert, wenn es eine serielle Ausführung gibt, die denselben Datenbankzustand erzeugt $\to$ Serialisierbarkeit

* **seriell**: schlechtere CPU-Auslastung
* **parallel**: besser CPU-Auslastung $\to$ mögliche Seiteneffekte bei paralleler Ausführung

Beim Scheduling von parallelen Transaktionen kann es zu Verklemmungen/Deadlocks kommen.

> Ziel von Synchronisierung: Konzistenz im Mehrbenutzerbetrieb <br>
> Mögliche Methode: Locking

## Optimistische Synchronisationsverfahren

* Two-Phase-Locking-Protocol garantiert Serialisierbarkeit $\to$ pessimistisches Verfahren
* Optimistische Synchronisierung
	* keine Sperren $\to$ man nimmt an Konflikte treten selten auf
	* Vor Commit wird nach Konflikten geprüft

## Recovery

* Wiederherstellen (nach Fehlerfall)
* Sicherstellung der Dauerhaftigkeit

> Deswegen: Es braucht eine Form von Logging auf RAM, Disk oder TAPE.