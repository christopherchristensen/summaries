# Datensicherheit

**Kategorien von Schutzmechanismen**:

* Identifikation/Authentisierung (Passwort)
* Autorisierung/Zugriffskontrolle (Rechte)
* Auditing

**Role-based Access Control (RBAC)**:

* **Data Object Types**<br>
Arten von Datenobjekten (HW-Instanz, DB, Schema, etc.)
* **Privileges**<br>
Recht auf bestimmte Operation (SELECT, INSERT, etc.)
* **Roles**<br>
Erlauben authentifiziert/authorisierte Änderungen auf DB-Server
* **Users**<br>
Rolle, welche mit Server verbinden darf (CONNECT-Privileg)
* **Groups**<br>
Rolle, welche Privilegien von anderen Rollen erben kann (typisch. ohne LOGIN)

**Autorisierung/Zugriffskontrolle in SQL**:

```
grant select
	on Tabelle
	to reader;
```
```
grant update (MatrNr, VorlNr, PersNr)
	on prüfen
	to eickler;
```
**Sichten**:<br>
Dienen als Schutz für Spalten und Zeilen (nur sichtbar für jene denen die Sicht granted wurde) oder als Schutz von Individualdaten durch Aggregation.

Schutz für Spalten und Zeilen,

```
create view ErstSemestler as
	Select MatrNr, Name
	from Studenten
	where Semester = 1;
grant select
	on ErstSemestler
	to tutor;
```
Schutz von Individualdaten durch Aggregation,

```
create view VorlesungsHärte (VorlNr, Härte) as
	select VorlNr, avg(Note)
	from prüfen
	group by VorlNr;
```
Entzug von Rechten,

```
revoke update (MatrNr, VorlNr, PersNr)
	on prüfen
	from eickler cascade;
```

**Mögliche Privilegien**:

* SELECT
* INSERT
* UPDATE
* DELETE
* READ
* REFERENCES, etc.

**MD5 Authentication** verhindert Snooping,<br>
`md5(md5(password+username)+salt)`

**SSL** verhindert ebenfalls Snooping

> Um gegen Spoofing zu kämpfen wird geraten dem Server die Wahl des Passwortes zu überlassen.


**SQL-Injection Attacken**<br>
Hinter den meisten Web-Applikationen verbergen sich DBS. Aus den Eingabe-Parametern werden SQL-Anfragen generiert. Man darf diesen Eingabe-Parametern NIEMALS trauen, da sie ausführbaren SQL-Code enthalten könnten.


**Wie kann man sich vor SQL-Injection schützen?**

* Prepared Statements (Client)
* Stored Procedures (DB-Server)

