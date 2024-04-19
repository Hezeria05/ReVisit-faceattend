#Page Utils
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path

# Constants
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")

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

def set_background_image(window, image_path, size=(1200, 800)):
    """Sets the background image for a given window."""
    bg_image_orig = Image.open(image_path)
    resized_bgimage = bg_image_orig.resize(size)
    bg_image_tk = ImageTk.PhotoImage(resized_bgimage)
    bg_image_label = CTkLabel(window, image=bg_image_tk)
    bg_image_label.place(relwidth=1, relheight=1)
    bg_image_label.image = bg_image_tk

def check_entries_complete(entries, match_label, createbtn):
    """Check if all entry fields are completed."""
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