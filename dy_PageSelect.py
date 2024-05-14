from customtkinter import *
from dy_PageSignin import open_signin_window
from dy_PageRegister import open_register_window
from dy_PageUtils import load_image

# Setup the main application window
select_window = CTk()
select_window.geometry('1200x800+400+100')
select_window.minsize(1000, 700)
select_window.maxsize(select_window.winfo_screenwidth(), select_window.winfo_screenheight())
select_window.title('Select Page')
select_window.configure(fg_color='#E9F3F2')

# Bind the resize event
def on_resize(event):
    width = event.width

    if width >= 1000 and width < 1300:
        column_weights = (1, 5, 1)
        row_weights = (1, 5, 1)
    elif width > 1300:
        column_weights = (2, 4, 2)
        row_weights = (1, 4, 1)

    # Apply column and row configuration
    for i, weight in enumerate(column_weights):
        select_window.columnconfigure(i, weight=weight, uniform='a')
    for i, weight in enumerate(row_weights):
        select_window.rowconfigure(i, weight=weight, uniform='a')

select_window.bind('<Configure>', on_resize)

# Setup the main frame
SelectFrame = CTkFrame(select_window, fg_color="white", corner_radius=10, width=830, height=700)
SelectFrame.grid(row=1, column=1, sticky="nsew")
SelectFrame.columnconfigure((0, 2), weight=1, uniform='a')
SelectFrame.columnconfigure(1, weight=10, uniform='a')
SelectFrame.rowconfigure((0, 1), weight=1, uniform='a')

# Load and display the logo image

logoimage = load_image('CarltonLOGO.png', (600, 210))
logolabel = CTkLabel(SelectFrame, image=logoimage, text="")
logolabel.grid(row=0, column=1, sticky="nsew", pady=20)

# Setup the button frame
ButtonFrame = CTkFrame(SelectFrame, fg_color="transparent", corner_radius=10, width=830, height=700)
ButtonFrame.grid(row=1, column=1, sticky="nsew", pady=20)
ButtonFrame.columnconfigure((0, 2), weight=1, uniform='a')
ButtonFrame.columnconfigure(1, weight=3, uniform='a')
ButtonFrame.rowconfigure((0, 3), weight=1, uniform='a')
ButtonFrame.rowconfigure((1, 2), weight=3, uniform='a')

#Buttons
signinbtn = CTkButton(ButtonFrame, text="SIGN IN", width=50, height=80, corner_radius=10, fg_color="#ADCBCF", 
                      hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333", command=lambda: open_signin_window(select_window))
signinbtn.grid(row=1, column=1, sticky="ew", padx=50, pady=15)
registerbtn = CTkButton(ButtonFrame, text="REGISTER", width=50, height=80, corner_radius=10, fg_color="#ADCBCF", 
                        hover_color="#93ACAF", font=("Inter", 25, "bold"), text_color="#333333", command=lambda: open_register_window(select_window))
registerbtn.grid(row=2, column=1, sticky="ew", padx=50, pady=15)


# Start the application loop
select_window.mainloop()




