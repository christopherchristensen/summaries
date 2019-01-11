# Compiler-Bau 2



## Optionen von TestRig

* `-tokens` : Gibt Token-Stream aus
* `-tree` : Gibt Syntaxbaum in LISP-Form aus
* `-gui` : Gibt Syntaxbaum visuell in Java-App aus
* `-ps file.ps` : erzeugt visuelle Darstellung des Syntaxbaums in PostScript und speichert sie in ein File
* `-trace` : Gibt Regelnamen und aktuelle Token nach Ein- und Austritt der Regel an
* `-encoding encodingname` : Gibt Codierung für Prüfstruktur an, wenn aktuelle Ländereinstellung Code nicht korrekt liest
* `-diagnostics` : Diagnosemeldungen während Parsen (nur ungewöhnliche Meldungen)
* `-SLL` : Schnelleres, schwächeres Parsen

> Optionen nur zum Testen der Grammatik



## Wie wird ein generierter Parser in ein Java-Programm integriert?

* Nach erfolgreichem Test der Grammatik
* Mit folgenden Schritten:
  1. Aus Quellcode lexikalische Analyse erstellen
  2. Aus lexikalischer Analyse Parser erstellen
  3. Parser erstellt abstrakten Syntaxbaum
  4. Abstrakten Syntaxbaum durchlaufen
  5. Auswertungen vornehmen



## Wie werden generierte Parser-Files in einer IDE kompiliert?

* `antlr-4.7.1-complete.jar` in IDE einbinden
* Kopieren der generierten Parser-Files ins Source Verzeichnis
* Erstellen der Main-Klasse (siehe Folie 6, PCP-Compiler-4)
* Erstellen eines JAR-Files
* Ausführen

```antlr
> java -jar AdamRiese.jar "(1+2)*3="
```