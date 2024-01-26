#include <WiFi.h>

const char* ssid = "HTLIoT";
const char* password = "hollabrunn";
const char* host = "192.168.1.100"; // Change this to the IP address of your ESP32 server

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Make a GET request to fetch the brightness value
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;

    if (client.connect(host, 80)) {
      Serial.println("Connected to server");

      client.print("GET /value HTTP/1.1\r\n");
      client.print("Host: ");
      client.print(host);
      client.print("\r\n");
      client.print("Connection: close\r\n\r\n");

      while (client.connected() || client.available()) {
        if (client.available()) {
          char c = client.read();
          Serial.print(c);
        }
      }

      Serial.println("Request sent");
      client.stop();
    } else {
      Serial.println("Connection to server failed");
    }

    delay(5000); // Wait for 5 seconds before making the next request
  }
}