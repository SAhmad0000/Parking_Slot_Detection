
# 🚗 Parking Slot Detection

A simple and effective web app built with Streamlit that uses YOLOv8 object detection to monitor parking slot availability from uploaded video footage.
The app detects vehicles (cars) in real-time and displays parking status — Empty or Occupied — frame-by-frame.


## ✨ Features

- Upload and process parking lot surveillance videos (.mp4 format).
- Detects cars using YOLOv8 object detection model.
- Displays live detection with bounding boxes.
- Shows real-time parking status (Empty/Occupied with car count).
- Visual progress bar during video processing.
- Works on Streamlit Cloud with lightweight setup.











## 🚀 Run Locally

1. Clone the repository:

```bash
  git clone https://github.com/your-username/parking-slot-detection.git
  cd parking-slot-detection

```

2. Install required Python packages:

```bash
  pip install -r requirements.txt

```

3. Make sure yolov8s.pt is in the project directory.
(You can download YOLOv8s model from Ultralytics)

4. Run the Streamlit:

```bash
  streamlit run parkingslot.py
```


## 📦 Deployment on Streamlit Cloud

Upload the following files to your GitHub repo:
- parking_detection_streamlit.py
- requirements.txt
- packages.txt
- yolov8s.pt

Connect your GitHub repository to Streamlit Cloud and deploy.

Ensure packages.txt installs system libraries like ffmpeg, libsm6, and libxext6 needed for video processing.



## 🛠 Tech Stack

**Python:** Language 

**Streamlit:** Web app framework

**OpenCV:** Video processing

**Ultralytics YOLOv8:** Object detection

**FFmpeg:** Video decoding support
## 🎥 Sample Usage

    1. Upload a parking lot video.

    2. Watch vehicles being detected live.

    3. See parking status updated automatically.

    4. Receive a success message once processing is complete!
## 🚀 About Me
**Name:** Sameer Ahmad

**GitHUb:** SAhmad0000

## 🙏 Acknowledgements

 - [Ultralytics YOLO](https://github.com/ultralytics/ultralytics): For their open-source object detection models.

 - [Streamlit](https://streamlit.io/): For enabling fast web application deployment.
## Thank You for Visiting!
