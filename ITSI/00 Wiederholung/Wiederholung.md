# Wiederholung

## Hash Funktionen

- **Unidirektionale**, **determinstriche Funktionen** zur **Koprimierung** von Eingangsdaten belieber Länge auf Ausgangsdaten fixer Länger

- Beispiele:
  
  - MD5,SHA-1 (SHA = Secure Hash Algorithum)
  
  - SHA-2 (SHA-256, SHA-512)
  
  - SHA-3

- **Kollisionen**: Mehrere unterschiedliche Eingangsdaten liefern die selben Ausgangsdaten **(sollten auf keinen Fall eintreten)**

Unidirektional => es geht nur in eine Richtung

Determinstriche Funktionen => geben bei jedem Aufrufen dasselbe Ergebnis zurück, wenn sie mit einem bestimmten Satz von Eingabewerten aufgerufen werden (selber Imput => selber Output)

Koprimierung => Die Datei ist eigentlich größer  

Bei MD5 tretten mitlerweile Kollisionen auf -> nicht mehr sicher



- **Avalanche Effect** (Avalance = Lavine): "Minimale Änderung" der Eingangsdaten führt zu maximaler Änderung der Ausgangsdaten

- Anwendungsfälle:
  
  - Einfacher/Schneller Vergleich von Daten
  
  - Prüfwerte (Integrität von Daten feststellen)
    
    

Salting verhindert Kollisionen



## Verschlüsselung

- **Bidirektionale Funktion**, welche Eingangsdaten unter der Verwendung eines Schlüssels in Ausgangsdaten überführt (=Verschlüsselung)

- Mit Hilfe des Schlüssels können die Ausgangsdaten wieder in die Eingangsdaten überführt werden, ohne Schlüssel ist dies nicht möglich (= Entschlüsselung)

- Varianten:
  
  - Symmetrisch
  
  - Asymmetrisch
    
    

#### Symmetrisch

- Es wird der selbe Schlüssel für die Verschlüsselung und Entschlüsselung verwendet

- Vorteile:
  
  - Schnell
  
  - Einfachere Implemtierung

- Nachteile:
  
  - Wie Schlüssel austauschen?
  
  - Alle Beteiligten kennen Schlüssel (Authentizität der Nachricht?)
    
    

#### Asymmetrisch

- Es werden für Ver- und Entschlüsselung unterschiedliche Schlüssel eingesetzt (überlicherweise ist einer davon privat und der andere öffentlich)

- Vorteile:
  
  - Es gibt einen öffentlichen Schlüssel - Austausch sehr einfach
  
  - Authentizität von Nachrichten kann gewährleistet werden

- Nachteile:
  
  - Langsam
  
  - Komplexere Implemtierungen notwendig
    
    

#### Kombination

- Oft werden symmetrische und asymmetrische Verschlüsselung kombiniert, um die Vorteile aus beiden Welten nutzen zu können

- Beispiel:
  
  - TLS => Asymmetrische Verschlüsselung wird verwendet, um symmetrischen Schlüssel auszutauschen. Kommunikation wird dann mit symmetrischen Schlüssel verschlüsselt. Symmetrischer Schlüssel wird regelmäßig getauscht
    
    

## Phishing

- Betrugsmasche, bei der offizielle Emails/Websites nachgebaut werden um an sensible Informationen zu bekommen

- Wie kann Phishing erkannt werden?

- DAU = Dümmster Anzunehmenster User
