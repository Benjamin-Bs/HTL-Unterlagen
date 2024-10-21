# PKI - Public Key Infrastructure

## Einführung

Asymmetrische Verschlüsselung: Public Key / Private Key

Probleme: Wie bekommt Kommunikationspartner B den Public Key des Kommunikationspartner A?

![4a07766e-259f-4aaf-8fed-9a704058b7e7](file:///C:/Users/bsulj/Pictures/Typedown/4a07766e-259f-4aaf-8fed-9a704058b7e7.png)



Lösung: Zertifikate

Zertifikat : Digitaler Datensatz, mit dessen Hilfe bestimmte Eigenschaften bzw. Identitäten nachgewissen werden können



PKI (Public-Key Infrastructure): Struktur zur Austellung, Verteilung und Prüfung von digitalen Zertifikaten

Zwei gängige Varianten:

- OpenPGP - Web of Trust

- X.509 - Hirarchische Zertifizierungstellen

## OpenPGP - Web of Trust

Netz an Teilnehmern

Teilnehmer erstellen Zertifikate selbst

Teilnehmer teilen Zertifikate mit anderen Teilnehmern (z.B. Keyserver, Email, USB Stick, Messenger, ...)

Zertifikate werden von anderen Teilnehmern signiert

Teilnehmer können selbst entscheiden, welchen Zertifikaten Sie vertrauen:

- Mindestens X andere haben das Zertifikat signiert

- Bestimmte andere Personen haben das Zertifikat signiert
  
  

## X.509 - Hierarchische Zertizierungsstellen

Streng hierarchisch aufgebaut - an der Spitze steht die Root-CA

Unterschied zu "Web of Trust": Nur eine CA signiert Zertifikate - nicht jeder

Root-CA kann auch Sub-CAs ermöglichen - diese können dann auch Zertifikate signieren, welchen jeder vertraut der  der Root-CA vertraut



- Root CA
  
  - Private Key (**stark geschützt - offline only**)
  
  - Public Key und Zertifikat (wird von gängigen OS/Browser vertraut)

- Sub CA 1/2
  
  - Private Key (stark geschützt - offline only)
  
  - Public Key und Zertifikate (Optional: wird von gängigen OS/Browsern vertraut), wird von Root CA signiert

- Intermediate Certificate
  
  - Private Key: wird für Signierung von Zertifikaten genutzt
  
  - Public Key und Zertifikat

- Zertifakat
  
  - Private Key: Sollte von Administrator erzeugtwerden (nicht von der CA)
  
  - Public Key und Zertifikat (wird von Intermediate Public Key signiert)
  
  - Damit Client dem Zertifikat vertraut, muss mit Zertifikat auch das Intermediate (und optional das Sub CA) Certificate ausgeliefert werden



Einmal signierte Zertifikate können nicht zurückgenommen warden - Lösung: CRL

CRL gibt Auskunft über gesperrte Zertifikate - Sollte vor dem akzeptieren eines Zertifikats überprüft werden



Weiterentwicklung: OCSP

Online Service, welcher über den Status eines Zertifikats Auskunft gibt



Weiterentwicklung: OCSP Stapling

Zertifikatstatus wird vorm Server in regelmäßigen Abständen bei der CA angefragt und dann bei Bedarf an den TLS Handshake angehängt
