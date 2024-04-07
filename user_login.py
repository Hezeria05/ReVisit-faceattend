# Imports and Setup
import customtkinter as ctk
from pathlib import Path
import subprocess
from db_con import validate_login_credentials
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
window.title("Login")

# Canvas and Images
canvas = Canvas(window, bg="#FFFFFF", height=550, width=745, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(373.0, 65.0, 708.0, 491.0, fill="#E6E6E6", outline="")

canvas.create_text(
    510.0, 95.0,  # Adjust the positioning as needed
    anchor="nw",
    text="Login",
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

# Username Label and Entry
canvas.create_text(406.0, 145.0, anchor="nw", text="Username:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))
username_2 = ctk.CTkEntry(master=window, width=275.0, height=42.0, placeholder_text="Username", corner_radius=10)
username_2.place(x=406.0, y=167.0)

# Password Label and Entry
canvas.create_text(406.0, 217.0, anchor="nw", text="Password:", fill="#5B757A", font=("Inter SemiBold", 15 * -1))
password_3 = ctk.CTkEntry(master=window, width=275.0, height=42.0, placeholder_text="Password", corner_radius=10, show="*")
password_3.place(x=406.0, y=239.0)

# Buttons and Actions
def login_action():
    username = username_2.get()
    password = password_3.get()
    result, sec_id = validate_login_credentials(username, password)
    if result:
        messagebox.showinfo("Login Successful", "You have successfully logged in.")
        window.destroy()
        subprocess.Popen(["python", r"C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/face_scan.py", str(sec_id)])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")



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

button_1 = ctk.CTkButton(master=window, text="Login", command=login_action, width=110, height=32, corner_radius=10, fg_color="#5B757A", hover_color="#719298")
button_1.place(x=482.0, y=386.0)

backbtn = ctk.CTkButton(master=window, text="Back", command=open_user_page, width=110, height=32, corner_radius=10, fg_color="#5B757A", hover_color="#719298")
backbtn.place(x=482.0, y=431.0)

openeye = PhotoImage(file=relative_to_assets("eye_icon.png"))
closeeye = PhotoImage(file=relative_to_assets("eye_closed.png"))
eyeButton = Button(window, image=closeeye, bg="#F9F9FA", bd=0, command=hide, activebackground="#F9F9FA", relief='flat', highlightthickness=0)
eyeButton.place(x=644.0, y=248.0)

button_mode = False

# Utility Functions
# Already defined relative_to_assets function at the beginning.

window.mainloop()
