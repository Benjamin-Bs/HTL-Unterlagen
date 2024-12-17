# AAA / Radius

## AAA - Triple A

- Authentication

- Authorization

- Accounting
  
  

Framework zur Steuerung Protokollierung von Zugriffen in Netwerken



### Authentication (Wer bin ich)

Nachweis einer Identität (z.B. Benutzername & Passwort)

Wichtig:

- Übertragung der Authentifizierungsdaten nur verschlüsselt

- Wenn verschlüsselte Übertragung nicht möglich, kann ein CR-Verfahren angewendet werden

- Wenn möglich/sinnvoll: TFA/MFA

CR-Verfahren anhand eines Beispiels: Alice möchte sich bei Bob authentifizieren:

- Bob schickt ein Nonce und die zu verwendende Hash-Funktion an Alice
  
  - Nonce: 2389d92n9, Hash-Funktion: SHA256

- Alice bildet die Hash-Funktion von ihrem Password und dem Nonce
  
  - SHA256 (<Password><Nonce>)

- Alice schickt das Ergebnis der Hash-Funktion an Bob. Bob berechnet die selbe Hash-Funktion und vergleicht es mit der Antwort von Alice

Probleme mit CR-Verfahren:

- Replay - Attacken
  
  - Mögliche Lösung: Zusätzlich wird zum Nonce der aktuelle Zeitpunkt an das Passwort angefügt und davon die Hash-Funktion gebildet
  
  - Der verwendete Zeitpunkt muss auch an Bob übertragen warden. Bob akzeptiert die Antwort nur, wenn der verwendete Zeitpunkt in einem kleinen Zeitfenster ist (z.B. 60 Sekunden)

- Wörterbuch - Attacken
  
  - Da das Nonce unverschlüsselt übertragen wird, kann ein Angreifer das Passwort von Alice erraten und die Hash-Funktion bilden und sich damit authentifizieren

- Passwort bei Bob als (Salted- ) Hash gespeichert
  
  - Entweder Bob speichert das Passwort in Plain-Text (No No No), oder Alice muss den selben (salted) Passwort-Hash, wie Bob berechnen, um die Response berechnen zu können
    
    

### Authorization (Was darf ich)

Erteilen einer Berechtigung

- Richtlinien legen fest welche Identitäten welche Art von Zugriff auf eine Ressource haben
  
  - z.B. Benutzer in der Gruppe "Schüler" haben lesenden Zugriff aud den Ordner "Unterlagen", aber schreibenden Zugriff auf den Ordner "Notzien"

"Principle of least privilege"

- Einer Identität sollte immer nur jener Zugriff gewährt werden, welcher zur Erfüllung einer Aufgabe notwendig ist
  
  - z.B. Nur MitarbeiterInnen der Personalabteilung haben Zugriff auf die Stammdaten der MitarbeiterInnen
    
    

### Accounting (Was mach ich)

Protokollierung von Änderungen - Audit Log

Beispiele:

- Alice hat sich in das WLAN verbunden (Zeitpunkt, SSID, MAC von Alice, ID des Accesspoint, zugewiesenes VLAN, ...)

- Alice ist (noch immer) in das Wlan verbunden

- Alice hat sich von dem WLAN getrennt

- Alice Sim-Karte hat sich von einem Sender zu einem anderen verbunden

Notwenig, um

- im Nachhinein Prozesse nachvollziehen zu können

- eine Verrechnung der verwendeten Dienste machen zu können
  
  

## AAA - Protokolle

TACACS+ / Terminal Access Controller Acces-Control System Plus

- Cisco Protokoll

- Verbindungsorientiert (TCP)

- Gesamte Kommunikation verschlüsselt

RADIUS

- Am meisten verbreitetes AAA Protokoll

- Verbindungslos (UDP) - typischerweise

- Nur Passwörter werden gehasht übertragen, Rest in plan text - Typischerweise

DIAMETER

- Weiterentwicklung von RADIUS

- Verbindungsorientiert (TCP)

- Transport-Verschlüsselung über IPSEC oder TLS
  
  

# RADIUS

Remote Authentication Dial-In User Service

AAA Protokoll zur zentralen Verwaltung von Benutzern mit Zugriff auf
Netzwerk Dienste

Einfaches Client/Server Protokoll

- Client: NAS – Network Access Server (z.B. Accesspoint, Switch, …)

- Server: RADIUS Server Instanz

Zwei Arten:

- AA – Authentication and Authorization

- A - Accounting

## Authentication and Authorization

Benutzer möchte Zugriff auf einen Netzwerk-Dienst erhalten

Benutzer übermittelt Zugangsdaten
(Benutzername/Passwort/Zertifikat) an NAS (= RADIUS Client)

NAS sendet eine “Access Request” Nachricht an den RADIUS Server

- Inhalt der Nachricht sind neben den Zugangsdaten noch weitere Attribute die dem NAS bekannt sind (z.B. MAC, …)

- Server antwortet mit einer von drei Antworten:
  
  - Access Reject: Zugriff verweigert (z.B. Passwort falsch, deaktivierter Benutzer, …)
  
  - Access Challenge: Weiterer Faktor notwendig
  
  - Access Accept: Zugriff erlaubt und Berechtigung erteilt
    
    - Weiterer Antwort-Parameter: VLAN-ID, IP-Adresse, QoS-Parameter, Session Lifetime, …

## Accounting

Accounting kann an den RADIUS Server oder einen weiteren Server
gesendet werden

Accounting ist optional und dient hauptsächlich der korrekten
Verrechnung bzw. der Erstellung von Statistiken

Nach AA, sendet der NAS eine “Accounting Start” Nachricht

In regelmäßigen Intervallen sendet der NAS “Interim Update”
Nachrichten, so lange der Benutzer den Netzwerk-Dienst verwendet    

Nach der Trennung des Benutzers vom Betzwerk-Dienst, wird eine
“Accounting Stop” Nachricht gesendet

## Roaming

Benutzer könen sich auf Netzwerk - Diensten von verbundenen Instiution anmelden

- eduroam

- Weltweit vernetzte Institutionen aus dem Forschungsbereich erlauben den Zugriff auf z.B. das lokale WLAN mit den Zugangsdaten der eigenen Institution

- Zuordnung auf Basis von REALMs – dadurch werden die Nachrichten an den “Heimat-RADIUS-Server” gesendet

# SSO - Single Sign-On

Szenario:

- Benutzer müssen mehrere Services verwenden

- Services erfordern, dass sich ein Benutzer authentifiziert

Problem: 

- Benutzer verwenden bei allen/vielen Services das gleiche (einfache) Passwort

- Benutzer müssen sich regelmäßig bei allen Services anmelden (kostet in Summe viel Zeit und ist für Benutzer mühsam)

![cb864a5f-f99d-4854-9a22-f205ac6da0b2](file:///C:/Users/bsulj/Pictures/Typedown/cb864a5f-f99d-4854-9a22-f205ac6da0b2.png)

Lösung: Single Sign-On

Benutzer melden sihc nur bei einemAuthentifiuierungsservice an

Die Anmeldung bei den einzelnen Services wird über den Authentifizierungsservice geleitet

Der Authentifizierungsservice führt auch die Autorisierung durch und führt den Sign-On nur auf berechtigte Services durch



Vorteile:

- Authentifizierung muss nur einmal durchgeführt werden

- MFA kann an einem zentralen Platz eingerichtet und verwaltet werden

- Autorisierung kann an einem zentralen Platz durchgeführt werden

Nachteile:

- Zugriff auf eine Session am Authentifizierungsserver ermöglicht Zugriff auf
  alle berechtigten Services

- Single Sign Off üblicherweise nicht implementiert --> Timeout meldet
  Benutzer bei einzelnen Services ab

## SAML

**SAML** = Security Assertion Markup Language

XML basiertes Framework zum Austausch von "Assertions"

Involvierte Rollen:

- Principal (Benutzer)

- Identity Provider (Idp) => Authentifizierungsservice

- Service Provider (SP) => Service



Typischer SAML Sign-On

- 1-7: SP-initiated SSO

- 3-7: IdP-Initiated SSO



SAML AuthnRequest:

- Wird Base64 enkodiert im GET Parameter SAMLRequest übertragen

- https://idp.example.org/SAML2/SSO/Redirect?SAMLRequest=PH ……. VzdD4=

SAML Response:

- Wird Base64 enkodiert im POST Parameter SAMLResponse an den SP
  übertragen



## OIDC

**OIDC** = OpenID Connect

Involierte Rollen:

- User

- Identity Provider (IdP) => Authentifizierungsservice

- Replying Party => Service



Claims:

- Können von der RP angegeben werden

- z.B. name, given_name, email...

- Müssen vom Benutzer freigegeben werden (Consent)

- Können mit dem Acces Token vom Userinfo Endpoint abgefragt werden
