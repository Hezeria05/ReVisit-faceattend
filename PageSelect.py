#Page Select
from customtkinter import *
from PageSignin import open_signin_window
from PageRegister import open_register_window
from PageUtils import ASSETS_PATH, set_background_image

select_window = CTk()
select_window.geometry('1200x800+400+100')
select_window.minsize(800, 400)
select_window.maxsize(1200, 800)
select_window.title('Select Page')

# Background for the new window
set_background_image(select_window, ASSETS_PATH / 'USER SELECT PAGE.png',size=(1200, 800))

# Create the button frame
ButtonFrame = CTkFrame(select_window, width=400, height=200, fg_color="#FEFEFE")
ButtonFrame.place(relx=0.5, y=450, anchor='n')

#  Select button
signinbtn = CTkButton(ButtonFrame, text="SIGN IN", width=250, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333", command=lambda: open_signin_window(select_window))
signinbtn.place(relx=0.5, rely=0.25, anchor='n')
registerbtn = CTkButton(ButtonFrame, text="REGISTER", width=250, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333", command=lambda: open_register_window(select_window))
registerbtn.place(relx=0.5, rely=0.6, anchor='n')
select_window.mainloop()
