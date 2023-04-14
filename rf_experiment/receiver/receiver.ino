#include <RH_ASK.h>
#include <SPI.h> 
 
// Create Amplitude Shift Keying Object
int index = 0;
RH_ASK rf_driver;

void setup()
{
    // Initialize ASK Object
    rf_driver.init();
    // Setup Serial Monitor
    Serial.begin(9600);
    index = 0;
}
 
void loop()
{
    // Set buffer to size of expected message
    char buf[6];
    uint8_t buflen = sizeof(buf);
    // Check if received packet is correct size
    if (rf_driver.recv(buf, &buflen))
    {
      
      // Message received with valid checksum
      Serial.println(String(index) + " " + String(buf).substring(0, buflen));  
      index++;       
    }
}
