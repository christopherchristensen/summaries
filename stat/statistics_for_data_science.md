# Statistics for Data Science

## Deskriptive Statistik

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

1. Werte der Grösse nach ordnen
2. Wert der mittleren Beobachtung ermitteln
3. Gibt es nur eine mittlere Beobachtung, dann ist das der Median
4. Gibt es zwei mittlere Beobachtungen, dann ist der Median der Mittelwert dieser beiden Werte

#### Quartile


