# VRSget
VRSget ist eine kleine python library mit der man z.B Informationen von VRS-monitoren abrufen kann. (Bis jetzt kann man wirklich nur das, aber es wird bald ein update geben)


# Verwendung
Bis jetzt gibt es diese funktionen:

1. Alle events eines monitors abrufen:
```python
import vrsget

events = vrsget.getEventsOfMonior("monitorID") #gibt alle events in einer liste aus. (Die events sind dicts)
```

2. Informationen ***von allen*** events abrufen:
```python
import vrsget

lines = vrsget.getLinesOfMonitor("monitorID") #gibt Informationen über jede Bus/Bahnlinie auf dem monitor als liste aus.
stopPoints = vrsget.getStopPointsOfMonitor("monitorID") #gibt Informationen über jeden/s Busteig/Bahngleis auf dem monitor als liste aus.
departures = vrsget.getDeparturesOfMonitor("monitorID") #gibt Informationen jede Ankuftszeit auf dem monitor als liste aus.
```

3. Informationen von einem (oder mehreren) event/s abrufen die der user übergibt: (das event **muss** ein `dict` sein
```python
import vrsget

lines = vrsget.getLinesOfInput("Liste von events oder ein event") #gibt Informationen über die Bus/Bahnlinie in dem event oder den events aus.
lines = vrsget.getStopPointsOfInput("Liste von events oder ein event") #gibt Informationen über die Busteige/Bahngleise in dem event oder den events aus.
lines = vrsget.getDeparturesOfInput("Liste von events oder ein event") #gibt Informationen über die Ankunftszeit in dem event oder den events aus.
```

# Installation
Leider kann ich das noch nicht beim PyPI (Python Package Index) einreichen, weil es ja momentan eine Registrierungs und Veröffentlichblockade gibt.
Deswegen musst du das Skript herunterladen und im gleichen ordner ein neues Skript erstellen worin du dann erst die funktionen verwenden kannst.
Leider geht es nicht anders.

**Du musst folgendes installiert haben:** `requests`

# Fragen
***Fallst du nicht weißt was ein VRS-monitor ist:***

> Ein VRS-monitor ist ein eigens konfigurierter abfahrtplan. Du kannst ihn [hier](https://www.vrs.de/am/admin "VRS-monitor Adminseite") erstellen.
Wenn du ihn dir zurechtkonfiguriert hast klicke auf `Zum Abfahrtsmonitor wechseln`.
Das ist dein VRS-monitor!

***Fallst du nicht weißt wie du an die ID deines Monitors kommst:***

> Der link zu deinem monitor müsste jetzt ungefähr so aussehen: `https://www.vrs.de/am/s/5b7344b942408df59f7bf681ff96780e`.
Die ID ist das was nach dem `https://www.vrs.de/am/s/` kommt, meine ID ist somit `5b7344b942408df59f7bf681ff96780e`.

Also:

| anderes URL zeugs        | ID          |
| ------------- |:-------------:|
| https://www.vrs.de/am/s/   | 5b7344b942408df59f7bf681ff96780e |

[![VRSlink](https://assets.static-bahn.de/dam/jcr:19280166-a739-4d8d-b896-305135ec0ae9/117045-138812.png)](https://vrs.de)
