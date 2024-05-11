#Page Utils
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from db_con import register_security_admin, fetch_resident_data, update_resident_data
from datetime import datetime


# Constants
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")

#General_____________________________________________________________________________________________________________
def set_background_image(window, image_path, size):
    # """Sets the background image for a given window."""
    bg_image_orig = Image.open(image_path)
    resized_bgimage = bg_image_orig.resize(size)
    bg_image_tk = ImageTk.PhotoImage(resized_bgimage)
    bg_image_label = CTkLabel(window, image=bg_image_tk, text='')
    bg_image_label.place(relwidth=1, relheight=1)
    # bg_image_label.image = bg_image_tk

def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"


#Register and Sign In_____________________________________________________________________________________________________________
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

#Sign In Page_____________________________________________________________________________________________________________
def check_sign_complete(entries, signbtn):
    # """Check if all entry fields are completed."""
    for entry in entries:
        if not entry.get():
            disable_submit_button(signbtn)
            return False
    enable_submit_button(signbtn)
    return True

def signin_failed(signin_window):
    LogFailfr = CTkFrame(signin_window, fg_color="white", width=650, height=280, border_color="#B9BDBD", border_width=2, corner_radius=10)
    LogFailfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(LogFailfr, ASSETS_PATH / 'warning_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))

    LbSuccess = CTkLabel(LogFailfr, text="Invalid Username or Password", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')

    # Destroy the frame after 3 seconds
    signin_window.after(2000, LogFailfr.destroy)


#Registration of Account Page_____________________________________________________________________________________________________________
def check_entries_complete(entries, ecp_label, createbtn, Epassword, Ecpassword):
    all_complete = True
    for entry in entries:
        if not entry.get().strip():  # Check if any field is empty
            all_complete = False
            break

    if all_complete:
        check_password_match(Epassword, Ecpassword, ecp_label, createbtn)  # Call password match check when all fields are complete
    else:
        disable_submit_button(createbtn)  # Disable button if any field is empty

# New function to handle input in the "Password" field
def handle_password_input(Epassword, Ecpassword, ecp_label, createbtn, ep_label):
    password = Epassword.get().strip()

    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        ep_label.configure(text="", text_color="red")
        Ecpassword.configure(state="normal")  # Enable "Confirm Password" field
        check_password_match(Epassword, Ecpassword, ecp_label, createbtn)  # Continue to check password match
    else:
        Ecpassword.configure(state="disabled")  # Keep "Confirm Password" field disabled
        ep_label.configure(text="Password must be at least 8 characters long", text_color="red")
        disable_submit_button(createbtn)  # Ensure submit button is disabled

def check_password_match(Epassword, Ecpassword, ecp_label, createbtn):
    password = Epassword.get().strip()
    confirm_password = Ecpassword.get().strip()

    if password and confirm_password:
        if password == confirm_password:
            ecp_label.configure(text="Passwords match", text_color="green")
            enable_submit_button(createbtn)  # Enable button if passwords match
        else:
            ecp_label.configure(text="Passwords do not match", text_color="red")
            disable_submit_button(createbtn)  # Disable button if passwords do not match
    else:
        ecp_label.configure(text="")  # Clear any previous messages
        disable_submit_button(createbtn)

def enable_submit_button(button):
    button.configure(state="normal")

def disable_submit_button(button):
    button.configure(state="disabled")

def display_success_and_close(register_window):
    RegisScssfr = CTkFrame(register_window, fg_color="white", width=650, height=280, border_color="#B9BDBD", border_width=2, corner_radius=10)
    RegisScssfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(RegisScssfr, ASSETS_PATH / 'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
    LbSuccess = CTkLabel(RegisScssfr, text="Registered Successfully", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
    register_window.after(2000, register_window.destroy)

#Main Page_____________________________________________________________________________________________________________
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

def logout(window, btn):
    LogoutModal = CTkFrame(window, fg_color="white", width=650, height=350, border_color="#B9BDBD", border_width=2, corner_radius=10)
    LogoutModal.place(relx=0.634, rely=0.5, anchor='center')
    set_icon_image(LogoutModal, ASSETS_PATH / 'question_icon.png', relx=0.5, rely=0.13, anchor='n', size=(110, 110))
    LbOut = CTkLabel(LogoutModal, text="Continue to Logout?", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbOut.place(relx=0.5, rely=0.5, anchor='n')
    contbtn = CTkButton(LogoutModal, text="Continue", width=250, height=50, corner_radius=10,
                        fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333",
                        command=lambda:window.destroy())
    contbtn.place(relx=0.725, rely=0.8, anchor='center')

    cancelbtn = CTkButton(LogoutModal, text="Cancel", width=250, height=50, corner_radius=10,
                      fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333",
                      command=lambda: (LogoutModal.destroy(), btn.configure(state='normal')))
    cancelbtn.place(relx=0.275, rely=0.8, anchor='center')

#Home Page_____________________________________________________________________________________________________________
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

#Log in Visitor Page_____________________________________________________________________________________________________________
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


# Visitor Page

def hide_btn( btn1, btn2, btn3, btn4):
    btn1.configure(fg_color="#FEFEFE")
    btn2.configure(fg_color="#FEFEFE")
    btn3.configure(fg_color="#FEFEFE")
    btn4.configure(fg_color="#FEFEFE")

def btnind(selected_btn, btn1, btn2, btn3, btn4):
    # Pass all indicator labels to hide_indicators
    hide_btn(btn1, btn2, btn3, btn4)
    selected_btn.configure(fg_color="#93ACAF")

#ResidentPage_____________________________________________________________________________________________________________
def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

def validate_phone_number(event):
    if event.keysym in ('BackSpace', 'Delete', 'Left', 'Right', 'Tab'):
        return True
    elif event.char.isdigit():
        current_text = event.widget.get()
        selection_length = len(event.widget.selection_get()) if event.widget.selection_present() else 0
        if len(current_text) - selection_length + 1 <= 11:
            return True
        else:
            return "break"
    else:
        return "break"

def create_resident_table(Residentframe, resident_data):
    entries_list = []
    id_list = []  # Separate list to store res_ids
    for i, data_row in enumerate(resident_data):
        y_offset = 0.234 + (i * 0.0375)
        entries = []
        res_id = data_row[0]  # First element is res_id
        row_data = data_row[1:]  # Skip res_id for display purposes
        for j, value in enumerate(row_data):
            entry = CTkEntry(Residentframe, width=320, height=30, fg_color="white", corner_radius=0, border_width=1)
            entry.place(relx=0.0465 + (j * 0.302), rely=y_offset)
            entry.insert(0, value if value is not None else "")
            entry.configure(state='disabled')
            if j == 0:  # Name field
                entry.bind("<KeyPress>", validate_full_name)
            elif j == 2:  # Phone number field
                entry.bind("<KeyPress>", validate_phone_number)
            entries.append(entry)
        entries_list.append(entries)
        id_list.append(res_id)  # Store res_id separately
    return entries_list, id_list

def toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, is_edit_mode):
    if is_edit_mode:
        edit_btn.configure(text="Save", state='disabled', command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, False))
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='normal')
                # Properly bind the KeyRelease event to validate input
                entry.bind("<KeyRelease>", lambda event, btn=edit_btn, elist=entries_list: on_entry_change(event, btn, elist))
    else:
        edit_btn.configure(text="Edit", command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, True))
        save_edited_data(Residentframe, entries_list, id_list)
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='disabled')
                entry.unbind("<KeyRelease>")

def on_entry_change(event, save_button, entries_list):
    all_valid = True
    for entries in entries_list:
        phone_entry = entries[2]
        if len(phone_entry.get()) < 11:  # Check for valid phone number length
            all_valid = False
            break
    save_button.configure(state='normal' if all_valid else 'disabled')

def save_edited_data(Residentframe, entries_list, id_list):
    for entries, res_id in zip(entries_list, id_list):
        name, address, phone = [entry.get() for entry in entries]
        update_resident_data(Residentframe, res_id, name, address, phone) # This function needs to be implemented in your db_con module
        save_success(Residentframe)


def save_success(window):
    SaveSucessfr = CTkFrame(window, fg_color="white", width=700, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
    SaveSucessfr.place(relx=0.5, rely=0.5, anchor='center')

    # Assuming the function set_icon_image is implemented and ASSETS_PATH is defined correctly
    set_icon_image(SaveSucessfr, ASSETS_PATH / 'success_icon.png', relx=0.5, rely=0.15, anchor='n', size=(95, 95))

    LbSuccess = CTkLabel(SaveSucessfr, text="Saved Successfully!", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.62, anchor='n')

    # Automatically destroy the frame after 3000 milliseconds (3 seconds)
    SaveSucessfr.after(2500, SaveSucessfr.destroy)

