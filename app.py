from customtkinter import *
import subprocess

def register_face():
    # Execute face_register.py using subprocess
    subprocess.Popen(["python", "C:\\Users\\grace\\Desktop\\GitReVisit\\ReVisit-faceattend\\face_register.py"])

app = CTk()
app.geometry("700x500")
set_appearance_mode("dark")

btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="transparent",
                 hover_color="gray", border_color="#FFCC70", border_width=2, text_color="black",
                 command=register_face)  # Assign the function to the button's command parameter
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=479.0,
    y=406.0,
    width=124.0,
    height=42.0
)