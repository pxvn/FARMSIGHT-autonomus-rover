#include <BTAddress.h>
#include <BTAdvertisedDevice.h>
#include <BTScan.h>
#include <BluetoothSerial.h>

BluetoothSerial ROVER_BT;

// The setup routine runs once when you press reset.
void setup() {
  Serial0.begin(115200);
  ROVER_BT.begin();
}

void loop() {
  if (ROVER_BT.available()) {
    char command = ROVER_BT.read();
    if (command == 's') {
      Serial0.println(100);
    } else if (command == 'f') {
      Serial0.println(200);
    } else if (command == 'b') {
      Serial0.println(300);
    } else if (command == 'r') {
      Serial0.println(500);
    } else if (command == 'l') {
      Serial0.println(400);
    } else {
      Serial0.println(100);
    }
  }
  delay(50);
  fflush(stdin);
}