#include <Arduino.h>

//Fischer Variante
int inputPins[8] = {34,35,32,33,25,26};
u_int8_t inputStatus = 0;

void setup() {

// 0  ...   Kanal Nr
// 50 ...   Frequenz
// 8  ...   Auflösung

  ledcSetup(0,50,8);
  ledcAttachPin(18,0);

/*
  pinMode(34, INPUT_PULLUP);
  pinMode(35, INPUT_PULLUP);
  pinMode(32, INPUT_PULLUP);
  pinMode(33, INPUT_PULLUP);
  pinMode(25, INPUT_PULLUP);
  pinMode(26, INPUT_PULLUP);
*/

  //Fischer Variante:
  for (int i = 0; i < 6; i++){
    pinMode(inputPins[i], INPUT_PULLUP);
  }
  
}

void loop() {
  //Fischer Variante:
  inputStatus = 0;
  for (int i = 0; i < 6; i++){
    //inputStatus += digitalRead(inputPins[i]) * pow(2, i);
    inputStatus += digitalRead(inputPins[i]) << i;

  }
  ledcWrite(0, inputStatus);
  delay(100);
  
/*
  size_t amount = 0;
  amount+= digitalRead(34)<<2;  //Die Bits werden 2 nach links verschoben
  amount+= digitalRead(35)<<3;
  amount+= digitalRead(32)<<4;
  amount+= digitalRead(33)<<5;
  amount+= digitalRead(25)<<6;
  amount+= digitalRead(26)<<7;
  ledcWrite(0, amount);
*/
  
/*
  for (size_t i = 0; i < 256; i++)
  {
      ledcWrite(0,i);
      delay(20);
  }

  for (size_t i = 255; i > 0; i--)
  {
      ledcWrite(0,i);
      delay(20);
  }
*/
  
}
