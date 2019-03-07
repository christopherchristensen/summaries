# Extra Exercises



## Uniforme Verteilung

> In Zürich fahren die Trams alle 7 Minuten. Angenommen, Sie kommen zu einer zufälligen Zeit an eine Haltestelle, an der ein Tram fährt. Wie wahrscheinlich ist es, dass Sie höchstens eine Minute warten müssen? 
> (`from scipy.stats import uniform`) 

* $$X:​$$ Wartezeit in Minuten
* Verteilung : $$X \sim Unif(0,7)$$
* $$P(X \leq 1) = F(1) = \frac{1-0}{7-0} = \frac{1}{7}$$
* oder: `uniform.cdf(x=1, loc=0, scale=7)` 

> Wie wahrscheinlich ist es, dass Sie zwischen einer halben und 2.2 Minuten warten müssen?

* $$P(0.5 \leq X \leq 2.2)$$ 
* `uniform.cdf(x=2.2,loc=0,scale=7) - uniform.cdf(x=0.5,loc=0,scale=7)`



## Exponentiale Verteilung

> Für welche Dauer $$t_{1/2}$$ wird die Wahrscheinlichkeit, dass das Isotop bis dahin „überlebt“ und dann zerfällt, gleich $$\frac{1}{2}$$? (Parameter $$\lambda$$ bleibt unbekannt)

* $$F(t_{1/2}) = 1 - e^{ - \lambda t_{1/2}} = \frac{1}{2} \implies - \lambda t_{1/2} = ln(\frac{1}{2}) \implies t_{1/2} = \frac{ln(2)}{\lambda} = \frac{0.693}{\lambda}$$
* Halbwertszeit : $$t_{1/2} = \frac{ln(2)}{\lambda}$$



## Zusammenhang Exponential- und Poisson-Verteilung

> Zum Zeitpunkt $$t_0 = 0$$ ereignet sich ein radioaktiver Zerfall in einem radioaktiven Sample. Wie gross ist die Wahrscheinlichkeit, dass erst nach dem Zeitpunkt $$t$$ erneut ein Zerfall eintreten kann?

* $$T$$ : Lebensdauer der Atome im radioaktiven Sample
* W'keit eines Zerfalls nach $$t$$ 
  * $$P(T > t) = P(\text{kein Zerfall in } [0, t])​$$
* $$X$$ : Anzahl Zerfälle im Zeitintervall $$[0, t]$$ folgt einer Poisson-Verteilung
  * $$P(X = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$$
  * $$\lambda$$ : mittlere Anzahl Zerfälle pro Zeiteinheit
  * $$\lambda t$$ : mittlere Anzahl Zerfälle in $$[0,t]$$
* W'keit erst nach $$t​$$ wieder einen Zerfall also,
  * $$P(T > t) = P(\text{kein Zerfall in } [0, t]) = \frac{(\lambda t)^0 e^{-\lambda t}}{0!} = e^{-\lambda t}​$$
  * $$F(t)=P(T \leq t)=1−P(T > t)=1−e^{−\lambda t} \text{ fuer } t \geq 0$$



## Normalverteilung

> IQ Tests folgen einer Normalverteilung mit Mittelwert $$100$$ und Standardabweichung $$15$$. Wie gross die W’keit ist, dass jemand einen IQ von mehr als $$130$$ hat, also als hochbegabt gilt?

* $$P(X > 130)$$, wobei $$X \sim \mathcal{N}(100, 15^2)$$ 
* $$P(X > 130) = 1 - P(X \leq 130)$$
* `1 - norm.cdf(x=130, loc=100, scale=15)`
* `# 0.022750` : also sind rund $$2\%$$ der Bevölkerung hochbegabt

> In welchem Intervall liegen $$90\%$$ der IQ-Ergebnisse?

* $$P(100 - c < X < 100 + c) = 0.9$$
* $$P(X < 100 - c) = 0.05$$ 
* $$P(X > 100 + c) = 0.95$$
* `norm.ppf(q=0.05, loc=100, scale=15)`
* `norm.ppf(q=0.95, loc=100, scale=15)`



## Normalverteilung: Standardisierung

> Sei $$X \sim N(\mu,\sigma^2)$$ mit $$\mu = 2$$ und $$\sigma^2 = 4$$. Berechne $$P(X ≤ 5)$$ mit Standardisieren.

* $$\displaystyle P(X \leq 5) = P\left(\frac{X - \mu}{\sigma} \leq \frac{5 - \mu}{\sigma} \right) = P\left(Z \leq \frac{5-2}{2} \right) = P(Z \leq 1.5) = \Phi(1.5) = 0.93$$
* `norm.cdf(x=1.5)`



