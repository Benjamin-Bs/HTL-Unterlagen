# UDP

UDP sendet **Datagramme**

Datagramme => abgeschlossene Dateneinheit

Was kann bei UDP nicht garentiert werden?
Etweder das Paket kommt an oder nicht



## UDP vs. TCP

Ist beides im Betriebssystem Porgrammiert und das was man benutzt sind Sockets

![Differences between TCP and UDP - GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20230406112559/TCP-3.png)

TCP ist nähmlich nur Stream => Streaming interface

TCP ist ein Datenstrom

Bei TCP kann nichts verloren gehen (sehr stabil) und bei UDP können Daten verloren gehen



Wie entscheidet man sich?

Mann muss sich die Fragen stellen: **Ist es in Ordnung Daten zu verlieren oder nicht**

Mit TCP eine höhere Datenrate



Es definiert einen Paket Formater um die Pakete zu übersetzten



### Nutztung von UDP

- Auto (Geschwindigkeitssignale)

- Streaming (Netflix)

- ...
  
  

### UDP Header

- Längenfeld (16 bit)

- Source Port (16 bit) & Destination Port (16 bit)

- Checksumme (16 bit)
  
  

Jedes Betriebssystem unterstütz **IP-Fregmentation**


