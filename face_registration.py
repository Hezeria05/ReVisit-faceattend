import tkinter as tk
from customtkinter import *
import cv2
import numpy as np
import os
import time
from PIL import Image, ImageTk
from dy_PageUtils import set_icon_image

def face_register(visitor_name, scanbtn, RegVframe, RCameraFrame, homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, cap, on_register_click):
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    scanbtn.destroy()
    cap.release()
    camera_label = CTkLabel(RCameraFrame, text="", width=680, height=480)
    camera_label.place(relx=0.5, rely=0.5, anchor='center')
    scanning_label = CTkLabel(RegVframe, text="Scanning...", font=("Inter", 40, "bold"), fg_color="transparent", text_color="#333333")
    scanning_label.place(relx=0.5, rely=0.85, anchor='center')

    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cas_path)
    face_data = []
    skip = 0
    error_count = 0  # Counter for errors

    start_time = time.time()

    def show_frame():
        nonlocal skip, error_count
        remaining_time = 10 - int(time.time() - start_time)

        if remaining_time <= 0:
            save_and_exit()
            return

        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            return
        else:
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

            # Draw the rule of thirds grid on the frame
            height, width, _ = frame.shape
            color = (207, 203, 173)  # Color of the grid lines (green)
            thickness = 1  # Thickness of the grid lines

            # Draw vertical lines
            cv2.line(frame, (width // 3, 0), (width // 3, height), color, thickness)
            cv2.line(frame, (2 * width // 3, 0), (2 * width // 3, height), color, thickness)

            # Draw horizontal lines
            cv2.line(frame, (0, height // 3), (width, height // 3), color, thickness)
            cv2.line(frame, (0, 2 * height // 3), (width, 2 * height // 3), color, thickness)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            camera_label.imgtk = imgtk
            camera_label.configure(image=imgtk)

            if skip % 10 == 0:
                try:
                    face_data.append(face_section)
                except Exception as e:
                    print(f"Error appending face data: {e}")
                    error_count += 1
                    if error_count >= 4:
                        cap.release()
                        display_success_and_close(RegVframe, 0)
            skip += 1

            camera_label.after(10, show_frame)

    def save_and_exit():
        if face_data:
            face_data_np = np.asarray(face_data)
            face_data_np = face_data_np.reshape((face_data_np.shape[0], -1))
            np.save(os.path.join(dirpath, visitor_name + '.npy'), face_data_np)
        cap.release()
        cv2.destroyAllWindows()
        display_success_and_close(RegVframe, 1)

    def display_success_and_close(register_frame, success):
        RegisScssfr = CTkFrame(register_frame, fg_color="white", width=600, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
        RegisScssfr.place(relx=0.5, rely=0.5, anchor='center')
        if success == 1:
            set_icon_image(RegisScssfr, 'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
            LbSuccess = CTkLabel(RegisScssfr, text="Registered Successfully", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
            LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
            register_frame.after(2000, lambda: register_frame.destroy())
        else:
            set_icon_image(RegisScssfr, 'warning_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
            LbFail = CTkLabel(RegisScssfr, text="Please Try Again", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
            LbFail.place(relx=0.5, rely=0.65, anchor='n')
            register_frame.after(1000, lambda: retry_registration())

    def retry_registration():
        RegVframe.destroy()
        on_register_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, visitor_name)

    show_frame()
