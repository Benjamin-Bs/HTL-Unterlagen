#include <Arduino.h>

#define PIN 26

int count = 0;
int debounce = 50;
int oldTime = 0;
bool isCounted = false;
bool lastSwitchState = false;

void IRAM_ATTR isrhandler()
{
  if ((millis() - oldTime) >= debounce)
  {
    bool switchState = digitalRead(PIN);
    if (switchState != lastSwitchState) {
      lastSwitchState = switchState;
      if (switchState == HIGH) { // Schalter umgelegt
        count++;
        isCounted = true;
      }
    }
    oldTime = millis();
  }
}

void setup()
{
  pinMode(PIN, INPUT_PULLUP); // Aktiviert den internen Pull-up-Widerstand
  attachInterrupt(digitalPinToInterrupt(PIN), isrhandler, CHANGE);
  Serial.begin(9600);
}

void loop()
{
  if (isCounted)
  {
    isCounted = false;
    Serial.print("Count: ");
    Serial.println(count);
  }
  delay(1000);
}
