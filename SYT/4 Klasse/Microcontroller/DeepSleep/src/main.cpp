#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

const char* mqtt_topic = "HTL/Test/4AHITS/temperatures";

const int oneWireBus = 4;

OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);

  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void setupWifi() {
  Serial.begin(9600);
  Serial.print("Connecting to ");
  Serial.print(SSID);
  WiFi.begin(SSID, WIFI_PW);
  while (!WiFi.isConnected()) {
    Serial.print(".");
    delay(200);
  }
  Serial.println("OK");
  Serial.print("IP-Address: ");
  Serial.println(WiFi.localIP());
}

void setupMQTT() {
  client.setServer("broker.hivemq.com", 1883);
  client.setCallback(callback);
}

void connectToMQTT() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP-29")) {
      Serial.println("connected");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void sendTemperatureToBroker(float temperature) {
  String payload = "{\"name\":\"ESP-29\",\"value\":" + String(temperature) + "}";
  client.publish("HTL/Test/4AHITS/temperatures", payload.c_str());
}


int TIME_TO_SLEEP = 5;

void doAction(){
setupWifi();
  setupMQTT();
  sensors.begin();

  //setupWifi();
  if (!client.connected()) {
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

void startDeepSleep(){ 

}

void setup() {
  Serial.begin(9600);
  Serial.println("Waking up...");

  doAction();

  Serial.println("Going to sleep...");
  Serial.flush();

  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * 1000000);
  esp_deep_sleep_start();
}
void loop() {
  // pass
}