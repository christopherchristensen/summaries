---
title: Cross-Site-Scripting (XSS)
author: https://github.com/christopherchristensen
---

# XSS Session Hijacking

## XSS
> Cross-Site-Scripting

- bösartige Skripts in gutartige und vertrauenswürdige Webseiten injizieren

## Wann treten XSS-Angriffe auf?
- wenn Angreifen Webanwendungen verwenden, um bösartigen Code an anderen Endbenutzer zu senden
- üblich in Form eines browserseitigen Skripts

## Fehler, die Angriffe erleichtern
- fehlende Validierung von Input-Daten vom Client
- fehlende Kodierung von Input-Daten vom Client

## Weshalb ist XSS gefährlich?
- Benutzer können nicht wissen, dass Skript nicht vertrauenswürdig ist, und führen ihn aus
- Angreifer kann somit auf folgende Daten zugreifen, die Browser speichert
    - Cookies
    - Sitzungstoken
    - andere sensible Informationen

## Wo treten XSS-Anfriffe häufig auf?
- Dort wo Daten über nicht vertrauenswürdige Quellen in eine Webanwendung (oft Webanfrage) gelangen

