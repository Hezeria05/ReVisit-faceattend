from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, ASSETS_PATH, check_sign_complete, signin_failed
from db_con import validate_login_credentials
from  MainPage import open_homepage

def open_signin_window(select_window):
    signin_window = CTkToplevel(select_window)
    signin_window.geometry('1200x800+400+100')
    signin_window.title('Sign In')
    signin_window.grab_set()
    signin_window.minsize(800, 400)
    signin_window.maxsize(1200, 800)

    # Background for the new window
    set_background_image(signin_window, ASSETS_PATH / 'USER ENTRY.png',size=(1200, 800))

    # Create the sign-in frame
    SignFrame = CTkFrame(signin_window, width=530, height=600, fg_color="#F0F6F9")
    SignFrame.place(x=555, y=100)

    # Add components to sign-in frame
    heading = CTkLabel(SignFrame, text='Sign In', fg_color="#F0F6F9", font=("Inter", 35, "bold"), text_color="#333333")
    heading.place(relx=0.5, y=75, anchor='n')

    Eusername = CTkEntry(SignFrame, width=420.0, height=45.0, placeholder_text="Enter Username", corner_radius=8, border_width=1, border_color='#DEE6EA')
    Eusername.place(relx=0.5, y=230, anchor='n')
    Lusername = CTkLabel(SignFrame, text='Username', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lusername.place(relx=0.17, y=200, anchor='n')
    create_asterisk(Eusername, SignFrame, relx=0.250, y=198, anchor='n')

    Epassword = CTkEntry(SignFrame, width=420.0, height=45.0, placeholder_text="Enter Password", corner_radius=8, border_width=1, border_color='#DEE6EA', show="*")
    Epassword.place(relx=0.5, y=320, anchor='n')
    Lpassword = CTkLabel(SignFrame, text='Password', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lpassword.place(relx=0.17, y=290, anchor='n')
    create_asterisk(Epassword, SignFrame, relx=0.250, y=288, anchor='n')

    # Eye Toggle
    create_password_toggle_button(Epassword, SignFrame, relx=0.82, y=330, anchor='n')

    def validate_and_open_homepage():
        username = Eusername.get()
        password = Epassword.get()
        success, sec_id = validate_login_credentials(username, password)
        if success:
            select_window.destroy()  # Destroy the select window
            open_homepage(sec_id)  # Pass sec_id as an argument
            signin_window.after(100, signin_window.destroy)
        else:
            signin_failed(signin_window)

    # Sign-in button
    signbtn = CTkButton(SignFrame, text="Sign In", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    signbtn.place(relx=0.5, rely=0.75, anchor="center")

     # Bind the validation function to entry events
    entries = [Eusername, Epassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, signbtn))

    signbtn.configure(command=validate_and_open_homepage)

    # Back button that closes this window and shows the main window
    back_button = CTkButton(SignFrame, text="Back", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", command=signin_window.destroy)
    back_button.place(relx=0.5, rely=0.83, anchor="center")
