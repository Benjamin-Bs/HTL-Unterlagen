#include <Arduino.h>

#define INPUT_PIN_1 17
#define INPUT_PIN_2 16
#define LED_PIN_1 18
#define LED_PIN_2 17

void setup() {
  // put your setup code here, to run once:
   pinMode(LED_PIN_1, OUTPUT);
    pinMode(LED_PIN_2, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN_1,LOW);
  digitalWrite(LED_PIN_2, LOW);
  delay(100);
  digitalWrite(LED_PIN_1, HIGH);
  digitalWrite(LED_PIN_2, HIGH);
  delay(100);
}

