from customtkinter import *
from PIL import Image
import os
from datetime import datetime
from db_con import update_resident_data
import re


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

def validate_all(event, entry_widget, length, char_val):
        if char_val == 1:
            vresult = validate_char(event)
            if vresult == "break":
                return vresult
        result = validate_and_remove_leading_space(event, entry_widget)
        if result == "break":
            return result
        lgresult = validate_length(event, entry_widget, length)
        if lgresult == "break":
            return lgresult

def check_leading_space(event, entry, label, btn):
    if entry.get().startswith(' '):
        label.configure(text="Invalid format!")
        btn.configure(state="disabled")
    else:
        label.configure(text="")

def validate_and_remove_leading_space(event, entry):
        if event.char == ' ' and entry.get() == '':
            return "break"  # Prevent space character from being inserted

def validate_length(event, entry, max):
    if len(entry.get()) >= max:
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Delete', 'Tab'):
            return True
        else:
            return "break"
    return True

def validate_char(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

def create_eye_button(parent_frame, entry_widget, visible_list, close_img, open_img, relx=0.93, rely=0.5):
    eye_button = CTkButton(parent_frame, image=close_img, text='', width=50, fg_color='#F9F9FA', hover_color="#F9F9FA", corner_radius=0, border_width=0)
    eye_button.place(relx=relx, rely=rely, anchor="center")
    eye_button.configure(command=lambda: toggle_password_visibility(entry_widget, eye_button, visible_list, close_img, open_img))
    return eye_button
def toggle_password_visibility(inputfield, btn, visible_flag, eye_close_img, eye_open_img):
    if visible_flag[0]:
        inputfield.configure(show="*")
        btn.configure(image=eye_close_img)
        visible_flag[0] = False
    else:
        inputfield.configure(show="")
        btn.configure(image=eye_open_img)
        visible_flag[0] = True

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

def view_history(sec_id, LogVframe, logsuccess, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct, logout_btn, home_page, home_button, visitor_button, resident_button):
    LogSuccessfr = CTkFrame(LogVframe, fg_color="white", width=700, height=350, border_color="#B9BDBD", border_width=2, corner_radius=10)
    LogSuccessfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(LogSuccessfr, 'success_icon.png', relx=0.5, rely=0.15, anchor='n', size=(95, 95))

    LbSuccess = CTkLabel(LogSuccessfr, text=logsuccess, fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.48, anchor='n')

    viewbtn = CTkButton(LogSuccessfr, text="View History", width=230, height=50, corner_radius=10, 
                    fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333")
    viewbtn.place(relx=0.3, rely=0.8, anchor='center')

    donebtn = CTkButton(LogSuccessfr, text="Done", width=230, height=50, corner_radius=10, 
                    fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333")
    donebtn.place(relx=0.7, rely=0.8, anchor='center')

    viewbtn.configure(command=lambda: indicate(Visitor_indct, Home_indct, Visitor_indct, Resident_indct, 
                            lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button)))
    donebtn.configure(command=lambda: home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button))


def logout(window, btn):
    LogoutModal = CTkFrame(window, fg_color="white", width=650, height=350, border_color="#B9BDBD", border_width=2, corner_radius=10)
    LogoutModal.place(relx=0.6125, rely=0.5, anchor='center')
    set_icon_image(LogoutModal,'question_icon.png', relx=0.5, rely=0.13, anchor='n', size=(110, 110))
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
#_______________________________________dyPAGEREGISTER

def create_image_label(parent_frame, image_path, w, h, relx=0, rely=0.1):
    image_size = (w, h)
    relx = relx
    rely = rely
    image = load_image(image_path, image_size)
    label = CTkLabel(parent_frame, image=image, text="")
    label.place(relx=relx, rely=rely, anchor="w")
    return label

def create_standard_label(parent, text, relx=0, rely=0, anchor="nw"):
    # Standard label properties
    font = ("Inter", 18, "bold")
    text_color = "#333333"

    # Create and configure the label
    label = CTkLabel(parent, text=text, fg_color="transparent", font=font, text_color=text_color)
    label.place(relx=relx, rely=rely, anchor=anchor)
    return label

def create_standard_entry(parent, placeholder, state="normal"):
    # Standard entry properties
    font = ("Inter", 15)
    corner_radius = 8
    border_width = 1.5
    border_color = '#ADCBCF'
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

#---------------------------------------------------------------------VALIDATIONS
# Ensure first letter is uppercase
def capitalize_first_letter(event, entry):
    content = entry.get()
    if content and content[0].islower():
        entry.delete(0, END)
        entry.insert(0, content.capitalize())

def validate_no_space(event):
        if event.keysym == 'space':
            return 'break'  # Prevents space from being entered

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
    Home_indct.configure(fg_color="#F6FCFC")
    Visitor_indct.configure(fg_color="#F6FCFC")
    Resident_indct.configure(fg_color="#F6FCFC")

def indicate(selected_indicator, Home_indct, Visitor_indct, Resident_indct, new_page):
    hide_indicators(Home_indct, Visitor_indct, Resident_indct)
    selected_indicator.configure(fg_color="#00507E")  # Update the active indicator color
    new_page()

#_______________________________________# Visitor Page

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
        new_text = current_text[:event.widget.index("insert")] + event.char + current_text[event.widget.index("insert"):]

        if len(new_text) == 1 and event.char == "0":
            return True
        elif len(new_text) == 2 and new_text.startswith("09"):
            return True

        if new_text.startswith("09") and len(new_text) - selection_length <= 11:
            return True
        else:
            return "break"
    else:
        return "break"

def toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, is_edit_mode):
    if is_edit_mode:
        edit_btn.configure(text="Save", state='disabled', command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, False))
        for entries in entries_list:
            for index, entry in enumerate(entries):
                if index != 1:  # Skip the address field (index 1)
                    entry.configure(state='normal')
                    entry.bind("<KeyRelease>", lambda event, btn=edit_btn, elist=entries_list: on_entry_change(event, btn, elist))
    else:
        edit_btn.configure(text="Edit", command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, True))
        save_edited_data(Residentframe, entries_list, id_list)
        for entries in entries_list:
            for index, entry in enumerate(entries):
                if index != 1:  # Skip the address field (index 1)
                    entry.configure(state='disabled')
                    entry.unbind("<KeyRelease>")

def on_entry_change(event, save_button, entries_list):
    all_valid = True
    for entries in entries_list:
        phone_entry = entries[2]
        if len(phone_entry.get()) < 11:
            all_valid = False
            break
    save_button.configure(state='normal' if all_valid else 'disabled')

def save_edited_data(Residentframe, entries_list, id_list):
    for entries, res_id in zip(entries_list, id_list):
        name, address, phone = [entry.get() for entry in entries]
        update_resident_data(Residentframe, res_id, name, address, phone)
        save_success(Residentframe)

def save_success(window):
    SaveSuccessfr = CTkFrame(window, fg_color="white", width=700, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
    SaveSuccessfr.place(relx=0.5, rely=0.5, anchor='center')

    set_icon_image(SaveSuccessfr, 'success_icon.png', relx=0.5, rely=0.15, anchor='n', size=(95, 95))

    LbSuccess = CTkLabel(SaveSuccessfr, text="Saved Successfully!", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.62, anchor='n')

    SaveSuccessfr.after(2500, SaveSuccessfr.destroy)