<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gaetancantelobre/VisionBlackOutM1">
    <img src="photo_docu/logo.png" alt="Logo"">
  </a>

<h3 align="center">SSL BLACKOUT</h3>

  <p align="center">
    SSL Blackout is a project that aims to provide an open-source alternative to the RoboCup SSL Vision system.
    <br />
    <a href="https://github.com/RoboCup-SSL/ssl-vision"><strong>Learn more about SSL »</strong></a>
    <br />
    <br />
    <video width="320" height="240" controls>
      <source src="photo_docu/demo.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Feautres</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Robot vision](photo_docu/live.gif)

As part of the M1 curriculum at the University of Bordeaux, we were asked to create a project that would allow us to learn about the different aspects of software engineering. We chose to create an alternative to the RoboCup SSL Vision system by making the SSL robots completely autonomous.
This autonomous system is based on the use of a camera placed on the robot and hooked up to a Jetson Nano. The Jetson Nano will process the images captured by the camera and send the information to the robot's microcontroller. The microcontroller will then be able to move the robot according to the information received.

The project is divided into two parts: the vision part and the strategy part. The vision part is responsible for capturing the images and processing them to extract the information, this part is done by training an AI model to detect the robots, the ball and the field goals. The strategy part is responsible for preforming the calculations to determine the best course of action for the robot to take.

This project is still in early stages of development.




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

1. Python
   ```sh
   sudo apt-get install python3
   ```
2. Yolo
   ```sh 
    # Install the ultralytics package from PyPI
    pip install ultralytics
    ```
3. OpenCV
   ```sh
   pip install opencv-python
   ```
4. [RSK](https://robot-soccer-kit.github.io/documentation)

5. A camera


### Installation
All the code is in the VisionBlackOutM1 folder. You can clone the repository and run the code from there.

be sure to have everything installed before running the code.
and to change the paths in the code to match your own paths as well as the camera you are using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- FEATURES -->
## Features

- Detect robots
- Detect ball
- Detect field goals
- ball shooting
- goal shooting

<p align="right">(<a href="#readme-top">back to top</a>)</p>

