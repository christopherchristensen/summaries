# Zeitreihen

## Ziele von Zeitreihen
- Deskriptive Analyse: Mit Visualisierungen grundsätzliche Eigenschaften verstehen
- Modellierung und Interpretation: Modellierung zu Grunde liegenden Prozesse für Verständnis
- Zerlegung: Saisonalität, Trends, etc.
- Vorhersage
- Regression: eine Zeitreihe durch mehrere andere erklären

## Zeitreihenmuster
- Trend $m_k$: Passagierdaten steigen jährlich
- Saisonalität $s_k$: In Ferienzeit wurde mehr geflogen als sonst
- Serielle Korrelation $e_k$: Beobachtungen nicht unabhängig voneinander (aufeinanderfolgend)

## Formel der Zeitreihenkurve
- $y = m_k + s_k + e_k$

## Log-Return
- Näherung der relativen Änderung (in Prozent) bezüglich des Vortags

## Multivariate Zeitreihen
- Zwei oder mehrere Zeitreihen, die gleichzeitig beobachtet werden

## Box-Cox-Transformation
- Familie von Transformationen
- Besonders geeignet, um Schiefe und Varianz zu korrigieren
- Parameter $\lambda$ wählen, dass gewünschte Eigenschaften erfüllt sind

```python
def boxcox(x, lambd):
    return np.log(x) if (lambd==0) else (x**lambd-1)/lambd

data["l_2"] = boxcox(data["column"], 2)
```

## Zeitachsentransformation
- TODO
