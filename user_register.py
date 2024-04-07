# Imports and Setup
import customtkinter as ctk
from customtkinter import BooleanVar
from pathlib import Path
import subprocess
from db_con import register_security_admin
from tkinter import messagebox, Tk, Canvas, Text, Button, PhotoImage

# Path Configuration
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Window Configuration
window = ctk.CTk()
window.geometry("745x550")
window.configure(bg="#FFFFFF")
window.resizable(False, False)
window.title("Create Account")

# Canvas and Images
canvas = Canvas(window, bg="#FFFFFF", height=550, width=745, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(373.0, 65.0, 708.0, 491.0, fill="#E6E6E6", outline="")

canvas.create_text(
    446.0, 95.0,  # Adjust the positioning as needed
    anchor="nw",
    text="Create Account",
    fill="#5B757A",
    font=("Inter SemiBold", 20, "bold")  # Adjust the font size and style as needed
)

def load_images():
    global image_image_1, image_image_2  # Make images global or attach to an object that persists
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))

    # Now, use these images wherever needed
    canvas.create_image(185.0, 175.0, image=image_image_1)
    canvas.create_image(185.0, 278.0, image=image_image_2)

load_images()

# Labels and Entry Fields
# Full Name Label and Entry
canvas.create_text(406.0, 145.0, anchor="nw", text="Full Name:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))
fullname_1 = ctk.CTkEntry(master=window, width=275, height=42, corner_radius=10, placeholder_text="Full Name")
fullname_1.place(x=406.0, y=167.0)

# Username Label and Entry
canvas.create_text(406.0, 217.0, anchor="nw", text="Username:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))
username_2 = ctk.CTkEntry(master=window, width=275.0, height=42.0, placeholder_text="Username", corner_radius=10)
username_2.place(x=406.0, y=239.0)

# Password Label and Entry
canvas.create_text(406.0, 289.0, anchor="nw", text="Password:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))
password_3 = ctk.CTkEntry(master=window, width=275.0, height=42.0, placeholder_text="Password", corner_radius=10, show="*")
password_3.place(x=406.0, y=311.0)

canvas.create_text(406.0, 363.0, anchor="nw", text="Shift:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))

# AM Checkbox
am_var = BooleanVar()
am_var.set(True)  # Set the value of AM checkbox to True (1)
am_checkbox = ctk.CTkCheckBox(master=window, text="AM", text_color="#5B757A", variable=am_var, corner_radius=5, fg_color="#5B757A", border_color="#5B757A", hover_color="gray", border_width=2, command=lambda: toggle_checkbox(am_checkbox))
am_checkbox.place(x=456.0, y=373.0)  # Adjust the y-coordinate as needed

# PM Checkbox
pm_var = BooleanVar()
pm_var.set(False)  # Set the value of PM checkbox to False (0)
pm_checkbox = ctk.CTkCheckBox(master=window, text="PM", text_color="#5B757A", variable=pm_var, corner_radius=5, fg_color="#5B757A", border_color="#5B757A", hover_color="gray", border_width=2, command=lambda: toggle_checkbox(pm_checkbox))
pm_checkbox.place(x=526.0, y=373.0)  # Adjust the y-coordinate as needed

# Function to ensure only one checkbox is selected
def toggle_checkbox(checkbox):
    if checkbox == am_checkbox and am_var.get():
        pm_var.set(False)  # Uncheck PM checkbox if AM checkbox is checked
    elif checkbox == pm_checkbox and pm_var.get():
        am_var.set(False)  # Uncheck AM checkbox if PM checkbox is checked

# Function to get the selected value
def get_shift_value():
    if am_var.get():
        return 1  # Return 1 if AM checkbox is selected
    elif pm_var.get():
        return 2  # Return 2 if PM checkbox is selected
    else:
        return None  # Return None if neither checkbox is selected


# Buttons and Actions
def submit_action():
    name = fullname_1.get()
    username = username_2.get()
    password = password_3.get()
    shift = get_shift_value()  # Get the shift value
    if shift is not None:  # Check if a shift value is selected
        success = register_security_admin(name, username, password, shift)
        if success:
            window.destroy()
            messagebox.showinfo("Registration Successful", "Registered Successfully")
            subprocess.Popen(["python", r"C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/user_page.py"])
        else:
            window.destroy()
            messagebox.showerror("Registration Failed", "Could not register. Please try again.")
    else:
        messagebox.showerror("Shift Not Selected", "Please select a shift (AM/PM).")


def open_user_page():
    window.destroy()
    subprocess.run(["python", r"C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/user_page.py"])

def hide():
    global button_mode
    if button_mode:
        eyeButton.configure(image=closeeye)
        password_3.configure(show="*")
        button_mode = False
    else:
        eyeButton.configure(image=openeye)
        password_3.configure(show="")
        button_mode = True

button_1 = ctk.CTkButton(master=window, text="Submit", command=submit_action, width=110, height=32, corner_radius=10, fg_color="#5B757A", hover_color="#719298")
button_1.place(x=556.0, y=432.0)

backbtn = ctk.CTkButton(master=window, text="Back", command=open_user_page, width=110, height=32, corner_radius=10, fg_color="#5B757A", hover_color="#719298")
backbtn.place(x=406.0, y=432.0)

openeye = PhotoImage(file=relative_to_assets("eye_icon.png"))
closeeye = PhotoImage(file=relative_to_assets("eye_closed.png"))
eyeButton = Button(window, image=closeeye, bg="#F9F9FA", bd=0, command=hide, activebackground="#F9F9FA", relief='flat', highlightthickness=0)
eyeButton.place(x=644.0, y=319.0)

button_mode = False

# Utility Functions
# Already defined relative_to_assets function at the beginning.

window.mainloop()
