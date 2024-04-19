from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import set_background_image, ASSETS_PATH, set_icon_image, logout


def Visitor_page(homepage_window):
    Visitorframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    Visitorframe.place(relx=0.266, rely=0.118)

    VisitorHeading = CTkLabel(Visitorframe, text="Visitor History", font=("Inter", 35, "bold"),text_color="#333333" )
    VisitorHeading.place(relx=0.043, rely=0.06)
