#include <Arduino.h>

#define SWITCH_ON 18
#define SWITCH_BLINK 19
#define LED_PIN 25

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(SWITCH_ON, INPUT_PULLUP);
  pinMode(SWITCH_BLINK, INPUT_PULLUP);
}

void loop() {

  boolean on = digitalRead(SWITCH_ON);
  boolean blinki = digitalRead(SWITCH_BLINK);

  if (on == LOW){
    if (blinki == LOW){
      Serial.print("Gleich kommt ein digitalWrite");
      digitalWrite(LED_PIN,LOW); 
      delay(100);
      
    }
    
    digitalWrite(LED_PIN,HIGH);
    delay(100);

  }else{
    digitalWrite(LED_PIN, LOW);
  }
  
}

