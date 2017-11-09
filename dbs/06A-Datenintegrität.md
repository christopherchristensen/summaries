# Datenintegrität

Definition Datenintegrität,

* Daten sind **integer**, wenn sie korrekt sind
* Um Integrität zu prüfen, gibt es Bedingungen
* syntaktische Integritätsbedingung
* semantische Integritätsbedingung

**Semantische Integritätsbedingung**<br>
Regeln, die definieren, wann die Daten korrekt sind,

* **statische** Integritätsbedingungen müssen von jedem Zustand der DB erfüllt sein:<br>
`not null`, `unique`, `check`, `primary key`, `references`
* **dynamische** Integritätsbedingungen müssen von Zustandsänderungen erfüllt werden:<br>
`cascade`, `set null`, `restrict`, `create trigger`

**Bedingungen**

* `not null`: Spalte ist nicht optional (muss Wert enthalten)
* `unique`: Wert/Wertkombination nur einmal in Tabelle vorhanden (Eindeutigkeit)

**Referenzielle Integrität**<br>
Jeder Wert eines Fremdschlüssels kommt als Wert beim zugehörigen Primärschlüssel vor. Bei der referentiellen Integrität können Datensätze die einen Fremdschlüssel aufweisen nur dann gespeichert werden, wenn der Wert des Fremdschlüssels einmalig in der referenzierten Tabelle existiert. Im Falle, dass ein referenzierter Wert nicht vorhanden ist, kann der Datensatz nicht gespeichert werden.

**Was passiert bei Änderung der referenzierten Primärschlüssel mit dem referenzierenden Fremdschlüssel?**<br>

3 Möglichkeiten:

1. Default: Verhindern
2. Kaskadieren (Verkettung)
3. Nullsetzen

**Trigger**
Ein Trigger ist eine benutzerdefinierte Prozedur, die automatisch bei Erfüllung einer bestimmten Bedingung vom DBMS gestartet wird. Sie kann nicht nur Überprüfungs-, sondern auch Berechnungsfunktion übernehmen (dynamische Integritätsbedingung)


