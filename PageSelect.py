from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageLogin import open_login_window


# Configure path to assets directory
ASSETS_PATH = Path(r"C:\Users\grace\Desktop\ReVisit-faceattend\assets")


select_window = CTk()
select_window.geometry('1200x800+400+100')
select_window.minsize(800, 400)
select_window.maxsize(1200, 800)
select_window.title('Sign In Page')

# Load background image
bgImage_orig = Image.open(ASSETS_PATH / 'USER SELECT PAGE.png')
resized_bgimage = bgImage_orig.resize((1200, 800))
bgImage_tk = ImageTk.PhotoImage(resized_bgimage)
bgImageL = CTkLabel(select_window, image=bgImage_tk, text='')
bgImageL.place(relwidth=1, relheight=1)

# Create the sign-in frame
SignFrame = CTkFrame(select_window, width=400, height=200, fg_color="#FEFEFE")
SignFrame.place(relx=0.5, y=450, anchor='n')

#  Select button
signinbtn = CTkButton(SignFrame, text="SIGN IN", width=250, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333", command=lambda: open_login_window(select_window, bgImageL, SignFrame))
signinbtn.place(relx=0.5, rely=0.25, anchor='n')
registerbtn = CTkButton(SignFrame, text="REGISTER", width=250, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333")
registerbtn.place(relx=0.5, rely=0.6, anchor='n')
select_window.mainloop()
