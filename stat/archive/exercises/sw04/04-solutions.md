# Serie 04 - Solutions



## 4.1 Kennwerte $E(X)$ und $Var(X)$  

> Wir wissen,
>
> * Erwartungswert $= \mu$
> * Standardabweichung $= \sigma$
> * Varianz $= \sigma^2$
>
> * $\mu_X = 40, \sigma_X = 15$ und $\mu_Y = 85, \sigma_Y = 18$  
> * $E(Y)=E(a+bX)=a+bE(X)$
> * $Var(Y ) = Var(a + bX) = b^2Var(X), σ_Y = |b|σ_X$
> * $Var(X) = E(X^2) - E(X)^2$



#### a.) Kennwerte berechnen I

> Aus den Vorlesungen der Woche 3 und 4 kennen wir verschiedene Gesetze für Erwartungswert und Varianz. Diese können wir hier anwenden.



$E(Y) = E(X + 2Y) = a + b E(X) = 1 * (40) + 2 * (85) = 210$

$Var(X + 2Y) = (1)^2 Var(X) + (2)^2Var(Y)  = 1 (15^2) +  4 (18^2) = 1521$

$E(X^2) = Var(X) + E(X)^2 = 15^2 + 40^2 = 1825$   



#### b.) Kennwerte berechnen II

> Hier wenden wir wieder Gesetze und Regeln, die in den Vorlesungen definiert wurden. Der Umfang beträgt $U = 2X + 2Y$. Wir wissen dazu noch, dass die Standardabweichung die Wurzel der Varianz ist. Aus diesem Grund berechnen wir vor der Standardabweichung die Varianz.



$E(U) = 2E(X) + 2E(Y) = 2 * (1000) + 2 * (500) = 3000$

$Var(U) = Var(2X) + Var(2Y) = (2)^2 Var(X) + (2)^2 Var(Y) = 4 * (0.02^2) + 4 * (0.01^2) = 0.002$

$\sigma_U = \sqrt{Var(U)} = \sqrt{0.002} = 0.04472135955$



#### c.) Normalverteilung

> Die Verteilung ist wegen der Aussage $Z \sim N(0,1)$  normalverteilt mit dem Erwartungswert $0$ und der Varianz $1$ , sprich der Standardabweichung $\sqrt{1} = 1$.

// TODO



## 4.2 Stichproben

> Anweisungen in der Aufgabenstellung folgen und den Code im eigenen Python-File übernehmen.



#### a.) Runs graphisch darstellen

Matrix plotten mit `plt.plot(sim)` und `plt.show()` 

![plot(sim)](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw04/plot(sim).png)



#### b.) Mittelwert berechnen und mit Histogramm plotten

> Wir wissen,
>
> * Mittelwerte sind normalverteilt mit $\lambda = 0$
> * Standardabweichung $\sigma = \frac{1}{\sqrt{n}}$

> **Frage**: Was ist der Unterschied zwischen Plot 1 und 2?



```python
plt.hist(sim.T, bins=20, density=True, edgecolor="black", 
         facecolor="white")
                                                              
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)

plt.plot(x,y) 
plt.title("Histogramm sim") 
plt.show()

sim_mean = sim.mean(axis=0)

plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))

plt.plot(x,y) plt.title("Histogramm sim_mean")
plt.show()
```

![histogramm(sim_mean)](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw04/histogramm(sim_mean).png)

![histogramm(sim)](/Users/christopher/Development/studies/github/summaries-me/stat/exercises/sw04/histogramm(sim).png)



#### c.) Siehe `./04-solutions.py`

> ...



## 4.3 Wahrscheinlichkeit mit Stichprobe

> Wir wissen,
>
> * Erwartungswert $= 100 \Omega$
> * Standardabweichung  $\sigma_X = 10 \Omega$
> * Wahrscheinlichkeit ist normalverteilt
> * Standardabweichung der mittleren Augenzahl $\sigma_{\overline{X}_n} = \frac{\sigma_X}{\sqrt{n}}$
> * Aus der Theorie wissen wir, dass die Standardabweichung kleiner wird je grösser $n$ ist



Zuerst berechnen wir die Standardabweichung der Anzahl Versuche (Standardabweichung der mittleren Augenzahl).



$\sigma_{\overline{X}_n} = \frac{\sigma_X}{\sqrt{n}} = \frac{10}{\sqrt{25}} = 2 $



Jetzt haben wir die Verteilung der Wahrscheinlichkeitsdichtefunktion.



$\overline{X}_n \sim N(100, (2)^2) = N(100, 4)$



Wir suchen in dieser normalverteilten Wahrscheinlichkeitsdichtefunktion nun die Wahrscheinlichkeit, dass sich für eine zufällige Stichprobe ein mittlerer Widerstand unter $95 \Omega$ ergibt. Das können wir in Python mit der `norm.cdf()` - Funktion berechnen.



`norm.cdf(x=95, loc=100, scale=2) # 0.006209665325776132`



#### b.) Stichprobe einer uniformen Verteilung



## 4.4 Unabhängige normalverteilte Zufallsvariablen

> Wir wissen,
>
> - Erwartungswert der Augensumme ist,
>   - $E(S_n) = n\mu$
> - Varianz der Augensumme ist,
>   - $Var(S_n) = n Var(X_i)$
> - Standardabweichung der Augensumme ist,
>   - $\sigma(S_n) = \sqrt{n} \sigma_X$
> - Erwartungswert der mittleren Augenzahl ist,
>   - $E(\overline{X}_n) = \mu$
> - Varianz der mittleren Augenzahl ist,
>   - $Var(\overline{X}_n) = \frac{\sigma^2_X}{n}$
> - Standardabweichung der mittleren Augenzahl ist,
>   - $\sigma(\overline{X}_n) = \frac{\sigma_X}{\sqrt{n}}$
> - Erwartungswert $= 1$
> - Standardabweichung $= 2$
> - Varianz $= (2)^2 = 4$



#### a.) $S_n$ und $\overline{X}_n$  bestimmen

Der Erwartungswert und die Varianz der Augensummen $S_n$ berechnen sich aus den Formeln oben im *Wissen wir* - Abschnitt.



$E(S_n) = n\mu = 50 * 1 = 50$

$Var(S_n) = n Var(X_i) = 50 * (4) = 200$

$\sigma(S_n) = \sqrt{n}\sigma_X = 14.1421356237$

$\to N(50, 200)$



Im *Wissen wir* - Abschnitt finden wir auch die Formeln um den Erwartungswert und die Varianz der mittleren Augenzahl zu berechnen.



$E(\overline{X}_n) = \mu = 1$

$Var(\overline{X}_n) = \frac{\sigma^2_X}{n} = \frac{(2)^2}{50} = 0.08$

$\sigma(\overline{X}_n) = \frac{\sigma_X}{\sqrt{n}} = 0.2828427125$

$\to N(1, 0.08)$



#### b.) Wahrscheinlichkeit einer Zufallszahl berechnen

Da der Erwartungswert $1$ beträgt für $E(X_1)$ müssen wir die Wahrscheinlichkeit des Intervals $[1 - 1, 1 + 1] \to [0, 2]$  berechnen. Also, $P(0 \leq X_1 \leq 2)$ . Dies berechnen wir am einfachsten mit `norm.cdf()` , denn wir wissen aus der Aufgabenstellung, dass die Wahrscheinlichkeitsdichtefunktion normalverteilt ist.



`norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2) `

`# 0.38292492254802624`



#### c.) Wahrscheinlichkeit einer Stichprobe der Augensumme berechnen

Da der Erwartungswert $50$ beträgt für $E(S_n)$ müssen wir die Wahrscheinlichkeit des Intervals $[50 - 1, 50 + 1] \to [49, 51]$  berechnen. Also, $P(49 \leq S_n \leq 51)$ . Dies berechnen wir am einfachsten mit `norm.cdf()` , denn wir wissen aus der Aufgabenstellung, dass die Wahrscheinlichkeitsdichtefunktion normalverteilt ist.



`norm.cdf(x=51, loc=50, scale=14.14) - norm.cdf(x=49, loc=50, scale=14.14) `

`# 0.056371977797139816`



#### d.) Wahrscheinlichkeit einer Stichprobe der mittleren Augenzahl berechnen

Da der Erwartungswert $1$ beträgt für $E(\overline{X}_n)$ müssen wir die Wahrscheinlichkeit des Intervals $[1 - 1, 1 + 1] \to [0, 2]$  berechnen. Also, $P(0 \leq \overline{X}_n \leq 2)$ . Dies berechnen wir am einfachsten mit `norm.cdf()` , denn wir wissen aus der Aufgabenstellung, dass die Wahrscheinlichkeitsdichtefunktion normalverteilt ist.



`norm.cdf(x=2, loc=1, scale=0.2828) - norm.cdf(x=0, loc=1, scale=0.2828) `

`# 0.9995938696952003`



## 4.5 Fehlerrechnung

> Wir wissen,
>
> * `dataSeries = Series([…])` um Beobachtungen festzuhalten
>
> * `dataSeries.mean()` um arithmetisches Mittel zu berechnen (Durchschnitt)
> * `dataSeries.std()` um den Standardfehler zu berechnen
> * Standardfehler $s_{\overline{x}_n} = \frac{s_x}{\sqrt{n}}$
> * absoluter Fehler $= \overline{x}_n \pm s_{\overline{x}_n}$
> * relativer Fehler $= \overline{x}_n \pm \frac{s_{\overline{x}_n}}{\overline{x}_n} \cdot 100\%$



#### a.) absolute Fehler berechnen

Zuerst berechnen wir das arithmetische Mittel der Beobachtungen.

```python
methodeA = Series([79.98 , 80.04 , 80.02 , 80.04 , 80.03 , 80.03 , 
                   80.04 , 79.97 , 80.05 , 80.03, 80.02 , 80.00 , 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 
                   79.97])

methodeA.mean() # 80.02076923076923
methodeB.mean() # 79.97875
```



Danach ermitteln wir mit Python den Standardfehler.

```python
methodeA.std() / np.sqrt(methodeA.size) # 0.00664691353682878
methodeB.std() / np.sqrt(methodeB.size) # 0.011090133968017208
```



Jetzt können wir die absoluten Fehler der beiden Methoden angeben als:



* $(80.0208 \pm 0.0066) cal/g$
* $(79.97875 \pm 0.0111) cal/g$



#### b.) relative Fehler berechnen

Wir haben bereits fast alle Komponenten des relativen Fehlers der beiden Methoden berechnen. Somit können wir den relativen Fehler berechnen wie folgt:



> Methode A

$\frac{s_{\overline{x}_n}}{\overline{x}_n} \cdot 100\% = \frac{0.0066}{80.0208} \cdot 100\% = 0.008247855558 \%$



> Methode B

$\frac{s_{\overline{x}_n}}{\overline{x}_n} \cdot 100\% = \frac{0.0111}{79.97875} \cdot 100\% = 0.01387868653 \%$



Und angeben als:



* $(80.0208 \pm 0.0082 \%) cal/g$
* $(79.97875 \pm 0.0139 \%) cal/g$

