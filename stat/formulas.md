# Formulas

## Deskriptive Statistik (1D)

* Ein Messwert wird beobachtet

### Arithmetische Mittel ($x_n$)

#### Mathematisch

> $\displaystyle\overline{x}_n = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{1}{n} \cdot \displaystyle\sum_{i=1}^{n} x_i$

#### Mit Python

```python
from pandas import Series, DataFrame
import pandas as pd

methodeA = Series([..,werte,..])
methodeA.mean()
```

### Empirische Varianz

Mittelwert (Arithmetisches Mittel) = $\overline{x}_n$

#### Mittlere absolute Abweichung
> $\displaystyle\frac{|(x_1 - \overline{x}_n)| + |(x_2 - \overline{x}_n)| + \dots + |(x_3 - \overline{x}_n)|}{n-1}$

#### Empirische Varianz
> $Var(x) = \displaystyle\frac{(x_1 - \overline{x}_n)^2 + (x_2 - \overline{x}_n)^2 + \cdots + (x_n - \overline{x}_n)^2}{n-1} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2$

```python
methodeA.var()
```

#### Standardabweichung
> $\displaystyle s_x = \sqrt{Var(x)} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2}$

```python
methodeA.std()
```

### Median

1. Werte der Grösse nach ordnen
2. Mittlere Beobachtung ermitteln
3. Bei einer mittleren Beobachtung ist das der Median
4. Bei zwei mittleren Beobachtungen ist der Median der Durchschnitt dieser Werte

```python
methodeA.median()
```

### Quartile

#### Untere Quartil

* Mehrere Möglichkeiten / Definitionen:

```python
methodeA.quantile(q=.25, interpolation="linear")
methodeA.quantile(q=.25, interpolation="lower")
methodeA.quantile(q=.25, interpolation="higher")
methodeA.quantile(q=.25, interpolation="midpoint")
methodeA.quantile(q=.25, interpolation="nearest")
```

#### Obere Quartil

* Mehrere Möglichkeiten / Definitionen:

```python
methodeA.quantile(q=.75, interpolation="linear")
methodeA.quantile(q=.75, interpolation="lower")
methodeA.quantile(q=.75, interpolation="higher")
methodeA.quantile(q=.75, interpolation="midpoint")
methodeA.quantile(q=.75, interpolation="nearest")
```

#### Quartilsdifferenz

> $\text{oberes Quartil} - \text{unteres Quartil}$

```python
q75, q25 = methodeA.quantile(q = [.75, .25])
iqr = q75 - q25
iqr
```

### Quantile

* Ein bestimmtes Quantil:

```python
methodeA.quantile(q=.5, interpolation="linear")
methodeA.quantile(q=.15, interpolation="lower")
methodeA.quantile(q=.25, interpolation="higher")
methodeA.quantile(q=.50, interpolation="midpoint")
methodeA.quantile(q=.65, interpolation="nearest")
```

* Mehrere Quantile gleichzeitig:

```python
import numpy as np

# Zeigt verschiedene Quantile von 20% bis 100%
methodeA.quantile(q = np.linspace(start=.2, stop=1, num=5)
```

### Histogramm

#### Standard
```python
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

methodeA = Series([4, 23, 23, 23, 2, 2, 2, 34, 4, 10, 9, 3, 3])

# bins = Anzahl Klassen (Säulen)
methodeA.plot(kind="hist", bins=7,  edgecolor="white")

plt.title("Histogramm von Methoden A")
plt.xlabel("methodeA")
plt.ylabel("Häufigkeit")

plt.show()
```

#### Normiert

```python
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

methodeA = Series([4, 23, 23, 23, 2, 2, 2, 34, 4, 10, 9, 3, 3])

# Normieren mit normed=True
methodeA.plot(kind="hist", normed=True,  edgecolor="white")

plt.title("Normiertes Histogramm von Methoden A")
plt.xlabel("methodeA")
plt.ylabel("Häufigkeit")

plt.show()
```

### Boxplot

```python
methodeA.plot(kind="box", title="Boxplot")
```

### Empirische kumulative Verteilungsfunktion

> $\displaystyle F_n(x) = \frac{1}{n} \text{Anzahl} \{ i | x_i \leq x \}$

```python
methodeA.plot(kind="hist", cumulative=True, histtype="step", 
					normed=True, bins=8, edgecolor="white")
```

## Deskriptive Statistik (2D)

### Streudiagramm

```python
import pandaas as pd
from pandas import DataFrame, Series
import numpy as np

mort = DataFrame({
	"wine": ([2.8, 3.2, 3.2, ..., 75.9]),
	"mor": ([6.2, 9.0, 7.1, ..., 2.1])
})

mort.plot(kind="scatter", x="wine", y="mor")
plt.xlabel("Weinkonsum (Liter / Jahr und Person)")
plt.ylabel("Mortalitaet")
plt.show()
```

### Einfache lineare Regression

> $\text{Residuum} = r_i = y_i - (a + bx_i) = y_i - a - bx_i$

Ziel ist es Summe der Quadrate der Residuen möglichst minimal zu machen:

$\displaystyle r_1^2 + r_2^2 + ... + r_n^2 = \sum_{i} r_i^2 = \sum_{i=1}^n (y_i - (a+bx_i))^2$

```python
b, a = np.polyfit(book["pages"], book["price"], deg=1)

```

> **Minimum**: <br>
> 
> $\displaystyle \frac{\delta}{\delta \alpha} \sum_{i=1}^n (y_i - (a+bx_i))^2 \doteq 0$<br>
> $\displaystyle \frac{\delta}{\delta \beta} \sum_{i=1}^n (y_i - (a+bx_i))^2 \doteq 0$

### Empirische Korrelation

> $\displaystyle r = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sqrt{(\sum_{i=1}^n (x_i - \bar{x})^2) \cdot (\sum_{i=1}^n (y_i - \bar{y})^2)}}$

```python
data.corr()
```

## Modelle für Messdaten

### kummulative Verteilungsfunktion

* Wahrscheinlichkeit einer stetigen Zufallsvariablen X: 

> $$ P(X \in (a, b]) = P(a < X \leq b)$$
> 

* Berechnen mit der kumulativen Verteilungsfunktion $F(x) = P(X \leq x)$

> Eigenschaften der kummulativen Verteilungsfunktion:
> 
> 1. $0 \leq F(x) \leq 1$ (Wahrscheinlichkeit)
> 2. $F(-\infty) = 0$ (Wahrscheinlichkeit, dass Messwert kleiner als $-\infty$)
> 3. $F(\infty) = 1$ (Wahrscheinlichkeit, dass Messwert kleiner als $\infty$)
> 4. $F(x)$ ist monoton wachsend: $F(a) < F(b)$. Ableitung $F'(x)$ von $F(x)$ also immer grösser gleich 0

