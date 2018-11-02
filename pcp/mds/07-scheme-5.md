# Scheme 5

> * Lokale Definitionen
> * Lexikalisches Scoping



## Was bildet in Scheme die globale Umgebung?

* Wichtiger Aspekt einer Programmiersprache ist die Möglichkeit Objekte über Namen zu referenzieren: `(define <identifier> <expression>)` 
  * Scheme wertet den Ausdruck `<expression>` aus und bindet resultierenden Wert an den Namen `<identifier>` 
  * Scheme holt Werte später über die Namen
  * Namen sind global gültig
* Beim Start einer Umgebung sind alle vordefinierten Basisfunktionen und Namen enthalten
* Zu jedem Zeitpunkt hat man in der Umgebung eine aktuelle Menge von Namen mit Bindungen für Werte und Funktionen
* Diese veränderlichen Bindungen bilden die globale Umgebung



## Weshalb kann man in  Scheme lokale Namen definieren (Lokale Definition)?

* Bei akkumulativer Rekursion sind Hilfsfunktionen wertvoll
* Deren Verwendung verursacht aber auch Probleme
  * Wenn Anzahl Funktionen zu gross, verliert man den Überblick 
    (Namensraum für Funktionen immer kleiner)
  * Gefahr von Verwechslungen oder Namenskonflikten wächst
  * Viele Daten müssen explizit als Parameter an Hilfsfunktionen weitergegeben werden
* Daher gibt es die Möglichkeit, lokale Namen zu definieren und an Werte oder Funktionen zu binden

```scheme
(local (<definition1>...<definitionN>)
       <expression>)
```

> `<expression>` ist (wie ein Funktionsrumpf) der Gültigkeitsbereich der lokalen Definition(en)



## Blockstruktur

* Zwei lokal definierte Funktionen: `f` und `g` 
* `g` ruft `f` und sich rekursiv auf
* Rumpf ruft `g` auf

```scheme
(define (redouble a-list)         		; Globale Definition
  (local(						  		; Lokale Definition
        (define (f x) (* x 2))    		; Lokale Funktion f
        (define (g a-numlist)  
          (cond
           [(empty? a-numlist) empty] 	; Lokale Funktion g
           [else
            (cons
             (f (first a-numlist))
             (g (rest a-numlist)))])))
        (g a-list)))					; Rumpf
```



* Ein `local` Konstrukt ist ein Ausdruck und daher universell einsetzbar
  (z.B. als Operator, Operand oder Rumpf einer Funktion)
* Insbesondere können lokale Definitionen beliebig geschachtelt werden (Blockstruktur, z.B. im Rumpf einer lokalen Definitions)



## Was sind die Eigenschaften von lokalen Definitionen?

* Rumpf der lokalen Definitionen kann auf weiter aussen definierte Namen zugreifen
* Von aussen sind die lokal definierten Namen nicht sichtbar
* An anderen Stellen könnte lokal noch mal der gleiche Namen definiert werden



## Was ist Scoping?

* Die Strategie, nach der ein Name einer Definition zugeordnet wird

> Wikipedia: In [computer programming](https://en.wikipedia.org/wiki/Computer_programming), the **scope** of a [name binding](https://en.wikipedia.org/wiki/Name_binding) – an association of a name to an entity, such as a [variable](https://en.wikipedia.org/wiki/Variable_(programming)) – is the region of a [computer program](https://en.wikipedia.org/wiki/Computer_program) where the binding is valid: where the name can be used to refer to the entity. Such a region is referred to as a **scope block**.



## Was bedeutet lexikalisches Scoping?

* Dass immer die in der Schachtelungsstruktur nächste Definition benutzt wird
* so kann man den Parameter von square auch `z` nennen
* trotzdem wird `z` im Rumpf von square nicht mit dem Parameter `z` von
  Funktion `f` verwechselt



## Was ist der Scope einer Namensbindung?

* Der textuelle Bereich, in dem sich ein Auftreten des Namens auf diese Namensbindung bezieht
  * Top-Level Definitionen haben globalen Scope
  * Der Scope eines Funktionsparameters ist der Körper der Funktion
  * Der Scope einer lokalen Definition ist der Ausdruck (letzter Operand) in der local Definition
* Es kann "Löcher" im Scope einer Namensbindung geben
  (z.B. Überdeckung der Namensbindung durch eine andere Namensbindung desselben Namens)



## Lokale Variablen

* "Hilfsvariablen" im Rumpf einer Funktionsdefinition
* Variablen, wie die Parameter, sind lokal sichtbar
* lokal definierte Variablen machen den Code unübersichtlich
* weniger Seiteneffekte, durch weniger globale Verfügbarkeit



## Wie können Variablen definiert werden?

* Durch die spezielle Form `let`

```scheme
(let ((<variable1> <expression1>)...
      (<variableN> <expressionN>))
      <expression>)
```

* wobei `<expression>` (wie ein Funktionsrumpf) der Gültigkeitsbereich der lokalen Definition(en) ist
* die Liste von `<variable>` und `<expression>` bilden Bindungspaare



## Welcher Definition entspricht `let ` ?

* Der `local` Definition

```scheme
(local (define <variable1> <expression1>)...
       (define <variableN> <expressionN>)
       <expression>)
```



## Worauf muss man achten wenn man `let` verwendet?

* Die `let` Form gilt nur für Variablendefinitionen und nicht für Funktionsdefinitionen



## Wie funktionert die Auswertung von `let` ?

```scheme
(let ((<var1> <exp1>)... (<varN> <expN>))
     <expression>)
```

1. Alle Ausdrücke ( `<exp1>...<expN>` ) zu lokale Werte auswerten
2. Alle Variablen ( `<var1>...<varN>` ) an ausgewertete Werte binden
   ( `((<var1> <value1>)...(<varN> <valueN>))` )
3. In der lokalen Umgebung wird `<expression>` mit den Bindungen (2.) ausgewertet, der Wert von `<expression>` wird als Wert von `let` zurückgegeben
4. Danach sind die lokalen Bindungen nicht mehr zugreifbar



## Was muss man beachten bei der Reihenfolge der `let` Bindungspaaren?

* Eine Variable `<var-i>` ist noch nicht an `<value-i>` gebunden, wenn `<exp-j>` mit `j > i` ausgewertet wird
* `<exp-j>` darf nicht auf `<value-i>` zugreifen!



## Was ist die Alternative zu `let` und inwiefern unterscheiden sie sich voneinander?

* Die spezielle Form `let*`
* Gleiche Syntax wie `let` und ähnliche Semantik
* Die Auswertung erfolgt aber von links nach rechts
  (deshalb auch sequentielles `let*` genannt)



## Anonyme Funktionen

* z.B. zur bildung einer Summe  $\sum_{i=1}^n i^3 = 1^3 + 2^3 + ... + n^3$
* Kann eine Funktion `sum` mit einer Funktion `f` als Parameter verwendet werden?

```scheme
(define (sum f a b)
  (if (> a b)
      0
      (+ (f a)
         (sum f (+ 1 a) b))))
```



## Wie sieht die konkrete Anwendung der Bildung einer Summe aus?

* Um die Summe von Quadrat- oder Kubik-Zahlen zu berechnen definiert man entsprechende Funktionen

```scheme
(define (square x) (* x x))
(define (cube x) (* x x x))

; Die entsprechende Funktion als Argument berechnet die gewünschte Summe
> (sum square 1 10)
385
> (sum cube 1 10)
3025
```



## Wie sieht die flexible Anwendung der Bildung einer Summe aus?

* Da die Laufweite nicht immer $1$  beträgt, ist es geschickt einen weiteren 
  Parameter, `next` , für `sum` einzuführen
* Der Parameter `next` , ebenfalls eine Funktion, berechnet den nächsten zu summiereden Term

```scheme
(define (sum f a next b)
  (if (> a b)
      0
      (+ (f a) (sum f (next a) next b))))

(define (inc1 n) (+ n 1)) ; Für jede Inkrementierung eine neue Funktion
(define (inc2 n) (+ n 2)) ; zu schreiben ist umständlich, zudem sind die
						  ; Funktionsnamen unerheblich
                          
> (sum square 1 incl 10)
385
> (sum square 1 inc2 10)
165
```



## $\lambda$ - Ausdruck

* Neuer Typ von Ausdruck, gekennzeichnet durch das Schlüsselwort `lambda`
* Definiert eine anonyme Funktion

```scheme
(lambda (<formal parameters>) <expression>)
```

* `<formal parameters>` ist eine Liste von Namen, die formalen Parameter 
  (auch leere Liste möglich)
* `<expression>` ist der Funktionsausdruck, auch Rumpf (body) der Funktion genannt

* Syntax der Anwendung

```scheme
((lambda (<formal parameters>) <expression>) 
 			  <argument-list>)
```

* `<argument-list>` : Liste von Argumenten, wird formalen Parametern zugewiesen

* Liste von Argumenten zuerst ausgewertet dann zugewiesen
* Zuordnung von links nach rechts



## Wie wird ein $\lambda$ - Ausdruck ausgewertet?

* Liefert eine Funktion mit entsprechender Parameterzahl
  (kann genau wie die vordefinierten Funktionen benutzt werden)
* Ein $\lambda$ - Ausdruck ist ein Wert, weil Funktionen Werte sind
* Beispiel:

```scheme
(lambda (x) (* x x)) ; Quadratfunktion
```



## Was ist der Scope eines $\lambda$ - Ausdrucks?

* Formale Parameter werden im Rumpf der Funktion vor Bindungen gleicher Namen in der Umgebung geschützt
* Äussere Bindungen haben keinen Einfluss auf, durch $\lambda$ als Parameter festgelegte Namen



## Umgebung und $\lambda$ - Ausdruck

* Scheinbar unterschiedliches Verhalten bei Benutzung von Namen aus der Umgebung

```scheme
> (define b (+ a 15))
a: this variable is not defined

> (define f (lambda (x) (+ a x))) ; Kein Fehler, obwohl a nicht definiert
> (f 15)
a: this variable is not defined ; Fehler erst wenn a benutzt wird

> (define a 10)
> (f 15) ; Erst OK wenn a definiert ist
25
```



## $\lambda$ - Ausdruck zur Funktionsdefinition

* Die bereits bekannte Funktionsdefinition

```scheme
(define (<identifier> <formal parameters>)
<expression>)
```

* Ist die Kurzform von

```scheme
(define <identifier>
(lambda (<formal parameters>) <expression>))
```



> * Werte werden auf diese Weise Namen zugeordnet (z.b. `(define PI 3.1415)` )
>
> * Funktionen sind Werte



## Was ist die Bedeutung von $\lambda$ - Ausdrücken?

* Gibt uns Möglichkeit für die Trennung **zweier** Ebenen zur Funktionsdefinition:
  1. Funktion selbst, die mittels `lambda` abhängig von anderen Grössen flexibel definiert werden kann
  2. Die Argumente der definierten Funktion
* Dadurch kann man beliebig komplexe Funktionen vom Programm aus erzeugen (als Ergebnis von Funktionen) und weiter verwenden



> **Richtlinie für $\lambda$ - Ausdrücke**: Benutze sie wenn, 
>
> * eine Funktion nicht rekursiv ist und
> * nur einmal als Argument gebraucht wird



## Was ist ein Vorteil der funktionalen Ausdruckweise?

* Man kann eine Gruppe verwandter Funktionen relativ leicht zu einer gemeinsamen Funktion "abstrahieren"

* Somit baut jede Funktion auf der vorhergehenden auf



## Was ist ein Vorteil von "Higher-Order Functions"?

* Erhöhen die Ausdruckskraft einer Programmiersprache und ermöglichen die Beschreibung komplexer Zusammenhänge in sehr kompakter Form



## Was ist ein Nachteil von "Higher-Order Functions"?

* Höheres Abstraktionsniveau im Denken:
  * Funktionen, die nur auf elementaren Daten wie Zahlen etc. arbeiten, sind leichter zu verstehen, als Funktionen, die andere Funktionen verarbeiten und/oder erzeugen



## Kontrollfragen



#### Wann besteht Bedarf lokale Definitionen anzuwenden?



#### Wie viele Definitionen sind innerhalb eines `local` - Blocks möglich?



#### Was bedeutet lexikalisches Scoping?



#### Welche Bereiche bei der Namensbindung sind Ihnen in Scheme bekannt?



#### Die Auswertung eines $\lambda$ - Ausdrucks liefert eine Funktion mit entsprechender Parameterzahl. Was heisst das?



#### Wann ist der Einsatz eines $\lambda$ - Ausdrucks sinnvoll?



#### Weshalb können anonyme Funktionen nicht rekursiv sein?



