# Certifiacte

Key of trust

#### Certificate beinhaltet:

- Isseur (Person die es Unterschrieben hat)

- Gültigkeitsdauer

- key usag
  
  - digital signate **certificate signing**

- public key

Certificade Signing Request:

- public key // wichtiges Teil

Das wird dann zur CA gesendet



Die Dateiendung ist **.pem**





#### openssl

.crl = certificate revrcation lut (????)

openssl kann was anfangen mit .cnt

- instead of CLI parameter



#### openssl Befehle

**openssl genrsa -out my.key 2048**   =>     generieren eines private Keys

**openssl req -new -out my.csr -key my.key -subj ""**    =>    certificate signing request erstellen

subject kann enthalten:

- /C = AT

- /O = HTL Hollabrunn

- /CN = Ebermann

**openssl x509 -req -in my.csr -out my.pem -CA CA.pem -CAkey CA.key**     =>     die CA nutzt den Befehl um aus der csr Datei eine pem Datei zu machen



#### Zertifikat aufbau:

1. Issuer

2. Subject

3. Gültigkeitsdauer

4. Key Usage

5. public key

Und das alle wird dann **Signiert**







openssl s_client -connect flagsdistribution.challs.open.scsc2024.it:38000 -cert my.pem -key my.key -CAfile rootCACert.pem (-no_tls1_3   -noservername) die letzten beiden Parameter werden normalerweise nicht angegeben
