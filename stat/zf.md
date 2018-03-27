## normalverteilte Zufallszahlen simulieren

Und mit Normalplot betrachten (Aufgabe 5.1):

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

x = st.norm.rvs(size = 10)
st.probplot(x, plot=plt)
```

## P-Wert

Der P-Wert ist die Wahrscheinlichkeit, unter der Nullhypothese ein mindestens so extremes Ereignis (in Richtung der Alternative) zu beobachten wie das aktuell beobachtete)

* 0: passt gar nicht (widerlegen!)
* 1: passt sehr gut (sein lassen!)

* P-Wert bei **einseitiger nach oben gerichteter** Alternativhypothese: $P(\overline{x}_{150} < \overline{X}_{150})$
* P-Wert bei **einseitiger nach unten gerichteter** Alternativhypothese: $P(\overline{x}_{150} < \overline{X}_{150})$
* P-Wert bei **zweiseitiger** Alternativhypothese: $P(\overline{x}_{150} < |\overline{X}_{150}|)$

### z-Test

$\sigma_x$ ist bekannt.

### t-Test

$\sigma_x$ aus Daten geschätzt $
(\hat{\sigma_x})$