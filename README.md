# **FarmSight Field Survey Rover**

## Overview
FarmSight Field Survey Rover is a versatile, field-ready rover designed for data collection and monitoring in agricultural environments. Equipped with a range of sensors, real-time streaming capabilities, and a servo-driven arm with modular attachments, FarmSight gathers actionable data to optimize farm management. This rover is powered by the Seeed Maixduino K210 and Arduino Mega 2560, selected for their robust processing power and extensive I/O capabilities, respectively.

<p align="center">
  <img src="path_to_main_thumbnail_image.jpg" alt="FarmSight Rover Thumbnail" width="600">
</p>

---

## Table of Contents
1. [Hardware and Electronics](#hardware-and-electronics)
2. [Software and GUI Interface](#software-and-gui-interface)
3. [System Architecture](#system-architecture)
4. [Methodology and Design](#methodology-and-design)
5. [Applications and Impact](#applications-and-impact)
6. [Installation and Code](#installation-and-code)
7. [Demo and Gallery](#demo-and-gallery)

---

## Hardware and Electronics

| Component            | Specification                    | Quantity |
|----------------------|----------------------------------|----------|
| **Microcontrollers** | Seeed Maixduino K210, Arduino Mega 2560 | 1 each   |
| **Motors**           | IG32 DC Motors with encoders    | 6        |
| **Motor Drivers**    | Cytron MDD20A                    | 3        |
| **Servos**           | Dual Shaft 16kg metal gear      | 3        |
| **Power Supply**     | Dual battery (7.4V and 12V)     | 1 each   |
| **LED Feedback**     | WS2812B LEDs                    | -        |
| **Chassis**          | Aluminum frame with rocker-bogie design | 1  |
| **Remote Control**   | FS-i6 Transmitter               | 1        |

**Additional Components:**
- PVC pipes, CNC-cut MDF parts, silver foil, nuts, bolts, and zip ties.

### Microcontroller Functions
- **Seeed Maixduino K210:** Handles AI-based image processing, video streaming, and WiFi communication.
- **Arduino Mega 2560:** Manages motor control, servo movements, and sensor data collection.

---

## Software and GUI Interface

### Graphical User Interface (GUI)
- **Platform:** Python with Pygame
- **Features:**
  - Real-time data display from sensors
  - Video streaming with recording option
  - Battery and signal strength indicators
  - Interactive control buttons for movement and arm adjustments

<p align="center">
  <img src="path_to_GUI_screenshot.jpg" alt="GUI Screenshot" width="600">
</p>

### Control Modes
- **Manual Control:** Via FS-i6 transmitter for real-time navigation.
- **Autonomous Mode:** Pre-programmed paths for hands-free operation.
  
### Lighting Effects
- WS2812B LEDs provide visual feedback for states like moving, idle, or braking.

### Image Processing and Streaming
- The K210 enhances image saturation and streams video to the GUI for real-time monitoring, with day and night visibility.

---

## System Architecture

### Block Diagram
<p align="center">
  <img src="path_to_circuit_diagram.jpg" alt="System Architecture" width="600">
</p>

### Circuit Diagram Explanation
The system integrates multiple components controlled by the Seeed Maixduino K210 and Arduino Mega 2560. The K210 handles video streaming, while the Mega 2560 manages motor control, servo actions, and sensor data. Power is supplied via dual batteries, regulated by a buck converter.

---

## Methodology and Design

FarmSight's design focuses on adaptability and ease of operation over challenging terrain. With a rocker-bogie suspension, the rover navigates rough fields while maintaining stability. The aluminum chassis, reinforced with silver foil, provides durability and weather resistance.

| Component           | Purpose                                                |
|---------------------|--------------------------------------------------------|
| **Rocker-Bogie Chassis** | Enables stable movement across uneven terrain       |
| **Servo Arm**       | Supports modular sensor attachments for field analysis |
| **LED Feedback**    | Enhances visibility and communication with the operator |

---

## Applications and Impact

FarmSight is optimized for agricultural fieldwork, offering remote, efficient navigation over rough terrain. It enables:
- **Precision Irrigation:** Using soil moisture data for targeted watering.
- **Crop Health Monitoring:** Real-time camera feed helps assess plant health.
- **Modular Attachments:** Allows sensor swapping for a variety of tasks, from soil sampling to environmental monitoring.

---

## Installation and Code

### GitHub Repository
Find the full project code on [GitHub](https://github.com/pxvn/FarmSight-Field-Survey-Rover).

#### Key Code Features
- **Server Side:**
  - Establishes GUI, streams live data, processes image data, and manages controls.
- **Client Side:**
  - Captures images, manages network communication, and transmits data.
- **Arduino Mega 2560:**
  - Manages servo controls, motor drivers, and LED animations for feedback.

### Code Snippets
```python
# GUI Server Setup
import pygame
import socket
from PIL import Image

# Initialize Pygame and setup display
pygame.init()
screen = pygame.display.set_mode((800, 600))
# Further GUI code here...

```
Demo and Gallery
Live Video Streaming and Record Feature
<p align="center"> <img src="path_to_recorded_gif.gif" alt="Recorded GIF Feature" width="600"> </p>
Field Demonstration
<p align="center"> <img src="path_to_youtube_video.jpg" alt="Demo Video" width="600"> <br>Watch the rover in action on [YouTube](https://youtu.be/your_video_link) </p>
Component Image
<p align="center"> <img src="path_to_components_image.jpg" alt="Components" width="600"> </p>
Summary
FarmSight Field Survey Rover provides a comprehensive solution for agricultural monitoring with advanced data collection, real-time analysis, and versatile control. From rugged hardware to user-friendly software, this rover empowers precision farming with technology.

For additional resources, diagrams, and setup details, refer to the GitHub repository.
