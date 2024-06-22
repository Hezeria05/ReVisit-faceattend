import tkinter as tk
import cv2
import os
from customtkinter import *
from PIL import Image, ImageTk
from dy_PageUtils import (configure_frame, create_image_label, validate_all, check_sign_complete, load_image)
from face_registration import face_register
import os

def on_register_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, ret_vname, logout_btn, home_page, home_button, visitor_button, resident_button):
    RegVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    RegVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(RegVframe, [2, 8, 1, 2], [1, 4, 1])
    backimage = load_image('Back_button.png', (35, 34))
    back_button = CTkButton(RegVframe, image=backimage, text='', fg_color="white", hover_color="white",
                            command=lambda:[home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button), RegVframe.destroy(), cap.release()])
    back_button.place(relx=0.001, rely=0.06, anchor="nw")
    RegVHeading = CTkLabel(RegVframe, text="Face Registration", font=("Inter", 35, "bold"), text_color="#333333")
    RegVHeading.place(relx=0.095, rely=0.06, anchor="nw")
    RCameraFrame = CTkFrame(RegVframe, fg_color="white", border_color="#B9BDBD", border_width=2)
    RCameraFrame.grid(row=1, column=1, sticky="nsew", padx=50)
    configure_frame(RCameraFrame, [1], [1])
    cap = None  # Placeholder for the camera object

    def setup_entry_frame():
        if ret_vname is not None:
            submit_and_destroy(None, None, scanbtn, 1)
        else:
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
            submitbtn = CTkButton(Entryframe, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state="disabled", command=lambda:submit_and_destroy(Entryframe, Existinglabel, scanbtn, 0))
            submitbtn.place(relx=0.52, rely=0.745, anchor="w")
            cancelbtn = CTkButton(Entryframe, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848", command=lambda: home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button))
            cancelbtn.place(relx=0.48, rely=0.745, anchor="e")

            entries = [Vname]
            for entry in entries:
                entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))

    scanbtn = CTkButton(RegVframe, text="Scan", width=140, height=60, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                    font=("Inter", 25, "bold"), text_color="#333333", state="disabled")
    scanbtn.place(relx=0.5, rely=0.845, anchor='n')

    homepage_window.after(300, setup_entry_frame)

    def submit_and_destroy(Entryframe, Existinglabel, scanbtn, entry):
        # Get the directory of the current script and data fodler
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, 'data')
        if entry == 1:
            face_name = ret_vname
        else:
            face_name = Vname.get()
            # Check if a file with the same name already exists
            if os.path.isfile(os.path.join(data_dir, face_name + '.npy')):
                Existinglabel.configure(text='Already Existing!')
                return  # Return early if the name already exists
            else:
                Entryframe.destroy()
        Cwarnlabel = CTkLabel(RegVframe, text="* Please center the visitor's face and make sure the frame is free of obstructions.", font=("Inter", 12), text_color="red")
        Cwarnlabel.grid(row=1, column=1, sticky="sew")
        nonlocal cap
        camera_label = CTkLabel(RCameraFrame, text="")
        camera_label.grid(row=0, column=0, sticky="nsew")

        cap = cv2.VideoCapture(0)  # Initialize the camera
        home_button.configure(state="disabled")
        visitor_button.configure(state="disabled")
        resident_button.configure(state="disabled")
        logout_btn.configure(state="disabled")

        attempt_counter = 0  # Counter to keep track of attempts
        success_counter = 0  # Counter to keep track of successful frames

        def show_frame():
            nonlocal attempt_counter, success_counter
            try:
                ret, frame = cap.read()  # Assuming 'cap' is your cv2.VideoCapture object
                if not ret:
                    raise ValueError("Failed to capture frame")
                # print("success")
                success_counter += 1  # Increment the success counter

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
                imgtk = CTkImage(img, size=(680, 480))
                camera_label.imgtk = imgtk
                camera_label.configure(image=imgtk)

                if success_counter >= 300:  # Check if the counter has reached 30
                    cap.release()  # Release the camera
                    return  # Stop the show_frame function

                camera_label.after(10, show_frame)  # Refresh the frame on the label every 10 ms
            except Exception as e:
                attempt_counter += 1
                if attempt_counter >= 5:
                    cap.release()  # Release the camera
                    RegVframe.destroy()
                else:
                    camera_label.after(3000, show_frame)  # Try again after 3 seconds

        show_frame()
        scanbtn.configure(state="normal")
        scanbtn.configure(command=lambda: face_register(face_name, scanbtn, RegVframe, RCameraFrame, homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, cap, on_register_click, logout_btn, home_page, back_button, home_button, visitor_button, resident_button))