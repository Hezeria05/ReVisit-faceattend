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
    
    Register_label = CTkLabel(Registerframe, fg_color="transparent",text="REGISTER", font=("Arial", 20, "bold"), text_color="#333333")
    Register_label.place(relx=0.5, rely=0.08, anchor="n")

    RegIconbg = CTkFrame(Registerframe, fg_color="white", width=180, height=160, corner_radius=10)
    RegIconbg.place(relx=0.5, rely=0.2, anchor='n')

    set_icon_image(RegIconbg, ASSETS_PATH / 'register_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    
    RegBtn = CTkButton(Registerframe, text="REGISTER", font=("Inter", 20, "bold"), hover_color="#93ACAF",text_color="#333333", 
                       width=220, height=40, fg_color="#ADCBCF", corner_radius=5)
    RegBtn.place(relx=0.5, rely=0.8, anchor='n')

    #__________________________________________________________________________________________________________________
    Loginframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=410, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Loginframe.place(relx=0.363, rely=0.36)
    
    Login_label = CTkLabel(Loginframe, fg_color="transparent",text="LOG IN", font=("Arial", 20, "bold"), text_color="#333333")
    Login_label.place(relx=0.5, rely=0.065, anchor="n")

    LoginIconbg = CTkFrame(Loginframe, fg_color="white", width=180, height=160, corner_radius=10)
    LoginIconbg.place(relx=0.5, rely=0.165, anchor='n')

    set_icon_image(LoginIconbg, ASSETS_PATH / 'login_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    
    LoginBtn = CTkButton(Loginframe, text="LOG IN", font=("Inter", 20, "bold"), hover_color="#93ACAF",text_color="#333333", 
                       width=220, height=40, fg_color="#ADCBCF", corner_radius=5)
    LoginBtn.place(relx=0.5, rely=0.66, anchor='n')
    
    LoginStatbg = CTkFrame(Loginframe, fg_color="white", width=220, height=68, corner_radius=10)
    LoginStatbg.place(relx=0.5, rely=0.8, anchor='n')
    #__________________________________________________________________________________________________________________
    Logoutframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=410, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Logoutframe.place(relx=0.683, rely=0.36)
    
    Logout_label = CTkLabel(Logoutframe, fg_color="transparent",text="LOG OUT", font=("Arial", 20, "bold"), text_color="#333333")
    Logout_label.place(relx=0.5, rely=0.065, anchor="n")

    LogoutIconbg = CTkFrame(Logoutframe, fg_color="white", width=180, height=160, corner_radius=10)
    LogoutIconbg.place(relx=0.5, rely=0.165, anchor='n')

    set_icon_image(LogoutIconbg, ASSETS_PATH / 'logout_icon.png', relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    
    LogoutBtn = CTkButton(Logoutframe, text="LOG OUT", font=("Inter", 20, "bold"), hover_color="#93ACAF",text_color="#333333", 
                       width=220, height=40, fg_color="#ADCBCF", corner_radius=5)
    LogoutBtn.place(relx=0.5, rely=0.66, anchor='n')

    LogoutStatbg = CTkFrame(Logoutframe, fg_color="white", width=220, height=68, corner_radius=10)
    LogoutStatbg.place(relx=0.5, rely=0.8, anchor='n')






    #__________________________________________________________________________________________________________________
    Totalframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=280, height=92, corner_radius=10,
                    border_color="#B9BDBD", border_width=2)
    Totalframe.place(relx=0.043, rely=0.18)
    
    Total_label = CTkLabel(Totalframe, fg_color="transparent",text="Total Number of Visitors Today", font=("Arial", 15, "bold"), text_color="#333333")
    Total_label.place(relx=0.5, rely=0.125, anchor="n")

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

