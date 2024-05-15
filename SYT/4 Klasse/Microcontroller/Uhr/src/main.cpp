#include <Arduino.h>
#include <Adafruit_SSD1306.h>
#include <sstream>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
hw_timer_t *Timer0_Cfg = NULL;

int tenth = 0;
int second = 0;
int minute = 0;
int hour = 0;

int swtenth = 0;
int swsecond = 0;
int swminute = 0;
int swhour = 0;

const int startWatchPin = 33;
const int endWatchPin = 35;

unsigned long lastDebounceTimeStart = 0;
unsigned long lastDebounceTimeEnd = 0;
unsigned long debounceDelay = 100;
bool running = false;

void incrementCount();
void stopwatch();

void IRAM_ATTR Timer0_ISR()
{
  tenth++;
  if (tenth == 10) {
    tenth = 0;
    second++;
    if (second == 60) {
      second = 0;
      minute++;
      if (minute == 60) {
        minute = 0;
        hour++;
      }
    }
  }
  if (running)
  {
    swtenth++;
    if (swtenth == 10) {
      swtenth = 0;
      swsecond++;
      if (swsecond == 60) {
        swsecond = 0;
        swminute++;
        if (swminute == 60) {
          swminute = 0;
          swhour++;
        }
      }
    }
  }
}

void setup()
{
  pinMode(startWatchPin, INPUT_PULLUP);
  pinMode(endWatchPin, INPUT_PULLUP);

  Timer0_Cfg = timerBegin(0, 80, true);
  timerAttachInterrupt(Timer0_Cfg, &Timer0_ISR, true);
  timerAlarmWrite(Timer0_Cfg, 100000, true);
  timerAlarmEnable(Timer0_Cfg);

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.display();

  attachInterrupt(digitalPinToInterrupt(startWatchPin), stopwatch, CHANGE);
  attachInterrupt(digitalPinToInterrupt(endWatchPin), stopwatch, CHANGE);
}

void loop()
{
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(2.5);
  display.setTextColor(WHITE);
  std::stringstream ss;
  ss << hour << ":" << minute << ":" << second << "," << tenth;
  display.print(ss.str().c_str());
  if (running)
  {
    display.setCursor(0, 20);
    std::stringstream ff;
    ff << swhour << ":" << swminute << ":" << swsecond << "," << swtenth;
    display.print(ff.str().c_str());
  }
  display.display();
}

void stopwatch()
{
  int startwatchstate = digitalRead(startWatchPin);
  int endwatchstate = digitalRead(endWatchPin);

  if (startwatchstate == LOW && millis() - lastDebounceTimeStart >= debounceDelay && !running)
  {
    lastDebounceTimeStart = millis();
    swtenth = 0;
    swsecond = 0;
    swminute = 0;
    swhour = 0;
    running = true;
  }
  if (endwatchstate == LOW && millis() - lastDebounceTimeEnd >= debounceDelay && running)
  {
    lastDebounceTimeEnd = millis();
    running = false;
  }
}
