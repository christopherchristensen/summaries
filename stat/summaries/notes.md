# Notes



## Momentenmethode

* 



## Basic Wahrscheinlichkeiten

* Wie wahrscheinlich trifft z.B. ein bestimmtes Ereignis ein?
  * Frage 1: Wie viele möglichen Ereignisse gibt es?
  * Frage 2: Sind alle Ereignisse gleich wahrscheinlich?
  * Falls ja, dann ist die Wahrscheinlichkeit, dass das bestimmte Ereignis eintrifft gleich das Ereignis durch die möglichen Ereignisse

* Bei Jasskarten ist die W'keit ein König zu ziehen
  * die Summe der W'keiten, die verschiedenen Könige zu ziehen
  * 4 mögliche Könige / 36 mögliche Karten **(Laplace-Modell)**
* $$P(X \leq 172) = P(X < 172)$$ bei stetiger Wahrscheinlichkeit!



## Wahrscheinlichkeitsdichtefunktion

* Im Gegensatz zu Wahrscheinlichkeiten können Wahrscheinlichkeitsdichtefunktionen auch Werte über eins annehmen
* In einem allgemeineren Kontext handelt es sich bei Wahrscheinlichkeitsdichtefunktionen um [Dichtefunktionen](https://de.wikipedia.org/wiki/Dichtefunktion) (im Sinne der Maßtheorie) bezüglich des [Lebesgue-Maßes](https://de.wikipedia.org/wiki/Lebesgue-Ma%C3%9F).
* Der $$y$$ - Wert der Dichtefunktion bedeutet **gar nichts**: keine physikalische Bedeutung



## Erwartungswert

* $$\displaystyle E(X^2) = \int^{\infin}_\infin x^2 f(x) dx$$



## Uniforme Verteilung

* `uniform.cdf(x=x, loc=a, scale=b-a)`



## Beispiele wann Bernoulli

* https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr

* Wenn zwei mögliche Ergebnisse (z.B. $$0$$ oder $$1$$)

* $$X_i$$ bezeichnet das $$i$$-te Los und hat den Wert $$1$$ bei einem Gewinn, sonst $$0$$
  * $$X_i \sim \text{ Bernoulli}(\pi)​$$ und $$X_1, …, X_n \text{ i.i.d.}​$$ 
  * Da ein Gewinn unabhängig von den anderen Losen ist



## Beispiele wann Binomialverteilung

* https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr
* Eine Binomialverteilung ist die Summe von i.i.d. Bernoulli-verteilte Zufallszahlen
* Sprich: Bernoulli, falls das Gesetz der Grossen Zahlen gilt



## Beispiele wann GGZ gilt

* Betrachtung einer Messung, die aus der Summe von mehreren Einzelmessungen besteht (SW04F14) TODO
* Oftmals hat einzelne Messung eine andere Verteilung
  * z.B. der Messfehler von der Arbeitsdauer (täglich) eines Mitarbeiters ist uniform verteilt
  * Jetzt miss man aber den Messfehler von 5000 Arbeitern

