from customtkinter import *
from PIL import Image
import os
from datetime import datetime

#_______________________________________GENERAL

def configure_frame(frame, row_weights, column_weights):
    for i, weight in enumerate(row_weights):
        frame.rowconfigure(i, weight=weight, uniform='a')

    for i, weight in enumerate(column_weights):
        frame.columnconfigure(i, weight=weight, uniform='a')

def load_image(file_name, size):
    image_path = os.path.join(os.path.dirname(__file__), 'assets', file_name)
    image = CTkImage(light_image=Image.open(image_path), size=size)
    return image

def set_icon_image(frame, image_path, relx, rely, anchor, size):
    icon_image = load_image(image_path, size)
    icon_image_label = CTkLabel(frame, image=icon_image, text='')
    icon_image_label.place(relx=relx, rely=rely, anchor=anchor)

def validate_length(event, entry, max):
    if len(entry.get()) >= max:
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Delete', 'Tab'):
            return True
        else:
            return "break"
    return True

def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"
def toggle_password_visibility(inputfield, btn, visible_flag, eye_close_img, eye_open_img):
    if visible_flag[0]:
        inputfield.configure(show="*")
        btn.configure(image=eye_close_img)
        visible_flag[0] = False
    else:
        inputfield.configure(show="")
        btn.configure(image=eye_open_img)
        visible_flag[0] = True
# Function to change border color on input
def change_border_color(entry):
    if entry.get():
        entry.configure(border_color="green")
    else:
        entry.configure(border_color="red")

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
#_______________________________________dyPAGEREGISTER

def create_standard_label(parent, text):
    # Standard label properties
    font = ("Inter", 18, "bold")
    text_color = "#333333"
    grid_options = {'row': 0, 'column': 0, 'sticky': 'ws', 'padx': 2}

    # Create and configure the label
    label = CTkLabel(parent, text=text, fg_color="transparent", font=font, text_color=text_color)
    label.grid(**grid_options)
    return label

def create_standard_entry(parent, placeholder, state="normal"):
    # Standard entry properties
    font = ("Inter", 15)
    corner_radius = 8
    border_width = 1.5
    border_color = '#F47575'
    grid_options = {'row': 1, 'column': 0, 'sticky': 'nsew'}

    # Create and configure the entry
    entry = CTkEntry(parent, placeholder_text=placeholder, font=font,
                     corner_radius=corner_radius, border_width=border_width, border_color=border_color, state=state)
    entry.grid(**grid_options)
    return entry

def create_warning_label(parent, text):
    # Standard warning label properties
    font = ("Inter", 12)
    text_color = "red"
    grid_options = {'row': 2, 'column': 0, 'sticky': 'ws', 'padx': 2}

    # Create and configure the warning label
    warning_label = CTkLabel(parent, text=text, fg_color="transparent", font=font, text_color=text_color)
    warning_label.grid(**grid_options)
    return warning_label

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
        Ecpassword.delete(0, 'end')  # Clear the "Confirm Password" field
        Ecpassword.configure(state="disabled", border_color="red")  # Keep "Confirm Password" field disabled
        ep_label.configure(text="Password must be at least 8 characters long", text_color="red")
        ecp_label.configure(text="")  # Clear any previous messages in the confirm password label
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
    set_icon_image(RegisScssfr,'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
    LbSuccess = CTkLabel(RegisScssfr, text="Registered Successfully", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
    register_window.after(2000, register_window.destroy)

#_______________________________________dyPAGESIGNIN
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
    set_icon_image(LogFailfr,'warning_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))

    LbSuccess = CTkLabel(LogFailfr, text="Invalid Username or Password", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')

    # Destroy the frame after 3 seconds
    signin_window.after(2000, LogFailfr.destroy)


#_______________________________________dyMainPage
def hide_indicators(Home_indct, Visitor_indct, Resident_indct):
    Home_indct.configure(fg_color="#FEFEFE")
    Visitor_indct.configure(fg_color="#FEFEFE")
    Resident_indct.configure(fg_color="#FEFEFE")

def indicate(selected_indicator, Home_indct, Visitor_indct, Resident_indct, new_page):
    hide_indicators(Home_indct, Visitor_indct, Resident_indct)
    selected_indicator.configure(fg_color="#00507E")  # Update the active indicator color
    new_page()
