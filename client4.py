# Import necessary modules
import socket
import time
import sensor
import image
import lcd
import _thread
from network_esp32 import wifi

# Network configuration
SSID = "0000"
PASW = "12121212"
server_ip = "192.168.16.150"  # Server IP address
video_port = 3456  # Port for video transmission
command_port = 3457  # Port for receiving commands

# Initialize LCD and camera
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)  # Set pixel format for the image
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.skip_frames(time=2000)  # Wait for sensor to adjust

# Initialize clock to control frame rate
clock = time.clock()

# Function to enable ESP32 Wi-Fi connection
def enable_esp32():
    if not wifi.isconnected():
        for i in range(5):
            try:
                wifi.reset(is_hard=True)  # Reset Wi-Fi if not connected
                print('Trying to connect to Wi-Fi...')
                wifi.connect(SSID, PASW)
                if wifi.isconnected():
                    break
            except Exception as e:
                print("Wi-Fi connection error:", e)
                time.sleep(1)
    print('Network connected:', wifi.isconnected(), wifi.ifconfig())

# Connect to Wi-Fi
enable_esp32()

# Function to connect to the server for video streaming
def connect_video_socket():
    while True:
        try:
            video_sock = socket.socket()  # Create a new socket
            video_sock.connect((server_ip, video_port))  # Connect to server IP and port
            print("Connected to video server")
            return video_sock  # Return the socket object if connection is successful
        except Exception as e:
            print("Video connection error:", e)
            time.sleep(1)  # Retry after 1 second

# Function to listen for commands from the server
def listen_for_commands():
    """Connect to the server's command socket and listen for control commands."""
    while True:
        try:
            command_sock = socket.socket()  # Create a socket for receiving commands
            command_sock.connect((server_ip, command_port))  # Connect to command port of server
            command_sock.settimeout(5)  # Set timeout for socket operations

            print("Connected to server for commands.")

            while True:
                command = command_sock.recv(1024).decode('utf-8')  # Receive command from server
                if command:
                    print("Received command:", command)
                    # Add command processing logic here
                    if command == "forward":
                        # Implement forward movement here
                        pass
                    elif command == "backward":
                        # Implement backward movement here
                        pass
                    elif command == "left":
                        # Implement left turn here
                        pass
                    elif command == "right":
                        # Implement right turn here
                        pass
        except Exception as e:
            print("Command connection error:", e)
            time.sleep(1)  # Retry after a delay
        finally:
            command_sock.close()  # Close the command socket
            print("Disconnected from command server, retrying...")

print("Running Thread")
# Start the command listening thread
_thread.start_new_thread(listen_for_commands, ())
print("Done Running.................")

# Main loop for capturing and sending video frames
while True:
    video_sock = connect_video_socket()  # Connect to video server
    video_sock.settimeout(5)  # Set timeout for socket operations

    while True:
        clock.tick()  # Maintain a constant frame rate
        img = sensor.snapshot()  # Capture an image from the camera
        img = img.compress(quality=60)  # Compress the image to reduce size
        img_bytes = img.to_bytes()  # Convert image to bytes for transmission

        try:
            # Split the image data into 2048-byte chunks and send it in parts
            block = int(len(img_bytes) / 2048)  # Number of blocks
            for i in range(block):
                video_sock.send(img_bytes[i*2048:(i+1)*2048])  # Send chunk of image
                time.sleep_ms(10)  # Small delay between sending chunks
            video_sock.send(img_bytes[block*2048:])  # Send the remaining bytes if any
        except Exception as e:
            print("Send failed:", e)  # Handle socket sending errors
            break  # Reconnect if sending fails

    video_sock.close()  # Close the socket after sending the image
