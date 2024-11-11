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

* Intel Realsense D435 [parameters](./intel-realsense-d435/parameters.md) in `/intel-realsense-d435`
* Primesense Carmine 1.09 [parameters](./primesense-carmine-1.09/parameters.md) in `/primesense-carmine-1.09`

## Markers

Once the camera is calibrated, markers can be detected in 3D space.

Build [ar_track_alvar](http://wiki.ros.org/ar_track_alvar) from [source](https://github.com/ros-perception/ar_track_alvar/tree/noetic-devel).

```
rosrun ar_track_alvar individualMarkers \
  _marker_size:=9.577 \
  _output_frame:="world" \
  _cam_image_topic:="/camera/rgb/image_raw" \
  _cam_info_topic:="/camera/rgb/camera_info" \
  _max_new_marker_error:=0.08 \
  _max_track_error:=0.2
```
