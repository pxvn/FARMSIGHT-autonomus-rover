from machine import I2C
import time

count = 0  # Global variable to keep track of transmissions

def on_receive(data):
    print("on_receive:", data)

def on_transmit():
    global count  # Ensure we're using the global count variable
    count += 1
    print("on_transmit, send:", count)
    return count  # Send count value back to master

def on_event(event):
    print("on_event:", event)

# Set up I2C as a slave on the K210
try:
    i2c = I2C(
        I2C.I2C0,
        mode=I2C.MODE_SLAVE,
        scl=30,
        sda=31,
        addr=0x24,
        addr_size=7,
        on_receive=on_receive,
        on_transmit=on_transmit,
        on_event=on_event
    )
    print("K210 I2C Slave setup complete")
except Exception as e:
    print("Error initializing I2C:", e)

# Keep running
while True:
    time.sleep(1)
