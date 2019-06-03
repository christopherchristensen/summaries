# Bootstrap

## Erläuterung
- Mehr Daten die gleicher Verteilung folgen generieren aus gegebenen Daten
- Macht keine Annahme über Verteilung der Messdaten

## Vorgehen

```python
np.random.seed(1)
x = np.array([...])
n = x.size
nboot = 1
tmpdata = np.random.choice(x, n*nboot, replace=True)
tmpdata.mean()
```
