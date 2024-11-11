# Camera Calibration

Contains calibration documents, logic, inputs, and outputs for several cameras that can be used with ROS.

## Installation

+ Python: `3.6` with [pyenv](https://github.com/pyenv/pyenv)
  ```
  pyenv install 3.6
  pyenv global 3.6
  ```
+ [OpenCV](https://pypi.org/project/opencv-python/) for Python
  ```
  pip install --upgrade pip
  pip install opencv-contrib-python
  ```

## Pattern

The pattern used is a `9`x`6` OpenCV chess board.
If it's printed on `8.5` x `11` sheet of paper with no scaling, real-world dimensions will be `217` mm x `153` mm.

## Capturing

- Connect your camera and ensure it works with ROS by using Rviz
- Create a folder for your camera in this repository
- Change into the folder
- Capture 20-40 images with `image_view`
  ```
  rosrun image_view image_view image:=<image topic>
  ```
  On the image view window, simply right-click and the current image will be saved to the current directory.

## Calibration

Run `calibration.py` script at the root of this repository with working directory containing the images to analyze.

## Cameras

* Intel Realsense D435 inputs and outputs in `/inteal-realsense-d435`
