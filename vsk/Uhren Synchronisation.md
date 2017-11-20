# Uhren Synchronisation

## Physische Uhren
Falls keine globale Einigung auf Zeit, ist folgendes Szenario denkbar:

<img src="img/img1.png" width="400">

**Konsequenz**: make wird nicht aufgerufen (Mischung aus alten/neuen Dateien)

**Voraussetzung für Uhr-Sync**:

* **Timer**: Schaltung in Computern, welche Zeit verwaltet
* **Uhr-Tick**: ein, durch Timer erzeugter Interrupt
* **Uhr-Asymmetrie**: Unterschiede von Zeitwerten versch. Uhren, auch wenn diese ursprünglich synchronisiert waren



