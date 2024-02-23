#include <Arduino.h>
#include <TheThingsNetwork.h>

#define loraSerial Serial1
#define debugSerial Serial

// Replace REPLACE_ME with TTN_FP_EU868 or TTN_FP_US915
#define freqPlan TTN_FP_EU868

// put function declarations here (forward declaration, prototypen):
void message(const uint8_t *payload, size_t size, port_t port);

// Set your AppEUI and AppKey
const char *appEui = "0000000000000000";
const char *appKey = "FE2A36A86EA525DE92B29D9B284D0635";

TheThingsNetwork ttn(loraSerial, debugSerial, freqPlan);

void setup()
{
  loraSerial.begin(57600);
  debugSerial.begin(9600);

  while (!debugSerial)
  {
  }

  debugSerial.println("-- STATUS");
  ttn.showStatus();

  debugSerial.println("-- JOIN TTN Application");
  ttn.join(appEui, appKey);

  // Set callback for incoming message
  ttn.onMessage(message);
}

void loop()
{

  debugSerial.println("-- SEND DATA");

  byte data[2];
  data[0] = 0x01;
  data[1] = 0xAA;

  // Send it off
  ttn.sendBytes(data, sizeof(data));

  delay(10000);
}

// put function definitions here:
void message(const uint8_t *payload, size_t size, port_t port)
{
  debugSerial.print("-- MESSAGE received:");

  for (unsigned int i = 0; i < size; i++)
  {
    debugSerial.print(payload[i]);
    debugSerial.print("");
  }
  debugSerial.println();
}
