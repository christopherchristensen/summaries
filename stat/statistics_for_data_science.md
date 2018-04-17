# Statistics for Data Science

## Deskriptive Statistik (1D)

* Ein Messwert wird beobachtet

### Definition

Quantitative Daten

* zusammenfassen, organisieren
* graphisch darstellen
* um interpretieren und analysieren zu können

Wichtig:

* nicht blind Modell anpassen
* nicht blind statistisches Verfahren anwenden
* zuerst mit Hilfe von graphischen Mitteln und Kennzahlen darstellen

### Nachkommastellen / Signifikante Stellen

#### Definition

* **Nachkommastellen**: Ziffern rechts des Kommas (Dezimal-Darstellung)
* **Signifikante Stellen**: erste von Null verschiedene Stelle bis zur Rundungsstelle

#### Regeln

1. Das Ergebnis einer **Addition / Subtraktion** bekommt genauso viele Nachkommastellen wie die Zahl mit den wenigsten Nachkommastellen.
2. Das Ergebnis einer **Multiplikation / Division** bekommt genauso viele signifikante Stellen wie die Zahl mit den wenisten signifakten Stellen.

$\to$ Rundungen möglichst erst am Schluss!

### Kennzahlen

#### Streuung

* Durchschnittliche Abweichung der Messwerte von mittleren Lage

#### Arithmetisches Mittel

* Durchschnitt ($\overline{x}_n$) der Messwerte. 
* Beachtet die Verteilung der Datensätze um den Mittelwert nicht. 

> $\displaystyle\overline{x}_n = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{1}{n} \cdot \displaystyle\sum_{i=1}^{n} x_i$

#### Empirische Varianz

* Beachtet die Verteilung der Datensätze um den Mittelwert (Streuung). 
* Mittlere absolute Abweichung eignet sich weniger gut (Ableitung ist schwieriger) als empirische Varianz.
* Bei der Varianz quadrieren wir Abweichungen, damit Abweichungen vom Mittelwert sich nicht gegenseitig aufheben.
* Standardabweichung ist Wurzel der Varianz
* Empirische Varianz hat keine physikalische Bedeutung
* Wir wissen nur, je grösser der Wert, desto grösser die Streuung

Mittelwert = $\overline{x}_n$

##### Mittlere absolute Abweichung
> $\displaystyle\frac{|(x_1 - \overline{x}_n)| + |(x_2 - \overline{x}_n)| + \dots + |(x_3 - \overline{x}_n)|}{n-1}$

##### Empirische Varianz
> $Var(x) = \displaystyle\frac{(x_1 - \overline{x}_n)^2 + (x_2 - \overline{x}_n)^2 + \cdots + (x_n - \overline{x}_n)^2}{n-1} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2$

##### Standardabweichung
> $\displaystyle s_x = \sqrt{Var(x)} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2}$

#### Median

* Alternatives Lagemass für mittlere Lage
* Wert, bei dem rund Hälfte der Messwerte unterhalb diesem Wert liegen
* Wird weniger stark durch extreme Beobachtungen beinflusst als arithmetisches Mittel (Robustheit)
* Empirische Median = 50%-Quantil

1. Werte der Grösse nach ordnen
2. Wert der mittleren Beobachtung ermitteln
3. Gibt es nur eine mittlere Beobachtung, dann ist das der Median
4. Gibt es zwei mittlere Beobachtungen, dann ist der Median der Mittelwert dieser beiden Werte

#### Quartile

* Quartile sind robust (schwach beinflussbar)
* Quartile haben verschiedene Definitionen (je nach Software, Mathematiker)
* Durch Robustheit haben Definitionen keinen starken Einfluss (höchsten ein Wert verschieden)

##### Untere Quartil

* Wert, bei welchem **etwa** 25% kleiner-gleich oder 75% grösser-gleich diesem Wert sind

##### Obere Quartil

* Wert, bei welchem **etwa** 25% grösser-gleich oder 75% kleiner-gleich diesem Wert sind

##### Quartilsdifferenz

* Misst Länge des Intervalls, das **etwa** Hälfte der mittleren Beobachtungen enthält
* Je kleiner, umso näher liegt Hälfte aller Werte beim Median (kleinere Streuung) $\to$ robustes Streuungsmass

> $\text{oberes Quartil} - \text{unteres Quartil}$

### Quantile

* Quartile auf jede Prozentzahl verallgemeinert
* 10%-Quantil, 20%-Quantil, etc.
* Empirisches $\alpha$-Quantil ($\alpha$ = Prozent)

### Histogramm

* Graphischer Überblick eines Datensatzes
* In welchem Wertebereich liegen viele Daten
* Einteilung in Klassen (Säulen)
* Werte auf Balkengrenze nur einmal berücksichtigen!
* **Faustregel**: bei weniger als 50 Messungen 5 bis 7 Klassen, bei mehr als 250 Messungen 10 bis 20 Klassen

<img src="img/histogramm.png" style="width:300px">

* Im normierten Histogramm entspricht die Höhe der Balken gerade der Anzahl Beobachtungen einer Klasse

### Boxplot

* Graphischer Überblick eines Datensatzes
* Besteht aus:
	* **Rechteck**, dessen Höhe vom empirischen 25%- und 75%-Quantil begrenzt wird
	* **Linien**, vom Rechteck bis zum kleinsten/grössten "normalen" Wert (1.5 mal Quartilsdifferenz) führen
	* **horizontaler Strich** für Median
	* **kleinen Kreisen**, die Ausreisser markieren
* Gut um Verteilung der Daten in verschiedenen Gruppen vergleichen will
* Höhe des Rechtecks zeigt wie gross Streuung ist (Quartilsdifferenz)

<img src="img/boxplot.png" style="width:300px">

### Empirische kumulative Verteilungsfunktion

> $\displaystyle F_n(x) = \frac{1}{n} \text{Anzahl} \{ i | x_i \leq x \}$

* Graphischer Überblick eines Datensatzes
* Median leicht ablesbar (im Gegensatz zum Histogramm)
* Treppenfunktion ($F_n(\cdot)$)
* links von $x_{(1)}$ ist die Funktion = 0
* bei jedem $x_{(i)}$ wir ein Sprung der Höhe $\frac{1}{n}$ gemacht

<img src="img/kumulative_verteilungsfunktion.png" style="width:300px">

* Bei 0.5 auf vertikaler Achse sind Hälfte aller Werte aufsummiert. Zeichnen wir von 0.5 eine horizontale Linie (siehe Abbildung) wird die kumulative Verteilungsfunktion bei 80.03 geschnitten.
* Das entspricht gerade dem Median.
* Dort, wo grosse Sprünge sind, hat es viele Beobachtungswerte.
* In der Abbildung liegen die meisten Beobachtungswerte zwischen 80.02 und 80.04 (hier untere und obere Quartil)

## Deskriptive Statistik (2D)

* Zwei Messwerte werden beobachet
* Korrelationen zwischen Daten finden

### Streudiagramm

* Zwei Messungen als Koordinaten von Punkten dargestellt
* Kausalitäten können anhand Streudiagramme erahnt werden
* Beweist jedoch keinen kausalen Zusammenhang

<img src="img/streudiagramm.png" style="width:300px">

### Einfache lineare Regression

* lineare Abhängigkeit (z.B. Zusammenhang Seitenzahl x und Buchpreis y $\to$ dickere Bücher sind teurer)
* $\text{Regressionsgerade} = y = a + bx$

#### Methode der kleinsten Quadrate

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


### Empirische Korrelation

* numerische Zusammenfassung der linearen Abhängigkeit zweier Grössen
* Kennzahl = $r$ oder $\hat{\rho}$
* misst Stärke und Richtung der linearen Abhängigkeit zw. x und y
* **steigende Gerade**: $r = +1$
* **fallende Gerade**: $r = -1$
* **keine Abhängigkeit**: $r = 0$
* python: `data.corr()`

> $\displaystyle r = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sqrt{(\sum_{i=1}^n (x_i - \bar{x})^2) \cdot (\sum_{i=1}^n (y_i - \bar{y})^2)}}$

## Modelle für Messdaten

### Stetige Zufallsvariablen und Wahrscheinlichkeitsverteilung

* Oft Messdaten statt Zähldaten
* Diese können jeden Wert in bestimmten Bereich annehmen
* Genauigkeitsangabe durch Messgenauigkeit vorgegeben

#### Diskrete Wahrscheinlichkeitsverteilung

* Zufallsvariable $X$
* Wertemenge $W_X$
* Wertemenge besteht aus endlich vielen **ganzen** Zahlen (diskret)
* Die Menge ist also löchrig
* Beispiel einer Realisierung von $X$: $X(Person) = 174$
* $x$ ist eine Zahl, $X$ ist eine Menge
* Wahrscheinlichkeit berechnen: $P(X = x) =$ Wahrscheinlichkeit der Zahl $x$ $\to$ Anzahl Personen mit x durch Gesamtmenge von X

#### Stetige Verteilung

* **nicht** löchrig (Wertemenge ist kontinuierlich)
* Wertemenge $W_X$ von Zufallsvariable $X$ = alle Werte die $X$ annehmen kann
* **runde Klammer** = Wert liegt ausserhalb des Intervalls
* **eckige Klammern** = Wert liegt innerhalb des Intervalls

> Notiz:

> Man hat eine Reihe von Daten, die alle gleichwahrscheinlich vorkommen. Je mehr Kommastellen man zulässt, desto mehr gegen null strebt die Wahrscheinlichkeit eine bestimmte Zahl zu ziehen. (i = Nachkommastellen)
> 
> $$\frac{1}{10^{i+1}}$$

#### Wahrscheinlichkeitsdichte

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

