# Hand Gesture-Based Media Player

## Overview
In today's fast-paced digital age, multitasking has become second nature. With the surge in media consumption across platforms like YouTube, Instagram, and Facebook, the ease of control becomes essential. Recognizing the challenges of traditional media controls, especially when multitasking or during meals, this project introduces a hand gesture-based media player. Utilizing real-time video capture and advanced image processing techniques, the system efficiently recognizes hand gestures and translates them into media playback controls, such as play, pause, volume adjustments, and navigation.

## Technical Highlights

- **Real-time Video Capture**: Leveraged OpenCV's video capture capabilities to fetch live feed from the webcam.
- **Image Processing**: Implemented image preprocessing steps like resizing, flipping, and region of interest cropping to facilitate gesture recognition.
- **HSV Color Space Transformation**: Transformed the image color space to HSV for accurate hand segmentation.
- **Contour Detection & Analysis**: Detected hand contours and employed convex hull to identify and count convexity defects, which signify finger gaps.
- **Gesture-Based Controls**: Mapped the number of convexity defects to specific media controls, which are executed using the `pyautogui` library.

## Skills Demonstrated

- **Programming**: Python
- **Computer Vision**: OpenCV
- **Automation**: PyAutoGUI
- **Mathematics**: Geometry (for angle calculations between fingers)

## Applications
This project finds its utility in scenarios where traditional media controls can be cumbersome or infeasible, such as during meals or other tasks. Beyond media playback, the core idea can be expanded to broader applications, including virtual presentations, gaming, and assistive technologies.
