#coding=utf-8
#!/usr/bin/env python2

import socket
import threading
import pygame
from pygame.locals import QUIT
from PIL import Image, ImageEnhance

local_ip = "192.168.16.192"
local_port = 3456
width, height = 800, 600  # Updated dimensions for more space
image_width, image_height = 320, 240  # Original image size
saturation_factor = 1.5  # Increase to make colors more vivid

# Function to enhance the saturation of the received image
def enhance_saturation(image_path, factor):
    image = Image.open(image_path)
    converter = ImageEnhance.Color(image)
    return converter.enhance(factor)

# Receiving and processing images
def receiveThread(conn):
    conn.settimeout(10)
    conn_end = False
    pack_size = 1024 * 5
    while True:
        if conn_end:
            break
        img = b""
        tmp = b''
        while True:
            try:
                client_data = conn.recv(1)
            except socket.timeout:
                conn_end = True
                break
            if tmp == b'\xFF' and client_data == b'\xD8':
                img = b'\xFF\xD8'
                break
            tmp = client_data
        while True:
            try:
                client_data = conn.recv(4096)
            except socket.timeout:
                client_data = None
                conn_end = True
            if not client_data:
                break
            img += client_data
            if img[-2:] == b'\xFF\xD9':
                break
            if len(client_data) > pack_size:
                break
        print("Received image, length:", len(img))

        if not img.startswith(b'\xFF\xD8') or not img.endswith(b'\xFF\xD9'):
            print("Image error")
            continue

        with open("tmp.jpg", "wb") as f:
            f.write(img)

        try:
            # Enhance saturation and save the modified image
            enhanced_image = enhance_saturation("tmp.jpg", saturation_factor)
            enhanced_image.save("tmp_enhanced.jpg")

            # Load the enhanced image
            surface = pygame.image.load("tmp_enhanced.jpg").convert()
            screen.fill((30, 30, 30))  # Dark background for contrast

            # Display the image centered without zoom
            screen.blit(surface, ((width - image_width) // 2, 150))  # Position below headers

            # Header text and subtitle
            header_text = font_large.render("FarmSight Rover Control GUI", True, (255, 255, 255))
            subheader_text = font_medium.render("Circuit Digest Design Contest", True, (255, 0, 0))
            screen.blit(header_text, ((width - header_text.get_width()) // 2, 20))
            screen.blit(subheader_text, ((width - subheader_text.get_width()) // 2, 80))

            # Control Buttons
            draw_control_buttons()

            # Sensor and Battery info
            sensor_data_text = font_small.render("Sensor Data: [40%]", True, (255, 255, 255))
            battery_text = font_small.render("Battery: 85%", True, (0, 255, 0))
            connection_text = font_small.render("Connection: Strong", True, (0, 255, 0))

            screen.blit(sensor_data_text, (20, height - 120))
            screen.blit(battery_text, (20, height - 90))
            screen.blit(connection_text, (20, height - 60))

            # Update display
            pygame.display.update()
            print("Displayed enhanced image and data")
        except Exception as e:
            print(e)
    conn.close()
    print("Receive thread ended")

# Function to draw control buttons with icons and rounded corners
def draw_control_buttons():
    button_radius = 20
    button_size = (100, 50)
    button_margin = 10

    # Colors
    button_color = (50, 150, 250)
    text_color = (255, 255, 255)

    # Button positions
    control_positions = {
        "Forward": (width // 2 - button_size[0] // 2, 420),
        "Left": (width // 2 - button_size[0] - button_margin - button_radius, 480),
        "Right": (width // 2 + button_margin + button_radius, 480),
        "Backward": (width // 2 - button_size[0] // 2, 540),
        "Stop": (width // 2 - button_size[0] // 2, 600),
    }

    # Draw each control button
    for label, (x, y) in control_positions.items():
        button_rect = pygame.Rect(x, y, *button_size)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=button_radius)
        
        button_text = font_small.render(label, True, text_color)
        text_x = x + (button_size[0] - button_text.get_width()) // 2
        text_y = y + (button_size[1] - button_text.get_height()) // 2
        screen.blit(button_text, (text_x, text_y))

# Initialize Pygame and fonts
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Farmsight - Rover Control Dashboard")

# Font setup
font_large = pygame.font.Font(None, 60)  # Larger font for header
font_medium = pygame.font.Font(None, 40)  # Medium font for subtitles
font_small = pygame.font.Font(None, 30)  # Smaller font for controls and sensor info

# Set up server socket
ip_port = (local_ip, local_port)
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(ip_port)
sk.listen(50)
print("Server listening, waiting for client...")

# Server function to handle connections
def server():
    while True:
        conn, addr = sk.accept()
        print("Connected to client at:", addr)
        t = threading.Thread(target=receiveThread, args=(conn,))
        t.start()

# Start the server in a new thread
tmp = threading.Thread(target=server, args=())
tmp.start()

# Main Pygame loop for handling window events
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
