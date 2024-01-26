#include <Arduino.h>

#define ANALOG_INPUT_PIN 36

void setup() {
  Serial.begin(9600);
  pinMode(ANALOG_INPUT_PIN, ANALOG);
}

void loop() {
  
  Serial.println(analogRead(ANALOG_INPUT_PIN), DEC);  
  delay(100);
}
