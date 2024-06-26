import tkinter as tk
from tkinter import simpledialog
import cv2
import numpy as np
import os
import time

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()

# Show an input box and ask the user to enter their name
name = simpledialog.askstring("Input", "Enter your name:", parent=root)

if name:  
    cap = cv2.VideoCapture(0)
    cas_path = "C:\\Users\\grace\\Desktop\\GitReVisit\\ReVisit-faceattend\\data\\haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cas_path)
    face_data = []
    skip = 0
    face_section = np.zeros((100, 100), dtype="uint8")
    dirpath = "C:\\Users\\grace\\Desktop\\GitReVisit\\ReVisit-faceattend\\data"

    # Check if a file with the same name already exists
    if os.path.isfile(os.path.join(dirpath, name + '.npy')):
        print("Warning: The name already exists in the dataset.")
        print("Please enter a different name.")
    else:
        start_time = time.time()
        while True:
            ret, frame = cap.read()
            if ret == False:
                continue

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
            faces = sorted(faces, key=lambda f: f[2] * f[3])

            for face in faces[-1:]:
                x, y, w, h = face
                face_section = gray_frame[y:y + h, x:x + w]
                face_section = cv2.resize(face_section, (100, 100))
                cv2.putText(frame, name, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
            
            # Calculate remaining time
            remaining_time = int(10 - (time.time() - start_time))
            cv2.putText(frame, "Time left: " + str(remaining_time), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Camera", frame)
            
            if skip % 10 == 0:
                face_data.append(face_section)
            skip += 1
            
            key_pressed = cv2.waitKey(1) & 0xFF
            if key_pressed == ord('x') or remaining_time <= 0:
                break

        face_data = np.asarray(face_data)
        face_data = face_data.reshape((face_data.shape[0], -1))
        np.save(os.path.join(dirpath, name + '.npy'), face_data)

    cap.release()
    cv2.destroyAllWindows()
