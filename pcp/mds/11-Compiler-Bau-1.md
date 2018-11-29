# Compiler Bau 1



## Was sind Parser Generatoren?

* Dienen der automatischen Generierung eines Parsers für eine entsprechende Sprachspezifikation
* Ausgabe: Programm, das einen Parser für diese Sprache in einer vorher angegebenen Sprogrammiersprache implementiert
* Umfang der möglichen Zielsprachen abhängig vom jeweiligen Generator

> Beispiel für Parser Generatoren: ANTLR



## Was ist ANTLR

* Werkzeug zur Implementierung von domänenspezifischen Sprachen
* Bietet kompakte Sprache zur Formulierung von Sprachgrammatiken
* Generiert Lexer und Parser aus LL(*)-Grammatiken
  * LL: Abarbeitung der Eingabe (links nach rechts mit linken Ableitungsregeln)
  * LL(k): "Schaut" k Tokens voraus, um korrekten Pfad in Grammatik zu finden
  * Die V4 kann Adaptive LL(*)-Grammatiken verarbeiten

> Kann Lexer und Parser aktuell in Sprachen Java, C#, Python, JS, Go, C++, Swift generieren



## Welche Werkzeuge gibt es für die Entwicklung (Java)?

* `org.antlr.v4.Tool` : 
  * Liest eine Grammatik ein
  * erzeugt einen Lexer und einen Parser sowie Java-Klassen, welche bei der Bearbeitung des Syntaxbaum verwendet werden
* `org.antlr.v4.gui.TestRig` :
  * Programm, dass den Parser anruft und den Syntaxbaum zeigt

> [antlr.org/tools.html](https://www.antlr.org/tools.html)



## Wie definiert man eine Grammatik (ANTLR)?

```antlr
// Definition einer Grammatik mit dem Namen Hello
grammar Hello;

// Parser-Regeln
greeting	: hello | bye ;
hello		: 'Hello' ID ;
bye			: 'Bye' ID ;

// Lexer-Regeln
ID			: [a-zA-Z]+ ;
WS			: [ \t\r\n]+ -> skip ;
```

* Startregel: Erste Regel
* Terminale Symbole in Anführungszeichen
* `-> skip` , damit Leerzeichen, Tabulatoren, CR, Zeilenumbrüche nicht an Parser weitergeleitet werden



## Wie führt man das obige ANTLR Beispiel aus?

1. Java Code mit ANTLR Tool erzeugen

2. Java Code kompilieren

   ```antlr
   > ./antlr4.sh Hello.g4
   Generate parser and lexer using ANTLR-4 ...
   Compile ANTLR-generated code ...
   ```

3. Testen mit TestRig Tool

   ```ant
   > ./trig.sh Hello greeting -tree
   Hello Jim
   <EOF>
   (greeting (hello Hello Jim))
   ```

> * Quellcode (grün) wird direkt eingegeben
>
> * `-tree` : Ausgabe des Syntaxbaumes als Liste in Lisp bzw. Scheme (blau)
> * `-gui` : Ergebnis des abstrakten Syntaxbaumes als Grafik
> * `-tokens` : Ausgabe der Tokens
> * `-trace` : Syntaxbaum durchlaufen



## Wie übergibt man Quellcode in einem File?

```ant
> ./trig.sh Hello greeting –tree test.hello
(greeting (hello Hello Jim))
```



## Was sind die Phasen der Kompilierung?

* Lexikalische Analyse (Lexer)
  * Einlesen des Quellcodes
  * Identifikation von Tokens (tokenizing)
  * Verwandte Token in Token-Klassen oder Token-Typen gruppieren
* Syntaxanalyse (Parser)
  * Strukturanalyse aufgrund der Tokens / Tokens-Struktur
  * Erzeugung der resultierenden Datenstruktur (Syntaxbaum)



## Wie ist eine Grammatikdatei aufgebaut?

* .g4 - Dateiendung

* ```antlr
  // Definition einer Grammatik
  grammar Parsername
  // Regeln der Grammatik
  // Regeln des Lexers
  ```

* Dateiname muss gleich Grammatikname



## Namensdefinition

* Parser-Regeln beginnen mit Kleinbuchstabe
* Lexer-Regeln beginnen mit Grossbuchstaben
* `EOF` : reservierter Name für Dateiende
* ANTLR akzeptiert Unicode-Zeichen in ANTLR-Name



## Welche Schlüsselwörter kenn ANTLR?

* `import`
*  `fragment`
* `lexer`
* `parser`
* `grammar`
* `returns`
* `locals`
* `throws`
* `catch`
* `finally`
* `mode`
* `options`
* `tokens`



## Was ist zu beachten bei der Definition von Regelnamen?

* Schlüsselwörter dürfen nicht als Regelnamen verwendet werden
* `rule` nicht als Regelname verwenden 
  (generiert eine Klasse RuleContext, die mit interner Klasse kollidiert)
* Keine Schlüsselwörter der Zielplattform als Regelnamen verwenden



## Parser- und Lexer-Regeln

```ant
':' : Definition für eine Regel
'|' : Alternative
''' : Kennzeichnungen von Sprachsymbolen
';' : Ende einer Regel
( ) : dienen der Gruppierung
( )? : optionaler Inhalt, der Null oder einmal vorkommt 
( )* : Wiederholung beliebig oft, auch 0-mal
( )+ : Wiederholung beliebig oft, aber mindestens 1-mal
```

> https://github.com/antlr/antlr4/blob/master/doc/index.md









## Kontrollfragen



#### Wo lässt sich ANTLR bei den Compiler-Arten einordnen?
* Compiler-Compiler



#### Lex/Yacc sind nur LL(1) Parser Generatoren, ANTLR ist ein LL(k) Parser Generator. Was bedeutet das? Was hat das für Auswirkungen?

* Schaut sich mehrere Tokens an



#### Das Tool TestRig, erzeugt als Ergebnis des Parsens einen abstrakten Syntaxbaumes als Grafik. Welche Phase der Kompilierung wird damit abgeschlossen?

* Analysephase



#### Wieso erkennt ANTLR bei der vorhergehenden Folie die zweite, korrekte Zeile nicht?

* Weil das Programm nach einer Zeile fertig ist (und nicht wegen dem Fehler!)
* Das ist in der Grammatik so definiert 



#### Bei der vorhergehenden Folie erkannte ANTLR die Eingabe «Jim2» als das Token «Jim». Wieso?

* Weil er nur [a-zA-z]+ kennt



#### Worin unterscheiden sich die Parser- und die Lexer-Regeln?

* Durch die Klein- und Grossbuchstaben (durch die Schreibweise)



#### Wofürs in die Parser-Regeln zuständig?

* Definieren Syntax des Quellprogramms und die Struktur der Tokens



#### Wofür sind die Lexer-Regeln zuständig?

* 



#### Mit der Option–tree listet TestRig den Syntaxbaum auf. Wofür könnte man das brauchen?

* Für Scheme



#### Wenn Sie das «Adam Riese» Beispiel zu einem Arithmetik Rechner ausbauen. Welche ANTLR Möglichkeit(en) nutzen Sie dafür?

* 