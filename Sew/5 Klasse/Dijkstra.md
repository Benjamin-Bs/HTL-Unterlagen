# Graphen kürzester Pfad Dijkstra

Ein kürzester Pfad ist ein Pfad zwischen zwei unterschiedlichen Knoten eines Graphen, der die minimale Länge bezüglich der Kantengewichtsfunktion hat. Der Algorithmus von Dijkstra löst  das Problem der kürzesten Pfade in dem er einen kürzesten Pfad zwischen dem gegebenen Startknoten und einem anderen Knoten in einem Kantengewichteten Graphen berechnet



## Pseudocode:

```java
 funktion Dijkstra (V,E,start)    // Knoten, Kanten, Startknoten
     Für alle v inElement V
         Wenn v == start
              distanz[v]:= 0        // Abstand zum Startknoten
         anderenfalls 
              distanz[v]:= unendlich
         vorgänger[v]:= null
         Q.einfügen(v)                // Menge der zu bearbeitenden Knoten
     Solange Q nicht leer ist
         u:= kleinstes aus Q        // Knoten mit geringster Distanz
         Q.entferne(u)
         Für alle (u,v) inElement E mit v inElement Q
             Wenn distanz[u] + gewicht(u,v) < distanz [v]        // Neue min. Distanz ?
                 distanz[v]:= distanz[u] + gewicht(u,v)          // Ja, aktualisieren
                 vorgänger[v]:= u               // Distanz und Vorgänger     
```



### Bemerkung:

Pseudocode ist eine detailierte und dennoch lesbare Beschreibung dessen was ein Computer Programm oder ein Algorithmus machen soll. Pseudocode wird in einer formal gestalteten natürlichen Sprache und nicht in einer Programmiersprache ausgedrückt

https://www.algorithmen.lernen.de/dijkstra


