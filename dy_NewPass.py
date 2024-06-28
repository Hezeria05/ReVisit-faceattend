from customtkinter import *
from dy_PageUtils import (create_standard_entry, create_image_label, create_warning_label, validate_and_remove_leading_space,
                          load_image, configure_frame, validate_all,
                          create_eye_button,validate_no_space,
                          set_icon_image, display_success_and_close)
from Utils_PageRegister import check_entries_complete, handle_password_input, handle_ecpassword_input
from db_con import validate_and_update_password

def new_password(forgot_frame, back_button):
    back_button.configure(state="disabled")
    # Create the ForgotPfr frame with fixed dimensions and configurations
    ForgotPfr = CTkFrame(forgot_frame, fg_color="#F6FCFC", width=753, height=679, border_color="#B9BDBD", border_width=2, corner_radius=10)
    ForgotPfr.place(relx=0.5, rely=0.5, anchor='center')
    configure_frame(ForgotPfr, [2, 8, 2], [1, 10, 1])

    # Ensure the frame does not resize with its contents
    ForgotPfr.grid_propagate(False)

    # Create the NewPLabel with specified properties
    NewPLabel = CTkLabel(ForgotPfr, fg_color="transparent", text="New Password", font=("Inter", 40, "bold"), text_color="#333333")
    NewPLabel.grid(row=0, column=1, sticky="s")
    NewpassF = CTkFrame(ForgotPfr, fg_color="transparent", corner_radius=10, width=660, height=780)
    NewpassF.grid(row=1, column=1, sticky="nsew", padx=10, pady=15)
    configure_frame(NewpassF, [1, 4, 4, 4, 1], [1, 10, 1])

    InputF2 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF2.grid(row=1, column=1, sticky="nsew", pady=2)
    configure_frame(InputF2, [2, 4, 2], [1])
    Eusername = create_standard_entry(InputF2, "Enter Username")
    Eusernameimage = create_image_label(InputF2, 'username_astrsk.png', 109, 16)
    Eusername.bind("<KeyPress>", lambda event: validate_all(event, Eusername, 50, 0))
    UnExistlabel = create_warning_label(InputF2, "")

    #------------------- Password
    eyecloseimg = load_image('Eye_Close.png', (25, 20))
    eyeopenimg = load_image('Eye_Open.png', (25, 16))
    InputF3 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF3.grid(row=2, column=1, sticky="nsew", pady=2)
    configure_frame(InputF3, [2, 4, 2], [1])
    Epassword = create_standard_entry(InputF3, "Enter New Password")
    Epasswordimage = create_image_label(InputF3, 'New_Password.png', 154, 16)
    Epassword.bind("<KeyPress>", lambda event: validate_all(event, Epassword, 16, 0))
    Epassword.bind("<Key>", validate_no_space)
    Epassword.configure(show="*")
    password_visible = [False]
    eyep_button = create_eye_button(InputF3, Epassword, password_visible, eyecloseimg, eyeopenimg)
    epExistlabel = create_warning_label(InputF3, "")

    InputF4 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF4.grid(row=3, column=1, sticky="nsew", pady=2)
    configure_frame(InputF4, [2, 4, 2], [1])
    Ecpassword = create_standard_entry(InputF4, "Confirm Password")
    Ecpasswordimage = create_image_label(InputF4, 'cpassword_astrsk.png', 194, 16)
    Ecpassword.bind("<KeyPress>", lambda event: validate_all(event, Ecpassword, 16, 0))
    Ecpassword.configure(show="*")
    confirm_password_visible = [False]
    eyecp_button = create_eye_button(InputF4, Ecpassword, confirm_password_visible, eyecloseimg, eyeopenimg)
    ecpExistlabel = create_warning_label(InputF4, "")

    BtnNPF = CTkFrame(ForgotPfr, fg_color="transparent", corner_radius=10, width=660, height=780)
    BtnNPF.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
    configure_frame(BtnNPF, [1], [1,1])
    submitbtn = CTkButton(BtnNPF, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.52, rely=0.42, anchor="w")

    entries = [Eusername, Epassword, Ecpassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event: check_entries_complete(entries, ecpExistlabel, submitbtn, Epassword, Ecpassword))
    Epassword.bind("<KeyRelease>", lambda event: handle_password_input(Epassword, Ecpassword, ecpExistlabel, submitbtn, epExistlabel, confirm_password_visible, entries))
    Ecpassword.bind("<KeyRelease>", lambda event: handle_ecpassword_input(Epassword, Ecpassword, ecpExistlabel, submitbtn, epExistlabel, confirm_password_visible, entries))

    def clear_warning_label():
        UnExistlabel.configure(text="")

    def validate_and_open_homepage():
        username = Eusername.get()
        newpassword = Ecpassword.get()
        success, message = validate_and_update_password(username, newpassword)
        if success:
            back_button.configure(state="normal")
            ForgotPfr.destroy()  # Destroy the select window first
            forgot_frame.after(100, lambda: display_success_and_close(forgot_frame, message))  # Display success message with a slight delay
        else:
            UnExistlabel.configure(text=message)  # Handle the invalid username case
            ecpExistlabel.configure(text="")
            Eusername.delete(0, END)
            Epassword.delete(0, END)
            Ecpassword.delete(0, END)
            UnExistlabel.after(3000, clear_warning_label)

    submitbtn.configure(command=validate_and_open_homepage)

    cancelbtn = CTkButton(BtnNPF, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848", command=lambda: [ForgotPfr.destroy(), back_button.configure(state="normal")])
    cancelbtn.place(relx=0.48, rely=0.42, anchor="e")

def display_success_and_close(forgot_frame, success):
    SetnpScssfr = CTkFrame(forgot_frame, fg_color="white", width=600, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
    SetnpScssfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(SetnpScssfr, 'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
    LbSuccess = CTkLabel(SetnpScssfr, text=success, fg_color="transparent", font=("Inter", 30, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
    forgot_frame.after(3500, SetnpScssfr.destroy)
