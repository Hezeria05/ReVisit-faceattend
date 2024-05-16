from tkinter import *
import tkinter as tk
from customtkinter import *
import cv2
from face_recognition import load_face_data
from PageUtils import ASSETS_PATH, set_icon_image, create_asterisk, check_sign_complete, indicate, view_history
from dy_PageUtils import (configure_frame, validate_length, validate_full_name,
                          check_sign_complete, change_border_color)
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from PageVisitor import Visitor_page
from VisitorLogOut import on_logout_click
import ttkbootstrap as tb

def on_login_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):

    # Main registration frame
    LogInVframe = CTkFrame(homepage_window, fg_color="white")
    LogInVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(LogInVframe, [3,10,2,1], [1,9,1,8,1])
    # # Heading
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.043, rely=0.06)

    CameraFrame = CTkFrame(LogInVframe, fg_color="white", border_color="#B9BDBD", border_width=2)
    CameraFrame.grid(row=1, column=1, sticky="nsew")
    BscanFrame = CTkFrame(LogInVframe, fg_color="white")
    BscanFrame.grid(row=2, column=1, sticky="nsew")
    scanbtn = CTkButton(BscanFrame, text="SCAN", width=140, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 18, "bold"), text_color="#333333", state="disabled")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')

    # Entry frame for name input
    LogInEframe = CTkFrame(LogInVframe, fg_color="#E9F3F2", corner_radius=10, border_color="#B9BDBD", border_width=2)
    LogInEframe.grid(row=1, column=3, rowspan=2, sticky="nsew")
    configure_frame(LogInEframe, [5,4,4,4,1,8], [1,6,1])
    LogInHeading =CTkLabel(LogInEframe, text='Login', fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LogInHeading.place(relx=0.5, rely=0.08, anchor='n')
    Vnamef = CTkFrame (LogInEframe, fg_color="light pink")
    Vnamef.grid(row=1,column=1,sticky="nsew", pady=3)

    Residf = CTkFrame (LogInEframe, fg_color="light pink")
    Residf.grid(row=2,column=1,sticky="nsew", pady=3)

    Purposef= CTkFrame (LogInEframe, fg_color="light pink")
    Purposef.grid(row=3,column=1,sticky="nsew", pady=3)

    submitbtn = CTkButton(LogInEframe, text="SUBMIT", width=140, height=50, corner_radius=10, fg_color="#ADCBCF",
                          hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.8, anchor='n')

