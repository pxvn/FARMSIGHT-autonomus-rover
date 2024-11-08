import time
import math
from modules import ws2812

led_io, led_num = 24, 16
ws = ws2812(led_io, led_num)

# Function to create a color gradient effect
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Gradient Fade In and Out
def fade_in_out(color, steps=50, wait=20):
    for brightness in range(steps):
        adjusted_color = (color[0] * brightness // steps,
                          color[1] * brightness // steps,
                          color[2] * brightness // steps)
        for i in range(led_num):
            ws.set_led(i, adjusted_color)
        ws.display()
        time.sleep_ms(wait)
    for brightness in range(steps, -1, -1):
        adjusted_color = (color[0] * brightness // steps,
                          color[1] * brightness // steps,
                          color[2] * brightness // steps)
        for i in range(led_num):
            ws.set_led(i, adjusted_color)
        ws.display()
        time.sleep_ms(wait)

# Color Wipe
def color_wipe(color, wait=50):
    for i in range(led_num):
        ws.set_led(i, color)
        ws.display()
        time.sleep_ms(wait)
    for i in range(led_num):
        ws.set_led(i, (0, 0, 0))  # Turn off the LED one by one
        ws.display()
        time.sleep_ms(wait)

# Theater Chase
def theater_chase(color, wait=100):
    for j in range(10):  # Number of cycles
        for q in range(3):  # Cycle offset
            for i in range(0, led_num, 3):
                ws.set_led(i + q, color)  # Turn on every third LED
            ws.display()
            time.sleep_ms(wait)
            for i in range(0, led_num, 3):
                ws.set_led(i + q, (0, 0, 0))  # Turn off every third LED

# Running Rainbow Cycle
def running_rainbow_cycle(wait):
    for j in range(256):  # Full cycle across 256 color positions
        for i in range(led_num):
            pixel_index = (i * 256 // led_num) + j
            ws.set_led(i, wheel(pixel_index & 255))
        ws.display()
        time.sleep_ms(wait)

# Breathing Light Effect
def breathing_light(color, wait=10):
    steps = 100  # Number of steps for fade in and fade out
    for step in range(steps):  # Fade in
        brightness = (math.sin(math.pi * step / steps) + 1) / 2  # Calculate brightness as sine wave
        adjusted_color = (int(color[0] * brightness),
                          int(color[1] * brightness),
                          int(color[2] * brightness))
        for i in range(led_num):
            ws.set_led(i, adjusted_color)
        ws.display()
        time.sleep_ms(wait)
    for step in range(steps, 0, -1):  # Fade out
        brightness = (math.sin(math.pi * step / steps) + 1) / 2
        adjusted_color = (int(color[0] * brightness),
                          int(color[1] * brightness),
                          int(color[2] * brightness))
        for i in range(led_num):
            ws.set_led(i, adjusted_color)
        ws.display()
        time.sleep_ms(wait)

# Loop through animations
while True:
    fade_in_out((255, 0, 0))  # Fade red in and out
    color_wipe((0, 255, 0))  # Green color wipe
    theater_chase((0, 0, 255))  # Blue theater chase
    running_rainbow_cycle(20)  # Smooth rainbow cycle
    breathing_light((255, 255, 0))  # Yellow breathing effect
