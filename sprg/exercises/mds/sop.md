# Same Origin Policy



## SOP

> Same Origin Policy

- Sicherheitskonzept, welches clientseitigen Skriptsprachen wie JavaScript untersagt, auf Objekte - insbesondere Skripte - zuzugreifen, die von einer anderen Origin stammen
- Origin ist definiert als eine Kombination aus URI-Schema, Hostname und Portnummer
- wesentliches Sicherheitselement in allen modernen Browsern und Webanwendungen



## Wann haben zwei Seiten dieselbe Origin?

- wenn URI-Schema (Protokoll), Host und Port für beide Seiten identisch sind
- Schema/Host/Port-Tupel



## Exkurs IE

- (IE) hat zwei grosse Ausnahmen, wenn es um die gleiche Origin geht
- Trust Zones: Wenn sich beide Domains in einer sehr vertrauenswürdigen Zone befinden, z.B. Firmendomains, dann werden nicht die gleichen Origin-Beschränkungen angewendet.
- Port: IE berücksichtigt die Komponente Port nicht, daher werden http://sop.hslu.ch:81/index.html und http://sop.hslu.ch/index.html von der gleichen Origin betrachtet und es werden keine Einschränkungen angewendet
- nicht standardisiert und werden in keinem anderen Browser unterstützt



## Cookie eines iFrames auslesen

- `document.getElementById("[ID des iFrames]").contentWindow.document.cookie`
- Geht oft nicht wegen SOP



## Welche Möglichkeiten gibt es SOPs zu umgehen (Javascript)?

- JavaScript von einer 3rd Party Seite darf auf das Cookie zugreifen, wenn dieses per `<script src="">` eingebunden wird (z.B. CDNs)
- Gefährlich, da man die Kontrolle und Autorität über die eigene Domain verliert



## Welche Lösungen gibt es um trotzdem JS einbinden zu können?

- Cross-Origin Ressource Sharing (CORS)