# SQL Injections



## SQL-Injection-Angriff

* Besteht aus Einfügen / Injizieren einer SQL-Abfrage (Query) über die Eingabedaten vom Client zur Anwendung, um 
  * sensible Daten aus der DB zu lesen
  * Daten in der DB zu modifizieren (CRUD)
  * Administrationsoperationen auf der DB auszuführen
  * Inhalt einer bestimmten Datei (auf DBMS) wiederherzustellen
  * Befehle an Betriebssystem auszugeben



## Anwendungen von SQL Injections

* Anmeldeverfahren eines Chats erhacken, um Zugang zu schaffen



## Wann werden SQL Injections ermöglicht?

* Wenn Entwickler dynamische DB-Abfragen erstellen,
  * die benutzerdefinierte Eingaben erhalten
  * und diese nicht filtern und maskieren (gegen böse Zeichen)
* z.B. bei Loginverfahren



## Beispiel, um an Logindaten zu gelangen

* Folgender Query existiert auf Server

  ```java
  String accountBalanceQuery =
  "SELECT accountNumber, balance FROM accounts WHERE account_owner_id = "
  + request.getParameter("user_id");
  
  try {
  
      Statement statement = connection.createStatement();
      ResultSet rs = statement.executeQuery(accountBalanceQuery);
  
      while(rs.next()) {
  
          page.addTableRow(
            rs.getInt("accountNumber"), 
            rs.getFloat("balance")
          );
  
      }
  
  } catch(SQLException e) { ... }
  ```

* Beabsichtigter Query

  ```mysql
  SELECT accountNumber, balance 
  FROM accounts 
  WHERE account_owner_id = 984
  ```

* Mit folgendem Query wird der Query immer `true` 

* ```mysql
  SELECT accountNumber, balance 
  FROM accounts 
  WHERE account_owner_id = 0 
  OR [true statement]
  ```

* Somit gibt die Abfrage alle Kontonummern und Salden zurück von jedem Benutzer

* Wenn man für Passwort `'` eingibt kann man überprüfen, ob ein SQL-Syntax-Error geworfen wird oder nicht. Wenn nicht dann wird nicht gesäubert!



## Massnahmen gegen SQL-Injections

* Prepared Statements
  * Sorgfältiges Überprüfen und Filtern von Eingaben und Parametern
* Stored Procedures
* White List Input Validation
* Web Application Firewall (WAF)