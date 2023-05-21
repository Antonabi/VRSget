# VRSget
VRSget ist eine kleine python library mit der man z.B Informationen von VRS-monitoren abrufen kann. (Bis jetzt kann man wirklich nur das, aber es wird bald ein update geben)

# Verwendung
Bis jetzt gibt es diese funktionen:

1. Alle events eines monitors bekommen:
```
import vrsget
events = vrsget.getEventsOfMonior("monitorID") #gibt alle events als liste aus. (Die events sind dicts)
```
2. Alle Informationen über Bus/Bahnlinie ***von allen*** events abrufen:
```
import vrsget
lines = vrsget.getLinesOfMonitor("monitorID") #gibt Informationen über jede Bus/Bahnlinie auf dem monitor als liste aus.
```

# Installation
Leider kann ich das noch nicht beim PyPI (Python Package Index) einreichen, weil es ja momentan einen Registrierungs und Veröffentlichblock gibt.
Deswegen musst du den ordner herunterladen und darin ein neues Skript erstellen worin du dann erst die funktionen verwenden kannst.
Leider geht es nicht anders.

**Du musst folgendes installiert haben:** requests
