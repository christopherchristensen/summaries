# Farbe, Halbtontechnik

* Drucker können nur schwarz, weiss darstellen

## Welche Farben können Drucker darstellen?

* nur schwarz, weiss

## Wie kann ein Bild verschiedene Intensitätsstufen darstellen?

* Durch Verfahren wie:
  * Quantisierung (Rundung auf verfügbare Farben)
  * Dithering (Farben mit Auflösung simuliert)
  * Error Diffusion



## Erkläre traditionelle Halbtontechnik

* für Darstellung von Photographien
* Gräutone durch schwarze Kreise auf weissem Hintergrund (oder umgekehrt) simuliert
* Anteil schwarzer und weisser Flächen entspricht dem Grauwert (Amplituden-Verfahren)



## Erkläre digitale Halbtontechnik

* Ersetzen eines Grauwertpixels durch eine Pixelmatrix mit fester Grösse
* Je nach Grauwert sind verschiedene Pixel gesetzt



## Dithermatrizen

* Die Darstellung der Matrizen kann durch eine Dithermatrix vereinfacht werden
* Die Matrix gibt an, ab welcher Stufe ein Pixel gesetzt wird



// TODO



## Error Diffusion

Idee:

* Der Fehler der durch Setzen eines Pixels auf schwarz oder weiss gemacht wird, wird auf die umliegenden Pixel verteilt
* Das Bild wird dabei sequentiell von oben nach unten und von links nach rechts durchlaufen
* Der Fehler wird anhand der folgenden Gewichte auf die noch nicht besuchten Pixel verteilt