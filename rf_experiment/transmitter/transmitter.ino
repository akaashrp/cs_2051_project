#include <RH_ASK.h>
#include <SPI.h>
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;
int num;
int index;
String msg;
char buf[10];
const int buflen = 10;

void setup() {
    // Initialize ASK Object
    rf_driver.init();
    Serial.begin(9600);
    index = 0;
}

void loop() {
    num = random(255);
    msg = String(index) + " " + "Hello!";
    msg.toCharArray(buf, buflen);
    rf_driver.send(buf, buflen);
    rf_driver.waitPacketSent();
    Serial.println(msg);
    index++;
    delay(2000);
}
