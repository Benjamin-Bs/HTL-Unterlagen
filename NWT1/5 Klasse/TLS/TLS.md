# TLS

Man nimmt das TCP Protokoll



1. TCP Handshake

2. Certificate Check

3. Key Exchange



Client => Server :

TCP Handshake

---> SYN

<--- SYN,ACK

---> ACK



Server braucht ein Certifikate => Ist ein Public Key der Signiert wurde mit dem Privat Key



--> Client Hello;     client random, client version, CIPHERS

<-- Server Halo;    server random, chosen version, chosen cipher

<-- Certifikat

<-- Server Hello Done

--> Client Key Exchange ENC/RSA(Seed,Key_public)

--> Change Cypher Spec (Ab jetzt nimmt man das obere zum Kommunizieren)

--> Finished

<-- Change Cypher Spec

<-- Finished



--> Enc-RSA (HTTP_GET+HMAC(HTTP_GET, Key Client MAC), Key Client Data)

<-- Enc-AES (HTTP_RESP + HMAC (HTTP_RESP, Key Server MAC), Key Server Data)
