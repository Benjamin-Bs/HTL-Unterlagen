

# Builder (Pattern)

[Java Builder Pattern: Build Complex Objects Efficiently](https://howtodoinjava.com/design-patterns/creational/builder-pattern-in-java/)

Builder Entwurfsmuster ist eine Möglichkeit Objekte zuerstellen. Es hilft bei der Erstellung unveränderlicher Objekte, die eine großeAnzahl von Eigenschaften aufweisen.

Wenn man von einem User Objekt ausgeht, dass 5 final Eigenschaften besitzt (firstName, lastName, age, phone and address), wovon nurfirstName und lastName verpflichtend sind, führt das zu einer hohen Anzahl von Konstruktoren(telescoping constructors problem).

Das Builder-Pattern bietet eine elegante Lösung, bei der die Unveränderlichkeit der Objekte erhalten bleibt.



```java
public static void main (String[] args){
    User user1 = new User.UserBuilder("Bart","Simpson")
    .age(13)
    .phone("1234567")
    .address("Springfield ?")
    .build();

    System.out.println(user1);

// new User2
    User user2 = new User.UserBuilder("James","Bond")
        .age(52)
        .phone("007")
        // no address
        .build();

    System.out.println(user2);


// new User3
    User user3 = new User.UserBuilder("Clark","Kent")
        // no age
        // no phone
        // no address
        .build();

    System.out.println(user3);
```



Die konkrete Implementierung, des **UserBuilder** findet sich im Projekt **BuilderPattern**
