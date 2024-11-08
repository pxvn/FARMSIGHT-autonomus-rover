from machine import I2C
import time

# Initialize I2C as master
i2c = I2C(I2C.I2C0, freq=100000, scl=30, sda=31)  # Use correct pins for your setup
esp32_addr = 0x10  # Set the ESP32 I2C address

def send_command(command):
    try:
        i2c.writeto(esp32_addr, command)
        print("Sent command:", command)
    except OSError as e:
        print("I2C communication error:", e)

while True:
    # Send "ON" command
    send_command(b'ON')
    time.sleep(1)  # LED stays on for 1 second

    # Send "OFF" command
    send_command(b'OFF')
    time.sleep(1)  # LED stays off for 3 seconds
