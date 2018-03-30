# QQ-Plots und Parameterschätzung

## Stichworte

* Betondruckfestigkeit
* QQ-Plot
* Empirisches / Theoretisches Quantil

## Normal-Plot

Theoretisches Quantil der Standardnormalverteilung gegen die empirischen Quantile plotten: 

1. Datensatz
2. $\alpha_{(k)} = \frac{k-0.5}{n}$, $k = 1, 2, ..., n$
3. Theoretisches Quantil
4. Empirisches Quantil
5. plotten

> theoretisches Quantil: $q(\alpha_k) = \Phi^-1(\alpha_k)$
> empirisches Quantil: $x_{(k)}$

```python
import numpy as np

				34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])

```

Je linearer der Plot, desto besser $\to$ theoretische entspricht empirischem Quantil. So kann man auch entscheiden, ob unser Histogramm nützlich ist.

## QQ Plot

Auf dem QQ-Plot müssen sich die Punkte des theoretischen Quantil und des empirischen Quantil auf einer Winkelhalbierenden befinden (45°).