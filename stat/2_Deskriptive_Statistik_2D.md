# Deskriptive Statistik (2D)

* Zwei Messwerte werden beobachet
* Korrelationen zwischen Daten finden

## Streudiagramm

* Zwei Messungen als Koordinaten von Punkten dargestellt
* Kausalitäten können anhand Streudiagramme erahnt werden
* Beweist jedoch keinen kausalen Zusammenhang

<img src="img/streudiagramm.png" style="width:300px">

## Einfache lineare Regression

* lineare Abhängigkeit (z.B. Zusammenhang Seitenzahl x und Buchpreis y $\to$ dickere Bücher sind teurer)
* $\text{Regressionsgerade} = y = a + bx$

### Methode der kleinsten Quadrate

* In Streudiagramm kann man keine Gerade durch alle Punkte ziehen
* Versuche Summe der vertikalen Differenzen zw. Beabachtungen und Gerade möglichst klein halten
* **Residuum**: Vertikale Differenz zw. Beabachtungspunkt $(x_i, y_i)$ und Gerade (Punkt auf Gerade = $(x_i, a+bx_i)$):

> $\text{Residuum} = r_i = y_i - (a + bx_i) = y_i - a - bx_i$

* **Ziel**: Summe der Residuen möglichst minimal,

> $\displaystyle r_1 + r_2 + ... + r_n = \sum_{i} r_i$

* **Schwäche**: Wenn Hälfte der Punkte weit über und andere Hälfte weit unter der Geraden, ist Summe der Residuen null. Gerade passt aber trotzdem nicht zu Datenpunkten
* **Lösung**: Vorzeichen eliminieren. 
	* Option 1: Absolutbetrag verwenden (schwierig abzuleiten)
	* Option 2: Quadrate der Residuen aufsummieren,
	* $\displaystyle r_1^2 + r_2^2 + ... + r_n^2 = \sum_{i} r_i^2 = \sum_{i=1}^n (y_i - (a+bx_i))^2$
	* python: `np.polyfit`

> **Minimum** (wird aber immer mit Python gemacht): <br>
> 
> $\displaystyle \frac{\delta}{\delta \alpha} \sum_{i=1}^n (y_i - (a+bx_i))^2 \doteq 0$<br>
> $\displaystyle \frac{\delta}{\delta \beta} \sum_{i=1}^n (y_i - (a+bx_i))^2 \doteq 0$

Die Regressiongerade ist nicht angebracht wenn,

* Die Punkte keiner Gesetzmässigkeit folgen
* Die Punkte einer nichtlinearen Gesetzmässigkeit folgen


## Empirische Korrelation

* numerische Zusammenfassung der linearen Abhängigkeit zweier Grössen
* Kennzahl = $r$ oder $\hat{\rho}$
* misst Stärke und Richtung der linearen Abhängigkeit zw. x und y
* **steigende Gerade**: $r = +1$
* **fallende Gerade**: $r = -1$
* **keine Abhängigkeit**: $r = 0$
* python: `data.corr()`

> $\displaystyle r = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sqrt{(\sum_{i=1}^n (x_i - \bar{x})^2) \cdot (\sum_{i=1}^n (y_i - \bar{y})^2)}}$

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

