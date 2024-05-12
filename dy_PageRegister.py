#Page Register
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, check_entries_complete, check_password_match, ASSETS_PATH, handle_password_input, display_success_and_close, validate_full_name
from db_con import register_security_admin
from dy_PageUtils import configure_grid, create_standard_entry, create_standard_label, create_warning_label

# def open_register_window(main_window):
register_window = CTk()
# register_window = CTkToplevel(main_window)
register_window.geometry('1200x800+400+100')
# register_window.grab_set()
register_window.title('Register Account')
register_window.minsize(1000, 900)
register_window.configure(fg_color='white')
register_window.maxsize(register_window.winfo_screenwidth(), register_window.winfo_screenheight())
register_window.rowconfigure((0, 2), weight=1, uniform='a')
register_window.rowconfigure(1, weight=10, uniform='a')

def on_resize(event):
    width = event.width
    min_width = 1000
    max_width = 1200

    # Use a static configuration for width thresholds
    if min_width <= width < max_width:
        column_weights = (1, 1, 1, 10, 3)
        # Adjust the LogoF frame placement
        LogoF.grid_forget()
        BackF.grid_forget()
    elif width >= max_width:
        column_weights = (2, 5, 2, 8, 1)
        LogoF.grid(row=1, column=1)
        BackF.grid(row=2, column=0, sticky="nsew")

    # Apply column configuration
    for i, weight in enumerate(column_weights):
        register_window.columnconfigure(i, weight=weight, uniform='a')

# Bind the resize event
register_window.bind('<Configure>', on_resize)

CreateF = CTkFrame(register_window, fg_color="#D1DDE2", corner_radius=10, width=660, height=780)
CreateF.grid(row=1, column=3, sticky="nsew", padx=10)
CreateF.columnconfigure((0, 2), weight=1, uniform='a')
CreateF.columnconfigure(1, weight=10, uniform='a')
CreateF.rowconfigure(0, weight=1, uniform='a')
CreateF.rowconfigure((1,2,3,4,5,6), weight=4, uniform='a')

LabelFrame = CTkLabel(CreateF, fg_color="transparent", text="Create Account",
                    font=("Inter", 40, "bold"), text_color="#333333")
LabelFrame.grid(row=1, column=1)

LogoF = CTkFrame(register_window, fg_color="light pink", corner_radius=10, width=660, height=400)
LogoF.grid(row=1, column=1)
BackF = CTkFrame(register_window, fg_color="light green", corner_radius=10, width=110, height=40)
BackF.grid(row=2, column=0, sticky="nsew")



# FULL NAME
InputF1 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
InputF1.grid(row=2, column=1, sticky="nsew", pady=2)
configure_grid(InputF1)
Efullname = create_standard_entry(InputF1, "Enter Full Name")
Lfullname = create_standard_label(InputF1, 'Full Name')
FnExistlabel = create_warning_label(InputF1, "Warning: Name Already Exists")


# USERNAME
InputF2 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
InputF2.grid(row=3, column=1, sticky="nsew", pady=2)
configure_grid(InputF2)
Eusername = create_standard_entry(InputF2, "Enter Username")
Lusername = create_standard_label(InputF2, 'Username')
UnExistlabel = create_warning_label(InputF2, "Warning: Username Already Exists")


# PASSWORD
InputF3 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
InputF3.grid(row=4, column=1, sticky="nsew", pady=2)
configure_grid(InputF3)
Epassword = create_standard_entry(InputF3, "Enter Password")
Lpassword = create_standard_label(InputF3, 'Enter Password')
epExistlabel = create_warning_label(InputF3, "Warning: Password Error")


# CONFIRM PASSWORD
InputF4 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
InputF4.grid(row=5, column=1, sticky="nsew", pady=2)
configure_grid(InputF4)
Ecpassword = create_standard_entry(InputF4, "Confirm Password")
Lcpassword = create_standard_label(InputF4, 'Confirm Password')
ecpExistlabel = create_warning_label(InputF4, "Warning: Passwords Do Not Match")


CAFrame= CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
CAFrame.grid(row=6, column=1, sticky="nsew")
CAFrame.columnconfigure(0, weight=1, uniform='a')
CAFrame.rowconfigure(0, weight=1, uniform='a')

CAbtn = CTkButton(CAFrame, text="Create Account", width=180, height=50, corner_radius=10,
                        fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"),
                        text_color="#333333", state="disabled")
CAbtn.grid(row=0, column=0, sticky="ne", pady=20)


register_window.mainloop()