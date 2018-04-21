# Modelle für Messdaten

## Stetige Zufallsvariablen und Wahrscheinlichkeitsverteilung

* Oft Messdaten statt Zähldaten
* Diese können jeden Wert in bestimmten Bereich annehmen
* Genauigkeitsangabe durch Messgenauigkeit vorgegeben

### Diskrete Wahrscheinlichkeitsverteilung

* Zufallsvariable $X$
* Wertemenge $W_X$
* Wertemenge besteht aus endlich vielen **ganzen** Zahlen (diskret)
* Die Menge ist also löchrig
* Beispiel einer Realisierung von $X$: $X(Person) = 174$
* $x$ ist eine Zahl, $X$ ist eine Menge
* Wahrscheinlichkeit berechnen: $P(X = x) =$ Wahrscheinlichkeit der Zahl $x$ $\to$ Anzahl Personen mit x durch Gesamtmenge von X

### Stetige Verteilung

* **nicht** löchrig (Wertemenge ist kontinuierlich)
* Wertemenge $W_X$ von Zufallsvariable $X$ = alle Werte die $X$ annehmen kann
* **runde Klammer** = Wert liegt ausserhalb des Intervalls
* **eckige Klammern** = Wert liegt innerhalb des Intervalls

> Notiz:

> Man hat eine Reihe von Daten, die alle gleichwahrscheinlich vorkommen. Je mehr Kommastellen man zulässt, desto mehr gegen null strebt die Wahrscheinlichkeit eine bestimmte Zahl zu ziehen. (i = Nachkommastellen)
> 
> $$\frac{1}{10^{i+1}}$$

### Wahrscheinlichkeitsdichte

* Die Wahrscheinlichkeitsdichte $f$ ist die Ableitung der kumulativen Verteilungsfunktion:

> $$f(x) = F'(x)$$

* experimentelle Messdaten
* relative Häufigkeit in bestimmten Intervallen grösser als in anderen
* **Wahrscheinlichkeit einer stetigen Zufallsvariablen X**: Wahrscheinlichkeiten aller Intervalle $(a, b]$,

> $$ P(X \in (a, b]) = P(a < X \leq b)$$

* Berechnen mit der kumulativen Verteilungsfunktion $F(x) = P(X \leq x)$

> Eigenschaften der kummulativen Verteilungsfunktion:
> 
> 1. $0 \leq F(x) \leq 1$ (Wahrscheinlichkeit)
> 2. $F(-\infty) = 0$ (Wahrscheinlichkeit, dass Messwert kleiner als $-\infty$)
> 3. $F(\infty) = 1$ (Wahrscheinlichkeit, dass Messwert kleiner als $\infty$)
> 4. $F(x)$ ist monoton wachsend: $F(a) < F(b)$. Ableitung $F'(x)$ von $F(x)$ also immer grösser gleich 0

