import time
import math
from modules import ws2812

led_io, led_num = 24, 16
ws = ws2812(led_io, led_num)

# Define the yellow/gold color for turn signals
GOLD_YELLOW = (255, 215, 0)

# Enhanced Red Ring Loading Animation

def red_ring_loading_cycle():
    for _ in range(2):  # Two cycles around the ring
        for i in range(led_num):
            # Set only the current LED to red
            for j in range(led_num):
                ws.set_led(j, (255, 0, 0) if j == i else (0, 0, 0))
            ws.display()
            time.sleep_ms(100)  # Adjust speed of movement

    # Blink all LEDs in red to indicate loading completion
    for _ in range(2):  # Three blinks
        for i in range(led_num):
            ws.set_led(i, (255, 0, 0))
        ws.display()
        time.sleep_ms(200)  # On duration
        for i in range(led_num):
            ws.set_led(i, (0, 0, 0))
        ws.display()
        time.sleep_ms(200)  # Off duration

# Fade in and out effect
def fade_in_out(color, steps=25, wait=50):
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

# Yellow/Gold Comet Effect for Turn Signals
def turn_signal_comet(color, start, end, duration, trail_length=4, wait=30):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        for head_offset in range(trail_length):
            for i in range(start, end):
                distance = min(abs(i - start - head_offset), abs(i - end + head_offset))
                if distance < trail_length:
                    brightness = (trail_length - distance) / trail_length
                    adjusted_color = (int(color[0] * brightness),
                                      int(color[1] * brightness),
                                      int(color[2] * brightness))
                    ws.set_led(i, adjusted_color)
                else:
                    ws.set_led(i, (0, 0, 0))
            ws.display()
            time.sleep_ms(wait)

# Red Blink or Dim for Breaks
def break_effect():
    fade_in_out((255, 0, 0), steps=20, wait=50)

# Forward Motion with Green Pulse Effect
def forward_motion(wait=50, duration=6000):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        fade_in_out((0, 255, 0), steps=25, wait=wait)

# Backward Motion with Red Wipe Effect
def backward_motion(wait=50, duration=4000):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        for i in range(led_num):
            ws.set_led(i, (255, 0, 0))
            ws.display()
            time.sleep_ms(wait)
        for i in range(led_num):
            ws.set_led(i, (0, 0, 0))
            ws.display()
            time.sleep_ms(wait)

# Initialization Sequence with Enhanced Loading Animation
def initialization_sequence():
    red_ring_loading_cycle()          # Enhanced red loading ring and blink (approx. 2.5 seconds)
    fade_in_out((0, 255, 0), steps=25, wait=30)  # Green for 1.5 seconds
    fade_in_out((255, 255, 255), steps=25, wait=20)  # White for 1 second

# Main animation sequence
def main():
    initialization_sequence()  # Start-up sequence (6s)

    # Forward motion
    forward_motion(wait=50, duration=6000)  # 6s
    time.sleep(1)  # Break with red animation
    break_effect()

    # Right turn: yellow/gold comet effect
    turn_signal_comet(GOLD_YELLOW, 8, led_num, duration=5000, trail_length=4)  # Right comet loop for 5s
    time.sleep(1)  # Break with red animation
    break_effect()

    # Forward motion (shorter)
    forward_motion(wait=50, duration=4000)  # 4s
    time.sleep(1)  # Break with red animation
    break_effect()

    # Left turn: yellow/gold comet effect
    turn_signal_comet(GOLD_YELLOW, 0, 8, duration=5000, trail_length=4)  # Left comet loop for 5s
    time.sleep(1)  # Break with red animation
    break_effect()

    # Backward motion
    backward_motion(wait=50, duration=4000)  # 4s
    time.sleep(2)  # Extended break with red animation
    break_effect()

# Run the main animation
main()
