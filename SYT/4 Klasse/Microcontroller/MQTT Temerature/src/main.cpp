#include <OneWire.h>
#include <DallasTemperature.h>
#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

const int oneWireBus = 4;

OneWire oneWire(oneWireBus);

DallasTemperature sensors(&oneWire);

WiFiClient espClient;
PubSubClient client(espClient);

void setupWifi()
{
  Serial.begin(9600);
  Serial.print("Connecting to ");
  Serial.print(SSID);
  WiFi.begin(SSID, WIFI_PW);
  while (!WiFi.isConnected())
  {
    Serial.print(".");
    delay(200);
  }
  Serial.println("OK");
  Serial.print("IP-Address: ");
  Serial.println(WiFi.localIP());
}

void setupMQTT()
{
  client.setServer("broker.hivemq.com", 1883);
}

void connectToMQTT()
{
  while (!client.connected())
  {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP-30"))
    {
      Serial.println("connected");
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void sendTemperatureToBroker(float temperature)
{
  String payload = "{\"name\":\"ESP-30\",\"value\":" + String(temperature) + "}";
  client.publish("HTL/NB/4AHITS/temperatures", payload.c_str());
}

void loop()
{
  if (!client.connected())
  {
    connectToMQTT();
  }
  client.loop();

  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);

  Serial.print("Temperature: ");
  Serial.println(temperature);

  sendTemperatureToBroker(temperature);

  delay(10000);
}

void setup()
{
  setupWifi();
  setupMQTT();
  sensors.begin();
}