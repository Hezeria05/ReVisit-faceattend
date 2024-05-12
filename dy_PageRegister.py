#Page Register
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, check_entries_complete, check_password_match, ASSETS_PATH, handle_password_input, display_success_and_close, validate_full_name
from db_con import register_security_admin

# def open_register_window(main_window):
    # register_window = CTkToplevel(main_window)
    # register_window.grab_set()

def on_resize(event):
    width = event.width
    min_width = 1000
    max_width = 1300

    # Use a static configuration for width thresholds
    if min_width <= width < max_width:
        column_weights = (1, 1, 1, 10, 3)
        # Adjust the LogoF frame placement
        LogoF.grid_forget()  # Remove the LogoF from the grid first  # Place LogoF back in its initial position
    elif width >= max_width:
        column_weights = (2, 5, 2, 8, 1)
        # In wider screens, keep or change LogoF position if needed
        LogoF.grid_forget()  # Remove the LogoF from the grid first
        LogoF.grid(row=1, column=1)  # You can change these parameters as needed

    # Apply column configuration
    for i, weight in enumerate(column_weights):
        register_window.columnconfigure(i, weight=weight, uniform='a')

register_window = CTk()
register_window.geometry('1200x800+400+100')
register_window.title('Register Account')
register_window.minsize(1000, 900)
register_window.configure(fg_color='white')
register_window.maxsize(register_window.winfo_screenwidth(), register_window.winfo_screenheight())
register_window.rowconfigure((0, 2), weight=1, uniform='a')
register_window.rowconfigure(1, weight=10, uniform='a')
# Bind the resize event
register_window.bind('<Configure>', on_resize)

CreateF = CTkFrame(register_window, fg_color="light blue", corner_radius=10, width=660, height=780)
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

register_window.mainloop()