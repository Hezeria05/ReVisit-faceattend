import tkinter as tk
import cv2
from customtkinter import *
from PIL import Image, ImageTk
from dy_PageUtils import (configure_frame, create_image_label, validate_all, check_sign_complete)
from face_registration import face_register
import os

def on_register_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):
    RegVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    RegVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(RegVframe, [2, 8, 1, 2], [1, 4, 1])
    RegVHeading = CTkLabel(RegVframe, text="Face Registration", font=("Inter", 35, "bold"), text_color="#333333")
    RegVHeading.place(relx=0.043, rely=0.06)
    RCameraFrame = CTkFrame(RegVframe, fg_color="white", border_color="#B9BDBD", border_width=2)
    RCameraFrame.grid(row=1, column=1, sticky="nsew", padx=50)
    configure_frame(RCameraFrame, [1], [1])
    cap = None  # Placeholder for the camera object

    def setup_entry_frame():
        global Vname
        vname_text = tk.StringVar()
        Entryframe = CTkFrame(RegVframe, fg_color="#E9F3F2", corner_radius=10, border_color="#B9BDBD", border_width=2)
        Entryframe.grid(row=1, column=1, sticky="nsew", padx=150, pady=120)
        configure_frame(Entryframe, [2, 2, 1, 2, 1], [1, 8, 1])
        Vname = CTkEntry(Entryframe, textvariable=vname_text, corner_radius=8, border_width=1.5, border_color='#ADCBCF')
        Vname.grid(row=1, column=1, sticky="nsew")
        Vname.bind("<KeyRelease>", lambda event: vname_text.set(Vname.get().upper()))
        Vname.bind("<KeyPress>", lambda event: validate_all(event, Vname, 50, 1))
        Lvnameimage = create_image_label(Entryframe, 'vname_astrsk.png', 134, 16, 0.1, 0.17)
        Existinglabel = CTkLabel(Entryframe, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
        Existinglabel.grid(row=2, column=1, sticky="nw", pady=2)

        def submit_and_destroy():
            face_name = Vname.get()
            dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"

            # Check if a file with the same name already exists
            if os.path.isfile(os.path.join(dirpath, face_name + '.npy')):
                Existinglabel.configure(text='Already Existing!')
            else:
                Cwarnlabel = CTkLabel(RegVframe, text="* Please center the visitor's face and make sure the frame is free of obstructions.", font=("Inter", 11), text_color="red")
                Cwarnlabel.grid(row=1, column=1, sticky="sew")
                Entryframe.destroy()
                nonlocal cap
                camera_label = CTkLabel(RCameraFrame, text="")
                camera_label.grid(row=0, column=0, sticky="nsew")

                cap = cv2.VideoCapture(0)  # Initialize the camera

                attempt_counter = 0  # Counter to keep track of attempts

                def show_frame():
                    nonlocal attempt_counter
                    try:
                        ret, frame = cap.read()  # Assuming 'cap' is your cv2.VideoCapture object
                        if not ret:
                            raise ValueError("Failed to capture frame")
                        
                        print("success")
                        attempt_counter = 0

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

                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                        img = Image.fromarray(cv2image)
                        imgtk = ImageTk.PhotoImage(image=img)
                        camera_label.imgtk = imgtk  # Keep a reference, avoid garbage collection
                        camera_label.configure(image=imgtk)
                        camera_label.after(10, show_frame)  # Refresh the frame on the label every 10 ms
                    except Exception as e:
                        attempt_counter += 1
                        print(f"fail: {e}")
                        if attempt_counter >= 5:
                            cap.release()  # Release the camera
                            RegVframe.destroy()
                            on_register_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct)
                        else:
                            camera_label.after(3000, show_frame)  # Try again after 3 seconds

                show_frame()
                scanbtn.configure(state="normal")
                scanbtn.configure(command=lambda: face_register(face_name, scanbtn, RegVframe, RCameraFrame, Entryframe, homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, cap, on_register_click))

        submitbtn = CTkButton(Entryframe, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                              hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state="disabled", command=submit_and_destroy)
        submitbtn.place(relx=0.48, rely=0.745, anchor="e")
        cancelbtn = CTkButton(Entryframe, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                              hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848", command=lambda: RegVframe.destroy())
        cancelbtn.place(relx=0.52, rely=0.745, anchor="w")
        entries = [Vname]
        for entry in entries:
            entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))

    homepage_window.after(300, setup_entry_frame)

    scanbtn = CTkButton(RegVframe, text="Scan", width=140, height=60, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 25, "bold"), text_color="#333333", state="disabled")
    scanbtn.place(relx=0.5, rely=0.845, anchor='n')
