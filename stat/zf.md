## normalverteilte Zufallszahlen simulieren

Und mit Normalplot betrachten (Aufgabe 5.1):

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

x = st.norm.rvs(size = 10)
st.probplot(x, plot=plt)
```
