import tkinter as tk
from customtkinter import *
import cv2
import numpy as np
import os
import time
from PIL import Image, ImageTk
from dy_PageUtils import set_icon_image

def face_register(visitor_name, scanbtn, RegVframe, RCameraFrame, Entryframe, homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    scanbtn.destroy()

    # Prepare the label for the camera feed inside RegVframe
    camera_label = CTkLabel(RCameraFrame, text="", width=680, height=480)
    camera_label.place(relx=0.5, rely=0.5, anchor='center')
     # Add a label for "Scanning..."
    scanning_label = CTkLabel(RegVframe, text="Scanning...", font=("Inter", 30, "bold"), fg_color="transparent", text_color="#333333")
    scanning_label.place(relx=0.5, rely=0.85, anchor='center')  # Adjust the 'rely' as needed to position below the camera feed

    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cas_path)
    face_data = []
    skip = 0

    start_time = time.time()

    def show_frame():
        nonlocal skip
        remaining_time = 10 - int(time.time() - start_time)  # Calculate remaining time

        if remaining_time <= 0:
            # Stop the session after 10 seconds
            save_and_exit()
            return

        ret, frame = cap.read()
        if not ret:
            return  # If frame read is not successful, do nothing

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
        faces = sorted(faces, key=lambda f: f[2] * f[3])

        for face in faces[-1:]:
            x, y, w, h = face
            face_section = gray_frame[y:y + h, x:x + w]
            face_section = cv2.resize(face_section, (100, 100))
            cv2.putText(frame, visitor_name, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.putText(frame, "Time left: " + str(remaining_time), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)

        if skip % 10 == 0:
            face_data.append(face_section)
        skip += 1

        camera_label.after(10, show_frame)

    def save_and_exit():
        if face_data:
            face_data_np = np.asarray(face_data)
            face_data_np = face_data_np.reshape((face_data_np.shape[0], -1))
            np.save(os.path.join(dirpath, visitor_name + '.npy'), face_data_np)
        cap.release()
        cv2.destroyAllWindows()
        display_success_and_close(RegVframe)  # Assuming RegVframe is your register window

    def display_success_and_close(register_frame):
        RegisScssfr = CTkFrame(register_frame, fg_color="white", width=600, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
        RegisScssfr.place(relx=0.5, rely=0.5, anchor='center')
        # Assuming ASSETS_PATH and set_icon_image are defined somewhere in your code
        set_icon_image(RegisScssfr,'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
        LbSuccess = CTkLabel(RegisScssfr, text="Registered Successfully", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
        LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
        register_frame.after(2000, lambda: register_frame.destroy())

    show_frame()