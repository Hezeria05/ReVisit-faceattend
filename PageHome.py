from customtkinter import *
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime
from VisitorFaceReg import on_register_click
from VisitorLogIn import on_login_click

def on_logout_click():
    print("Logout button clicked!")

# Function to create a frame for the register, login, and logout sections
def create_section_frame(parent, title, icon_path, button_text, button_command,relx, rely,
                         has_status=False, bgy=0.165, btny=0.66, lby=0.065):
    section_frame = CTkFrame(parent, fg_color="#E9F3F2", width=280, height=410 if has_status else 340, corner_radius=10,
                             border_color="#B9BDBD", border_width=2)
    section_frame.place(relx=relx, rely=rely)
    
    label = CTkLabel(section_frame, fg_color="transparent", text=title, font=("Arial", 20, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=lby, anchor="n")

    icon_bg = CTkFrame(section_frame, fg_color="white", width=180, height=160, corner_radius=10)
    icon_bg.place(relx=0.5, rely=bgy, anchor='n')
    set_icon_image(icon_bg, icon_path, relx=0.5, rely=0.5, anchor='center', size=(135, 135))
    
    button = CTkButton(section_frame, text=button_text, font=("Inter", 20, "bold"), hover_color="#93ACAF", text_color="#333333", 
                       width=220, height=40, fg_color="#ADCBCF", corner_radius=5,  command=button_command)
    button.place(relx=0.5, rely=btny, anchor='n')
    
    if has_status:
        status_bg = CTkFrame(section_frame, fg_color="white", width=220, height=68, corner_radius=10)
        status_bg.place(relx=0.5, rely=0.8, anchor='n')

    return section_frame

# Function to create a frame for the total number of visitors
def create_info_frame(parent, text, width, height, relx, rely):
    info_frame = CTkFrame(parent, fg_color="#E9F3F2", width=width, height=height, corner_radius=10,
                          border_color="#B9BDBD", border_width=2)
    info_frame.place(relx=relx, rely=rely)
    
    label = CTkLabel(info_frame, fg_color="transparent", text=text, font=("Arial", 15, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=0.125, anchor="n")
    
    return info_frame

def Home_page(homepage_window, sec_id):
    Homeframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    Homeframe.place(relx=0.266, rely=0.118)

    HomeHeading = CTkLabel(Homeframe, text="Welcome to Home Page!", font=("Inter", 35, "bold"), text_color="#333333" )
    HomeHeading.place(relx=0.043, rely=0.06)

    # Create register, login, logout sections
    Registerframe = create_section_frame(Homeframe, "REGISTER", ASSETS_PATH / 'register_icon.png', "REGISTER",
                                     lambda: on_register_click(homepage_window), 0.043, 0.36, bgy=0.2, btny=0.8, lby=0.08)
    Loginframe = create_section_frame(Homeframe, "LOG IN", ASSETS_PATH / 'login_icon.png', "LOG IN", lambda: on_login_click(homepage_window, sec_id),
                                      0.363, 0.36, has_status=True)
    Logoutframe = create_section_frame(Homeframe, "LOG OUT", ASSETS_PATH / 'logout_icon.png', "LOG OUT", lambda:on_logout_click(homepage_window),
                                       0.683, 0.36, has_status=True)

    # Create frames for additional information
    Totalframe = create_info_frame(Homeframe, "Total Number of Visitors Today", 280, 92, 0.043, 0.18)
    DateTimeframe = create_info_frame(Homeframe, "", 280, 102, 0.683, 0.05)

    # Configure date and time display
    time_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Arial", 28, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")

    date_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Inter", 14, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.52, anchor="n")
    set_icon_image(DateTimeframe, ASSETS_PATH / 'calendar_icon.png', relx=0.75, rely=0.09, anchor='n', size=(75, 75))

    # Update date and time periodically
    update_datetime(date_label, time_label)
    homepage_window.after(1000, lambda: update_datetime(date_label, time_label))
