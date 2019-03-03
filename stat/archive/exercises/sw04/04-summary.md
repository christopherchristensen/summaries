# 04 Gesetz der Grosse Zahlen, Zentraler Grenzwertsatz

> * Lineare Transformation
> * Gesetz der grossen Zahlen
> * Zentraler Grenzwertsatz



## Lineare Transformation

$Y = a + bX$



## Eigenschaften Lineare Transformationen

> Es gelten folgende Beziehungen

* $E(Y)=E(a+bX)=a+bE(X)$
* $Var(Y ) = Var(a + bX) = b^2Var(X), σ_Y = |b|σ_X$
* $α − \text{Quantil von Y} =q_Y(α)=a+bq_X(α)$
* $f_Y(y) = \frac{a}{b} f_X \left( \frac{y - a}{b} \right)$



## Was sagt das Gesetz der grossen Zahlen (GGZ) aus?



* Je grösser n, desto grösser wird die Streuung der Augensumme
* Für die durchschnittliche Augenzahl wird die Streuung aber kleiner, und
  man ist immer näher am Erwartungswert
* Wenn wir über viele Beobachtungen mitteln, werden wir immer genauer
* für $n$ sehr gross ist das arithmetische Mittel $\overline{X}_n$ sehr nahe am Erwartungswert



## Kennzahlen der Augensumme $S_n$

* Erwartungswert der Augensumme ist,
  * $E(S_n) = n\mu$
* Varianz der Augensumme ist,
  * $Var(S_n) = n Var(X_i)$
* Standardabweichung der Augensumme ist,
  * $\sigma(S_n) = \sqrt{n} \sigma_X$



## Kennzahlen der mittleren Augenzahl $\overline{X}_n$

* Erwartungswert der mittleren Augenzahl ist,
  - $E(\overline{X}_n) = \mu$
* Varianz der mittleren Augenzahl ist,
  - $Var(\overline{X}_n) = \frac{\sigma^2_X}{n}$
* Standardabweichung der mittleren Augenzahl ist,
  - $\sigma(\overline{X}_n) = \frac{\sigma_X}{\sqrt{n}}$



## Was ist der Standardfehler?

* Die Standardabweichung des arithmesischen Mittels
* Ist nicht proportional zu $\frac{1}{n}$
* Nimmt mit dem Faktor $\frac{1}{\sqrt{n}}$
* Standardfehler $\sigma_{\overline{X}_n} = \frac{1}{\sqrt{n}}\sigma_X$



## Wieviele Beobachtungen braucht man um den Standardfehler zu halbieren?

* Viermal so viele Beobachtungen
* Dies nennt man das $\sqrt{n}$ - Gesetz



## Was sagt der Zentraler Grenzwertsatz aus?

* Sagt aus wie die Augensumme und mittlere Augenzahl bei vielen Zufallsvariablen verteilt sind
* $S_n \approx N(n\mu, n\sigma^2_X)$
* $\overline{X}_n \approx N \left(\mu, \frac{\sigma^2_X}{n} \right)$

> Je grösser $n$ desto besser ist die Approximation 

* Sagt zudem aus,
  * Binomialverteilung ≈ Normalverteilung für $n$ gross und $π$ nicht zu klein
  * Poissonverteilung ≈ Normalverteilung für λ gross



