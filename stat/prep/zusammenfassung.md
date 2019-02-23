# Zusammenfassung STAT

## Nachkommastellen / Signifikaten Stellen

1. Das Ergebnis einer Addition/Subtraktion bekommt genauso viele Nachkommastellen wie die Zahl mit den wenigsten Nachkommastellen
2. Das Ergebnis einer Multiplikation/Division bekommt genauso viele signifikante Stellen wie die Zahl mit den wenigsten signifikanten Stellen



## Lageparameter

- Arithmetisches Mittel (Durchschnitt / Schwerpunkt der Daten $\bar{x}_n$) 
- Median
- Quantile



## Streuungsparameter

- Empirische Varianz / Standardabweichung
- Quartilsdifferenz
  $$\to$$ Differenz von $$25$$- und $$75$$-Quantil



## Arithmetisches Mittel (Lage)

- Durchschnitt / Mean / Schwerpunkt der Daten
- $$\overline{x}_n = \frac{x_1 + x_2 + … + x_n}{n} = \frac{1}{n} \sum^n_{i=1} x_i$$
- `data.mean()`



## Median (Lage)

* `data.median()`

* Berechnung (ohne Python):
  1. Datensatz der Grösse nach sortieren
  2. Der **Median** ist Wert der mittleren Beobachtung (Messung) 
     $$\to$$ aus 5 Beobachtungen ist Median also 3. Beobachtung
  3. Bei ungerader Anzahl Beobachtungen mittlere Beobachtung nehmen
  4. Bei gerader Anzahl Beobachtungen Durchschnitt der mittleren beiden Beobachtungen nehmen
* Empirischer Median = $$50\%$$ - Quantil



## $$\alpha$$ - Quantil / Quartil (Lage)

* Quantil: Bereich in dem bestimmter `[Prozentsatz]` ($$\alpha$$) aller Beobachtung sind
* Quartil: Quantil, mit bestimmten Prozentsätzen (`25%` und `75%`)

* Unteres Quartil: `data.quantile(q=.25, interpolation="midpoint")` 
* Oberes Quartil: `data.quantile(q=.75, interpolation="midpoint")` 



## Empirische Varianz (Streuung)

* Verteilung der Daten um den Mittelwert
* Wenn empirische Varianz gross 
  $\to​$ Streuung um arithmetisches Mittel gross
* $$\displaystyle Var(x) = \frac{(x_1 - \overline{x})^2 + (x_2 - \overline{x})^2 + … + (x_n - \overline{x})^2}{n-1} = \frac{1}{n-1} \sum^n_{i=1} (x_i - \overline{x})^2$$

* $$\overline{x}$$ : arithmetisches Mittel
* Abweichungen $x_i − \bar{x}$ wird quadriert damit sich Abweichungen nicht gegenseitig aufheben können. Nenner $n - 1$ anstelle von $n$
* `data.var()`



## Empirische Standardabweichung (Streuung)

* Verteilung der Daten um Mittelwert in derselben Einheit wie Daten
* "mittlere" Abweichung vom Mittelwert
* $s_n = \sqrt{Var(x)} = 0.024\ cal/g$ 



## Quartilsdifferenz (Streuung)

* oberes Quartil - unteres Quartil
* Hälfte der "mittleren" Beobachtungen ($$50\%$$)
* Je kleiner, umso näher liegt Hälfte aller Werte um den Median



## Histogramm

* Werte graphisch darstellen
*  `data.plot(kind="hist", bins=7, edgecolor="black")` 
* Bei weniger als 50 Messungen ca. 5 - 7 Klassen
* Bei mehr als 250 Messungen ca. 10 - 20 Klassen
* Klasse erhält Balken mit Höhe proportional zur Anzahl Beobachtungen in dieser Klasse



## Normiertes Histogramm

* Gesamtfläche der Balken $= 1$
* Auf Y-Achse sind die Dichten angegeben
* Balkenhöhe als $\frac{1}{n}$
* Vorteil: Messungen mit unterschiedlichen Umfängen besser miteinander vergleichbar
* `data.plot(kind="hist", normed=True, edgecolor="black")` 



