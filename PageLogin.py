from customtkinter import *
from PIL import Image, ImageTk

login_window = CTk()
login_window.geometry('1200x800+400+100')
login_window.minsize(800, 400)
login_window.maxsize(1200, 800)
login_window.title('Sign In Page')

bgImage_path = r'C:\Users\grace\Desktop\ReVisit-faceattend\assets\SIGN IN PAGE.png'
bgImage_orig = Image.open(bgImage_path)
resized_bgimage = bgImage_orig.resize((1200, 800))
bgImage_tk = ImageTk.PhotoImage(resized_bgimage)

bgImageL = CTkLabel(login_window, image=bgImage_tk, text='')
bgImageL.place(relwidth=1, relheight=1)  # Fill the whole window

# The coordinates for the SignFrame
x_coordinate = 555  # Adjusted to match the provided screenshot
y_coordinate = 100

SignFrame = CTkFrame(login_window, width=530, height=600, fg_color="red")
SignFrame.place(x=x_coordinate, y=y_coordinate)

# You may adjust the anchor and pady to position the heading exactly where you want it
heading = CTkLabel(SignFrame, text='Sign In', fg_color="#F0F6F9", font=("Inter", 30, "bold"), text_color="#333333")
heading.place(relx=0.5, y=70, anchor='n')  # Placed at the top-center of the SignFrame, with 10 pixels from the top edge

username = CTkEntry(SignFrame, width=400.0, height=40.0, placeholder_text="Username", corner_radius=8, border_width=1, border_color='#DEE6EA')
username.place(relx=0.5, y=250, anchor='n')

password = CTkEntry(SignFrame, width=400.0, height=40.0, placeholder_text="Password", corner_radius=8, border_width=1, border_color='#DEE6EA')
password.place(relx=0.5, y=350, anchor='n')

login_window.mainloop()
