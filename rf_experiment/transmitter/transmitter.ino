#include <RH_ASK.h>
#include <SPI.h>
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;
int num;
int index;
char *msg;
String output;

void setup() {
    // Initialize ASK Object
    rf_driver.init();
    Serial.begin(9600);
    index = 0;
}

void loop() {
  num = random(255);
  msg = "Hello!";
  rf_driver.send(msg, strlen(msg));
  rf_driver.waitPacketSent();
  Serial.println(String(index) + " " + String(msg));
  index++;
  delay(2000);
}
