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



## Wie entsteht die Farbe einer Fläche / eines Objektes?

* $\text{Illumination} \cdot \text{Reflectance} = \text{Color signal}$



## Wie ist das Auge aufgebaut?

* **Iris**: Kreisring mit radialen Muskeln

* **Pupille**: Öffnung, durch Iris kontrolliert

* **Linse**: Fokussieren

* **Photorezeptoren**: Nehmen das Licht wahr

  $\to$ Stäbchen und Zäpfchen 



## Für was benötigen wir Stäbchen und Zäpfchen in unseren Augen?

- Stäbchen: 
  - ca. $75 \ – 100 \cdot 10^6$ 
  - für Intensität (Helligkeit)
- Zäpfchen: 
  - ca. $6 \ – 7 \cdot 10^6$
  - für Farbe
- Wenn Lichtwellen darauf strahlen, geben sie Signale an das Gehirn weiter



## Was ist die Fovea?

- Gebiet im Zentrum des Sichtfeldes mit grosser Zäpfchendichte, aber ohne Stäbchen



## Was sind die drei Arten von Zäpfchen?

* S (440nm)
* M (530nm)
* L (560nm)
* Verhältnis im Auge $\to$ $L : M : S = 10 : 5 : 1$



## Wie sehen wir Farbe?

1. Licht strahlt auf unser Auge ein
2. Die Stäbchen und Zäpfchen reagieren auf diese Signale
3. Leiten die Signale an das Gehirn weiter
4. Gehirn verarbeitet die Signale



## Von wo kommt RGB?

* Drei Arten von Zäpfchen,
* die jeweils einen Peak bei R, G und B haben



## Helligkeitswahrnehmung

* **TODO (Folie 15)**

* Die Stäbchen (Scoptic Vision) und Zäpfen (Photopic Vision) haben unterschiedliche Empfindlichkeiten
  * Die Stäbchen haben einen Empfindlichkeits-Peak bei ca. der Wellenlänge $510 nm$
  *  Die Zäpfchen haben einen bei ca. der Wellenlänge $560nm$



## Können alle Farben durch 3 Farben gemischt werden?

* **TODO (Folie 17)**



## Kann RGB alle Farben darstellen?

* Nein

* <p style="color:red">TODO Erklärung (Folie 20) </p>

* rot ist negativ



## Was ist das CIE Farbsystem?

* Spektralwertkurven

  * <p style="color:red">// Integral TODO</p>

* Ist eine beliebige Farbe durch ihre Spektralzusammensetzung $C = P(\lambda)$ gegeben, so sind ihre $X$, $Y$, und $Z$ Anteile gegeben durch

  * $X = k \int{P(\lambda) \overline{x}_\lambda} \ d\lambda$
  * $Y = k \int{P(\lambda) \overline{y}_\lambda} \ d\lambda$
  * $Z = k \int{P(\lambda) \overline{z}_\lambda} \ d\lambda$

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



## Was ist der Zusammenhang zwischen RGB und CMY?


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



## Was wird deutlich durch das Mc Adams Experiment?

* Man kann nicht alle Farben voneinander unterscheiden
* Eingekreiste Bereiche enthalten Farben, die man nicht voneinander unterscheiden kann



## CIE Lab

* absolutes Farbsystem
* gleiche Abstände für gleich empfundene Farbunterschiede
* (bessere Unterscheidung der Farben)



## Was ist die Gamma Korrektur?

> Manche Bildbearbeitungsprogramme (z. B. GIMP) geben bei der **Gammakorrektur** nicht den Gammawert selbst, sondern den Kehrwert 1/**Gamma** an, so dass eine Erhöhung des Wertes einer Erhöhung der Helligkeit entspricht.

* Kontrastunterschied
* Darstellung und Verbesserung
* Durch Gamma Korrektur, Farben linear verteilt $ \to$ um Kontraste richtig darzustellen



 ## Helligkeits / Kontrast Wahrnehmung

* Helligkeit und Kontrast werden logarithmisch wahrgenommen
* Webers law $$\frac{\Delta I}{I} = c$$



## Was ist HD, UHD und 4K?

* Auflösung



## Was ist HDR?

* High Dynamic Range
* Hoher Kontrast
* (Dolby Vision = HDR Spezifikation)



## Was sind bekannte Auflösungen?

| Auflösung | Name            |
| --------- | --------------- |
| 720x480   | NTSC            |
| 720x576   | PAL / SECAM     |
| 1280x720  | Blu-ray (720p)  |
| 1920x1080 | Blu-ray (1080p) |
| 3840x2160 | 4K UHDTV        |
| 4096x2169 | 4K DCI (Cinema) |



## Wie funktionieren HDR Aufnahmen?

* nimmt mehrere Bilder
* legt diese übereinander
* das bestmögliche Bild



## HDR Video (Darstellung)

* HDR 10:
  * Wide gamut color space $\to$ gamut = the complete range or scope of something 
  * 10 bit color depth
  * Transfer function
  * High contrast (0.05 - 1000 nits, or 0.0005 - 540 nits)
* HDR 10+:
  * Metadata per frame
* Dolby Vision:
  * Similar, but up to 12 bit color depth and 4k



## Bit depth

* HD / Blue-ray: 8 bit color
* HDR: 10 bit color