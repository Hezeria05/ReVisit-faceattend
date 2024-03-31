
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import customtkinter as ctk
from pathlib import Path
import subprocess
from db_con import register_security_admin
from tkinter import messagebox




# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\grace\Desktop\GitReVisit\ReVisit-faceattend\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = ctk.CTk()

window.geometry("745x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 745,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    373.0,
    65.0,
    708.0,
    491.0,
    fill="#E6E6E6",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    185.0,
    175.0,
    image=image_image_1
)

def submit_action():
    # Get the values from the entry fields
    name = fullname_1.get()
    username = username_2.get()
    password = password_3.get()
    
    # Call the function to insert these values into the database
    success = register_security_admin(name, username, password)
    if success:
        # Close the current window
        window.destroy()
        # Show a message box indicating successful registration
        messagebox.showinfo("Registration Successful", "Registered Successfully")
        # Open user_page.py
        subprocess.Popen(["python", r"C:\Users\grace\Desktop\GitReVisit\ReVisit-faceattend\user_page.py"])
    else:
        messagebox.showerror("Registration Failed", "Could not register. Please try again.")


# Update the submit button command


button_1 = ctk.CTkButton(
    master=window,
    text="Submit",  # Added spaces for horizontal 'padding'
    command=lambda: print("Submit button clicked"),
    width=110,  # Adjusted width
    height=32,   # Adjusted height
    corner_radius=10,  # Optional: adjust the corner radius for rounded corners
    fg_color="#5B757A",
    hover_color="#719298",
    font=("Inter", 15,)
)
button_1.configure(command=submit_action)

button_1.place(
    x=482.0,
    y=375.0,
)

def open_user_page():
    window.destroy()  # This will close the current window
    subprocess.run(["python", r"C:\Users\grace\Desktop\GitReVisit\ReVisit-faceattend\user_page.py"])  # Adjust the path as needed


backbtn = ctk.CTkButton(
    master=window,
    text="Back", 
    font=("Inter", 15),
    width=110,
    height=32,
    corner_radius=10,
    fg_color="#5B757A",
    hover_color="#719298",
    command=open_user_page  # Use the function here
)


backbtn.place(
    x=482.0,
    y=420.0,
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    185.0, #left to right
    278.0,
    image=image_image_2
)

canvas.create_text(
    399.0,
    125.0,
    anchor="nw",
    text="Full Name:",
    fill="#5B757A",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    399.0,
    197.0,
    anchor="nw",
    text="User Name:",
    fill="#5B757A",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    399.0,
    269.0,
    anchor="nw",
    text="Password:",
    fill="#5B757A",
    font=("Inter SemiBold", 15 * -1)
)

fullname_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
fullname_bg_1 = canvas.create_image(
    540.5,
    169.0,
    image=fullname_image_1
)
fullname_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
fullname_1.place(
    x=406.0,
    y=152.0,
    width=269.0,
    height=32.0
)

username_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
username_bg_2 = canvas.create_image(
    540.5,
    241.0,
    image=username_image_2
)
username_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
username_2.place(
    x=406.0,
    y=224.0,
    width=269.0,
    height=32.0
)

password_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
password_bg_3 = canvas.create_image(
    540.5,
    313.0,
    image=password_image_3
)
password_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show="*"  # This makes the password hidden
)


password_3.place(
    x=406.0,
    y=296.0,
    width=269.0,
    height=32.0
)

button_mode=False

def hide():
    global button_mode
    if button_mode:
        eyeButton.configure(image=closeeye, activebackground="white")
        password_3.configure(show="*")
        button_mode=False
    else:
        eyeButton.configure(image=openeye, activebackground="white")
        password_3.configure(show="")
        button_mode=True


openeye=PhotoImage(file=r"C:\Users\grace\Desktop\GitReVisit\ReVisit-faceattend\assets\frame1\eye_icon.png")
closeeye=PhotoImage(file=r"C:\Users\grace\Desktop\GitReVisit\ReVisit-faceattend\assets\frame1\eye_closed.png")

eyeButton = Button(window, image=closeeye, bg="white", bd=0, command=hide)
eyeButton.place(x=644.0,y=299.0)

window.resizable(False, False)
window.mainloop()
