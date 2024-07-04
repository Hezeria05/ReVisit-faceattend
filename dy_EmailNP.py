from customtkinter import *
from dy_PageUtils import (create_standard_entry, create_image_label, create_warning_label, validate_and_remove_leading_space,
                          load_image, configure_frame, validate_all,
                          create_eye_button, validate_no_space,
                          set_icon_image, display_success_and_close)
from Utils_PageRegister import check_entries_complete, handle_password_input, handle_ecpassword_input
from db_con import validate_and_update_password, validate_uname
from dy_NewPass import forgot_password

def new_password(forgot_frame, back_button, eyep_button, SIbtn):
    eyep_button.configure(state="disabled")
    SIbtn.configure(state="disabled")
    back_button.configure(state="disabled")
    
    # Create the ForgotPfr frame with fixed dimensions and configurations
    EmailPfr = CTkFrame(forgot_frame, fg_color="#F6FCFC", width=753, height=350, border_color="#B9BDBD", border_width=2, corner_radius=10)
    EmailPfr.place(relx=0.5, rely=0.5, anchor='center')
    configure_frame(EmailPfr, [2, 3, 2], [1, 10, 1])
    
    # Ensure the frame does not resize with its contents
    EmailPfr.grid_propagate(False)
    EmPLabel = CTkLabel(EmailPfr, fg_color="transparent", text="Forgot Password", font=("Inter", 35, "bold"), text_color="#333333")
    EmPLabel.grid(row=0, column=1, sticky="s", pady=10)

    # USERNAME
    InputF2 = CTkFrame(EmailPfr, fg_color="transparent", corner_radius=10)
    InputF2.grid(row=1, column=1, sticky="nsew", pady=2)
    configure_frame(InputF2, [2, 3, 1], [1])
    Eusername = create_standard_entry(InputF2, "Enter Username")
    UnExistlabel = create_warning_label(InputF2, "")
    Eusernameimage = create_image_label(InputF2, 'username_astrsk.png', 124, 18)
    Eusername.bind("<KeyPress>", lambda event: validate_all(event, Eusername, 50, 0))

    BtnNPF = CTkFrame(EmailPfr, fg_color="transparent", corner_radius=10)
    BtnNPF.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
    configure_frame(BtnNPF, [1], [1, 1])
    submitbtn = CTkButton(BtnNPF, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.52, rely=0.42, anchor="w")
    cancelbtn = CTkButton(BtnNPF, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848", 
                        command=lambda: [EmailPfr.destroy(), back_button.configure(state="normal"), eyep_button.configure(state="normal")])
    cancelbtn.place(relx=0.48, rely=0.42, anchor="e")
    
    def clear_warning_label():
        UnExistlabel.configure(text="")

    def validate_and_open_homepage():
        username = Eusername.get().strip()
        success, message, secquestion, sec_id = validate_uname(username)
        if success:
            # Destroy the select window first
            forgot_password(forgot_frame, back_button, eyep_button, SIbtn, secquestion, sec_id)
            EmailPfr.destroy() 
        else:
            UnExistlabel.configure(text=message)  # Handle the invalid username case
            submitbtn.configure(state="disabled")
            Eusername.delete(0, END)
            UnExistlabel.after(3000, clear_warning_label)
    
    def on_username_change(event):
        username = Eusername.get().strip()
        if username:
            submitbtn.configure(state="normal")
        else:
            submitbtn.configure(state="disabled")

    Eusername.bind("<KeyRelease>", on_username_change)

    submitbtn.configure(command=validate_and_open_homepage)
