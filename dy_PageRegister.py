#Page Register
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from db_con import register_security_admin
from dy_PageUtils import (create_standard_entry, create_standard_label, create_warning_label,
                          load_image, configure_frame, validate_length, validate_full_name,
                          toggle_password_visibility, check_entries_complete, change_border_color,
                          check_password_match, handle_password_input, display_success_and_close)
def open_register_window(main_window):
    # register_window = CTk()
    register_window = CTkToplevel(main_window)
    register_window.grab_set()
    register_window.geometry('1200x800+400+100')
    register_window.title('Register Account')
    register_window.minsize(1000, 900)
    register_window.configure(fg_color='white')
    register_window.maxsize(register_window.winfo_screenwidth(), register_window.winfo_screenheight())
    register_window.rowconfigure((0, 2), weight=1, uniform='a')
    register_window.rowconfigure(1, weight=10, uniform='a')

    def registeron_resize(event):
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
            register_window.columnconfigure(i, weight=weight, uniform='a')

    register_window.bind('<Configure>', registeron_resize)

    CreateF = CTkFrame(register_window, fg_color="#D1DDE2", corner_radius=10, width=660, height=780)
    CreateF.grid(row=1, column=3, sticky="nsew", padx=10)
    configure_frame(CreateF, [1, 4, 4, 4, 4, 4, 4], [1, 10, 1])

    LabelFrame = CTkLabel(CreateF, fg_color="transparent", text="Create Account", font=("Inter", 40, "bold"), text_color="#333333")
    LabelFrame.grid(row=1, column=1)

    LogoF = CTkFrame(register_window, fg_color="light pink", corner_radius=10, width=660, height=400)
    LogoF.grid(row=1, column=1)

    BackF = CTkFrame(register_window, fg_color="transparent", corner_radius=10, width=110, height=40)
    BackF.grid(row=2, column=0, sticky="nsew")
    configure_frame(CreateF, [1], [1])

    backimage = load_image('Back_icon.png', (95, 40))
    back_button = CTkButton(BackF, image=backimage, text='', fg_color="white", hover_color="white", command=register_window.destroy)
    back_button.grid(row=0, column=0, sticky="e", padx=18)

    # FULL NAME
    InputF1 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
    InputF1.grid(row=2, column=1, sticky="nsew", pady=2)
    configure_frame(InputF1, [2, 4, 2], [1])
    Efullname = create_standard_entry(InputF1, "Enter Full Name")
    Lfullname = create_standard_label(InputF1, 'Full Name')
    Efullname.bind("<KeyPress>", validate_full_name)
    Efullname.bind("<KeyPress>", lambda event: validate_length(event, Efullname, 50))
    Efullname.bind("<KeyRelease>", lambda event: change_border_color(Efullname))
    FnExistlabel = create_warning_label(InputF1, "")

    # USERNAME
    InputF2 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
    InputF2.grid(row=3, column=1, sticky="nsew", pady=2)
    configure_frame(InputF2, [2, 4, 2], [1])
    Eusername = create_standard_entry(InputF2, "Enter Username")
    Eusername.bind("<KeyPress>", lambda event: validate_length(event, Eusername, 50))
    Eusername.bind("<KeyRelease>", lambda event: change_border_color(Eusername))
    Lusername = create_standard_label(InputF2, 'Username')
    UnExistlabel = create_warning_label(InputF2, "")

    # PASSWORD
    InputF3 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
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

    # CONFIRM PASSWORD
    InputF4 = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
    InputF4.grid(row=5, column=1, sticky="nsew", pady=2)
    configure_frame(InputF4, [2, 4, 2], [1])
    Ecpassword = create_standard_entry(InputF4, "Confirm Password")
    Ecpassword.bind("<KeyPress>", lambda event: validate_length(event, Ecpassword, 45))
    Ecpassword.bind("<KeyRelease>", lambda event: change_border_color(Ecpassword))
    Ecpassword.configure(show="*")
    Lcpassword = create_standard_label(InputF4, 'Confirm Password')
    eyecp_button = CTkButton(InputF4, image=eyecloseimg, text='', width=10, fg_color='#F9F9FA', hover_color="#F9F9FA", corner_radius=0, border_width=0)
    eyecp_button.place(relx=0.93, rely=0.5, anchor="center")
    confirm_password_visible = [False]
    eyecp_button.configure(command=lambda: toggle_password_visibility(Ecpassword, eyecp_button, confirm_password_visible, eyecloseimg, eyeopenimg))
    ecpExistlabel = create_warning_label(InputF4, "")

    CAFrame = CTkFrame(CreateF, fg_color="transparent", corner_radius=10)
    CAFrame.grid(row=6, column=1, sticky="nsew")
    configure_frame(CAFrame, [1], [1])

    CAbtn = CTkButton(CAFrame, text="Create Account", width=180, height=50, corner_radius=10,
                    fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"),
                    text_color="#333333", state="disabled")
    CAbtn.grid(row=0, column=0, sticky="ne", pady=20)

    entries = [Efullname, Eusername, Epassword, Ecpassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries, ecp_label=ecpExistlabel, createbtn=CAbtn,
                Epassword=Epassword, Ecpassword=Ecpassword: check_entries_complete(entries, ecp_label, createbtn, Epassword, Ecpassword))
    Epassword.bind("<KeyRelease>", lambda event: handle_password_input(Epassword, Ecpassword, ecpExistlabel, CAbtn, epExistlabel))
    Ecpassword.bind("<KeyRelease>", lambda event: check_password_match(Epassword, Ecpassword, ecpExistlabel, CAbtn))

    def handle_registration():
        CAbtn.configure(state="disabled")

        full_name = Efullname.get()
        username = Eusername.get()
        password = Ecpassword.get()

        try:
            success = register_security_admin(full_name, username, password, register_window, FnExistlabel, UnExistlabel)
            if success:
                display_success_and_close(register_window)
            else:
                register_window.after(3000, clear_error_labels)
                CAbtn.configure(state="normal")
        except Exception as e:
            print(f"Error during registration: {e}")
            ecpExistlabel.configure(text="An unexpected error occurred. Please try again.", text_color="red")
            CAbtn.configure(state="normal")
            register_window.after(3000, clear_error_labels)

    def clear_error_labels():
        FnExistlabel.configure(text='')
        UnExistlabel.configure(text='')

    CAbtn.configure(command=handle_registration)
