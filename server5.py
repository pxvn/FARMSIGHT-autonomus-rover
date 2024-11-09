import socket
import threading
import pygame
from pygame.locals import QUIT, KEYDOWN, K_w, K_a, K_s, K_d, K_r, MOUSEBUTTONDOWN
from PIL import Image, ImageEnhance, ImageOps, ImageDraw

# Constants
PC_IP = "192.168.16.150"       # IP address of the PC for receiving video
MAIXDUINO_IP = "192.168.16.186" # IP address of the Maixduino for sending commands
VIDEO_PORT = 3456
COMMAND_PORT = 3457
WIDTH, HEIGHT = 800, 600
IMAGE_WIDTH, IMAGE_HEIGHT = 640, 280
SATURATION_FACTOR = 1.5

# Initialize Pygame and fonts
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Farmsight - Rover Control Dashboard")

font_large = pygame.font.Font(None, 60)
font_medium = pygame.font.Font(None, 30)  # Smaller font for subheader
font_small = pygame.font.Font(None, 25)

# Function to enhance image saturation and add rounded corners
def enhance_saturation(image_path, factor):
    """Enhance saturation, rotate image, and add rounded corners."""
    image = Image.open(image_path)
    converter = ImageEnhance.Color(image)
    enhanced_image = converter.enhance(factor)
    rotated_image = ImageOps.exif_transpose(enhanced_image.rotate(-90, expand=True))
    resized_image = rotated_image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

    # Create rounded corners
    mask = Image.new("L", resized_image.size, 0)
    draw = ImageDraw.Draw(mask)
    corner_radius = 20
    draw.rounded_rectangle([(0, 0), resized_image.size], corner_radius, fill=255)
    rounded_image = Image.composite(resized_image, Image.new("RGB", resized_image.size), mask)

    return rounded_image

# Set up command socket to send commands to Maixduino
def connect_command_socket():
    cmd_sock = socket.socket()
    cmd_sock.connect((MAIXDUINO_IP, COMMAND_PORT))  # Connect to Maixduino's IP and COMMAND_PORT
    return cmd_sock

cmd_sock = connect_command_socket()

# Function to send control commands
def send_control_command(command):
    """Send a control command to Maixduino."""
    try:
        cmd_sock.send(command.encode('utf-8'))
        print(f"Sent command: {command}")
    except Exception as e:
        print(f"Command send error: {e}")

# Function to handle receiving and displaying images
def receive_thread(conn):
    conn.settimeout(10)
    conn_end = False
    while not conn_end:
        img_data = b""
        while True:
            try:
                client_data = conn.recv(4096)
                if not client_data:
                    conn_end = True
                    break
                img_data += client_data
                if img_data.endswith(b'\xFF\xD9'):
                    break
            except socket.timeout:
                conn_end = True
                break

        if img_data.startswith(b'\xFF\xD8') and img_data.endswith(b'\xFF\xD9'):
            with open("tmp.jpg", "wb") as f:
                f.write(img_data)

            try:
                enhanced_image = enhance_saturation("tmp.jpg", SATURATION_FACTOR)
                enhanced_image.save("tmp_enhanced.jpg")
                surface = pygame.image.load("tmp_enhanced.jpg").convert()
                screen.fill((30, 30, 30))
                screen.blit(surface, ((WIDTH - IMAGE_WIDTH) // 2, 100))
                draw_control_buttons()
                draw_texts()
                pygame.display.update()
            except Exception as e:
                print("Error processing image:", e)

    conn.close()

# Start the video server for receiving video data
def start_server():
    sk = socket.socket()
    sk.bind((PC_IP, VIDEO_PORT))  # Bind to PC's IP for video server
    sk.listen(50)
    while True:
        conn, addr = sk.accept()
        print("Connected to client at:", addr)
        threading.Thread(target=receive_thread, args=(conn,)).start()

server_thread = threading.Thread(target=start_server)
server_thread.start()

# Draw control buttons (GUI unchanged)
def draw_control_buttons():
    """Draw control buttons with click functionality."""
    button_radius = 20
    button_size = (100, 50)
    button_margin = 10

    button_color = (50, 150, 250)
    text_color = (255, 255, 255)

    control_positions = {
        "F": (WIDTH // 2 - button_size[0] // 2, 420),
        "L": (WIDTH // 2 - button_size[0] - button_margin - button_radius, 480),
        "R": (WIDTH // 2 + button_margin + button_radius, 480),
        "B": (WIDTH // 2 - button_size[0] // 2, 540),
    }

    # Draw control buttons with labels
    for label, (x, y) in control_positions.items():
        button_rect = pygame.Rect(x, y, *button_size)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=button_radius)
        button_text = font_small.render(label, True, text_color)
        text_x = x + (button_size[0] - button_text.get_width()) // 2
        text_y = y + (button_size[1] - button_text.get_height()) // 2
        screen.blit(button_text, (text_x, text_y))

# Draw sensor info and heading text
def draw_texts():
    header_text = font_large.render("FarmSight Rover Control GUI", True, (255, 255, 255))
    subheader_text = font_medium.render("CIRCUIT DIGEST DESIGN CONTEST", True, (255, 0, 0))
    sensor_data_text = font_small.render("Sensor Data: [40%]", True, (255, 255, 255))
    battery_text = font_small.render("Battery: 85%", True, (0, 255, 0))
    connection_text = font_small.render("Connection: Strong", True, (0, 255, 0))

    screen.blit(header_text, ((WIDTH - header_text.get_width()) // 2, 20))
    screen.blit(subheader_text, ((WIDTH - subheader_text.get_width()) // 2, 65))
    screen.blit(sensor_data_text, (20, HEIGHT - 120))
    screen.blit(battery_text, (20, HEIGHT - 90))
    screen.blit(connection_text, (20, HEIGHT - 60))

# Main event loop for handling control commands
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                send_control_command("forward")
            elif event.key == K_s:
                send_control_command("backward")
            elif event.key == K_a:
                send_control_command("left")
            elif event.key == K_d:
                send_control_command("right")
            elif event.key == K_r:
                recording = not recording
                if not recording and frames:
                    frames[0].save("recording.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
                    frames = []
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.Rect(WIDTH - 120, HEIGHT - 70, 100, 50).collidepoint(event.pos):
                recording = not recording
                if not recording and frames:
                    frames[0].save("recording.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
                    frames = []

pygame.quit()

