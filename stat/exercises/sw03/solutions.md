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

> **Frage 1**: Wieso wird hier das Intervall $[0, 60]$ verwendet in der Lösung und nicht $[-\infin, \infin]$ wie in der Formel? 
>
> **Frage 2**: Wann weiss man, dass es sich bei einer Wahrscheinlichkeitsdichtefunktion um eine normalverteilte symmetrische Kurve handelt?

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

Wir haben hier die beiden Werte $5$ und $10$ gegeben, die Werte auf der $x$-Achse beschreiben. Da wir die Dichtefunktion in der vorherigen Teilaufgabe ermittelt haben, können wir diese hier verwenden, um die kummulative Verteilungsfunktion $F(x)$ von $X$ zu berechnen. Diese lässt sich berechnen durch Integration der Dichtefunktion $f(x)$ im Interval $[0, 20]$.



 



* $f(5) = 0.075 = 7.5\%$
* $f(10) = 0.05 = 5\%$



