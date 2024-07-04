from customtkinter import *
from dy_PageUtils import (create_standard_entry, create_image_label, create_warning_label, validate_and_remove_leading_space,
                          load_image, configure_frame, validate_all,
                          create_eye_button, validate_no_space,
                          set_icon_image, display_success_and_close)
from Utils_PageRegister import check_entries_complete, handle_password_input, handle_ecpassword_input, disable_submit_button, enable_submit_button
from db_con import validate_and_update_password
import re

def forgot_password(forgot_frame, back_button, si_eye, SIbtn, secquestion, sec_id):
    def validate_password_policy(password, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel):
        if len(password) >= 8:
            ep8charlabel.configure(text_color="green")
        else:
            ep8charlabel.configure(text_color="red")

        if re.search(r'[A-Z]', password):
            epupperlabel.configure(text_color="green")
        else:
            epupperlabel.configure(text_color="red")

        if re.search(r'[a-z]', password):
            eplowerlabel.configure(text_color="green")
        else:
            eplowerlabel.configure(text_color="red")

        if re.search(r'[0-9]', password):
            epnumberlabel.configure(text_color="green")
        else:
            epnumberlabel.configure(text_color="red")

        if re.search(r'[!@#$%_&*(),.?]', password):
            epspeclabel.configure(text_color="green")
        else:
            epspeclabel.configure(text_color="red")

    def set_policy_labels_color_to_red(ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel):
        ep8charlabel.configure(text_color="red")
        epnumberlabel.configure(text_color="red")
        epupperlabel.configure(text_color="red")
        epspeclabel.configure(text_color="red")
        eplowerlabel.configure(text_color="red")

    def check_password_match(Epassword, Ecpassword, ecpExistlabel, submitbtn, Secqstn):
        password = Epassword.get().strip()
        confirm_password = Ecpassword.get().strip()
        security_question = Secqstn.get().strip()

        if password and confirm_password:
            if password == confirm_password:
                ecpExistlabel.configure(text="Passwords match", text_color="green")
                if password and confirm_password and security_question:
                    enable_submit_button(submitbtn)
                else:
                    disable_submit_button(submitbtn)
            else:
                ecpExistlabel.configure(text="Passwords do not match", text_color="red")
                disable_submit_button(submitbtn)
        else:
            ecpExistlabel.configure(text="", text_color="red")
            disable_submit_button(submitbtn)

    def handle_password_input(Epassword, Ecpassword, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel, ecpExistlabel, submitbtn, Secqstn):
        password = Epassword.get().strip()
        confirm_password = Ecpassword.get().strip()

        if not password:
            set_policy_labels_color_to_red(ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel)
            ecpExistlabel.configure(text="Enter Password First!" if confirm_password else "", text_color="red")
        else:
            validate_password_policy(password, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel)
            if all([ep8charlabel.cget("text_color") == "green",
                    epnumberlabel.cget("text_color") == "green",
                    epupperlabel.cget("text_color") == "green",
                    epspeclabel.cget("text_color") == "green",
                    eplowerlabel.cget("text_color") == "green"]):
                Ecpassword.configure(state="normal", show='' if confirm_password_visible[0] else '*')
                check_password_match(Epassword, Ecpassword, ecpExistlabel, submitbtn, Secqstn)
            else:
                ecpExistlabel.configure(text="", text_color="red")
                disable_submit_button(submitbtn)

    def handle_security_question_input(Secqstn, Epassword, Ecpassword, ecpExistlabel, submitbtn):
        security_question = Secqstn.get().strip()
        password = Epassword.get().strip()
        confirm_password = Ecpassword.get().strip()

        if security_question and password and confirm_password and password == confirm_password:
            enable_submit_button(submitbtn)
        else:
            disable_submit_button(submitbtn)

    ForgotPfr = CTkFrame(forgot_frame, fg_color="#F6FCFC", width=753, height=700, border_color="#B9BDBD", border_width=2, corner_radius=10)
    ForgotPfr.place(relx=0.5, rely=0.5, anchor='center')
    configure_frame(ForgotPfr, [2, 8, 2], [1, 10, 1])

    ForgotPfr.grid_propagate(False)

    NewPLabel = CTkLabel(ForgotPfr, fg_color="transparent", text="New Password", font=("Inter", 40, "bold"), text_color="#333333")
    NewPLabel.grid(row=0, column=1, sticky="s")
    NewpassF = CTkFrame(ForgotPfr, fg_color="transparent", corner_radius=10, width=660, height=780)
    NewpassF.grid(row=1, column=1, sticky="nsew", padx=10, pady=15)
    configure_frame(NewpassF, [1, 4, 5, 4, 1], [1, 10, 1])

    def to_lowercase(event):
        current_text = Secqstn.get()
        Secqstn.delete(0, 'end')
        Secqstn.insert(0, current_text.lower())

    InputF2 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF2.grid(row=1, column=1, sticky="nsew", pady=2)
    configure_frame(InputF2, [2, 4, 2], [1])
    Secqstn = create_standard_entry(InputF2, secquestion)
    Secqstnimage = create_image_label(InputF2, 'secquestion_astrsk.png', 184, 19)
    Secqstn.bind("<KeyPress>", lambda event: validate_all(event, Secqstn, 16, 0))
    Secqstn.bind('<KeyRelease>', to_lowercase)
    SecExistlabel = create_warning_label(InputF2, "")

    eyecloseimg = load_image('Eye_Close.png', (25, 20))
    eyeopenimg = load_image('Eye_Open.png', (25, 16))

    InputF3 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF3.grid(row=2, column=1, sticky="nsew", pady=2)
    configure_frame(InputF3, [2, 4, 1, 1, 1], [1])
    Epassword = create_standard_entry(InputF3, "Enter Password")
    Epasswordimage = create_image_label(InputF3, 'password_astrsk.png', 124, 18, anchor="w")
    Epassword.bind("<KeyPress>", lambda event: validate_all(event, Epassword, 16, 0))
    Epassword.bind("<Key>", validate_no_space)
    Epassword.configure(show="*")
    password_visible = [False]
    eyep_button = create_eye_button(InputF3, Epassword, password_visible, eyecloseimg, eyeopenimg, relx=0.93, rely=0.44)

    pass1_policy = CTkFrame(InputF3, fg_color="transparent")
    pass1_policy.grid(row=2, column=0, sticky="nswe")
    configure_frame(pass1_policy, [1], [2, 3])
    ep8charlabel = CTkLabel(pass1_policy, text="* At least  8 characters.", fg_color="transparent", font=("Inter", 12), text_color="red")
    ep8charlabel.grid(row=0, column=0, sticky="w")
    epnumberlabel = CTkLabel(pass1_policy, text="* At least one number.", fg_color="transparent", font=("Inter", 12), text_color="red")
    epnumberlabel.grid(row=0, column=1, sticky="w")

    pass2_policy = CTkFrame(InputF3, fg_color="transparent")
    pass2_policy.grid(row=3, column=0, sticky="nswe")
    configure_frame(pass2_policy, [1], [2, 3])
    epupperlabel = CTkLabel(pass2_policy, text="* At least one uppercase letter.", fg_color="transparent", font=("Inter", 12), text_color="red")
    epupperlabel.grid(row=0, column=0, sticky="w")
    epspeclabel = CTkLabel(pass2_policy, text="* At least one special character. !@#$%_&*(),.?", fg_color="transparent", font=("Inter", 12), text_color="red")
    epspeclabel.grid(row=0, column=1, sticky="w")

    pass3_policy = CTkFrame(InputF3, fg_color="transparent")
    pass3_policy.grid(row=4, column=0, sticky="nswe")
    configure_frame(pass3_policy, [1], [2, 1])
    eplowerlabel = CTkLabel(pass3_policy, text="* At least one lowercase letter.", fg_color="transparent", font=("Inter", 12), text_color="red")
    eplowerlabel.grid(row=0, column=0, sticky="w")

    Epassword.bind("<KeyRelease>", lambda event: handle_password_input(Epassword, Ecpassword, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel, ecpExistlabel, submitbtn, Secqstn))

    InputF4 = CTkFrame(NewpassF, fg_color="transparent", corner_radius=10)
    InputF4.grid(row=3, column=1, sticky="nsew", pady=2)
    configure_frame(InputF4, [2, 5, 2], [1])
    Ecpassword = create_standard_entry(InputF4, "Confirm Password")
    Ecpasswordimage = create_image_label(InputF4, 'cpassword_astrsk.png', 209, 18)
    Ecpassword.bind("<KeyPress>", lambda event: validate_all(event, Ecpassword, 16, 0))
    Ecpassword.bind("<Key>", validate_no_space)
    Ecpassword.configure(show="*")
    confirm_password_visible = [False]
    eyecp_button = create_eye_button(InputF4, Ecpassword, confirm_password_visible, eyecloseimg, eyeopenimg)
    ecpExistlabel = create_warning_label(InputF4, "")

    Ecpassword.bind("<KeyRelease>", lambda event: handle_password_input(Epassword, Ecpassword, ep8charlabel, epnumberlabel, epupperlabel, epspeclabel, eplowerlabel, ecpExistlabel, submitbtn, Secqstn))
    Secqstn.bind("<KeyRelease>", lambda event: handle_security_question_input(Secqstn, Epassword, Ecpassword, ecpExistlabel, submitbtn))

    BtnNPF = CTkFrame(ForgotPfr, fg_color="transparent", corner_radius=10)
    BtnNPF.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
    configure_frame(BtnNPF, [1], [1, 1])
    submitbtn = CTkButton(BtnNPF, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.52, rely=0.42, anchor="w")

    cancelbtn = CTkButton(BtnNPF, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848", 
                        command=lambda: [ForgotPfr.destroy(), back_button.configure(state="normal"), si_eye.configure(state="normal")])
    cancelbtn.place(relx=0.48, rely=0.42, anchor="e")


    def clear_warning_label():
        SecExistlabel.configure(text="")

    def validate_and_open_homepage():
        answer = Secqstn.get().strip()
        newpassword = Ecpassword.get().strip()
        success, message = validate_and_update_password(sec_id, answer, newpassword)
        if success:
            back_button.configure(state="normal")
            si_eye.configure(state="normal")
            ForgotPfr.destroy()  # Destroy the select window first
            forgot_frame.after(100, lambda: display_success_and_close(forgot_frame, message))  # Display success message with a slight delay
        else:
            ecpExistlabel.configure(text="")
            submitbtn.configure(state="disabled")
            Secqstn.delete(0, END)
            SecExistlabel.configure(text=message)
            SecExistlabel.after(3000, clear_warning_label)

    submitbtn.configure(command=validate_and_open_homepage)


def display_success_and_close(forgot_frame, success):
    SetnpScssfr = CTkFrame(forgot_frame, fg_color="white", width=600, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
    SetnpScssfr.place(relx=0.5, rely=0.5, anchor='center')
    set_icon_image(SetnpScssfr, 'success_icon.png', relx=0.5, rely=0.195, anchor='n', size=(110, 110))
    LbSuccess = CTkLabel(SetnpScssfr, text=success, fg_color="transparent", font=("Inter", 30, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.65, anchor='n')
    forgot_frame.after(3500, SetnpScssfr.destroy)
