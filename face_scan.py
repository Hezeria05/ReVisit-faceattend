import tkinter as tk
from customtkinter import *
import cv2
import os
from face_recognition import KNN
from PIL import Image, ImageTk
from dy_PageUtils import load_image

def load_cascade_classifier(cas_path):
    face_cascade = cv2.CascadeClassifier(cas_path)
    return face_cascade

def start_camera(log_stat, CameraFrame, btn_confi, scanbtn, Selectwarn, LogVname, face_dataset, face_labels, name, face_cascade, cap, reload_page, 
                 homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button, callback=None):
    # Disable the scan button immediately when the camera starts
    scanbtn.configure(state="disabled")
    home_button.configure(state="disabled")
    visitor_button.configure(state="disabled")
    resident_button.configure(state="disabled")
    logout_btn.configure(state="disabled")
    camera_label = CTkLabel(CameraFrame, width=450, height=350, text="")
    camera_label.place(relx=0, rely=0)

    # Initialize a counter for face classifications
    face_classification_count = 0
    classification_threshold = 300  # Threshold for number of classifications before stopping
    def update_frame():
        nonlocal face_classification_count  # To modify the counter inside the nested function
        ret, frame = cap.read()
        if not ret:
            # print("not ret")
            camera_label.after(10, update_frame)
            return
        else:
            # print("recognizing")
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
            faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)

            for face in faces[-1:]:
                # print("face classified")
                face_classification_count += 1
                x, y, w, h = face
                face_section = gray_frame[y:y+h, x:x+w]
                face_section = cv2.resize(face_section, (100, 100))
                pred = KNN(face_dataset, face_labels, face_section)
                pred_name = name[int(pred)]
                cv2.putText(frame, pred_name, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                LogVname.configure(state='normal')  # Enable the entry for update
                LogVname.delete(0, tk.END)
                LogVname.insert(0, pred_name)
                LogVname.configure(state='disabled')
                if Selectwarn is not None:
                    Selectwarn.configure(text="")

                if face_classification_count >= classification_threshold:
                    cap.release()

                    if log_stat == 1:
                        btn_confi.configure(width=120, height=45)
                        scanbtn.configure(width=120, height=45)
                        btn_confi.place(relx=0.698, rely=0.5, anchor='center')
                        scanbtn.place(relx=0.9, rely=0.5, anchor='center')
                    retryimage = load_image('retryscan.png', (32, 32))
                    scanbtn.configure(state="normal", image=retryimage, text="", command=lambda: 
                        reload_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button))
                    return
            # Draw the rule of thirds grid on the frame
            height, width, _ = frame.shape
            color = (207, 203, 173)  # Color of the grid lines
            thickness = 1  # Thickness of the grid lines

            # Draw vertical lines
            cv2.line(frame, (width // 3, 0), (width // 3, height), color, thickness)
            cv2.line(frame, (2 * width // 3, 0), (2 * width // 3, height), color, thickness)

            # Draw horizontal lines
            cv2.line(frame, (0, height // 3), (width, height // 3), color, thickness)
            cv2.line(frame, (0, 2 * height // 3), (width, 2 * height // 3), color, thickness)

            # Convert the image to PIL format and then to ImageTk format.
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = CTkImage(img, size=(680, 480))
            camera_label.imgtk = imgtk
            camera_label.configure(image=imgtk)

            # Repeat after an interval to get the next frame.
            camera_label.after(10, update_frame)

    update_frame()  # Start the loop
    # Call the callback if provided after initializing the camera
    if callback:
        callback()
