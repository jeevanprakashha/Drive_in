# Car Parking for Drive-In Cinemas

A project report submitted to Mr. Biswajit Jena, School of Electronics Engineering, in partial fulfillment of the requirements for the course of ECE2035 – Sensors, Actuators, and Signal Conditioning in B.Tech. Computer Science and Engineering.

## Acknowledgement

We wish to express our sincere thanks and deep sense of gratitude to our project guide, Dr. Biswajit Jena, School of Electronics Engineering, for her consistent encouragement and valuable guidance offered to us throughout the course of the project work. We are extremely grateful to Dr. R. Ganesan, Dean, School of Computer Science and Engineering (SCOPE), Vellore Institute of Technology, Chennai, for extending the facilities of the School towards our project and for his unstinting support. We express our thanks to our Head of the Department for her support throughout the course of this project. We also take this opportunity to thank all the faculty of the School for their support and their wisdom imparted to us throughout the courses. We thank our parents, family, and friends for bearing with us throughout the course of our project and for the opportunity they provided us in undergoing this course in such a prestigious institution.

## Bonafide Certificate

Certified that this project report entitled "Car Parking for Drive-In Cinemas" is a bona-fide work of Jeevan Prakash (20BRS1259) carried out the "J"-Project work under my supervision and guidance for ECE2035 - Sensors, Actuators, and Signal Conditioning.

Dr. Biswajit Jena
SENSE

## Table of Contents

1. [Introduction](#introduction)
2. [Related Works](#related-works)
3. [Proposed Methodology](#proposed-methodology)
4. [Results and Discussion](#results-and-discussion)
5. [Conclusion](#conclusion)
6. [References](#references)

## Abstract

The idea of this project is to create a model that is able to detect a car and inquire about the ticket price and the number of members. If it meets all requirements, it can access the parking lot, which also has conditions like how many slots are available. If a slot is available, it will allow entry; otherwise, it won't. The project uses Arduino for programming, IR sensors for detection, and Python for serial communication. A servo motor is used for entry and exit gate control.

## Introduction

Drive-in cinemas have gained popularity in recent years as a way to enjoy movies from the comfort of your own car. However, parking can become a hassle as the number of attendees increases. To address this problem, we have designed a car parking system using IR sensors, servo motors, and an Arduino board for a drive-in cinema. The system aims to make parking easier and more efficient for customers attending the cinema.

## Related Works

- Rooftop Cinema Club
- Secret Cinema
- Pop-up cinemas
- Drive-in cinema revival
- Virtual cinema

## Methodology

### Hardware Setup

The hardware setup consisted of two IR sensors, a servo motor, an Arduino board, jumper wires, a breadboard, and a power supply. The IR sensors were placed at the entrance of the parking lot, facing each other to detect the presence of a car. The servo motor was attached to a cardboard box to create a parking slot that could move in a horizontal direction. The Arduino board was connected to the IR sensors and servo motor using jumper wires and a breadboard.

### Software Implementation

The software implementation consisted of two parts: the Arduino code and the Python code.

- Arduino Code: The code for the Arduino board was written in the Arduino IDE. It consisted of two main functions: one for detecting the presence of a car using the IR sensors and the other for controlling the servo motor to adjust the position of the parking slot. The code also included the implementation of serial communication with Python using the Serial library.

- Python Code: The Python code was written in the Python IDE. It consisted of a program that communicated with the Arduino board through serial communication. The Python program displayed the status of each parking slot and sent commands to the Arduino board to control the servo motor under certain conditions.

### Testing

The car parking system was tested by simulating the presence of a car in the parking lot using a test object. The IR sensors accurately detected the presence of the object, and the servo motor smoothly adjusted the position of the parking slot. The Python program provided real-time monitoring of the parking lot and allowed for remote control of the car parking system under certain conditions.

### Finalization

The finalization of the car parking system consisted of integrating all the components and testing the system under real-world conditions. The system was installed at a drive-in cinema, and the system's performance was monitored during peak hours. The system efficiently managed parking, making it easier and more efficient for customers attending the cinema.

## Conclusion

The car parking system for a drive-in cinema using IR sensors, servo motors, and an Arduino board with serial communication with Python was successfully implemented. The project demonstrated the use of technology to solve the problem of parking at drive-in cinemas. The implementation of IR sensors, servo motors, and an Arduino board provided an efficient car parking system, while the implementation of serial communication with Python provided additional flexibility and control over the system. The project is a great example of how technology can be used to make our lives easier and more efficient.

## References

- [Arduino Tutorial: IR Sensor - How it works and How to use it with Arduino](https://www.arduino.cc/en/Tutorial/LibraryExamples/IRremote)
- [Arduino Tutorial: Servo Motors - How they work and How to use them with Arduino](https://www.arduino.cc/en/Tutorial/LibraryExamples/Servo)
- [PySerial Library - Python Serial Communication with Arduino](https://pyserial.readthedocs.io/en/latest/shortintro.html)
- [ResearchGate: Drive-in cinema parking system using IR sensors and servo motors](https://www.researchgate.net/publication/351402598_Drive-in_cinema_parking_system_using_IR_sensors_and_servo_motors)
- [Instructables: Arduino Serial Communication With Python](https://www.instructables.com/Arduino-Serial-Communication-With-Python/)
- [Electronics Hub: Using IR Sensor with Arduino for Obstacle Detection](https://www.electronicshub.org/using-ir-sensor-with-arduino-for-obstacle-detection/)
- [Electronics Hub: Servo Motor Control using Arduino](https://www.electronicshub.org/servo-motor-control-using-arduino/)
- [PyImageSearch: Real-Time Object Detection with YOLOv4 and OpenCV](https://www.pyimagesearch.com/2020/09/28/real-time-object-detection-with-yolov4-and-opencv/)
- [IEEE Xplore: An Improved Automatic Parking System using IoT and Image Processing](https://ieeexplore.ieee.org/document/9057684)
- [ScienceDirect: Intelligent Parking System Based on Image Processing](https://www.sciencedirect.com/science/article/pii/S1877050917323344)
- [IEEE Xplore: Smart Parking System Using IoT and Machine Learning](https://ieeexplore.ieee.org/document/8937815)
- [IJARIIT: Automated Car Parking System using Image Processing](https://www.ijariit.com/manuscript/automated-car-parking-system-using-image-processing/)

## G-Drive Links for Additional Materials

- [Project Documentation](https://drive.google.com/file/d/1rAp1QSyPAoZKVJVmGlbOC6RO4jGRtka4/view?usp=sharing)
- [Project Presentation](https://drive.google.com/file/d/1UuPkPP1O-0gOd9_pIohGBd7oxnzVmPIl/view?usp=sharing)
