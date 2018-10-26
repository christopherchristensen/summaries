# SW06 - Scan Konvertierung



## Rastern von Linien

* Wie soll eine Linie gezeichnet werden?

* mathematische Beschreibung einer Linie (explizit)
  $y(x) = mx + B$
* Grundidee:
  * Pro Spalte 1 Pixel
  * Es wird dasjenige Pixel gezeichnet, das den geringsten Abstand zur korrekten Linie hat

> Wir nehmen an, dass Endpunkte genau auf Raster liegen



## Brute Force Algorithmus

* Verbesserung des vorherigen Ansatzes 
* $y_{i+1} = m \cdot x_{i+1} + B = y_i + m$
  bekommt pro Pixel ein $m$ mehr über

* DDA (Digital Differential Analyzer):

```
for x=x0 to x1 do 
	y=m * x + B 
	WritePixel(x, Round(y))
end
```

> Nachteile:
>
> * es wird mit Gleitkommazahlen gerechnet
> * Rundungsoperation ist aufwendig



## Mittelpunktschema

* Implizite Darstellung einer Linie:
  $F(x,y) =ax+by+c$ 

* Ist der Punkt (x,y) auf der Linie, so gilt:
  $F(x, y) = 0$

* Ist der Punkt (x,y) unterhalb oder oberhalb der Linie so ist:
  $F(x, y) = d \neq 0$




// TODO

* Ist M (Pixelmittelpunkt) unter- oder oberhalb der Linie

// TODO



## Rastern von Kreisen

* Zum Zeichnen von Kreisen kann auch Mittelpunktschema benutzt werden