# Volume Controller 🔊

## Overview 🖐️

This Python project allows you to easily control your system's volume. Using **Computer Vision**, you can adjust the volume simply by manipulating the distance between your thumb and index finger 🤏. All you need is a webcam and your hand!

## Features ✨
- Real-time hand detection and tracking using OpenCV.
- Hand gesture recognition to control system volume.
- Visual feedback with graphical overlays for volume level and hand tracking.
- FPS (frames per second) display to monitor performance.


## Dependencies 📦

- **NumPy (np):** numerical operations and arrays.
- **OpenCV (cv2):** Image processing and computer vision.
- **Pycaw:** Provides access and control over audio devices.
- **ctypes, comtypes:** For interaction with Windows system libraries.
- **MediaPipe (HandTrackingModule):** Detects and tracks hand landmarks.


## Installation & Setup 🔧
    pip install -r requirements.txt

## How It Works ⚙️

- **Hand Detection:** 🖐️ MediaPipe detects your hand and identifies landmarks.
- **Distance Calculation:** 📏 The distance between the tips of your thumb and index finger is calculated.
- **Volume Mapping:** 📈 The distance is mapped to a volume level within a defined range. A visual volume bar is displayed for feedback.
- **Audio Adjustment:** 🎶 Pycaw takes over and sets your system's master volume accordingly.


## Usage 🚀

### Run the script:
    python VolumeHandControl.py

1. **Webcam Time!** 📸 Your webcam feed appears.

2. **Hand Control:**  🖐️ Adjust the distance between your thumb and index finger to control the volume.

3. **Exit:**  🚪 Press 'q' to quit.


## Important Notes
- **Windows Only:** This project is currently tailored for Windows. Adjustments might be needed for other operating systems.
- **Calibration:** Adjust distance ranges for optimal performance with your setup.
- **Let me know** if you have any other questions or requests!

## Acknowledgments
- This project uses the **pycaw** library for controlling system volume.
- Thanks to the creators of **OpenCV** and other open-source tools used in this project.

## License
This project is licensed under the **MIT** License. See the **LICENSE** file for more details.
