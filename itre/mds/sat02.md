# Repetitionsblatt 1

1.  Erklären Sie den Unterschied zwischen Security und Safety und wie die beiden Begriffe zusammenhängen.
    *   Security: Schutz des Systems vor Unfug und Schabernack
    *   Safety: Schutz der Umwelt vor Systemen, die schlecht / falsch funktionieren (Flugzeugabsturz)
    *   Security kann Auswirkungen auf Safety haben

2.  Was versteht man unter Perimeter Security und warum reicht die nicht aus?
    *   Sicherheitsmassnahmen, die an der Aussengrenze eines Systems getroffen werden, z.B. Firewall, Authentifizierung… Dieese reicht i.d.R. nicht aus: Insider Threads, Schutz nach dem Eindringe, Aussengrenze kann oft nicht mehr genau definiert werden etc.
    *   Massnahmen, die nicht Perimeter Security sind: 
        *   Netzwerksegmentierung
        *   System Monitoring
        *   Intrusion Detection Systeme sind Grenzfälle, kann von innen und aussen funktionieren

3.  Erklären Sie die Begriffe Vulnerability (Schwachstelle) und Exploit.
    *   Vulnerability (Schwachstelle)
        *   Ein generelles Sicherheitsrisiko, eine Situation, die nicht vorgesehen war
        *   Eingaben durch Benutzer nicht prüfen, z.B. Injections
        *   Schwachstelle in Systemkonfiguration (z.B. alte Apache-Version installieren mit Vulnerabilities, "ist aber eigentlich ein Systemfehler von Apache")
4.  Warum muss Security von Beginn an in einem Software-Entwicklungsprojekt berücksichtigt werden?
    *   Kann teuer sein nachträglich zu implementieren
    *   Hat oft starken Einfluss auf das Design der Software
5.  Erklären Sie den Unterschied zwischen Anforderungsanalyse, Spezifikation und Design.
    *   Anforderungsanalyse: Anforderungen
    *   Spezifikation:
    *   Design:
6.  Was ist ein Prozessmodell der Software-Entwicklung und welche Modelle gibt es?
    *   Wasserfall-Modell, Scrum, Unified Process
    *   Die zeitliche Anordnung der Schritte wie die Software entwickelt wird
7.  7 Phasen
    1.  Training
    2.  Requirements
    3.  Design
    4.  Implementierung
    5.  Verifikation (Testen, wobei testen alleine nicht ausreicht) (wird das Produkt richtig gemacht) (Validierung: wird gemacht was gewollt war)
    6.  Release (wie wird installiert und konfiguriert, etc.)