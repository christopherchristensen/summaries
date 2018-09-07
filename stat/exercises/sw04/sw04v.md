# Gesetz der Grossen Zahlen / Zentraler Grenzwertsatz

## Stichworte

* lineare Transformation
* Transformation von Grad zu Fahrenheit
* Standardabweichung des Messfehlers

## Lineare Transformation einer Zufallsvariable

> Verteilungsfunktion: $Y = a + bX (a, b \in \mathbb{R})$

Eigenschaften linearer Transformationen:

> 1. $E(Y) = E(a+bX) = a + bE(X)$
> 2. $Var(Y) = Var(a + bX) = b^2Var(X), \sigma_y = |b|\sigma_x$
> 3. $\alpha - \text{Quantil von Y} = q_y(\alpha) = a + bq_x(\sigma)$
> 4. $f_y(y) = \frac{1}{b} \text{ } f_x \text{ } (\frac{y-a}{b})$

Merke: 

* Varianz (Var) ist das Quadrat des Erwartungswert (E) (deswegen wird auch $b$ im Quadrat berechnet)
* $\sigma_y$ = Standardabweichung
* $b$ = Transformationskoeffizient

## Zufällige Fehler

Entstehen durch Ungeschicklichkeit beim Messen oder äussere/innere Einflüsse (Druck, Temperatur, Luftfeuchtigkeit)

Um relativen Fehler zu berechnen:

1. Anzahl Messungen gegeben ($n$)
2. Standardfehler berechnen: $s_\overline{x_n} = \frac{s_x}{\sqrt{n}}$
3. Standardfehler ist dann der absolute Fehler: $\overline{x}_n \pm s_\overline{x_n}$
4. relativer Fehler: $\overline{x}_n \pm \frac{s_\overline{x_n}}{\overline{x}_n} * 100%$