# FARMSIGHT: Autonomous Field Surveyor Rover

![FARMSIGHT Logo](link-to-your-logo-image)

## Overview

**FARMSIGHT** is an innovative autonomous rover designed to enhance modern farming through real-time data processing and analysis. Built around the Sipeed Maxduino microcontroller, this rover integrates advanced sensors and wireless technology to provide farmers with critical insights on soil health, plant conditions, and optimal resource management.

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

- **Autonomous Navigation**: Utilizes ultrasonic sensors for obstacle avoidance and GPS for location tracking.
- **Soil Analysis**: Measures soil moisture and pH levels to provide insights for optimal crop health.
- **Plant Disease Detection**: Integrates a camera and TensorFlow Lite for real-time identification of plant diseases.
- **Wireless Data Transmission**: Sends collected data to the Blynk cloud for real-time monitoring and analysis.
- **Energy Efficient Design**: Carefully selected components for optimal battery performance.

## Technical Specifications

- **Microcontroller**: Sipeed Maxduino (K210 chip)
- **Power Supply**: 12V Li-ion battery
- **Sensors**:
  - Ultrasonic Sensor (for obstacle detection)
  - Capacitive Soil Moisture Sensor
  - pH Sensor
- **Communication**: ESP32 for wireless data transmission
- **Motor Control**: H-bridge motor driver for DC motors

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
- Connect all components as per the circuit diagram.
- Power on the rover.
- Use the Blynk app to monitor soil conditions and control the rover wirelessly.
- Collect data on soil health and plant conditions in real-time.
- Future Enhancements
- Integrate solar power for sustainable energy use.
- Expand the dataset for plant disease detection to improve accuracy.
- Implement machine learning algorithms for predictive analysis.

## License
See the LICENSE file for more details.

### Acknowledgments
Thank you to Sipeed for sponsoring the project.(CIRCUIT DIGEST)
