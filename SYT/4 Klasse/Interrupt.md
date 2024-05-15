# Interrupt

## Polling (Abfragemethode)

**Polling** ist in der Informatik der Ausdruck für eine zyklische Abfrage, die den Status von Hard- oder Software oder das Ereignis einer Wertänderung ermittelt.



```c++
while(1){
    #Befehl 1
    #Befehl 2
    #...
    digitalRead()

    #Befehl n
}
```



#### Polling (Abfragemethode):

Vorteile:

- einfach

Nachteil:

- Ressourcenverbrauch (CPU)

- hohe latenzeit
  
  

#### Interrupt Methode (Unterbrechung):

Wenn der Fall eintrieft dann wird die Interrupt Methode ausgeführt und ein anderen Codeabschnitt wird ausgeführt und wenn das vorbei geht es zurück zur Hauptfunktion

### Wichtige Befehle:

```c++
attachInterrupt(digitalPintoInterrupt(Pin), isrhandler, mode) 
# 1. Pin der genutzt wird
# 2. ISR-Handler
# 3. CHANGE (Reagiert auf steigend und fallende Flanken), RISING, FALLING
```

```c++
void IRAM_ATTr isrhandler(){    // IRAM_ATTr wo im Speicher es abgelegt wird
    count++;
}
```



#### Prellen:

Als Prellen wird ein mechanisch ausgelöster Störeffekt bei elektromechanischen Schaltern und Tastern bezeichnet: 

Statt des sofortigen elektrischen Kontaktes ruft die Betätigung des Schalters kurzzeitig ein mehrfaches Schließen und Öffnen des Kontakts hervor.

Entprellzeit (engl. Debounce ~ 20 - 50ms)

 

```c++

void IRAM_ATTr isrhandler(){    // IRAM_ATTr wo im Speicher es abgelegt wird
    
    if((millis - alteZeit)> debounceZeit){
        count++;
        alteZeit = millis();
    }
}
```


