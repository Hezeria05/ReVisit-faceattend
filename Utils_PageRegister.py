from customtkinter import *
from PIL import Image
import os
from datetime import datetime
from db_con import update_resident_data
import re
from dy_PageUtils import disable_submit_button, enable_submit_button

def check_entries_complete(entries, ecp_label, createbtn, Epassword, Ecpassword, Efullname, FnExistlabel, Eusername, UnExistlabel):
    all_complete = all(entry.get().strip() for entry in entries)
    password = Epassword.get().strip()

    if all_complete and len(password) >= 8:
        check_password_match(entries, Epassword, Ecpassword, ecp_label, createbtn, Efullname, FnExistlabel, Eusername, UnExistlabel)
    else:
        disable_submit_button(createbtn)

def handle_password_input(Epassword, Ecpassword, ecp_label, createbtn, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel, confirm_password_visible, entries, Efullname, FnExistlabel, Eusername, UnExistlabel):
    password = Epassword.get().strip()
    confirm_password = Ecpassword.get().strip()

    if not password:
        set_policy_labels_color_to_red(ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel)
        if len(confirm_password) >= 1:
            ecp_label.configure(text="Enter Password First!", text_color="red")
    else:
        validate_password_policy(password, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel)
        if all([ep8charlabel.cget("text_color") == "green",
                epnumberlabel.cget("text_color") == "green",
                epupperlabel.cget("text_color") == "green",
                epspeclabel.cget("text_color") == "green",
                eplowerlabel.cget("text_color") == "green"]):
            Ecpassword.configure(state="normal", show='' if confirm_password_visible[0] else '*')
            check_password_match(entries, Epassword, Ecpassword, ecp_label, createbtn, Efullname, FnExistlabel, Eusername, UnExistlabel)
        else:
            ecp_label.configure(text="", text_color="red")
            disable_submit_button(createbtn)

def handle_ecpassword_input(Epassword, Ecpassword, ecp_label, createbtn, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel, confirm_password_visible, entries, Efullname, FnExistlabel, Eusername, UnExistlabel):
    password = Epassword.get().strip()
    confirm_password = Ecpassword.get().strip()

    if not confirm_password:
        ecp_label.configure(text="", text_color="red")
        if len(password) >= 1:
            ecp_label.configure(text="", text_color="red")
    else:
        validate_password_policy(password, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel)
        if all([ep8charlabel.cget("text_color") == "green",
                epnumberlabel.cget("text_color") == "green",
                epupperlabel.cget("text_color") == "green",
                epspeclabel.cget("text_color") == "green",
                eplowerlabel.cget("text_color") == "green"]):
            check_password_match(entries, Epassword, Ecpassword, ecp_label, createbtn, Efullname, FnExistlabel, Eusername, UnExistlabel)
        else:
            ecp_label.configure(text="", text_color="red")
            disable_submit_button(createbtn)

def check_password_match(entries, Epassword, Ecpassword, ecp_label, createbtn, Efullname, FnExistlabel, Eusername, UnExistlabel):
    password = Epassword.get().strip()
    confirm_password = Ecpassword.get().strip()
    full_name = Efullname.get()
    user_name = Eusername.get()

    # Check for leading spaces in full name and username
    if full_name.startswith(' ') or user_name.startswith(' '):
        ecp_label.configure(text="")
        disable_submit_button(createbtn)
        return

    if password and confirm_password:
        if password == confirm_password:
            ecp_label.configure(text="Passwords match", text_color="green")
            if all(entry.get().strip() for entry in entries):
                enable_submit_button(createbtn)
            else:
                disable_submit_button(createbtn)
        else:
            ecp_label.configure(text="Passwords do not match", text_color="red")
            disable_submit_button(createbtn)
    else:
        ecp_label.configure(text="")
        disable_submit_button(createbtn)

def validate_password_policy(password, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel):
    if len(password) >= 8:
        ep8charlabel.configure(text_color="green")
    else:
        ep8charlabel.configure(text_color="red")

    if re.search(r'[A-Z]', password):
        epupperlabel.configure(text_color="green")
    else:
        epupperlabel.configure(text_color="red")

    if re.search(r'[a-z]', password):
        eplowerlabel.configure(text_color="green")
    else:
        eplowerlabel.configure(text_color="red")

    if re.search(r'[0-9]', password):
        epnumberlabel.configure(text_color="green")
    else:
        epnumberlabel.configure(text_color="red")

    if re.search(r'[!@#$%_&*(),.?]', password):
        epspeclabel.configure(text_color="green")
    else:
        epspeclabel.configure(text_color="red")

def set_policy_labels_color_to_red(ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel):
    ep8charlabel.configure(text_color="red")
    epnumberlabel.configure(text_color="red")
    epupperlabel.configure(text_color="red")
    epspeclabel.configure(text_color="red")
    eplowerlabel.configure(text_color="red")