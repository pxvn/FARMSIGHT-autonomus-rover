# FARMSIGHT: Autonomous Field Surveyor Rover

(UNDER DEVLOPMENT)

![FARMSIGHT Logo](link-to-your-logo-image)

## Overview

**FARMSIGHT**  is a versatile, autonomous rover designed to revolutionize modern agriculture by delivering real-time data insights for efficient field management. Using the Sipeed Maixduino microcontroller, FARMSIGHT collects and analyzes data on soil conditions, plant health, and environmental parameters, enabling farmers to make data-driven decisions. The rover features detachable sensor modules for flexibility, robust wireless connectivity, and the option for remote or autonomous control.

## Table of Contents

- [Features](#features)
- [Technical Specifications](#technical-specifications)
- [Components](#components)
- [System Architecture](#system-architecture)
- [Circuit Diagram](#circuit-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Autonomous Navigation: Utilizes multiple sensors for obstacle detection, terrain adaptation, and fixed-path navigation.
- Soil Health Analysis: Measures soil moisture and other environmental factors to optimize crop health and growth.
- Edge AI Plant Analysis: Integrated camera and AI model on the Maixduino for on-device plant health monitoring and disease detection.
- Wireless Data Transmission: Sends sensor data to Arduino Cloud for real-time monitoring and analysis from any location.
- Modular Design: Features detachable sensor and analysis modules, allowing easy customization for various field tasks.

## Technical Specifications

- **Microcontroller** Sipeed Maixduino (K210 chip)
- Supporting Controllers: (as of now) Arduino Mega 2560 and ESP32 for sensor integration and wireless data transmission
- Power Supply: 12V Li-Po battery and 7.4V Li-ion battery for reliable field operation
- Sensors:Capacitive Soil Moisture Sensor for moisture analysis
- Environmental sensors for air quality and pH levels
- Camera Module for plant image analysis
- Communication: ESP32 for Wi-Fi and cloud data transfer
- Motor Control: Cytron MDD20A motor drivers and high-torque servos for maneuvering on rough terrain

## Components

| Component                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| Sipeed Maxduino               | The main microcontroller for processing data and controlling functions.     |
| Ultrasonic Sensor             | Used for obstacle avoidance during navigation.                              |
| Soil Moisture Sensor          | Measures moisture levels in the soil.                                      |
| pH Sensor                     | Measures the pH level of the soil for health assessment.                   |
| Camera Module                 | Captures images for plant analysis and disease detection.                  |
| ESP32                         | Provides Wi-Fi connectivity for data transmission to the cloud.            |
| H-bridge Motor Driver         | Controls the movement of DC motors based on commands from the microcontroller. |
| 12V Li-ion Battery            | Powers the entire system, ensuring portability and efficiency.             |

## System Architecture

```mermaid
graph LR
    A[Power Supply<br>(12V Li-ion Battery)] --> B[ESP32 Microcontroller]
    B --> C[Ultrasonic Sensor]
    B --> D[Soil Moisture Sensor]
    B --> E[pH Sensor]
    B --> F[Camera Module]
    B --> G[Motor Driver]
    G --> H[DC Motors]
```
## Usage
Power On:

Ensure batteries are fully charged, then power on the rover.
Use the emergency kill switch to quickly disable the rover if needed.

## Operational Modes:

### Autonomous Mode: Set a fixed path using the control software, and the rover will navigate independently, collecting data and transmitting it to the cloud.
### Remote-Controlled Mode: Use Bluetooth or the Arduino Cloud dashboard to control the rover remotely, ideal for areas needing precise control.

## Data Collection:

The rover will continuously gather soil moisture, environmental, and image data for cloud analysis.
View real-time data through the Arduino Cloud dashboard or mobile app.


## License
See the LICENSE file for more details.

### Acknowledgments
Thank you to Sipeed for sponsoring the project.(CIRCUIT DIGEST)

Note: For this submission, I am setting up the system on one or two controllers while continuously working on integrating all components. Due to limited library support on the Sipeed Maixduino, I am developing custom configurations and libraries to meet project requirements before the deadline.
