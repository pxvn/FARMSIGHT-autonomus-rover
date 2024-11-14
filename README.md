# **FarmSight Field Survey Rover**

## Overview
FarmSight Field Survey Rover is a versatile, field-ready rover designed for data collection and monitoring in agricultural environments. Equipped with a range of sensors, real-time streaming capabilities, and a servo-driven arm with modular attachments, FarmSight gathers actionable data to optimize farm management. This rover is powered by the Seeed Maixduino K210 and Arduino Mega 2560, selected for their robust processing power and extensive I/O capabilities, respectively.

## YT Video
<p align="center">
  <a href="https://youtu.be/Q7DP26K7eiE" target="_blank">
    <img src="https://img.youtube.com/vi/Q7DP26K7eiE/0.jpg" alt="Watch FarmSight Demo Video" width="600">
  </a>
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

## Features

- **Real-Time Video Streaming**  
  [See it in Action!](#demo-and-gallery)

- **Interactive GUI**  
  [Demo the Interface](#software-and-gui-interface)

- **Autonomous & Manual Control**  
  Switch between autonomous and manual modes. [Learn More](#software-and-gui-interface)

- **Modular Sensor System**  
  Detachable sensors for soil, air, and more. [See Sensor Attachments](#hardware-and-electronics)

- **LED State Indicators**  
  Visual feedback via WS2812B LEDs. [View LED Status Indicators](#methodology-and-design)

- **Versatile Rover Design**  
  Rocker-bogie system for stability. [Rover in Action](#demo-and-gallery)

- **Remote Control (500m range)**  
  Control via FS-i6 with up to 500m range. [Control Demo](#demo-and-gallery)

- **Live Data Recording**  
  Record videos and sensor data directly. [Check Recording Feature](#software-and-gui-interface)

- **Multi-Sensor Integration**  
  Real-time environmental monitoring. [See Sensors in Action](#hardware-and-electronics)

---

## Hardware and Electronics
<p align="center">
  <img src="https://github.com/user-attachments/assets/dbb3bf43-1578-493a-95c4-b947194a8f82" alt="FarmSight Rover Thumbnail" width="600">
</p>

| Component            | Specification                    | Quantity |
|----------------------|----------------------------------|----------|
| **Microcontrollers** | Seeed Maixduino K210, Arduino Mega 2560 | 1 each   |
| **Motors**           | IG32 DC Motors with encoders    | 6        |
| **Motor Drivers**    | Cytron MDD20A                    | 3        |
| **Servos**           | Dual Shaft 16kg metal gear      | 3        |
| **Power Supply**     | Dual battery (7.4V and 12V)     | 1 each   |
| **LED Feedback**     | WS2812B LED                    | 1        |
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
  <img src="https://github.com/user-attachments/assets/86160e37-0115-4db4-bfee-031932d1ad78" alt="GUI Screenshot" width="600">
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

### Circuit Diagram Explanation

<p align="center">
  <img src="https://github.com/user-attachments/assets/82190d08-dbb4-495d-8b9b-dc3eb0264aa5" alt="CIRCUIT DIAGRAM" width="600">
</p>
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

For the code implementation, check out the following files in the repository:

- **[Server Side Code](https://github.com/pxvn/FARMSIGHT-autonomus-rover/blob/main/boot.py)**  
  Handles server-side operations such as GUI, image processing, and control management.
  
- **[Client Side Code (Maixduino K210)](https://github.com/pxvn/FARMSIGHT-autonomus-rover/blob/main/megarover.ino)**  
  Manages client-side operations, such as image capture, network communication, and data transmission.
  
- **[Arduino Mega 2560 Code](https://github.com/pxvn/FARMSIGHT-autonomus-rover/blob/main/rovergui.py)**  
  Controls motor drivers, servos, and LEDs, handling the physical rover movements.

### Code Snippets

!! You can find detailed explanations and code snippets in each of these files that implement the various rover functionalities.

---

## Demo and Gallery
---

## Additional info

- **Versatile Rover Design**  
  Sturdy, all-terrain design (2 x 1.5 ft, approx. 5kg) with a rocker-bogie suspension for stability over rough surfaces.
  
- **Runtime**  
  Operates for approximately 15-20 minutes on a single charge, suitable for field analysis sessions.
