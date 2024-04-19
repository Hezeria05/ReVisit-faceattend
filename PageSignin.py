#Page Sign in
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, ASSETS_PATH

def open_signin_window(main_window):
    signin_window = CTkToplevel(main_window)
    signin_window.geometry('1200x800+400+100')
    signin_window.title('Sign In')
    signin_window.grab_set()

    # Background for the new window
    set_background_image(signin_window, ASSETS_PATH / 'USER ENTRY.png')

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

     #Eye Toggle
    create_password_toggle_button(Epassword, SignFrame, relx=0.82, y=330, anchor='n')

    # Sign-in button
    createbtn = CTkButton(SignFrame, text="Sign In", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333")
    createbtn.place(relx=0.6, rely=0.75)
    # Back button that closes this window and shows the main window
    back_button = CTkButton(SignFrame, text="Back", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", command=signin_window.destroy)
    back_button.place(relx=0.6, rely=0.85)


