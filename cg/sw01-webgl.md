# WebGL



## Was ist OpenGL?

* Spezifikation einer plattform- und programmiersprachenübergreifenden Programmierschnittstelle (API) 
* zur Entwicklung von 2D- und 3D-Computergrafikanwendungen 
* Der OpenGL-Standard beschreibt etwa 250 Befehle
* die die Darstellung komplexer 3D-Szenen in Echtzeit erlauben



## Was sind OpenGL Merkmal?

* Low Level Graphics API
* Unterstützung für verschiedene Platformen
* gute Hardware Unterstützung auf allen Grafikkarten
* Definierte Extensions



## Was ist WebGL?

* ist eine JavaScript-Programmierschnittstelle
* mit deren Hilfe 3D-Grafiken hardwarebeschleunigt im Webbrowser 
* ohne zusätzliche Erweiterungen dargestellt werden können

$\to$ rasterization engine



## Wie wird der Code von WebGL der GPU bereitgestellt?

* in Form von zwei Funktionen
  * Vertex Shader (Koordinaten)
  * Fragment Shader (Farben)



## Welche 4 Wege gibt es einem Shader Daten zur Verfügung zu stellen?

* Attribute und Buffers
* Uniforms
* Textures
* Varyings