from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import set_background_image, ASSETS_PATH, set_icon_image, logout


def Resident_page(homepage_window):
    Residentframe = CTkFrame(homepage_window, fg_color="purple", width=1057, height=715)
    Residentframe.place(relx=0.266, rely=0.118)

    ResidentHeading = CTkLabel(Residentframe, text="Resident's List", font=("Inter", 35, "bold"),text_color="white" )
    ResidentHeading.place(relx=0.043, rely=0.06)
