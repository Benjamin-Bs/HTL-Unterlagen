#include <OneWire.h>
#include <DallasTemperature.h>
#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

WebServer myServer( 80 );

float brightness = 78; // Beispielwert für Helligkeit
float potenziometerValue = 0;

// Monitor Settings:
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

void handleInput() {
  myServer.send( 200, "text/html", "\
    <!DOCTYPE html>\
    <html lang=\"en\">\
    <head>\
        <meta charset=\"UTF-8\">\
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\
        <script src=\"https://code.jquery.com/jquery-3.6.4.min.js\"></script>\
        <title>Dynamic Brightness Update</title>\
    </head>\
    <body>\
    \
    <div id=\"brightnessContainer\">\
        <!-- Your existing HTML code here -->\
        <h1>Input</h1>\
          <p id=\"output\">loading</p>\
    </div>\
    \
    <script>\
        function updateBrightness() {\
            $.ajax({\
                url: '/value',\
                type: 'GET',\
                dataType: 'text',\
                success: function (data) {\
                    $('#output').text(\"Value: \"+data);\
                },\
                error: function (error) {\
                    console.error('Error fetching brightness:', error);\
                }\
            });\
        }\
    \
        updateBrightness();\
    \
        setInterval(updateBrightness, 300);\
    </script>\
    \
    </body>\
    </html>");
}

void handleValue() {
  myServer.send( 200, "text", String(brightness));
}

void WifiSetUp() {
  Serial.begin( 9600 );
  Serial.print( "Connecting to " );
  Serial.print( SSID );
  WiFi.begin( SSID, WIFI_PW );
  while ( ! WiFi.isConnected() ){
    Serial.print( "." );
    delay( 200 );
  }
  Serial.println( "OK" );
  Serial.print( "IP-Address: " );
  Serial.println( WiFi.localIP( ) );
  myServer.on( "/temperature.html", handleInput );
  myServer.on( "/value", handleValue );
  myServer.begin( );
}

void TemperatureToHTML() {
  sensors.requestTemperatures(); 
  float value = sensors.getTempCByIndex(0);
  brightness = value; // Aktualisiere die Helligkeit basierend auf dem Temperaturwert
  potenziometerValue = value;
}

void DisplayTemperatureOnOLED() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("Temperature:");
  display.println(brightness); // Zeige die Helligkeit (Temperaturwert) auf dem OLED an
  display.display();
}

void setup() {
  sensors.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  WifiSetUp();
}

void loop() {
  myServer.handleClient();
  TemperatureToHTML();
  DisplayTemperatureOnOLED();
  delay(20);
}
