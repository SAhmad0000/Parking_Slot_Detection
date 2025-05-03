# parking_detection_streamlit.py

import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
import time

# Title
st.title("🚗 Parking Slot Detection App")

# Upload video
uploaded_file = st.file_uploader("parking1.mp4", type=['mp4'])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    
    # Load the model
    model = YOLO('yolov8s.pt')  # Or your trained model
    
    # Open video
    cap = cv2.VideoCapture(tfile.name)
    
    frame_placeholder = st.empty()  # For showing frames

    # Optional progress bar
    progress_bar = st.progress(0)

    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.resize(frame, (1020, 500))

        # Inference (predict)
        results = model(frame, verbose=False)
        boxes = results[0].boxes
        class_ids = boxes.cls.cpu().numpy() if boxes else []

        # Parking logic: check if 'car' class (id 2) detected
        car_count = sum(1 for class_id in class_ids if int(class_id) == 2)

        if car_count == 0:
            status_text = "Parking Empty"
            color = (0, 255, 0)  # Green
        else:
            status_text = f"Parking Occupied ({car_count} car(s))"
            color = (0, 0, 255)  # Red
        
        # Draw status on frame
        cv2.putText(frame, status_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, color, 3)
        
        # Draw YOLO detections
        annotated_frame = results[0].plot()

        # Show in Streamlit
        frame_placeholder.image(annotated_frame, channels="BGR", use_container_width=True)

        # Update progress bar
        frame_count += 1
        progress_bar.progress(min(frame_count / total_frames, 1.0))

        # Optional: Slow down for human view
        time.sleep(0.03)  # 30ms ~ 30fps

    cap.release()
    st.success("Video processing completed! ✅")
