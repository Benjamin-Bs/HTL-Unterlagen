#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

WebServer myServer( 80 );

#define LED_PIN 18
#define ANALOG_INPUT_PIN 34

Adafruit_SSD1306 display(128, 64, &Wire, -1);

int brightness = 78;
String HtmlOutput = "";
int HtmlInput = 0;

void handleInput( ) {
  int value = myServer.arg("inputField").toInt();
  if ( value != NULL ) {
    HtmlInput = value;
  }

  myServer.send( 200, "text/html", "\
    <h1>Input</h1>\
    <form action=\"/input.html\" method=\"POST\">\
    <input type=\"text\" name=\"inputField\"><br>\
    <input type=\"submit\" value=\"submit\">\
    </form>");
}
void handleOutput( ) {
  String answer = "<h1>Output</h1> ";
  answer += HtmlOutput;
  myServer.send( 200, "text/html", answer );
}

void WifiSetUp() {
  Serial.begin( 9600 );
  Serial.print( "Connecting to " );
  Serial.print( SSID );
  WiFi.mode( WIFI_STA );
  WiFi.begin( SSID, WIFI_PW );
  delay( 1000 );
  WiFi.disconnect( );
  delay( 1000 );
  WiFi.begin( SSID, WIFI_PW );
  while ( ! WiFi.isConnected() ){
    Serial.print( "." );
    delay( 200 );
  }
  Serial.println( "OK" );
  Serial.print( "IP-Address: " );
  Serial.println( WiFi.localIP( ) );
  myServer.on( "/input.html", handleInput );
  myServer.on( "/output.html", handleOutput );
  myServer.begin( );
}
void DisplaySetup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.write("Starting Up");
  display.setTextSize(3);
  display.display();
}
void LedSetup() {
   ledcSetup(0, 50, 8);
  ledcAttachPin(LED_PIN, 0);
}
void PotenziomterSetup() {
 

  pinMode(ANALOG_INPUT_PIN, ANALOG);
  analogReadResolution(8);
}

void setup() {
  WifiSetUp();
  DisplaySetup();
  LedSetup();
  PotenziomterSetup();
}

void PotenziometerToHTML() {
  float value = (analogRead(ANALOG_INPUT_PIN) * 100 / 255);
  HtmlOutput = "<p>" + String(value) + "%</p>";
}

void HTMLToDisplay() {
  float value = HtmlInput / 100 * 255.0;

  ledcWrite(0, value);
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print(HtmlInput);
  display.display();
}

void loop() {
  myServer.handleClient( );
  PotenziometerToHTML();
  HTMLToDisplay();
  delay(20);
}