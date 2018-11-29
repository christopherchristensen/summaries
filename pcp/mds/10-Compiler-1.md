# Compiler 1



## Was ist ein Compiler?

* Übersetzerprogramm, das
  * ein Programm in einer Quellsprache liest und
  * in ein äquivalentes Programm einer Zielsprache übersetzt

* Wichtigste Eigenschaft: den Inhalt, Syntax und Semantik, beider Sprachen nicht zu verfälschen
* Eine Teilaufgabe des Compilers: Fehlererkennung und Fehlermeldungen an den Benutzer
  * Syntaktische Fehler
  * Semantische Fehler, z.B. nicht deklarierte Variable in Ausdruck



## Was sind die Phasen der Kompilierung

* Zweiteilung der Kompilierung: Analyse und Synthese
* FrontEnd:
  * TODO
* BackEnd:
  * // TODO



## Was passiert in der Analysephase eines Kompilers?

* Lexikalische Analyse (Scanner)
  * Identifikation von Operatoren, Symbolen, Schlüsselwörtern usw.
* Syntaxanalyse
  * Strukturanalyse (Parser)
    * Analyse des hierarchischen Programmaufbaus, z.B. Erkennung von Variablen-/Funktions-/Klassen-Definitionen, arithmetischen Ausdrücken, Anweisungen usw.
* Semantische Analyse
  * Typprüfung, Berechnung von Typkonversionen u.a.
* Aus den Analysen resultieren
  * Symboltabellen: zu jedem Bezeichner (symbolischer Name für
    Variable, Funktion o.a.) wird die vorhandene Information abgelegt
  * Abstrakter Syntaxbaum: Repräsentation hierarchischer Strukturen, enthält nur Informationen, welche für die Weiterverarbeitung nötig sind



## Was geschieht in der lexikalischen Analyse?

> Scanner

* Scanner zerlegt Quellcode in seine Bestandteile
* Erzeugt daraus Tokens
  * Bezeichner, Symbol-Zuweisung, Konstante
* Kommentare, irrelevante Zeichen entfernen



## Was ist ein Token?

- kleinste sinngebende Einheit einer Programmiersprache
- folgen den Grammatikregeln



## Was geschieht in der Syntaxanalyse?

> Parser

* Grammatikregeln (Beispiel)
  * Jeder Bezeichner ist ein Ausdruck
  * Jede Zahl ist ein Ausdruck
  * Angenommen ex1 und ex2 sind Ausdrücke, dann sind auch ex1 ∗ ex2 und ex1 - ex2 Ausdrücke.
  * Ein Bezeichner := Ausdruck ist eine Anweisung (hier Zuweisung)
* Erzeugung einer Zwischendarstellung: Syntaxbaum, Abstrakter Syntaxbaum (AST)



## Was geschieht in der semantischen Analyse?

* Überprüfung auf semantische Fehler
  * Auf Namen bezogene Überprüfung (Namenskonventionen)
  * Typüberprüfungen (z.B. Zuweisungen, Parameterübergaben)
  * Identifizierung der Operatoren und Operanden (korrekter Operator für den entsprechenden Typen)
  * Überprüfungen der Kontrollflusses (z.B. erreichbarer Code)
  * Überprüfung auf Eindeutigkeit (z.B. Lexikalisches Scoping, mehrfach Definitionen)

* Notwendig für Code-Generierung, 
  z.B. Type-Casting: Konvertierung von `int` zu `real`



## Was sind mögliche semantische Fehler im Code?

* Array-Zugriff auf ein nicht Array
* Einem integer wird ein `char` zugewiesen
* Variablenname «bsp» doppelt definiert
* Funktion «max» wurde mehrfach definiert
* Die Funktion «max» wurde ohne Parameter aufgerufen



## Was geschieht in der Synthesephase?

* Aus dem Syntaxbaum wird maschinenunabhängiger Zwischencode erzeugt
  * Der Zwischencode ist ein Programm für eine besonders einfach strukturierte virtuelle Maschine
  * Der Zwischencode ist oft nur ein Zwischenprodukt und wird weiter verarbeitet
* Der Zwischencode kann optimiert werden
  * Erkennung und Eliminierung bestimmter Rekursionsformen,
    Verkürzung von Sprungketten
  * Maschinenspezifische Optimierung
* Der Zwischencode vereinfacht die Implementierung einer Sprache für unterschiedliche Zielmaschinen (Zielprogramm)
  * Nur der letzte Transformationsschritt hat maschinenspezifische Varianten
* Zwischencode hat die Form einer Maschinensprache, welche aber nicht real existiert, z.B. three-address code (TAC)



## Was geschieht in der Code-Optimierungsphase?

- Ziel: schneller Maschinencode



## Was geschieht in der Code-Erzeugungsphase?

* Generierung des eigentlichen Ziel Code, z.B.
  * Bytecode
  * Maschinencode
  * Assembler



## Welche Arten von Compiler gibt es?

* Nativer Compiler
  * erzeugt Zielcode (Maschinencode) für Plattform, auf der er selbst läuft
* Cross-Compiler
  * erzeugt Zielcode für Plattform, auf der selbst nicht läuft
* Single-pass-Compiler
  * erzeugt Zielcode in einem Durchlauf aus dem Quellcode
  * üblicherweise schnell
  * nur einfache Optimierungen möglich
  * nur für bestimmte Programmiersprachen (z.B. Pascal)
* Multi-pass-Compiler
  – übersetzt Quellcode in mehreren Schritten in Zielcode



## Welche Sonderformen von Compiler gibt es?

* Transcompiler
  * übersetzt Quellcode zwischen Hochsprache (z.B. C# in Java)
* Compiler-Compiler
  * Hilfsprogramme zur automatischen Generierung von Compiler-Teilen
    oder vollständigen Compilern (z.B. ANTLR, Coco/R, YACC, ...)
* Just-in-time-Compiler
  * Verfahren um (Teil-)Programme zur Laufzeit in Maschinencode zu
    übersetzen (z.B. HotSpot, VM für Java mit JIT-Compiler)
  * Ziel: Ausführungsgeschwindigkeit gegenüber Interpreter steigern
* Compreter
  * übersetzt Quellcode zuerst in Zwischencode, dann zur Laufzeit interpretieren (heutige Interpreter verwenden Compreter)



## Was ist ein Interpreter?

* Dienstprogramme (wie Compiler), die höhere Programmiersprachen realisieren
* lesen Quellcode ein und analysieren ihn
* erzeugen keine Programme, 
  * lösen direkt zu jedem Befehl der Programmiersprache zugehörigen Aktionen auf entsprechender Plattform (physische/virtuelle Maschine) aus



## Was sind Beispiele von Interpretersprachen?

* APL, BASIC, Forth, Perl, Python, Ruby, PHP, verschiedene Skriptsprachen...



## Vergleich Compiler / Interpreter

* Interpreter
  * Vorteile:
    * Eine Programmzeile kann sofort getestet werden
    * Fehler bei der Programmierung werden sofort erkannt und behoben
  * Nachteile:
    * Bei jeder Programmausführung muss das Programm erneut analysiert
      werden; daher längere Laufzeit.
    * Es gibt kein Objektprogramm, das Quellprogramm benötigt mehr
      Speicherplatz

* Compiler
  * Vorteile:
    * Programmanalyse muss nicht bei jeder Programmausführung
      vorgenommen werden
    * Das Objektprogramm benötigt weniger Ausführungszeit und weniger
      Speicherplatz
  * Nachteile:
    * Mehrere Schritte sind erforderlich, um ein Programm auszuführen
    * Fehlersuche bei der Programmentwicklung ist meist aufwändiger



## Welche Nachteile hat die klassische Implementierung einer Programmiersprache auf Zielplattformen (physische Rechner)?

* unterschiedliche Instruktionssätze von Prozessoren zu implementieren
* effiziente Code-Erzeugung bei gegebenen Instruktionssatz schwierig
* Rahmenbedingungen sollten gleich bleiben, trotz ändernder Instruktionssätze und Rechnerarchitekturen



## Wie wird gegen das oben erwähnte Problem vorgegangen?

* Bei Implementierung neuerer Programmiersprachen wird deshalb dazu übergegangen, den Instruktionssatz einer idealisierten abstrakten oder virtuellen Maschine als Zielsprache des Compilers zu definieren

* Vorteile:
  * Befehlssatz der VM kann passend zu Paradigmen und Konzepten der Quellsprache gewählt werden
  * Plattformunabhängige Entwicklung, Portierbarkeit, sicherere Ausführung (Sand-Boxing)



## Klassische vs virtualisierte Kompilierung

* TODO



## Was ist der wesentliche Unterschied zwischen Bytecodes und herkömmlichen Zwischensprachen?

* Unterschied im Aufbau seines Befehlssatzes
* Für herkömmlichen Zwischencode ist entscheidend
  * grundsätzliche Architekturunabhängigkeit
  * schnelle und einfache Maschinencode Erzeugung
  * Optimierbarkeit durch Algorithmen

* Bytecode setzt zudem voraus, dass er
  * auf ungewöhnlichen oder sehr einfachen Architekturen bearbeitbar ist
  * Typinformationen enthält, um zulässige Operationen eindeutig zuordnen zu können
  * Instruktionen zur Organisation von Threads und Interaktion mit nativen Quellcode enthält
  * möglichst kompakt und serialisierbar sein muss (Plattform Transfer)
  * auch zusätzliche Metainformationen enthält (z.B. Debug Infos)



## Was sind die komponenten einer virtuellen Maschine?

* TODO



## Was ist das Funktionsprinzip einer VM?

1. Bytecode wird vom Code-Optimierer allgemein oder maschinenbezogen optimiert
   * Code wird zudem auf Fehlerfreiheit und Sicherheit verifiziert
2. Bytecode wird ausgeführt
   * Die einzelnen Instruktionen beziehen sich dabei ausschliesslich auf virtuelle Register oder den Stack
3. Benötigter Speicher wird von dervirtuellenMaschine organisiert (automatische Speicherverwaltung)
   Organisation der Threads (abhängig von Implementierung )
   * Threads können auf darunterliegenden Betriebssystems abgebildet werden (emuliert)
   * Threads können auf Betriebssystem Ebene laufen
   * Threads können direkt auf der Zielhardware laufen



## Kontrollfragen

