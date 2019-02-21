1. Daten einlesen
2. relativer Fehler<br>
```python
rf = (x.std()/np.sqrt(x.size))/x.mean()*100
```
3. Verwerfungsbereich : 
   `t.ppf(q=0.05, loc=1, scale=x.std()/np.sqrt(x.size), df=…`



## DataFraming

* data:

| Index  | Treibstoff   | Elektrizität |
| ------ | ------------ | ------------ |
| Bern   | Elektrizität | 200          |
| Luzern | Elektrizität | 100          |
| Zürich | Elektrizität | 400          |



* Spalte ausgeben: `data["Treibstoff"]`
* Reihe ausgeben: `data.loc["Luzern"]`
* Spalte einer Reihe ausgeben: `data.loc["Luzern", "Treibstoff"]`

