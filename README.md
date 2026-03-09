
## Project Overview


This project implements a smart automated urine collection system designed to measure urine flow volume and route samples automatically for collection or disposal. The system integrates embedded sensing hardware with a web-based monitoring backend to create a fully automated biomedical fluid management prototype.

The system uses an ESP32 microcontroller to collect data from sensors and control actuators. Urine flow is measured using a Hall-effect based inline flow sensor, while a relay-controlled solenoid valve and stepper motor system manages sample routing and container rotation. Data is transmitted via Wi-Fi to a Django backend, where measurements are stored and visualized through a web dashboard.

### Key Features

1. Real-time urine flow measurement using Hall-effect flow sensor

2. Ultrasonic-based user detection

3. Automated sample routing using relay-controlled valves

4. Stepper motor-based rotating sample collection platform

5. ESP32 Wi-Fi communication with Django backend

6. Web dashboard for monitoring and manual valve control

7. Fully modular IoT-based biomedical fluid monitoring prototype

### Hardware Components

1. ESP32 microcontroller

2. Hall-effect inline flow sensor

3. Ultrasonic distance sensor

4. Relay module

5. Solenoid valve

6. Stepper motor with ULN2003 driver

7. Silicone tubing and fluid connectors

8. External power supply

### Software Stack

1. Embedded firmware: Arduino IDE (C++ for ESP32)

2. Backend server: Django + Django REST Framework

3. Communication: HTTP API

4. Database: SQLite (default Django DB)


## System Architecture

User Detection (Ultrasonic)
            ->
Fluid Flow Measurement (Hall Sensor)
            ->
ESP32 Processing
            ->
Relay / Stepper Actuation
            ->
WiFi Data Transmission
            ->
Django Backend + Database
            ->
Web Dashboard Monitoring


### This project demonstrates:

1. Embedded systems development

2. Sensor interfacing

3. Real-time flow measurement

4. Electromechanical control (relay + stepper motor)

5. IoT communication with ESP32

6. Backend API development using Django

7. Full-stack hardware–software system design
