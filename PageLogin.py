from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path

# Configure path to assets directory
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")

def manage_asterisk(entry_widget, asterisk_label, relx, y, anchor):
    if entry_widget.get():
        asterisk_label.place_forget()
    else:
        asterisk_label.place(relx=relx, y=y, anchor=anchor)

def create_asterisk(entry_widget, parent_frame, relx, y, anchor):
    asterisk_image_orig = Image.open(ASSETS_PATH / 'asterisk.png')
    resized_asterisk_image = asterisk_image_orig.resize((7, 7))
    asterisk_image_tk = ImageTk.PhotoImage(resized_asterisk_image)
    asterisk_label = CTkLabel(parent_frame, image=asterisk_image_tk, text='')
    asterisk_label.image = asterisk_image_tk  # Keep a reference!
    manage_asterisk(entry_widget, asterisk_label, relx, y, anchor)
    entry_widget.bind("<KeyRelease>", lambda event: manage_asterisk(entry_widget, asterisk_label, relx, y, anchor))

def hide():
    global button_mode
    if button_mode:
        eyeButton.configure(image=open_eye_tk)
        Epassword.configure(show="")
        button_mode = False
    else:
        eyeButton.configure(image=close_eye_tk)
        Epassword.configure(show="*")
        button_mode = True

login_window = CTk()
login_window.geometry('1200x800+400+100')
login_window.minsize(800, 400)
login_window.maxsize(1200, 800)
login_window.title('Sign In Page')

# Load background image
bgImage_orig = Image.open(ASSETS_PATH / 'SIGN IN PAGE.png')
resized_bgimage = bgImage_orig.resize((1200, 800))
bgImage_tk = ImageTk.PhotoImage(resized_bgimage)
bgImageL = CTkLabel(login_window, image=bgImage_tk, text='')
bgImageL.place(relwidth=1, relheight=1)

# Create the sign-in frame
SignFrame = CTkFrame(login_window, width=530, height=600, fg_color="#F0F6F9")
SignFrame.place(x=555, y=100)

# Add components to sign-in frame
heading = CTkLabel(SignFrame, text='Sign In', fg_color="#F0F6F9", font=("Inter", 30, "bold"), text_color="#333333")
heading.place(relx=0.5, y=70, anchor='n')

Eusername = CTkEntry(SignFrame, width=400.0, height=40.0, placeholder_text="Username", corner_radius=8, border_width=1, border_color='#DEE6EA')
Eusername.place(relx=0.5, y=230, anchor='n')
Lusername = CTkLabel(SignFrame, text='Username', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
Lusername.place(relx=0.19, y=200, anchor='n')
create_asterisk(Eusername, SignFrame, relx=0.275, y=198, anchor='n')

Epassword = CTkEntry(SignFrame, width=400.0, height=40.0, placeholder_text="Password", corner_radius=8, border_width=1, border_color='#DEE6EA')
Epassword.place(relx=0.5, y=320, anchor='n')
Lpassword = CTkLabel(SignFrame, text='Password', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
Lpassword.place(relx=0.19, y=290, anchor='n')
create_asterisk(Epassword, SignFrame, relx=0.275, y=288, anchor='n')

# Toggle password visibility
open_eye = Image.open(ASSETS_PATH / 'Eye_Open.png')
open_eye_tk = ImageTk.PhotoImage(open_eye)
close_eye = Image.open(ASSETS_PATH / 'Eye_Close.png')
close_eye_tk = ImageTk.PhotoImage(close_eye)
eyeButton = CTkButton(SignFrame, image=close_eye_tk, text='', width=10, fg_color='#F9F9FA', hover_color="#F9F9FA", cursor='hand2', command=hide)
eyeButton.place(relx=0.82, y=326, anchor='n')
button_mode = False

# Sign-in button
createbtn = CTkButton(SignFrame, text="Sign In", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333")
createbtn.place(relx=0.6, rely=0.75)

login_window.mainloop()
