#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define LED_PIN 18

#define ANALOG_INPUT_PIN 34

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);


u_int8_t inputStatus = 0;

void setup()
{
  ledcSetup(0, 50, 8);
  ledcAttachPin(18, 0);

  pinMode(ANALOG_INPUT_PIN, ANALOG);
  analogReadResolution(8);

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.write("Hockn");
  display.display();
}

void loop()
{
  inputStatus = analogRead(ANALOG_INPUT_PIN);
  delay(20);

  float value = inputStatus / 255.0 * 100;

  ledcWrite(0, inputStatus);
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print(value);
  display.display();
}