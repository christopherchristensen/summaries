# Serie 03 - Solutions



## 3.1 Anwendungsbeispiel 1 Wahrscheinlichkeitsdichtefunktion



> **Frage 1**: Sind die Werte im Intervall $[0, 60]$ Anzahl CHF? 
>
> **Frage 2**: Was repräsentiert die y-Achse?

> **Notiz 1**: Die x-Achse repräsentiert einen Werte, wie zum Beispiel Menge oder CHF. 
>
> **Notiz 2**: Die Wahrscheinlichkeit $P$, dass meine Werte im Intervall $[a, b]$ liegen, kann wie folgt dargestellt werden: $$P(a < X < b) = \int_{a}^{b} f(x) dx = Wahrscheinlichkeit$$
>
> **Notiz 3**: Es ist wichtig, dass die gesammte Fläche unter der Funktion $1$ ergibt. 



#### a.) Konstanter Wert $c$ berechnen 



$$\displaystyle f(x) = \begin{cases} cx (15 - \frac{x}{4}) & \quad \text{falls } 0 \leq x \leq 60  \\ 0 & \quad \text{sonst} \end{cases}$$



> Die Konstante $c$ ist ein unbekannter Wert, der uns verhindert $x$ zu berechnen. Deshalb müssen wir ihn aus der folgenden Bedingung  berechnen:
>
> * Wir wissen, dass die gesammte Fläche unterhalb der Funktion $1$ geben  muss, denn eine Wahrscheinlichkeit kann nicht über $1$ ($100\%$) sein.
> * Wir wissen, dass die Kurve im Intervall $[0, 60]$ liegt, denn überall sonst ist die Wahrscheinlichkeit $0$ 



Wir rechnen das Integral der Wahrscheinlichkeitsdichtefunktion $f(x) = cx (15 - \frac{x}{4})$ im Intervall $[0, 60]$ aus und setzen dieses gleich $1$:



$\displaystyle F(x) = \int_{0}^{60} f(x)\  dx = \int_{0}^{60} cx (15 - \frac{x}{4})\  dx = c \cdot \int_{0}^{60} 15x - \frac{x^2}{4} \ dx = 1$

$F(x) = \displaystyle c \cdot \int_{0}^{60} 15x - \frac{x^2}{4} \ dx = c \cdot \left| \frac{15}{2} x^2 - \frac{x^3}{12} \right|_0^{60} = c \cdot \left( \frac{15}{2}(60)^2 - \frac{(60)^3}{12}\right) - 0 = 1$

$\displaystyle F(x) = c \cdot \left( \frac{15}{2}(60)^2 - \frac{(60)^3}{12}\right) - 0 = c \cdot 9000 - 0 = 1$

$\displaystyle c = \frac{1}{9000}$



Nun haben wir die Konstante $c$ berechnet und können weitere Berechnungen mit der nun vollständigen Wahrscheinlichkeitsdichtefunktion durchführen.



#### b.) Verteilungsfunktion $F(X)$ der Zufallsvariablen $X$ angeben

Da wir nun $c$ berechnet haben können wir die Verteilungsfunktion problemlos angeben. Die Zufallsvariablen $X$ werden als Parameter übergeben, da wir die Wahrscheinlichkeit für das Auftreten der Zufallsvariable $X$ im Intervall $[a, b]$ berechnen wollen. Da wir das Integral von $f(x)$ im Interval $[a, b]$ berechnet haben müssen wir nur die Funktion mit den verschiedenen Wertebereichen angeben.



$\displaystyle F(x) =  \frac{1}{9000} \left(\frac{15}{2}x^2 - \frac{x^3}{12} \right) \quad \text{falls } 0 \leq x \leq 60$



Und wenn wir nun alle Wertebereiche in Betracht ziehen (auch diese ausserhalb $0 \leq x \leq 60$), dann erhalten wir:



$\displaystyle F(x) = \begin{cases} 0 & \quad \text{falls } 0 < x \\ F(x) =  \frac{1}{9000} \left(\frac{15}{2}x^2 - \frac{x^3}{12} \right) & \quad \text{falls } 0 \leq x \leq 60 \\ 1 & \quad \text{falls } x > 60 \end{cases}$



#### c.) Welcher Wert der Aufwendungen mit $10\%$ Wahrscheinlichkeit überschritten?

Wir können nun die Verteilungsfunktion $F(x)$ verwenden, um den Wert der Aufwendung mit dieser Wahrscheinlichkeit zu berechnen. 

![stat-ex03-c](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw03/stat-ex03-c.png)

Dies bedeutet, dass wir einen Wert für $x$ (in diesem Fall ist $x$ die monatliche Aufwendung für den Wasserverbrauch eines 2-Personenhaushalts in CHF) finden müssen, welcher $90\%$ der gesammten Wahrscheinlichkeit (Fläche unter der Kurve) entspricht. Mathematisch gesehen bedeutet das (wenn $a$ den gesuchte Wert darstellt):



$\displaystyle F(a) = \frac{1}{9000} \left(\frac{15}{2}a^2 - \frac{a^3}{12} \right) = 0.9$



Jetzt löst man das mit dem Taschenrechner (oder mit [WolframAlpha](https://www.wolframalpha.com/)) auf und erhält für $a$ folgende Werte:



* $a = -28.625$
* $a = 48.252$
* $a = 70.373$ 



>  Man erhält 3 Werte, weil die Verteilungsfunktion ein Polynom dritten Grades ist.

Wir nehmen nun den einzigen Wert der sich in unserem Interval $[0, 60]$ befindet und zwar $a = 48.252$. 



#### d.) Erwarteten monatlichen Aufwendungen berechnen

> **Frage 3**: Wieso wird hier das Intervall $[0, 60]$ verwendet in der Lösung und nicht $[-\infin, \infin]$ wie in der Formel? 
>
> **Frage 4**: Wann weiss man, dass es sich bei einer Wahrscheinlichkeitsdichtefunktion um eine normalverteilte symmetrische Kurve handelt?

In dieser Aufgabe liegt die Antwort, wie wir vorgehen müssen, bereits in der Aufgabenstellung. Die **erwarteten** monatlichen Aufwendungen sind zu berechnen. Dabei handelt es sich, um den wahrscheinlichsten Wert oder dem Schwerpunkt der Funktion: **der Erwartungswert**.

Wir kennen bereits die Formel, um den Erwartungswert einer **stetigen** Wahrscheinlichkeitskurve zu berechnen: 



$\displaystyle E(X) = \int_{-\infin}^{\infin} x \cdot f(x) \ dx$



Wie man sieht wird hier nicht die Verteilungsfunktion $F(x)$ verwendet, sondern die Wahrscheinlichkeitsdichtefunktion $f(x)$. In unserem Beispiel heisst das folgendes:



$\displaystyle E(X) = \int_{0}^{60} x \cdot cx \left( 15 - \frac{x}{4}\right) = \int_{0}^{60} x \cdot \frac{1}{9000}  x  \left( 15 - \frac{x}{4}\right) = \frac{1}{9000} \int_{0}^{60}   x^2  \left( 15 - \frac{x}{4}\right)$

$\displaystyle E(X) = \frac{1}{9000} \cdot  \left| 5x^3 - \frac{1}{16} x^4 \right|_{0}^{60} = \frac{1}{9000} \cdot (1080000 - 810000) = 30$



>  **Alternative**: Da es sich bei der Wahrscheinlichkeitsdichtefunktion um eine normalverteilte Gaussche Glockenkurve handelt, weiss man, dass der Schwerpunkt direkt in der Mitte der Kurve liegt und die Dichte um diesen Wert symmetrisch verteilt ist. Somit kann man auch die Hälfte von 60 nehmen und den Erwartungswert direkt berechnen.



## 3.2 Anwendungsbeispiel 2 Wahrscheinlichkeitsdichtefunktion



#### a.) Warum handelt es sich bei $c$ um den Wert $0.1$ ?

>  Wir wissen, dass 
>
> * die Fläche unter der Kurve immer gleich $1$ sein muss, da nicht über eine $100\%$ -ige Wahrscheinlichkeit erziehlen kann. Die Kurven sind auf $100\%$ normiert. 
> * die Formel, um die Flächen von Dreiecken zu berechnen: $A = \frac{a \cdot b}{2}$ 

Mit unserem Vorwissen können wir nun folgendes berechnen:



$A = \frac{c \cdot 20}{2} = 1$



Der Wert $c$  ist somit gleich $\frac{1}{10}$ oder auch als $0.1$ geschrieben. Nun müssen wir noch die Dichtefunktion $f(x)$ finden. Dies machen wir folgendermassen.



* $\text{Steigung der Kurve } = -\frac{0.1}{20}$
* $\text{Geradenfunktion f(x) } = y = mx + q$



Damit erhalten wir die Wahrscheinlichkeitsdichtefunktion $f(x) = \frac{1}{10}(1 - \frac{x}{20})$ für den Bereich $[0, 20]$. Für alle Wertebereiche lautet die Dichtefunktion:



$\displaystyle f(x) = \begin{cases} 0 & \quad \text{falls }  60 < x < 20 \\ \frac{1}{10}(1 - \frac{x}{20}) & \quad \text{falls } 20 \leq x \leq 60 \end{cases}$

 



 #### b.)  Wahrscheinlichkeit, dass Wert kleiner als $5$ und $10$ ist, berechnen

Wir haben hier die beiden Werte $5$ und $10$ gegeben, die Werte auf der $x$-Achse beschreiben. Da wir die Dichtefunktion in der vorherigen Teilaufgabe ermittelt haben, können wir diese hier verwenden, um die kummulative Verteilungsfunktion $F(x)$ von $X$ zu berechnen. Diese lässt sich berechnen durch Integration der Dichtefunktion $f(x)$.



$\displaystyle F(x) = \int_{0}^{x} f(t) \ dt = \int_{0}^{x} \frac{1}{10} \left( 1 - \frac{t}{20} \right) \ dt = \frac{1}{10} \left(x - \frac{x^2}{40}\right) = \frac{x}{10} - \frac{x^2}{400}$



> Merke: Dies gilt nur für den Wertebereich $[0, 20]$. Für die Werte wo $x \leq 0$ ist, ist die Wahrscheinlichkeit 0 und für die Werte wo $x \geq 20$ ist, ist die Wahrscheinlichkeit $1$.



* $F(5) = \frac{(5)}{10} - \frac{(5)^2}{400} = 0.4375 = 43.75\%$
* $F(10) = \frac{(10)}{10} - \frac{(10)^2}{400} = 0.75 = 75\%$



Die Wahrscheinlichkeit, dass Werte unter $5$ angenommen werden, liegt bei $43.75\%$ und dass Werte unter $10$ angenommen werden liegt bei $75\%$.  Wir schreiben:



* $P[X < 5] = 43.75\%$
* $P[X < 10] = 75\%$



 #### c.) Kummulative Verteilungsfunktion skizzieren

Am besten skizziert man sich die gesammte Funktion (ohne Rücksicht auf das Intervall $[0, 20]$) und schneidet dann eifach bei $20$ ab. So sieht man, dass die Funktion bis $20$ steigt.



![stat-ex03-3.2c](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw03/stat-ex03-3.2c.png)



#### d.) Erwartungswert, Median und Standardabweichung berechnen

##### Erwartungswert

Den Erwartungswert können wir wie im Beispiel vorhin mit der Wahrscheinlichkeits&shy;dichtefunktion $f(x)$ berechnen. Die Formel dazu lautet:

 

$\displaystyle E(X) = \int_{-\infin}^{\infin} x \cdot f(x) \ dx$



Nun setzen wir die zuvor ermittelte Wahrscheinlichkeitsdichtefunktion in diese Formel ein, um den Erwartungswert zu berechnen:



$\displaystyle E(X) = \int_{0}^{20} x \cdot \left( \frac{1}{10}(1 - \frac{x}{20}) \right) \ dx = \int_{0}^{20} x \cdot \left( \frac{1}{10} - \frac{x}{200} \right) \ dx = \left| \frac{x^2}{20} - \frac{x^3}{600} \right|_{0}^{20}$

$\displaystyle E(X)  = \left| \frac{x^2}{20} - \frac{x^3}{600} \right|_{0}^{20} = \left[ \frac{(20)^2}{20} - \frac{(20)^3}{600} \right] - 0 = \frac{20}{3} = 6.\overline{666}$



##### Median

Der Median entspricht $50\%$ der Fläche unter der Wahrscheinlichkeitsdichtefunktion. Deshalb wissen wir, dass die kummulative Verteilungsfunktion $F(x) \overset{!}{=} 0.5$ sein muss im Bereich $[0, 20]$.



$\displaystyle F(x) = \frac{x}{10} - \frac{x^2}{400} \overset{!}{=} 0.5$



Wir wandeln die Funktion um damit wir ein Polynom zweiten Grades erhalten und diese dann mit der "Mitternachtsformel" oder eine andere Methode eurer Wahl (z.B. [WolframAlpha](https://www.wolframalpha.com)) auflösen können.



$\displaystyle \frac{x^2}{400} - \frac{x}{10} + 0.5 \overset{!}{=} 0$



Nach Auflösen dieser Gleichung erhalten wir die folgenden zwei Resultate:



* $x = 5.85786$
* $x = 34.1421$



Da der zweite Wert nicht in unserem gesuchten Wertebereich liegt können wir diesen vernachlässigen und erhalten als Median den Wert $5.85786$.



 ##### Standardabweichung

> Wir wissen, dass
>
> * Die Standardabweichung ist gleich der Wurzel der Varianz $\sigma_x = \sqrt{Var(X)}$
> * Die Varianz lässt sich aus dem Erwartungswert berechnen: $Var(X) = E(X^2) − (E(X))^2$



Aus dem vorhin berechneten Erwartungswert können wir nun die Varianz berechnen, um damit nachher die Standardabweichung ausrechnen zu können. Zuerst berechnen wir jedoch die Teilkomponenten der Varianzformel:



$\displaystyle E(X)^2 = (\frac{20}{3})^2 = (6.\overline{666})^2 = \frac{400}{9}$



$\displaystyle E(X^2) = \int_{-\infin}^{\infin} x^2 \cdot f(x^2) \ dx = \int_{0}^{20} x^2 \cdot \frac{1}{10}(1 - \frac{x^2}{20}) = \frac{200}{3}$



$\displaystyle Var(X) = E(X^2) − (E(X))^2 =  \frac{200}{3} - \frac{400}{9} = \frac{200}{9}$



Die Standardabweichung lässt sich nun kann einfach aus der Wurzel der Varianz ($\frac{200}{9}$) berechnen: 



$\displaystyle \text{Standardabweichung }  \sigma_x = \sqrt{Var(X)} = \sqrt{\frac{200}{9}} = 4.7140$



#### e.) Wahrscheinlichkeit, dass Kosten höchstens $120'000.- \text{Fr.}$ sind

Wir haben die Formel um aus der Zufallsvariable $X$ die Kosten $K$ zu berechen. Diese lautet $K = 40000 \cdot \sqrt{X}$. Wir wollen die Wahrscheinlichkeit kennen, bei der die Kosten  $K = 120000.- \text{Fr.}$ sind. Um diese Wahrscheinlichkeit ausrechnen zu können, müssen wir zuerst die Zufallsvariable $X$ kennen.



$K = 120000 = 40000 \cdot \sqrt{X}$

$\text{Zufallsvariable } X = 9$ 



> Wir wissen, dass 
>
> * wir für die Wahrscheinlichkeit die kummulative Verteilungsfunktion brauchen
> * die kummulative Verteilungsfunktion $F(x) = \frac{x}{10} - \frac{x^2}{400}$ (siehe Teilaufgabe b.))
>
>
> **Merke**: Wir wollen nur die Fläche bis und mit der Zufallsvariable kennen, denn in der Aufgabenstellung steht "höchstens" 120'000 Fr. und nicht "mindestens".



Nun können wir diese Zufallsvariable $X$ in die kummulative Verteilungsfunktion einsetzen und erhalten die entsprechende Wahrscheinlichkeit.

 

$\displaystyle F(9) = P[X \leq 9] = \frac{(9)}{10} - \frac{(9)^2}{400} = 0.6975 = 69.75\%$



#### f.) Für welchen Parameter $\lambda$ hat die Exponentialverteilung denselben Erwartungswert?

> **Frage 5**: Wieso kann man einfach eine andere Verteilung nehmen? Verändert dies nicht die komplette Aussage der Wahrscheinlichkeiten?
>
>
> Wir wissen, dass
>
> * Der Erwartungswert in einer Exponentialverteilung wie folgt definiert ist: $E(X) = \frac{1}{\lambda}$ 
> * Der Erwartungswert dieser Aufgabe $\frac{20}{3}$ ist. 



Wir nehmen den zuvor berechneten Erwartungswert $E(X) = \frac{20}{3}$ und verwenden die Formel $E(X) = \frac{1}{\lambda}$ um den Parameter $\lambda$ zu berechnen.



$E(X) = \frac{1}{\lambda} = \frac{20}{3}$

$\lambda = \frac{3}{20}$



#### g.) Wahrscheinlichkeit mit Exponentialverteilung berechnen

> Wir wissen, dass
>
> * $\lambda = \frac{3}{20}$ ist
> *  die Formel für die kummulate Verteilungsfunktion mit einer Exponentialverteilung ist immer $F(x) = 1 − e^{−λx}$, wobei sich der Parameter $\lambda$ sich je nach Werten / Wahrscheinlichkeiten ändert 
> * die Zufallsvariable $X = 9$  



Wir berechnung nun mit der kummulativen Verteilungsfunktion einer Exponentialverteilung die Wahrscheinlichkeit erneut wie in der Teilaufgabe e.):



$F(9) = 1 − e^{−(\frac{3}{20})(9)} = 0.7408 = 74.08\%$



Nehmen wir an die Dauer der Baustellen ist exponentialverteilt, ist die Wahrscheinlichkeit, dass die Kosten einer Baustelle unter $120000.- \text{Fr.}$ liegt grösser. Die verschiedenen Verteilungen sind einfach Modelle, um die Wahrscheinlichkeiten annehmen zu können. Aus Erfahrung nimmt man für bestimmte Anwendungsbeispielen unterschiedliche Verteilungen an. Merke jedoch wie die Erwartungswerte immer gleich bleiben.

> **Frage 6**: Stimmt diese Aussage oben?



## 3.3 Exponentialverteilung

> Wir wissen, dass
>
> * der Parameter $\lambda = 0.04$
> * der Median 50% der Fläche unter der Wahrscheinlichkeitsdichtefunktion
>
> * der Wertebereich über 0 ist $\to W_X =[0, \infin)$
> * die Wahrscheinlichkeitsdichtefunktion $f(x) = \lambda e^{−λx}$
> * die kummulative Verteilungsfunktion $F(x) = 1 − e^{−λx}$
> * der Erwartungswert $E(X) = \frac{1}{\lambda}$
> * die Varianz $Var(X) = \frac{1}{\lambda^2}$



#### a.) Median, Erwartungswert und Wahrscheinlichkeit berechnen

##### Median

Wir kennen $\lambda$  (0.04) und wissen, dass der Median 50% der Fläche unter der Wahrscheinlichkeitsdichtefunktion entspricht und können somit folgendes gleichstellen:



$F(x) \overset{!}{=}  1 − e^{−(0.04)x} \overset{!}{=} 0.5$

$x = 17.3$



Hier entspricht $x$ dem Median, denn bei diesem Wert befinden sich die Hälfte der Werte unterhalt und die andere Hälfte oberhalb dieses Wertes.



##### Erwartungswert

Der Erwartungswert ist ziemlich einfach zu ermitteln, denn wir kennen das folgenden Gesetzt $E(X) = \frac{1}{\lambda}$ für exponentialverteilte Modelle.



$\displaystyle E(X) = \frac{1}{(0.04)} = 25h$



Der Erwartungswert entspricht in dieser Aufgabe der Lebenserwartung einer Maschine. Wir können jetzt mit der kummulativen Verteilungsfunktion berechnen, mit welcher Wahrscheinlichkeit die Maschine mindestens die Lebenserwartung erreicht $\to 1 - P[T_1 > E(T_1)]$. Dies entspricht der Fläche nach dem Erwartungswert. Wir berechnen also $1$  minus die kummulative Verteilungsfunktion für die Zufallsvariable $25$.



$\displaystyle P(T_1 > E(T_1)) = 1 - F(25) = 1 - \left(1 - e^{-(0.04 \cdot 25)}\right) \approx 0.368$



> **Frage**: Wieso entspricht dieser Wert nicht gleich dem Wert des Erwartungswertes?
>
> **Antwort**: Die Verteilung ist exponentiell was dazu führt, dass die Wahrscheinlichkeit für Zufallszahlen höher als der Erwartungswert sich anders verhalten als bei einer Normalverteilung.



#### b.) Wahrscheinlichkeit eines Intervals

Wir sollen die Wahrscheinlichkeit des Intervals $E[T_1] \pm \sigma_{T_1}$ berechnen, also Erwartungswert ($25$) $\pm$ Standardabweichung $(\frac{1}{\lambda})$. Dazu verwendet man wieder die kummulative Verteilungsfunktion, um den linken und rechten Wert des Intervals und dessen Differenz zu berechnen.



$P(\mu_1 - \sigma_{T_1} \leq T_1 \leq \mu_1 + \sigma_{T_1})$  

> Wahrscheinlichkeit des Erwartungswerts minus Standardabweichung ist kleiner als $T_1$ und die Wahrscheinlichkeit des Erwartungswerts plus Standardabweichung ist grösser als $T_1$.  Wir berechnen die Wahrscheinlichkeit, dass diese Bedingungen erfüllt werden.



Da Erwartungswert und Standardabweichung in diesem Fall gleich sind ergibt sich folgende Wahrscheinlichkeit:



$P(0 \leq T_1 \leq \frac{2}{\lambda_1})$



Das können wir nun einfach mit der kummulativen Verteilungsfunktion berechnen.



$P(0 \leq T_1 \leq \frac{2}{\lambda_1}) = F(\frac{2}{\lambda_1}) - F(0) = 1 - e^{-2} - 0 \approx 0.865$



#### c.) Ermitteln der kummulativen Verteilungsfunktion

> Wir wissen,
>
> * Die gesamte Fläche unter der Wahrscheinlichkeitsdichtefunktion beträgt $1$
> * also, kummulative Verteilungsfunktion $= 1$

Uns fehlt eine unbekannte der Wahrscheinlichkeitsdichtefunktion um die kummulative Verteilungsfunktion und somit den Erwartungswert und die Standardabweichung zu ermitteln. Die Fläche unter der Wahrscheinlichkeitsdichtefunktion ergibt $1$ also gilt,



$\displaystyle \int_{-\infin}^{\infin} f_{T_2}(t) \ dt = 1$



Nach Auflösen dieser Gleichung erhält man für $c_2 = \frac{1}{1000}$. Der Erwartungswert ist bekanntlich $\frac{1}{\lambda}$ und auch die Standardabweichung, also $= 1000$. 



#### d.) Wahrscheinlichkeit zweier Maschinen

Die Wahrscheinlichkeit beider Maschinen berechnen für den Fall, dass sie länger als 200 Stunden leben. Danach miteinander multiplizieren. Dies ergibt schlussendlich folgendes:



$e^{-200(c_1 + c_2)} = 0.00027465$

 

## 3.4 Normverteilung I



#### a.) Skizze der Dichte

> Wir wissen,
>
> * Die Wahrscheinlichkeit ist annähernd normalverteilt (also eine Gaussche Glockenkurve)
> * Erwartungswert ist 32ppb (Mitte der Glockenkurve)
> * Standardabweichung 6ppb (Streuung um die Glockenkurve)



![glockenkurve](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw03/glockenkurve.png)



#### b.) Kummulative Verteilungsfunktion I

> Wir wissen,
>
> * `from scipy.stats import norm`
> * normale Verteilung
> * standardisierte Zufallsvariable $\displaystyle Z = \Phi \left( \frac{X − μ}{σ} \right)$ 
>   (siehe Slide 35 / 42 Verteilungsfunktion)
> * $\mu = $ Erwartungswert, $\sigma = $  Standardabweichung 
> * kummulative Verteilungsfunktion `cdf`

> **Frage 8**: Wieso dient die standardisierte Zufallsvariable Z als Kontrolle der erhaltenen Wahrscheinlichkeit? Oder sind das einfach zwei Arten dieselbe Wahrscheinlichkeit zu berechnen?



Da die Wahrscheinlichkeit normalverteilt ist verwenden wir die Funktion `norm.cdf()` von `scipy.stats` , um zu ermitteln wie wahrscheinlich der Schwermetallgehalt in einer Bodenprobe höchstens $40ppb$ ist. 

`norm.cdf(x=40, loc=32, scale=6) # 0.9087887802741321` 

* `x` = "höchstens"
* `loc` = Erwartungswert
* `scale` = Standardabweichung



Wir wollen nun überprüfen, dass die erhaltene Wahrscheinlichkeit stimmt indem wir die **standardisierte Zufallsvariable Z** einführen und mit der Standardnormalverteilung die Wahrscheinlichkeit berechnen.

standardisierte Zufallsvariable $\displaystyle Z = \frac{(X − μ)}{σ} = \frac{(40 - 32)}{6} = \frac{4}{3} = \Phi$

`norm.cdf(x = (40 - 32) / 6) # 0.9087887802741321`



#### c.) Kummulative Verteilungsfunktion II

> Gleiches Verfahren wie in Teilaufgabe b.)

`norm.cdf(x=27, loc=32, scale6) # 0.20232838096364308`



#### d.) Wahrscheinlichkeitsdichtefunktion I

> Wir wissen,
>
> * `from scipy.stats import norm`
> * normale Verteilung
> * Wahrscheinlichkeitsdichtefunktion `ppf` 



Wir wollen nun die Zufallsvariable (Bleigehalt) finden, die mit einer Wahrscheinlichkeit von 97.5% unterschritten wird. Dazu wenden wir die Python-Funktion `norm.ppf()` an. 

`norm.ppf(q=0.975, loc=32, scale=6) # 43.759783907240326`

* `q ` = Quantil
* `loc` = Erwartungswert
* `scale` = Standardabweichung



// TODO Alternative (siehe Lösungen)



#### e.) Wahrscheinlichkeitsdichtefunktion II

> Gleiches Verfahren wie in Teilaufgabe d.)

`norm.ppf(q=0.1, loc=32, scale=6) # 24.310690606732397`



#### f.) Wahrscheinlichkeit eines Wertebereiches

> Wir wissen,
>
> * die Wahrscheinlichkeit der tieferen Zufallsvariable und der höheren Zufallsvariable



Zuerst die Wahrscheinlichkeit der ersten Zufallsvariable ermitteln:

`P1 = norm.cdf(x=32+6, loc=32, scale=6)`



Dann die Wahrscheinlichkeit der zweiten Zufallsvariable ermitteln:

`P2 = norm.cdf(x=32-6, loc=32, scale=6)` 



Danach die Differenz der Wahrscheinlichkeit dieser beiden Variablen berechnen:

`P = P1 - P2 # 0.6826894921370859`



## 3.5 Normalverteilung II

> Wir wissen,
>
> * Grundrauschen normalverteilt
> * Mittelwert (Erwartungswert) ist $0 V$
> * Standardabweichung ist $0.45 V$ 
> * digitale $1$, wenn Spannung über $0.9$   



#### a.) kummulative Verteilungsfunktion

Wir betrachten hier nur das Grundrauschen und **nicht** das eigentliche Übertragen eines Signals. Deswegen nimmt das System aus Versehen ein digitales Signal wahr, wenn das Grundrauschen über $0.9$ Volt steigt.

Somit müssen wir die Wahrscheinlichkeit berechnen, dass das Grundrauschen einen Wert grösser gleich $0.9$ Volt hat. Das ist das Gegenteil wie wenn wir die Wahrscheinlichkeit, dass das Grundrauschen höchstens $0.9$ Volt hat, berechnen wollen. 

Wir berechnen also: $1 - \text{Wahrscheinlichkeit, dass Grundrauschen hoechsten 0.9V}$.



In Python können wir dies folgendermassen berechnen:

`1 - norm.cdf(x=0.9, loc=0, scale=0.45) # 0.02275013194817921` 

* `x` = Zufallsvariable
* `loc` = Erwartungswert
* `scale` = Standardabweichung



#### b.) Quantile

Die Grenzen entsprechen den beiden Quantilen links und rechts der $99\%$ - Fläche der Wahrscheinlichkeit. Die Kurve ist normalverteilt um den Nullpunkt und symmetrisch. Das heisst diese $99\%$ der Fläche verteilen sich gleichmässig links und rechts des Nullpunktes (hier auch Erwartungswert). Somit entsteht eine Grenze links und rechts dieser Fläche, die je beide $0.5\%$ der Gesamtfläche entsprechen.

 Um ein Quantil zu berechnen verwenden wir die Methode `norm.ppf` .

`norm.ppf(q=0.05, loc=0, scale=0.45) # -1.1591231865970053 `



Mit diesem Ergebnis können wir nun sagen:

* $99\%$ des Grundrauschens befinden sich im Intervall $[-1.1591, 1.1591]$ 



 #### c.) kummulative Verteilungsfunktion

In diesem Beispiel berechnen wir das Gegenteil wie in Teilaufgabe a.). Wir wollen wissen wie gross die Wahrscheinlichkeit ist, dass die Spannung höchstens $0.9$ Volt beträgt.

`norm.cdf(x=0.9, loc=1.8, scale=0.45) # 0.022750131948179195`



> **Frage 9**: Was ist Standardisieren genau?



## 3.6 Normalverteilung III



#### a.) kummulative Verteilungsfunktion

> Wir wissen,
>
> * Erwartungswert = $0.2508 mm$
> * Standardabweichung = $0.0005 mm$ 
> * Intervall $0.2500 \pm 0.0015 mm \to [0.2485, 0.2515]$ 

> **Frage**: Wie kommt man darauf, dass die Wahrscheinlichkeit gesucht ist?
>
> **Antwort**: Es wird nach einem Anteil (Prozentsatz) gefragt, der innerhalb der technischen Angaben liegt.



Wir verwenden wie in den vorherigen Aufgaben wieder die Python-Funktion der kummulativen Verteilungsfunktion `norm.cdf` um die Wahrscheinlichkeit zu berechnen.

`norm.cdf(x=0.2515, loc=0.2508, scale=0.0005) - norm.cdf(x=0.2485, loc=0.2508, scale=0.0005) # 0.91924122831152`



#### b.) kummulative Verteilungsfunktion

> Genau gleiches Vorgehen wie bei Teilaufgabe a.), einfach mit dem Erwartungswert $0.2508$ .

`norm.cdf(x=0.2515, loc=0.2500, scale=0.0005) - norm.cdf(x=0.2485, loc=0.2500, scale=0.0005) # 0.9973002039367398`



## 3.6 Uniforme Verteilung

> **Frage**: Wieso ist der Erwartungswert $-1$ ? 

1. $100$ gleichmässig-verteilte Zufallszahlen generieren mit `uniform.rvs`

```python
x = uniform.rvs(size=100, loc=-1, scale=2)
y = uniform.rvs(size=100, loc=-1, scale=2)
```

2. Anzahl Punkte im Kreis ist gegeben durch

```python
points_in_circle = np.sum(np.sqrt(x * x + y * y) < 1) 
```

3. Aus der Aufgabenstellung wissen wir dass $\displaystyle P[(x, y) \in Kreis] = \frac{\pi}{4}$ gilt. Deswegen können wir nun folgendes Rechnen um $\pi$ zu berechnen. Die Anzahl Punkte im Kreis durch die Anzahl Punkte insgesamt (Wahrscheinlichkeit) * 4 ausrechnen.

```  python
pi = 4 * points_in_circle / 100 = 3
```

> Je mehr Zufallsvariablen man generiert, desto genauer wird $\pi$ 

