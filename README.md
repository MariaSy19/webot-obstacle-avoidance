# Robot Obstacle Avoidance

## Description

This project implements a simple obstacle avoidance behavior for a robot created from scratch in the Webots application. The robot, equipped with two distance sensors, detects obstacles in its environment and navigates around them autonomously.

## Installation

1. **Install Webots**: Download and install the Webots application from [the official website](https://www.cyberbotics.com/).

2. **Set Up Project Environment**: 
    - Clone or download this repository to your local machine.
    - Open the project in Webots.

## Usage

1. **Run the Simulation**:
    - Launch the Webots application.
    - Open the project in Webots.
    - Run the simulation to see the robot in action.
    - The robot should autonomously navigate around obstacles detected by its sensors.

2. **Modify Behavior (Optional)**:
    - You can modify the behavior of the robot by editing the Python script (`my_controller2.py`) in the project.
    - Adjust parameters such as sensor thresholds or motor speeds to change the robot's behavior.

## Robot Configuration

The robot in this project is created from scratch in Webots. It consists of:
- Two distance sensors (`Rsensor` and `Lsensor`) for obstacle detection.
- Four motor devices for controlling the left and right wheels (`Lmotor1`, `Lmotor2`, `Rmotor1`, and `Rmotor2`).

## Project Structure

- `my_controller2.py`: Python script containing the robot controller code.
- `assignment1.wbt`: containing the Webots world files.

## Acknowledgments

- This project is created using Webots, a powerful robotics simulation platform.
