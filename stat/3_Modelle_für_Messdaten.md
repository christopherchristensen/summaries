# 3 Modelle für Messdaten

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
* Wahrscheinlichkeit berechnen: 
	* $P(X = x)$: Wahrscheinlichkeit der Zahl $x$ 
	* $\to$ Anzahl Personen mit x durch Gesamtmenge von X

### Stetige Verteilung

* **nicht** löchrig (Wertemenge ist kontinuierlich)
* Wertemenge $W_X$ von Zufallsvariable $X$ = alle Werte die $X$ annehmen kann
* **Intervall**: z.B. (a, b]
* **runde Klammer** = Wert liegt ausserhalb des Intervalls
* **eckige Klammern** = Wert liegt innerhalb des Intervalls

> Notiz:

> Man hat eine Reihe von Daten, die alle gleichwahrscheinlich vorkommen. Je mehr Kommastellen man zulässt, desto mehr gegen null strebt die Wahrscheinlichkeit eine bestimmte Zahl zu ziehen. (i = Nachkommastellen)
> 
> $$\frac{1}{10^{i+1}}$$

### Wahrscheinlichkeitsdichte

* Die Wahrscheinlichkeitsdichte $f$ ist die Ableitung der kumulativen Verteilungsfunktion:

> $$f(x) = F'(x)$$

* bei experimentellen Messdaten verwendet,
* wo relative Häufigkeit in bestimmten Intervallen grösser als in anderen ist
* **Wahrscheinlichkeit einer stetigen Zufallsvariablen X** kann mit Wahrscheinlichkeiten aller Intervalle $(a, b]$ beschreiben werden,

> $$ P(X \in (a, b]) = P(a < X \leq b)$$
> 
> $$ P(a < X \leq b) = F(b) - F(a)$$

* Berechnen mit der kumulativen Verteilungsfunktion $F(x) = P(X \leq x)$

> Eigenschaften der **kummulativen Verteilungsfunktion**:
> 

<img src="img/kumulativeverteilung.png" style="width:400px"/>

> 
> 1. $0 \leq F(x) \leq 1$ (Wahrscheinlichkeit)
> 2. $F(-\infty) = 0$ (Wahrscheinlichkeit, dass Messwert kleiner als $-\infty$)
> 3. $F(\infty) = 1$ (Wahrscheinlichkeit, dass Messwert kleiner als $\infty$)
> 4. $F(x)$ ist monoton wachsend: $F(a) < F(b)$. Ableitung $F'(x)$ von $F(x)$ also immer grösser gleich 0

> Eigenschaften der **Wahrscheinlichkeitsdichte**:
> 
> 1. $f(x) \geq 0$, F(x) ist monoton wachsend
> 2. $P(a < X \leq b) = F(b) - F(a) = \int\limits_a^b f(x) dx$, Fläche zwischen a und b unter f(x)
> 3. $\int\limits_{-\infty}^\infty f(x) dx = 1$


## Kennzahlen von stetigen Verteilungen

### Erwartungswert
* Mittlere Lage der Verteilung von Daten: $\mu$
* Bei diskreter Verteilung z.B. Mittelwert oder Median

> $$\displaystyle E(X) = \mu x = \int\limits_{-\infty}^\infty x \cdot f(x) dx$$

### Standardabweichung
Selbe Bedeutung, wie bei diskreter Verteilung: $\sigma_x$

### Varianz
Selbe Bedeutung, wie bei diskreter Verteilung: $\sigma^2_x$

> $$\displaystyle Var(X) = \sigma^2_x = E((X - E(X))^2 = \int\limits_{-\infty}^\infty (x - E(X))^2 \cdot f(x) dx = E(X^2) - E(X)^2$$

### Quantile

Selbe Bedeutung, wie bei diskreter Verteilung:  $q(\alpha)$

## Wichtige stetige Verteilungen

* Im diskreten Fall gibt es Binomial- und Poisson-Verteilung
* Im stetigen Fall gibt es
	* uniforme Verteilung
	* Exponentialverteilung
	* Normalverteilung (Gauss-Verteilung)
	* Standardnormalverteilung

### Uniforme Verteilung

* "Ignoranz"
* Dichte ist konstant (gleichförmig)
* gleiche Wahrscheinlichkeit auf ganzem Wertebereich
* Zufallsvariable X ist Uniform verteilt, falls:

> $$ f(x) =
  \begin{cases}
    \frac{1}{b - a}  & \quad \text{falls } a \leq x \leq b \\
    0 & \quad \text{sonst}
  \end{cases} $$

#### python
Probability density function

```python
from scipy.stats import uniform

# An der Stelle x = 5, Intervall [1, 10]
uniform.pdf(x=5, loc=1, scale=9)
```

Falls $X \sim \text{Uniform}([1, 10])$:

```python
uniform.cdf(x = 5, loc = 1, scale=9)
```

Wahrscheinlichkeit $P(1.2 \leq X \leq 4.8)$:

```python
uniform.cdf(x = 4.8, loc = 1, scale=9) - uniform.cdf(x = 1.2, loc = 1, scale=9)
```

Uniform verteilte Zufallsvariablen:

```python
uniform.rvs(loc = 1, scale=9, size=5)
```

### Exponentialverteilung