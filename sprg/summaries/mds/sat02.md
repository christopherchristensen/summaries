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

7.  Was sind die 7 Phasen des MS Security Development Lifecycles (SDL)?

    1.  Training
    2.  Requirements
    3.  Design
    4.  Implementierung
    5.  Verifikation (Testen, wobei testen alleine nicht ausreicht) (wird das Produkt richtig gemacht) (Validierung: wird gemacht was gewollt war)
    6.  Release (wie wird installiert und konfiguriert, etc.)
    7.  Response (projektunabhängig): Patch-Zyklen

8.  Welche Festlegungen müssen im Trainingsprogramm für SDL getroffen werden?

    *   Welcher Grad muss festgelegt werden
    *   Inhalt: was muss er an Schulung haben (Mindestinhalt)
    *   Grad: 

9.  Was ist ein Bug Bar?

    *   Fehlerschranke: wieviele der Fehler der Threads wurden eliminiert, dass wir sagen, es ist jetzt sicher
    *   Wann hört man auf mit dem Testing
    *   (Man kann also die Bug Bars "fälschen", indem man die Schranke tief setzt, ist aber nicht sinnvoll, …)

10.  Was versteht man unter Threat Modeling?

     *   Bedrohungsanalyse
     *   Sollte aus der Sicht des Angreifers gemacht werden

11.  Was ist der Unterschied zwischen funktionalen und nicht-funktionalen Sicherheitsanforderungen? Geben Sie jeweils einige Beispiele.

     *   funktional: Als Funktion implementieren kann (HTTPS, Passwort muss mind. etc.)
     *   nicht-funktional: Qualitative Anforderungen ("man darf nur lesen, was erlaubt ist", alles was der Manager als sicher versteht)

12.  Welche Hilfsmittel / Dokumente können zu Identifizieren von Bedrohungen herangezogen werden?

     *   OWASP (Web)
     *   Common Criteria (sind nicht sehr konkret)
     *   Common Criteria wird oft ergänzt mit einem Schutzprofil, wo mögliche Implementierungen erläutert werden für eine bestimmte Anwendungen (BSI)

13.  Wo findet man wichtige Standardkataloge für mögliche Bedrohungen?

     *   Im Ilias und im Interwebs.
     *   OWASP
     *   Bestimmte Dinge, die … … … … eh bestimmte Dokument wie diese … … eh eben OWASP … steht auf den Folien

14.  Was versteht man unter einem Protection Profile (Schutzprofil)? Nennen sie zumindest zwei Beispiele für Schutzprofile.

15.  Was ist der spezielle Fokus der OWASP-Dokumente?

16.  Gibt es gesetzliche Vorschriften, die Security-Maßnahmen bei der Software-Entwicklung erfordern? Geben Sie zumindest 2 Beispiele.

17.  Was ist der Unterschied zwischen einem Threat (Bedrohung), einer Vulnerability
   (Schwachstelle) und einer Mitigation?

   *   Threat: Bedrohung, erfolgt an der Schwachstelle, kann mit einer Mitigation kann eliminiert werden
   *   Schwachstelle: 
   *   Mitigation: Gegenmassnahme

18.  Aus welchen Schritten besteht der Threat Modeling Prozess?

     >    Bedrohungsanalyse

     1.  Was muss ich schützen (Identify the Assets, ...)?
     2.  Systemarchitektur
     3.  Applikation grob unterteilen
     4.  Wo können Bedrohungen stattfinden (z.b. an Systemgrenzen)
     5.  Schwachstellen
     6.  Gegenmassnahmen

19.  Was sind Trust Boundaries?

     *   Dort wo zwei Vertrauensgrenzen aneinanderstossen
     *   Eigenes System vertraue ich, an der Grenze (z.b. zu einem anderen System) habe ich aber ein mögliches Problem

20.  Was sind die 6 Elemente der STRIDE Attack Classification?

     *   **S**poofing: Person oder System mit "gefälschter" Identität
     *   **T**ampering: Daten ändern (z.B. Kontonummer des Lieferanten ändern, im SAP Rechnungen ändern)
     *   **R**epudiation: Abstreitbarkeit (versuchen Möglichkeiten zu finden, abzustreiten, dass ich es nicht war, $\to$ Login des Mitarbeiters verwenden, elektronische Wahlen)
     *   **I**nformation disclosure
     *   **D**enial of service: Rechner überlasten
     *   **E**levation of privilege: Höhere Rechte aneignen

21.  Erklären Sie diese 6 Elemente einzeln.

22.  Führen Sie für jedes dieser 6 Elemente geeignete Mitigation Maßnahmen an.