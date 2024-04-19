from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime
from datetime import datetime



def Home_page(homepage_window):

    Homeframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    Homeframe.place(relx=0.266, rely=0.118)

    HomeHeading = CTkLabel(Homeframe, text="Welcome to Home Page!", font=("Inter", 35, "bold"),text_color="#333333" )
    HomeHeading.place(relx=0.043, rely=0.06)

    #__________________________________________________________________________________________________________________

    Registerframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=340, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Registerframe.place(relx=0.043, rely=0.36)


    RegIconbg = CTkFrame(Registerframe, fg_color="white", width=180, height=160, corner_radius=10)
    RegIconbg.place(relx=0.5, rely=0.2, anchor='n')

    set_icon_image(RegIconbg, ASSETS_PATH / 'register_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    #__________________________________________________________________________________________________________________
    Loginframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=410, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Loginframe.place(relx=0.363, rely=0.36)

    LoginIconbg = CTkFrame(Loginframe, fg_color="white", width=180, height=160, corner_radius=10)
    LoginIconbg.place(relx=0.5, rely=0.165, anchor='n')

    set_icon_image(LoginIconbg, ASSETS_PATH / 'login_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    #__________________________________________________________________________________________________________________
    Logoutframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=410, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Logoutframe.place(relx=0.683, rely=0.36)

    LogoutIconbg = CTkFrame(Logoutframe, fg_color="white", width=180, height=160, corner_radius=10)
    LogoutIconbg.place(relx=0.5, rely=0.165, anchor='n')

    set_icon_image(LogoutIconbg, ASSETS_PATH / 'logout_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    #__________________________________________________________________________________________________________________
    Totalframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=92, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Totalframe.place(relx=0.043, rely=0.18)

    #__________________________________________________________________________________________________________________
    DateTimeframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=102, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    DateTimeframe.place(relx=0.683, rely=0.05)

    # Create a label to display the time
    time_label = CTkLabel(DateTimeframe, fg_color="transparent",text="", font=("Arial", 28, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")

    date_label = CTkLabel(DateTimeframe, fg_color="transparent",text="", font=("Inter", 14, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.52, anchor="n")
    set_icon_image(DateTimeframe, ASSETS_PATH / 'calendar_icon.png', relx=0.75, rely=0.09, anchor='n', size=(75, 75))
    # Update the date and time labels initially
    update_datetime(date_label, time_label)
    # Update the date and time labels every second
    homepage_window.after(1000, lambda: update_datetime(date_label, time_label))

