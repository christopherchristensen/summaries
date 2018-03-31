# Formulas

## Deskriptive Statistik

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

#### Mathematisch

Mittelwert (Arithmetisches Mittel) = $\overline{x}_n$

##### Mittlere absolute Abweichung
> $\displaystyle\frac{|(x_1 - \overline{x}_n)| + |(x_2 - \overline{x}_n)| + \dots + |(x_3 - \overline{x}_n)|}{n-1}$

##### Empirische Varianz
> $Var(x) = \displaystyle\frac{(x_1 - \overline{x}_n)^2 + (x_2 - \overline{x}_n)^2 + \cdots + (x_n - \overline{x}_n)^2}{n-1} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2$

##### Standardabweichung
> $\displaystyle s_x = \sqrt{Var(x)} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x}_n)^2}$

#### Mit Python

```python
# Empirische Varianz
methodeA.var()
# Standardabweichung
methodeA.std()
```

### Median

#### Mathematisch
1. Werte der Grösse nach ordnen
2. Mittlere Beobachtung ermitteln
3. Bei einer mittleren Beobachtung ist das der Median
4. Bei zwei mittleren Beobachtungen ist der Median der Durchschnitt dieser Werte

#### Mit Python

```python
methodeA.median()
```


### Quartilsdifferenz