import tkinter as tk
import cv2
from customtkinter import *
from PageUtils import create_asterisk, check_sign_complete, validate_full_name
from face_registration import face_register
from PIL import Image, ImageTk

def on_register_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):
    RegVframe = CTkFrame(homepage_window, fg_color="white")
    RegVframe.grid(row=1, column=1, sticky="nsew")
    RegVHeading = CTkLabel(RegVframe, text="Face Registration", font=("Inter", 35, "bold"), text_color="#333333")
    RegVHeading.place(relx=0.043, rely=0.06)
    RCameraFrame = CTkFrame(RegVframe, fg_color="white", width=680, height=480, border_color="#B9BDBD", border_width=2)
    RCameraFrame.place(relx=0.5, rely=0.5, anchor='center')
    cap = None  # Placeholder for the camera object

 

if __name__ == "__main__":
    app = tk.Tk()
    on_register_click(app)
    app.mainloop()
