#Buildserver

**Buildserver (Automation Server)**: Serversoftware, welche automatisierten Build eines SW-Projektes ausführt und die Resultate allen EntwicklerInnen im Team zur Verfügung.

**Auslöser des Buildservers**:

* Automatisch, Änderung im Versionskontrollsystem
* Automatisch, Zeitsteuerung
* Manuell

**Vorteile**:

* Entlastung repetitiver Aufgaben
* Häufigere Verifikation
* Statische Info über Entwicklungsprozess
* Offensive (automatische) Info über Zustand der Projekte

**Beispiele**:

* Jenkins/Hudson (populär)
* CruiseControl (ältest)
* TeamCity (kommerziell)

## Die 2 Konfigurationen

**Variante 1 (Gewaltentrennung)**:

* Konfiguration vom Projekt getrennt
* Interaktiv auf Buildserver
* Infrastruktur geschützt
* Eher bei Firmen

**Variante 2 (Eigenverantwortung)**:

* Konfiguration im Projekt
* Von Entwickler konfiguriert
* Weniger Restriktiv (oft mit Docker) $\to$ mehr Freiheit
* Eher bei OSS

## Einsatz vom Buildserver

Setzt folgende Technologien voraus:

* Automatisierte Builds (Maven, Gradle, etc.)
* Versionskontrollsystem (Git, etc.)

Man sollte auf saubere Aufgabentrennung zwischen Systemen und Technologien achten:

* **Wann** wird Build ausgeführt (Buildserver, Anwender)
* **Was** wird gebaut (VKS)
* **Wie** wird gebaut (Buildautomatisation)
* **Wohin** gehen Artefakte (Buildserver, Build)

$\to$ '**Wie**' sollte nie im Buildserver umgesetzt werden!

**Buildarten**:

* **Continuous** (bei Push): schnelles Feedback
* **Nightly** (Zeitsteuerung): Resultate am Morgen zur Verfügung
* **Release** (Manuell): Reproduzierbarkeit gewährleisten

https://jenkins-vsk.el.eee.intern/jenkins/ (nur im HSLU-Netz)



