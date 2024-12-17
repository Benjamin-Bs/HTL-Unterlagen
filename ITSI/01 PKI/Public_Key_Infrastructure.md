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
    
    

![7ed27168-ebbf-410b-90e6-a703616583f8](file:///C:/Users/bsulj/Pictures/Typedown/7ed27168-ebbf-410b-90e6-a703616583f8.png)

Einmal signierte Zertifikate können nicht zurückgenommen warden - Lösung: CRL

CRL gibt Auskunft über gesperrte Zertifikate - Sollte vor dem akzeptieren eines Zertifikats überprüft werden



Weiterentwicklung: **OCSP** - ****Online Certificate Status Protocol****

Online Service, welcher über den Status eines Zertifikats Auskunft gibt



Weiterentwicklung: OCSP Stapling

Zertifikatstatus wird vorm Server in regelmäßigen Abständen bei der CA angefragt und dann bei Bedarf an den **TLS Handshake** angehängt

Die Antwort die von der OSCP geschickt wird ist verschlüsselt mit dem Private Key vom RootCA sodass man mit dem Public Key das entschlüsseln kann

Der Public Key steckt im Zertifikat drinnen 

Damit muss der Browser nicht immer nach dem OCSP Server fragen sondern nur der Webserver



### Typische Bestandteile eines Zertifikats

- Subject/ Common Name: Domain/Email - mittlerweile eher unwichtig

- Subject Alternative Name: Domains - sehr wichtig

- Validity: Not Before, Not After - sehr wichtig

- Issuer - informativ

- Serial Number - wichtig zur Überprüfung, ob Zertifikat gefälscht wurde
  
  

## Freie CA - Let's Encrypt

Freie / Gemeinnützige CA aus den USA

Aktiv seit 2014

Ziel: HTTPS Verbindung zum Standard machen

Gültigkeit der Zertifikate: 90 Tage

- Reduziert den Schaden bei Kompromittierung des Zertifikats / Keypairs

- Motiviert Anwender den Prozess der Zertifikatsaustellung zu automatisieren

Größte CA nach Anzahl Domains / ausgestellten Zertifikaten



### Protokoll zur Austellung von Zertifikaten: ACME

Aktuelle Version: v2

Mögliche Zertifikate:

- Domain Validated Certificates

- Domain Validated Wildcard Certificates

Beschreibt die Kommunikation zwischen den Servern der CA und den Servern der Andwender

- Basis: Austausch von JSON Nachrichten über HTTPS

- Basis sind so genannte Challanges:
  
  - HTTP-01 challenge
  
  - DNS-01 challenge
  
  - TLS-ALPN-01 challange
    
    

#### HTTP-01 challenge

Anfrage an Let's Encrypt ACME API

Let's Encrypt ACME API liefert einen Token zurück

Url muss via Port 80 erreichbar sein (Datei mit Token + Fingerprint von Account-Key):

```
http://<YOUR_DOMAIN>/.well-known/acme-challenge/<TOKEN>
```

Rückmeldung an Let's Encrypt API

Let's Encrypt überprüft die Verfügbarkeit von mehreren Standorten weltweit

Zertifikat wird ausgestellt

Pro: Einfach zu automatisieren /Ohne Zugriff auf DNS verwendbar

Contra: Keine Wildcard Zertifikate / Port 80 erforderlich / Schwieriger bei lastverteilten Webservern



#### DNS-01 challenge

Anfrage an Let's Encrypt ACME API

Let's Encrypt ACME API liefert einen Token zurück

TXT Eintrag für ``_acme-challenge.<YOUR_DOMAIN>`` mit dem Token als Wert muss angelegt werden

Rückmeldung an Let's Encrypt API

Let's Encrypt überprüft die Verfügbarkeit von mehreren Standorten weltweit 

Zertifikat wird ausgestellt

Pro: Ermöglicht Wildcard Zertifikate / Einfacher bei lastverteilten Webservern

Contra: Nur Sinnvoll, wenn DNS Anbieter eine API anbietet und Aktualisierungen schnell genug ausgerollt werden



Das wird alles mit Tools gemacht, der bekannteste ist CertBot (Python)



#### TLS-ALPN-01 challenge

Nachfolger der TLS-SNI-01 challenge

Operiert auf Port 443 im Zuge des TLS Handshakes

Aktuell nicht stark verbreitet

Pro: Kann verwendet werden, wenn Port 80 nicht verfügbar ist

Contra: Aktuell nicht mit Apache/Nginx/Certbot unterstützt / Keine Wildcard Zertifikate möglich



TLS operiert am Presentation Layer (Ebene 6)



# Certificate Transparency Logs

CAs können bzw. müssen Informationen zu ausgestellten Zertifikaten in CTL ablegen

CTLs warden von verschiedensten Anbietern bereitgestellt (Letsencrypt, Cloudflare, Google, ...)

Browser prüfen, ob Zertifikat in genügent "passed" CTLs hinterlegt sind (Certificate Transparency Policy)

- Google Chrome
  
  - Gültigkeitsdauer < 180 Tage: Zertifikat muss in min 2 CTL vorhanden sein
  
  - Gültigkeitsdauer > 180 Tage: Zertifikat muss in min 3 CTL vorhanden sein
    
    

# Qualys SSL Server/Client Test

https://www.ssllabs.com/ssltest/

Einfach Überprüfung der Konfiguration eines Webservers

SNI/HSTS/CAA



https://clienttest.sslabs.com:8843/ssltest/viewMyClient.html
