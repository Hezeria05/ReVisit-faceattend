import customtkinter as ctk
from tkinter import PhotoImage, Canvas  # Import Canvas from tkinter
import os
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return Path(__file__).parent / Path(f"C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/assets/frame0/{path}")
def open_personnel_register():
    window.destroy()
    os.system('python "C:/Users/grace/Desktop/GitReVisit/ReVisit-faceattend/user_register.py"')

window = ctk.CTk()
window.geometry("745x550")
window.configure(bg="#FFFFFF")
window.resizable(False, False)

canvas = Canvas(window, bg="#FFFFFF", height=550, width=745)  # Use the standard tkinter Canvas
canvas.place(x=0, y=0)
canvas.create_rectangle(66.0, 56.0, 674.0, 482.0, fill="#E6E6E6")

image_1 = PhotoImage(file=relative_to_assets("image_1.png"))  # Create the PhotoImage
canvas.create_image(372.0, 112.0, image=image_1)  # Place the image on the canvas

image_2 = PhotoImage(file=relative_to_assets("image_2.png"))  # Create the PhotoImage
canvas.create_image(370.0, 204.0, image=image_2)  # Place the image on the canvas

button_1 = ctk.CTkButton(window, text="Log In", command=lambda: print("Submit button clicked"), width=150, height=42, corner_radius=10, fg_color="#5B757A", hover_color="#719298", font=("Inter", 18, "bold"))
button_1.place(x=310.0, y=307.0)

button_2 = ctk.CTkButton(window, text="Register", command=open_personnel_register, width=150, height=42, corner_radius=10, fg_color="#5B757A", hover_color="#719298", font=("Inter", 18, "bold"))
button_2.place(x=310.0, y=365.0)

window.mainloop()