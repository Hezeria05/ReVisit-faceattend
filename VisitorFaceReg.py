import tkinter as tk
from customtkinter import *
from tkinter import simpledialog, Canvas
import cv2
from PIL import Image, ImageTk
import os
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime, create_asterisk, check_sign_complete

def on_register_click(homepage_window):
    # Main registration frame
    RegVframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    RegVframe.place(relx=0.266, rely=0.118)

    # Heading
    RegVHeading = CTkLabel(RegVframe, text="Face Registration", font=("Inter", 35, "bold"), text_color="#333333")
    RegVHeading.place(relx=0.043, rely=0.06)
    
    # Entry frame for name input
    Entryframe = CTkFrame(RegVframe, fg_color="#E9F3F2", width=600, height=220, corner_radius=10,
                             border_color="#B9BDBD", border_width=2)
    Entryframe.place(relx=0.5, rely=0.35, anchor='n')
    
    Vname = CTkEntry(Entryframe, width=485.0, height=50, placeholder_text="Enter Visitor Name", corner_radius=8, border_width=1, border_color='#DEE6EA')
    Vname.place(relx=0.5, rely=0.35, anchor='n')

    LVname = CTkLabel(Entryframe, text='Visitor Name', fg_color="transparent", font=("Inter", 20, "bold"), text_color="#333333")
    LVname.place(relx=0.2, rely=0.18, anchor='n')

    create_asterisk(Vname, Entryframe, relx=0.314, y=32, anchor='n')

    submitbtn = CTkButton(Entryframe, text="Submit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.7, anchor='n')

    # Validation and submission
    entries = [Vname]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))
    submitbtn.configure(command=lambda: try_opencamera(Vname.get(), RegVframe, Entryframe))

def try_opencamera(visitor_name, RegVframe, Entryframe):

        Entryframe.destroy()  # Remove the entry frame after name is submitted
        # Setup camera frame within the registration frame
        camera_frame = CTkFrame(RegVframe, fg_color="#E9F3F2", width=600, height=450, corner_radius=10)
        camera_frame.place(relx=0.5, rely=0.2, anchor='n')
        canvas = Canvas(camera_frame, width=590, height=440, bg='black')
        canvas.pack()

        # Initialize and check camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Failed to open camera.")
            return

        def update_frame():
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame.")
                return
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame_image = ImageTk.PhotoImage(image=frame)
            canvas.create_image(0, 0, image=frame_image, anchor=tk.NW)
            canvas.image = frame_image  # Keep reference to prevent garbage-collection
            camera_frame.after(10, update_frame)

        update_frame()

# Main application setup
if __name__ == "__main__":
    app = tk.Tk()
    on_register_click(app)
    app.mainloop()
