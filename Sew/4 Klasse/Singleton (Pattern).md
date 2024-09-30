# Singleton (Pattern)

Das Entwurfsmuster "Singleton" stellt sicher, dass von einer Klasse genau ein Objekt existiert.

#### Implementierung:

```java
public class MySingleton{
    private static mySingleton instance;

    private MySingleton(){
    }

    public static synchronized MySingleton getInstance(){
        if (instance == null){
            instance = new MySingleton();
        }    
        return instance;
    }    
    // Other methods ...
    public int getValue(){
        return ...;
    }
}
```

Das Schlusselwort "synchronized" stellt sicher, dass der Singleton nur 1x instanziiert wird (Thread sicher).

#### Zugriff aus anderer Klasse:

```java
MySingleton mySingleton = MySingleton.getInstance();
oder:
int wert = MySingleton.getInstance().getValue();
```

#### Alternative Impleentierung mittels enum:

```java
public enum MySingleton{
    INSTANCE;
    public MySingleton getInstance(){
        return INSTANCE;
    }
    // Other methods ...
    public int getValue(){
        // ...
    }
}
```

#### Anwendungsbeispiele:

z.B.:

Zugriff auf zentrale Logging-Funktionalität in eine Datei

#### Vorsicht:

Eine Singleton Implementierung sollte sehr sparsam eingesetzt werden, da die Gefahr besteht, quasi eine Äquivalent zu globalen Variablen zu schaffen. Die Testbarkeit wird darüber hinaus sehr erschwert.


