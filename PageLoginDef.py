from PIL import Image, ImageTk
from pathlib import Path

# Configure path to assets directory
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")

def manage_asterisk(entry_widget, asterisk_label, relx, y, anchor):
    if entry_widget.get():  # If entry is not empty
        asterisk_label.place_forget()  # Hide asterisk
    else:
        asterisk_label.place(relx=relx, y=y, anchor=anchor)  # Show asterisk

def create_asterisk(entry_widget, parent_frame, relx, y, anchor, ImageTk):
    asteImage_orig = Image.open(ASSETS_PATH / 'asterisk.png')
    resized_asteimage = asteImage_orig.resize((7, 7))
    asteImage_tk = ImageTk.PhotoImage(resized_asteimage)
    asterisk_label = parent_frame.CTkLabel(image=asteImage_tk, text='')
    asterisk_label.image = asteImage_tk  # Keep a reference!
    manage_asterisk(entry_widget, asterisk_label, relx, y, anchor)
    entry_widget.bind("<KeyRelease>", lambda event: manage_asterisk(entry_widget, asterisk_label, relx, y, anchor))

def toggle_eye(button_mode, eyeButton, Epassword, open_eye_tk, close_eye_tk):
    if button_mode:  # If currently showing the password (eye closed)
        eyeButton.configure(image=open_eye_tk)  # Change to open eye
        Epassword.configure(show="")  # Show password
        return False  # Toggle mode
    else:  # If currently hiding the password (eye open)
        eyeButton.configure(image=close_eye_tk)  # Change to closed eye
        Epassword.configure(show="*")  # Hide password
        return True  # Toggle mode
