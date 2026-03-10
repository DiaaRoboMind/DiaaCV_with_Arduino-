# AI-Powered Hand Control for Arduino 

This project demonstrates how to bridge Python (Computer Vision) with Arduino (Hardware) to control LEDs and a Servo Motor in real-time using hand gestures.

-> Project Description
A Computer Vision-based system that uses a webcam to track hand landmarks and sends serial commands to an Arduino Uno. This allows for dynamic control of:
* 3 LEDs:Turning them ON/OFF or controlling brightness.
* Servo Motor: Adjusting movement speed based on finger distance.

->Tech Stack
* Language: Python 3.12.3
* AI Libraries: MediaPipe, OpenCV
* Communication: PySerial
* Hardware: Arduino Uno, SG90 Servo, 3 LEDs
* OS: Linux (Ubuntu)

-> How to Run
1. Hardware: Connect your Arduino and components as per the code pins.
2. Setup Python:
   pip install opencv-python mediapipe pyserial
