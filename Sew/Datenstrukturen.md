# Datenstrukturen

Datenstrukturen werden benötigt, um Daten zu speichern, zu organisieren und zu verwalten. Sie ermöglichen die effizient Verarbeitung von Daten und sind grundlegend für die effektive Implementierung von Algorithmen (sortieren, suchen, ...)

Die wichtigsten Vertreter sind:

- List ( z.B. ArrayList, LinkedList, ...)

- Set (z.B.: HashSet, TreeSet, ...)

- Map (z.B.: HashMap)

- Queue

### List

Doppelte Objekte erlaubt, Reihenfolge bleibt erhalten, komfortable Alternative zu Arrays

```java
List<String> stringList = new ArrayList<>();
stringList.add("Tim");
```

### Set

Menge an Objekten, in der jeder Element nur einmal vorkommt

```java
Set<String> nameSet = new HashSet<>();
nameSet.add("Tim");
```

### Map

Helfen bei der Speicherung von Schlüssel-Wert-Paaren.

```java
Map<String, String> capitalCities = new HashMap<>();
// Add keys and values (Country, City)
capitalCities.put("England","London");
```

### Queue

Realisierung von **FIFO (First in First out)** und **LIFO (Last in First Out)** Speichern.


