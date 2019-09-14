# Object Detection and Object Tracking with Opencv

This repository contains some image processing solution implemented with
opencv in python including optical flow, face tracking, eye tracking, etc. 

### Table of contents
| | Source | Description |
| --- | --- | --- | 
|1| **[Frame Differencing](frame_diff.py)** | Taking differences between consecutive frames. Display the difference. Identifying moving parts.
|2| **[Object Tracking Using Color Spaces](colorspaces.py)** | Tracking objects using HSV color space which performs better than rgb in object detection tasks. Improve robustness comparing to previous method. Use it to detect human skin.
|3| **[Object Detection Using Background Subtraction](backgnd_subtract.py)** | Build an adaptive model that represents background in a video. Use the model to detect moving objects.
|4| **[Object Tracking Using CAM-Shift Algorithm](camshift.py)** | Select an object in a live video. use mean shift to track that object.
|5| **[Optical Flow Based Tracking](optical_flow.py)** | Optical flow and its process. Extract feature points and create tracking lines.
|6| **[Face Detection and Tracking](face_detector.py)** | Automatically detect and track face and eyes separately. 

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
