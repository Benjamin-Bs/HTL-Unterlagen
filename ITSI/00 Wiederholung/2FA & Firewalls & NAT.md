# Zwei-/Mehr-Faktor Authentifierung

Authentifizierung = Nachweis einer Identität



- "Something you know" - Passwort / PIN    => Erster Faktor

- "Something you have" - Smartphone / Hardware Token / Token List / OTP App

- "Something you are" - Fingerabdruck / Iris / Handvene

- "Somewhere you are" - IP Adresse / Netzwerk / GPS Standort / Land

- "Sometimes you are" - Zeitfenster
  
  

# Firewalls

Aufgaben : Zugriff auf Systeme/Netzwerke nur an Hand von festgelegten Regeln zulassen (Policies)

Hardware-Appliance / Software-Appliance

Appliance => Speziell gehärtetes Betriebssystem zur Erhöhung der Sicherheit



Platzierung : "Gateway" zu einem Netzwerk (Trennung zw. Internet und internem Netz/zw. Internen Netzen/zw. DMZ und internen Netzen)



![a06ee68c-16d3-4fa9-abe2-be6b94077dbd](file:///C:/Users/bsulj/Pictures/Typedown/a06ee68c-16d3-4fa9-abe2-be6b94077dbd.png)



Arten von Firewalls:

- State-less // Zustand wird nicht beachtet => Zustand das eine Verbindung nicht hat

- State-full // Zustand wird beachtet => Zustand das eine Verbindung hat => TCP
  
  - Die Firewall muss sich den State von der TCP Verbindung merken damit sie ein SYN ACK durchlässt

- Application-Level
  
  

OSI-Ebene:

- Layer 3 (IP)

- Layer 4 (TCP/UDP, Port) 

- Layer 7 (Application)
  
  

## State less

Paketfilter: Statische Filterung von Paketen aufgrund von Regeln

Operiert auf Layer 3 und 4 des OSI Modells

ACL: <Quelle - Host/Subnet/Port> <Ziel - Host/Subnet/Port> <Aktion>

Beispiele:

- Any Any 192.168.10.1/32 tcp/80,tcp/443 Allow

- 192.168.10.1/32 Any 192.168.20.2/32 tcp/3306 Allow

- Any Any Any Any Deny

## State full

Zusätzlich zum Paketfilter wird der jeweilige Kontext berücksichtigt

Zusätzlich zur **ACL** gibt es State Table

Operiert auch auf Layer 3 und 4 des OSI Modells

Ermöglicht aufgrund der State Table einen Schutz vor komplexeren Angriffen

=> Packetfilter + Tables



## Application Level

Analysiert auch höhere  Ebenen des OSI Modells

Layer 7 hat **http/https** als Protokolle

Beispiele:

- Webfilter (inkl. SSL Inspection)

- Erkennung von Protokollen auf untypischen Ports (SSH auf Port 443)
  
  

## NAT

NAT = Network Address Translation

Wurde ursprünglich entwickelt, um zu verhindern, dass zu wenige IPv4 Adressen verfügbar sind

Dient dem Verstecken von Ips/Netzweken hinter anderen Ips/Netzwerken



SRC NAT => Die SRC Adresse wird genated
