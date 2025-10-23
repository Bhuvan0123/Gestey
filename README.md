# 🤖 Gestey - Gesture Controlled Robotic Arm


## 🧠 Overview

**Gestey** is a Python-based real-time gesture control system for the **Dobot Magician** robotic arm. Using **OpenCV** and **MediaPipe**, Gestey detects hand gestures through a webcam and converts them into movement commands for the robotic arm via the **pydobot** library.

## 🚀 Features

* Real-time gesture tracking and robotic arm control.
* Move the arm in **Left**, **Right**, **Up**, and **Down** directions.
* Perform **Grab** and **Release** actions using hand gestures.
* Lightweight, simple, and interactive system for beginners in robotics and computer vision.

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV** – for video capture and frame processing.
* **MediaPipe** – for hand landmark tracking.
* **pydobot** – to communicate with the Dobot Magician robotic arm.

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bhuvan0123/Gestey.git
   cd Gestey
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python mediapipe pydobot
   ```

3. Connect your **Dobot Magician** via USB and set the correct port in the code:

   ```python
   port = 'COM3'  # Example for Windows
   dobot = Dobot(port=port)
   ```

## 🎮 Controls

| Gesture     | Action                |
| ----------- | --------------------- |
| 👈 Left     | Move the arm left     |
| 👉 Right    | Move the arm right    |
| 👆 Up       | Move the arm upward   |
| 👇 Down     | Move the arm downward |
| ✊ Grab      | Close gripper         |
| 🖐️ Release | Open gripper          |

## ▶️ Usage

Run the main program:

```bash
python gestey.py
```

A webcam window will open — control the robotic arm in real-time using your hand gestures.
Press **'q'** to exit.


## 🌟 Future Enhancements

* Add gesture-based rotation and height control.
* Introduce voice-assisted control.
* Add GUI for sensitivity adjustment and gesture calibration.

## 👤 Author

**Bhuvan Chandra P**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/bhuvanchandrap/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/Bhuvan0123)

---

> 💡 *Gestey bridges the gap between human gestures and robotics — making interaction intuitive and futuristic!*
