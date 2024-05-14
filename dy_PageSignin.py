from customtkinter import *
from PIL import Image, ImageTk
from dy_PageUtils import (create_standard_entry, create_standard_label, create_warning_label,
                          load_image, configure_frame, validate_length, validate_full_name,
                          toggle_password_visibility, check_entries_complete, change_border_color,
                          check_password_match, handle_password_input, display_success_and_close
                          , check_sign_complete, signin_failed)
from db_con import validate_login_credentials
from  MainPage import open_homepage

def open_signin_window(select_window):
# signin_window = CTk()
    signin_window = CTkToplevel(select_window)
    signin_window.grab_set()
    signin_window.geometry('1200x800+400+100')
    signin_window.title('Sign In')
    signin_window.minsize(1000, 900)
    signin_window.configure(fg_color='white')
    signin_window.maxsize(signin_window.winfo_screenwidth(), signin_window.winfo_screenheight())
    signin_window.rowconfigure((0, 2), weight=1, uniform='a')
    signin_window.rowconfigure(1, weight=10, uniform='a')

    def signinon_resize(event):
            width = event.width
            min_width = 1000
            max_width = 1200
            if min_width <= width < max_width:
                column_weights = (1, 1, 1, 10, 3)
                LogoF.grid_forget()
                BackF.grid(row=2, column=0, columnspan=1, sticky="nsew")
            elif width >= max_width:
                column_weights = (2, 5, 2, 7, 1)
                LogoF.grid(row=1, column=1)
                BackF.grid(row=2, column=0, sticky="nsew")

            for i, weight in enumerate(column_weights):
                signin_window.columnconfigure(i, weight=weight, uniform='a')

    signin_window.bind('<Configure>', signinon_resize)

    SignFrame = CTkFrame(signin_window, fg_color="#D1DDE2", corner_radius=10, width=660, height=780)
    SignFrame.grid(row=1, rowspan=2, column=3, sticky="ew", padx=10)
    configure_frame(SignFrame, [1, 4, 2, 4, 4, 4, 4], [1, 10, 1])

    LabelFrame = CTkLabel(SignFrame, fg_color="transparent", text="Sign In", font=("Inter", 40, "bold"), text_color="#333333")
    LabelFrame.grid(row=1, column=1, sticky="s")

    LogoF = CTkFrame(signin_window, fg_color="light pink", corner_radius=10, width=660, height=400)
    LogoF.grid(row=1, column=1)

    BackF = CTkFrame(signin_window, fg_color="transparent", corner_radius=10, width=110, height=40)
    BackF.grid(row=2, column=0, sticky="nsew")
    configure_frame(SignFrame, [1], [1])

    backimage = load_image('Back_icon.png', (95, 40))
    back_button = CTkButton(BackF, image=backimage, text='', fg_color="white", hover_color="white", command=signin_window.destroy)
    back_button.grid(row=0, column=0, sticky="e", padx=18)


    # USERNAME
    InputF2 = CTkFrame(SignFrame, fg_color="transparent", corner_radius=10)
    InputF2.grid(row=3, column=1, sticky="nsew", pady=2)
    configure_frame(InputF2, [2, 4, 2], [1])
    Eusername = create_standard_entry(InputF2, "Enter Username")
    Eusername.bind("<KeyPress>", lambda event: validate_length(event, Eusername, 50))
    Eusername.bind("<KeyRelease>", lambda event: change_border_color(Eusername))
    Lusername = create_standard_label(InputF2, 'Username')
    UnExistlabel = create_warning_label(InputF2, "")

    # PASSWORD
    InputF3 = CTkFrame(SignFrame, fg_color="transparent", corner_radius=10)
    InputF3.grid(row=4, column=1, sticky="nsew", pady=2)
    configure_frame(InputF3, [2, 4, 2], [1])
    Epassword = create_standard_entry(InputF3, "Enter Password")
    Epassword.bind("<KeyPress>", lambda event: validate_length(event, Epassword, 45))
    Epassword.bind("<KeyRelease>", lambda event: change_border_color(Epassword))
    Epassword.configure(show="*")
    Lpassword = create_standard_label(InputF3, 'Enter Password')
    eyecloseimg = load_image('Eye_Close.png', (25, 20))
    eyeopenimg = load_image('Eye_Open.png', (25, 16))
    eyep_button = CTkButton(InputF3, image=eyecloseimg, text='', width=10, fg_color='#F9F9FA', hover_color="#F9F9FA", corner_radius=0, border_width=0)
    eyep_button.place(relx=0.93, rely=0.5, anchor="center")
    password_visible = [False]
    eyep_button.configure(command=lambda: toggle_password_visibility(Epassword, eyep_button, password_visible, eyecloseimg, eyeopenimg))
    epExistlabel = create_warning_label(InputF3, "")

    SIFrame = CTkFrame(SignFrame, fg_color="transparent", corner_radius=10)
    SIFrame.grid(row=5, column=1, sticky="nsew")
    configure_frame(SIFrame, [1], [1])

    SIbtn = CTkButton(SIFrame, text="Sign In", width=180, height=50, corner_radius=10,
                    fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"),
                    text_color="#333333", state="disabled")
    SIbtn.grid(row=0, column=0, padx=20)

    entries = [Eusername, Epassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, SIbtn))

    def validate_and_open_homepage():
        username = Eusername.get()
        password = Epassword.get()
        success, sec_id = validate_login_credentials(username, password)
        if success:
            select_window.destroy()  # Destroy the select window
            open_homepage(sec_id)  # Pass sec_id as an argument
            signin_window.after(100, signin_window.destroy)
        else:
            signin_failed(signin_window)

    SIbtn.configure(command=validate_and_open_homepage)



    #signin_window.mainloop()