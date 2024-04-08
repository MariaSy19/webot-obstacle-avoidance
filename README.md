# ObstacleRobot-
# ObstacleBot

## Description
ObstacleBot is a 4-wheel robot equipped with 2 distance sensors for autonomously avoiding obstacles. This project aims to implement a controller algorithm that enables the robot to navigate its environment safely.

## Components
- 4-wheel robot chassis
- 4 DC motors
- Motor driver module (e.g., L298N)
- Microcontroller board (e.g., Arduino Uno)
- 2 ultrasonic distance sensors (e.g., HC-SR04)
- Breadboard and jumper wires
- Battery pack or power source

## Controller Algorithm
The controller algorithm reads distance values from the ultrasonic sensors and adjusts motor speeds based on obstacle detection to navigate around obstacles autonomously.

## Repository Structure
- `controller_code/`: Contains the Arduino sketch for the controller.
- `schematics/`: Contains the schematic diagram of the robot.
- `documentation/`: Contains optional project documentation such as a detailed project report.

## Usage
1. Assemble the robot according to the schematic diagram provided.
2. Upload the Arduino sketch (`obstacle_avoidance_controller.ino`) to the microcontroller board.
3. Power on the robot and observe its autonomous obstacle avoidance behavior.

## Contributors
- [Your Name]

## License
[License information]
