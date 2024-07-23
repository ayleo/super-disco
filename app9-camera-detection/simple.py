import cv2
import streamlit as st
import time


st.title("Webcam Live Feed")
start = st.button("Start Camera")


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        day = time.strftime(f"%A")
        current_time = time.strftime("%T")

        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=day, org=(20, 40),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(100, 100, 200),
                    thickness=1, lineType=cv2.LINE_AA)
        
        cv2.putText(img=frame, text=current_time, org=(20, 70),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(100, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)
        

        streamlit_image.image(frame)