Aufgabe crypto reversing:

Gegeben ist ein Katzenbild in einem raw image format.
So kann das Katzenbild angezeigt werden:
```
python3 display_raw.py cat.raw
```
Dazu müssen die fehldenen python libraries installiert werden (z.B. mit pip).

Dieses Katzenbild wurde verschlüsselt.
Das verschlüsselte Katzenbild kann so angezeigt werden:
```
python3 display_enc.py cat.enc
```

Das verschlüsselte Katzenbild kann so erzeugt werden:
```
python3 myaes_file.py cat.raw > cat.enc.2
```

Das Katzenbild dient nur der Illustration!

Als eigentliche Aufgabe muss ein Symmetrischer Krypto-Algorithmus
reversed werden, der nur im source code vorliegt um eine
geheime Datei out.enc, die nur im verschlüsselter Form vorliegt zu
entschlüsseln und so das Flag zu finden.

Das ver- und entschlüsseln könnt ihr mit dem Katzenbild testen.

Folgende Fragen müssen beatwortet werden:
* beschreibe das File format .raw

  * Das RAW-Dateiformat (*.raw) speichert die unkomprimierten Sensordaten einer Digitalkamera und bietet maximale Flexibilität und Detailgenauigkeit in der Nachbearbeitung.
  
* beschreibe das File format .enc

  * Die Dateierweiterung *.enc kennzeichnet generische verschlüsselte Dateien, deren Inhalt zum Schutz vor unbefugtem Zugriff codiert wurde.
  
* handelt es sich um einen symmetrischen oder asymmetrischen Algorithmus?

  * symmetrische

* Wieviele byte im .raw file entsprechen viewielen byte im .enc file?
  * 
* In welchen Variablennamen ist der Schlüssel enthalten?
  * 
* Welcher Mode wird verwendet? ECB, CBC, WTF?
  * 
* Schreibe ein Program myaes_undo_file.py das die verschlüsselten Files entschlüsselt!

Hilfestellungen:

XOR (^) Gleichungen umstellen:
```
x ^ x = 0
x ^ 0 = x

x = a ^ b  | ^ x
0 = a ^ b ^ x | ^ b
b = a ^ x
```

32 bit integer arithmetik modulo 2^32:
```
x = a + b | -b
(x - b + 0x100000000)&0xFFFFFFFF = a
^^
this is to get a positive number modulo 2^32
```

Folgende Fragen sind optionale Bonusfragen, und müssen nicht beantwortet werden (schwierig):
* der Algorithmus wurde fälschicherweise mit AES bezeichnet, in Wirklichkeit ist es nicht AES. Um welchen Algorithmus handelt es sich?

