# Farbe



## Was ist Farbe?

* elektromagnetische Strahlung
* Wellenlängen (zwischen 380 und 760 Nanometer)
* vermittelter Sinneseindruck
* subjektiv (philosophischer Ansatz)



## Wie beschreibt man eine Farbe?

* Farbton/Farbe
* Farbstich/Sättigung
* Helligkeit



## Was ist weiss?

* Kombination von Wellenlängen
* Es gibt verschiedene Verteilungen für weiss



## Wie entsteht die Farbe einer Fläche?

// TODO (Folie 7)



## Wie ist das Auge aufgebaut?

* **Iris**: Kreisring mit radialen Muskeln
* **Pupille**: Öffnung, durch Iris kontrolliert
* **Linse**: Fokussieren
* **Photorezeptoren**: Nehmen das Licht wahr



## Für was benötigen wir Stäbchen und Zäpfchen in unseren Augen?

- 75 – 100 106 Stäbchen für Intensität (Helligkeit)
- 6 – 7 106 Zäpfchen für Farbe
- Wenn Licht darauf strahlt, geben sie Signale an das Gehirn weiter



## Was ist die Fovea?

- Fovea: Gebiet im Zentrum des Sichtfeldes mit grosser Zäpfchendichte, aber ohne Stäbchen



## Was sind die drei Arten von Zäpfchen?

* S (440nm)
* M (530nm)
* L (560nm)
* Verhältnis im Auge $\to$ L : M : S = 10 : 5 : 1



## Wie sehen wir Farbe?

1. Licht strahlt auf unser Auge ein
2. Die Stäbchen und Zäpfchen reagieren auf diese Signale
3. Leiten die Signale an das Gehirn weiter
4. Gehirn verarbeitet die Signale



## Von wo kommt RGB?

* Drei Arten von Zäpfchen,
* die jeweils einen Peak bei R, G und B haben



## Helligkeitswahrnehmung

// TODO (Folie 15)



## Kann RGB alle Farben darstellen?

* Nein

* <p style="color:red">TODO Erklärung (Folie 20) </p>

* rot ist negativ



## Was ist das CIE Farbsystem?

* Spektralwertkurven

  * <p style="color:red">// Integral TODO</p>

* Ist eine beliebige Farbe durch ihre Spektralzusammensetzung $C = P(\lambda)$ gegeben, so sind ihre $X$, $Y$, und $Z$ Anteile gegeben durch

* Man erhält mit diesen Integralen einen Farbraum

* Vorteil: Man kann im Gegensatz zu RGB alle Farben darstellen



## Was ist eine Normfarbtafel

* Ebene im $X$, $Y$, $Z$ Farbraum, die durch $(1,0,0)$, $(0,1,0)$ und $(0,0,1)$ geht



## Was sind Komplementärfarben

* Zwei Farben, die gemischt weiss ergeben
* sich gegenseitig "aufheben"



## Wieso nimmt man für Drucker nicht RGB sondern CMYK

* RGB ist additiv

* CMYK ist subtraktiv

* <p style="color:red">// Explanation TODO</p>



## Was heisst additiv?

* Auf dem Computer werden jeweils rote, grüne und gelbe Lichter nebeneinander eingeschalten
* Unser Auge nimmt es als ein Farbgemisch wahr, auch wenn die Lichter leicht nebeneinander platziert sind



## Welche Farbkalibrierungen gibt es?

* sRGB
* AdobeRGB 
  (z.B. hat einen grösseren Farbraum als sRGB, meisten Bildschirme können AdobeRGB nicht darstellen)
* D65



## Wieso wird beim Drucker subtraktive Farbmischung verwendet?

* Man ist daran interessiert, was reflektiert wird



## Was ist das CMY Farbmodell?

* Farbsystem für die subtraktive Farbmischung
* Grundfarben sind die Komplementärfarben von R, G, B:
  C = cyan, M = magenta, Y = yellow



## Was ist der Zusammenhang zwischen RGB?


$$
\begin{pmatrix}
C \\
M \\
Y 
\end{pmatrix} = 
\begin{pmatrix}
1 \\
1 \\
1 
\end{pmatrix} -
\begin{pmatrix}
R \\
G \\
B 
\end{pmatrix}
$$


## Was bedeutet CMYK

* **C**yan
* **M**agenta
* **Y**ellow
* Blac**k**

## Was ist das HSV Farbsystem?

* Farbsystem in dem der Farbort einer Farbe durch die folgenden drei empfindungsmässig bedeutsamen Dimensionen dargestellt wird:
  * **H**ue (Farbton, Farbe)
  * **S**aturation (Sättigung, Reinheit)
  * **V**alue (Intensität)



## Welche Gradwerte von HSV werden den RGB Grundfarben zugeordnet?

* 000 - Rot
* 120 - Grün
* 240 - Blau



## Was ist YUV?

* Composite Video
* Y: Helligkeit
* UV: Farbkodierung, häufig mit 1⁄4 der Auflösung

<p style="color:red">// Explanation TODO</p>



## Wie kann YUV aus RGB verechnet werden?

$$
Y = 0.299*R + 0.587*G + 0.114*B \\
U = \frac{0.436*(B - Y)}{(1 - 0.114)} \\
V = \frac{0.615*(R - Y)}{(1 - 0.299)}
$$

