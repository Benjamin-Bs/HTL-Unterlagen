# Observer (Pattern)

Jedes Objekt hat einen Zustand, in dem es sich aktuell befindet. Bei Änderungen an diesem Zustand kann es vorkommen, dass es andere Objekte gibt, die von diesem einem Objekt abhängig sind und von solchen Zustandsänderungen benachrichtet werden möchten. Man bezeichnet diese abhängigen Objekte als Observer und das zu beochtende Objekt als Subjekt

Das gewünschte Verhalten des Observer Pattern kann man folgendermaßen erreichn:

- Man kann Observer bei einem Subjekt "anmelden"

- Jeder Observer hat eine Update-Methode, in der der Zustand aktulisiert wird

- Ändert sich der Zustand eines Subjekts werden die Observer benachrichtigt (englisch: to notify), indem deren Update-Methode aufgerufen wird




