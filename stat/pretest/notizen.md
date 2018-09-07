1. Daten einlesen
2. relativer Fehler<br>
```python
rf = (x.std()/np.sqrt(x.size))/x.mean()*100
```
3. Verwerfungsbereich t.ppf(q=0.05, loc=1, scale=x.std()/np.sqrt(x.size), df=...

