# VRSget
VRSget ist eine kleine python library mit der man z.B Informationen von VRS-monitoren abrufen kann. (Bis jetzt kann man wirklich nur das, aber es wird bald ein update geben)
VRS steht für Verkehrsverbund-Rhein-Sieg.

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
**Da ich ascheinend zu dumm bin das bei PyPI einzutragen, musst du das herunterladen oder mit git klonen und dann im Ornder ein Skript damit erstellen.**
Du kannst es per pip zu installlieren: `pip install VRSget` 
(Ich bin mir nicht sicher ob das funktioniert, weil ich nicht weiß ob es jetzt geuploaded ist oder nicht)

Mit git klonen: `git clone https://github.com/Antonabi/VRSget.git`
Zum herunterladen der Dateien, musst du einfach auf `Code` klicken dann ist da schon direkt der Button `download ZIP` zu sehen. Darauf kennst du dann eifach klicken und, wenn es fertig heruntergeladen ist kannst du es einfach entpacken.

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

***Denke daran, dass Monitore gelöscht werden wenn sie ein halbes Jahr nicht mehr abgerufen werden.***
***Denke auch daran, dass jeder der die ID deines Monitors hat ihn beliebig verändern kann.***
