#Page Utils
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from db_con import register_security_admin
from datetime import datetime


# Constants
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")

#General
def set_background_image(window, image_path, size):
    # """Sets the background image for a given window."""
    bg_image_orig = Image.open(image_path)
    resized_bgimage = bg_image_orig.resize(size)
    bg_image_tk = ImageTk.PhotoImage(resized_bgimage)
    bg_image_label = CTkLabel(window, image=bg_image_tk, text='')
    bg_image_label.place(relwidth=1, relheight=1)
    # bg_image_label.image = bg_image_tk

#Register and Sign In
# Globals to hold the eye images (to avoid loading them multiple times)
open_eye_tk = None
close_eye_tk = None

def initialize_eye_icons():
    global open_eye_tk, close_eye_tk
    open_eye = Image.open(ASSETS_PATH / 'Eye_Open.png')
    close_eye = Image.open(ASSETS_PATH / 'Eye_Close.png')
    open_eye_tk = ImageTk.PhotoImage(open_eye)
    close_eye_tk = ImageTk.PhotoImage(close_eye)

def toggle_password_visibility(password_entry, eye_button, is_hidden):
    """Toggle the visibility of a password entry."""
    if is_hidden:
        eye_button.configure(image=open_eye_tk)
        password_entry.configure(show="")
        return False  # Password is now visible
    else:
        eye_button.configure(image=close_eye_tk)
        password_entry.configure(show="*")
        return True  # Password is now hidden

def create_password_toggle_button(password_entry, parent_frame, relx, y, anchor='n'):
    """Create a password toggle visibility button and attach it next to a password entry."""
    global open_eye_tk, close_eye_tk
    # Initialize eye icons if not already done
    if open_eye_tk is None or close_eye_tk is None:
        initialize_eye_icons()
    eye_button = CTkButton(parent_frame, image=close_eye_tk, text='', width=30, fg_color='#F9F9FA', hover_color="#F9F9FA", cursor='hand2')
    eye_button.place(relx=relx, y=y, anchor=anchor)
    eye_button.is_hidden = True
    eye_button.configure(command=lambda: setattr(eye_button, 'is_hidden', toggle_password_visibility(password_entry, eye_button, eye_button.is_hidden)))
    return eye_button

def manage_asterisk(entry_widget, asterisk_label, relx, y, anchor):
    if entry_widget.get():
        asterisk_label.place_forget()
    else:
        asterisk_label.place(relx=relx, y=y, anchor=anchor)

def create_asterisk(entry_widget, parent_frame, relx, y, anchor):
    asterisk_image_orig = Image.open(ASSETS_PATH / 'asterisk.png')
    resized_asterisk_image = asterisk_image_orig.resize((7, 7))
    asterisk_image_tk = ImageTk.PhotoImage(resized_asterisk_image)
    asterisk_label = CTkLabel(parent_frame, image=asterisk_image_tk, text='')
    asterisk_label.image = asterisk_image_tk  # Keep a reference!
    manage_asterisk(entry_widget, asterisk_label, relx, y, anchor)
    entry_widget.bind("<KeyRelease>", lambda event: manage_asterisk(entry_widget, asterisk_label, relx, y, anchor))

#Sign In Page
def check_sign_complete(entries, signbtn):
    # """Check if all entry fields are completed."""
    for entry in entries:
        if not entry.get():
            disable_submit_button(signbtn)
            return False
    enable_submit_button(signbtn)
    return True


#Registration of Account Page
def check_entries_complete(entries, match_label, createbtn):
    # """Check if all entry fields are completed."""
    for entry in entries:
        if not entry.get():
            disable_submit_button(createbtn)
            return False
    enable_submit_button(createbtn)
    return True

def check_password_match(Epassword, Ecpassword, match_label, createbtn):
    password = Epassword.get()
    confirm_password = Ecpassword.get()

    if password and confirm_password:
        if password == confirm_password:
            match_label.configure(text="Password matched", text_color="green")
        else:
            match_label.configure(text="Password not matched", text_color="red")
            disable_submit_button(createbtn)
    else:
        match_label.configure(text="")
        disable_submit_button(createbtn)

def enable_submit_button(button):
    button.configure(state="normal")

def disable_submit_button(button):
    button.configure(state="disabled")

def register_user(efullname, eusername, epassword, ecpassword, register_window):
    full_name = efullname.get()
    username = eusername.get()
    password = epassword.get()
    confirm_password = ecpassword.get()

    if password == confirm_password:
        success = register_security_admin(full_name, username, password)
        register_window.destroy()  # Destroy the window first
        if success:
            messagebox.showinfo("Success", "User registered successfully")
        else:
            messagebox.showerror("Error", "Failed to register user")
    else:
        messagebox.showerror("Error", "Password and confirm password do not match")

#Main Page
def set_icon_image(frame, image_path, relx, rely, anchor, size):
    icon_image_orig = Image.open(image_path)
    resized_iconimage = icon_image_orig.resize(size)
    icon_image_tk = ImageTk.PhotoImage(resized_iconimage)
    icon_image_label = CTkLabel(frame, image=icon_image_tk, text='')
    icon_image_label.place(relx=relx, rely=rely, anchor=anchor)

def hide_indicators(Home_indct, Visitor_indct, Resident_indct):
    Home_indct.configure(fg_color="#FEFEFE")
    Visitor_indct.configure(fg_color="#FEFEFE")
    Resident_indct.configure(fg_color="#FEFEFE")

def indicate(selected_indicator, new_page, Home_indct, Visitor_indct, Resident_indct):
    # Pass all indicator labels to hide_indicators
    hide_indicators(Home_indct, Visitor_indct, Resident_indct)
    selected_indicator.configure(fg_color="#00507E")  # Update the active indicator color
    new_page()

def logout(window):
    window.destroy()

#Home Page
def update_datetime(date_label, time_label):
    # Get the current date and time
    now = datetime.now()

    # Format date as "Month Day, Year"
    formatted_date = now.strftime("%B %d, %Y")

    # Format time as "Hour:Minute:Second AM/PM"
    formatted_time = now.strftime("%I:%M %p")

    # Update the text of the labels with the current date and time
    date_label.configure(text=formatted_date)
    time_label.configure(text=formatted_time)

    #Log in Visitor Page
def view_history(sec_id, LogVframe, logsucess, ASSETS_PATH, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct):
    LogSucessfr = CTkFrame(LogVframe, fg_color="white", width=700, height=350, border_color="#B9BDBD", border_width=2, corner_radius=10)
    LogSucessfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(LogSucessfr, ASSETS_PATH / 'success_icon.png', relx=0.5, rely=0.15, anchor='n', size=(95, 95))
    
    LbSuccess = CTkLabel(LogSucessfr, text=logsucess, fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.48, anchor='n')
    
    viewbtn = CTkButton(LogSucessfr, text="View History", width=230, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333")
    viewbtn.place(relx=0.3, rely=0.8, anchor='center')
    
    donebtn = CTkButton(LogSucessfr, text="Done", width=230, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333")
    donebtn.place(relx=0.7, rely=0.8, anchor='center')
    
    viewbtn.configure(command=lambda: indicate(Visitor_indct, lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct), Home_indct, Visitor_indct, Resident_indct))
    donebtn.configure(command=lambda: LogVframe.destroy())
