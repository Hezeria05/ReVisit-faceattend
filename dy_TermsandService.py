from customtkinter import *
from pathlib import Path
from db_con import register_security_admin, check_security_admin
from dy_PageUtils import (
    create_standard_entry, create_image_label, create_warning_label, check_leading_space,
    load_image, configure_frame, validate_all, create_eye_button, capitalize_first_letter, validate_no_space,
    display_success_and_close
)
from Utils_PageRegister import check_entries_complete, handle_password_input, handle_ecpassword_input

def submit_registration(window, sec_frame, full_name, username, password, security_question, security_answer):
    print(f"Full Name: {full_name}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Security Question: {security_question}")
    print(f"Security Answer: {security_answer}")
    
    def agree_registration(full_name, username, password, security_question, security_answer, window, sec_frame):
        try:
            success = register_security_admin(full_name, username, password, security_question, security_answer, window)
            if success:
                terms_frame.destroy()
                sec_frame.destroy()
                display_success_and_close(window)
            else:
                display_success_and_close(window, path='warning_icon.png', text="An error has occurred.")
        except Exception as e:
            print(f"Error during registration: {e}")
            display_success_and_close(window, path='warning_icon.png', text="Please Try Again.")

    def toggle_submit_button():
        if terms_var.get() == 1:
            submitbtn.configure(state=NORMAL)
        else:
            submitbtn.configure(state=DISABLED)
    
    # Creating the main terms frame
    terms_frame = CTkFrame(window, fg_color="#F6FCFC", width=800, height=800, border_color="#B9BDBD", border_width=1, corner_radius=5)
    terms_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    # Creating a frame within the terms frame for agreement content
    agree_f = CTkFrame(terms_frame, fg_color="transparent", width=750, height=650, corner_radius=0)
    agree_f.place(relx=0.5, rely=0.03, anchor='n')

    # Creating the scrollable frame inside the agree_f
    scrollable_frame = CTkScrollableFrame(agree_f, width=700, height=620, corner_radius=0, fg_color="white",
                                          border_color="#D1DDE2", border_width=1,scrollbar_button_color= "#D1DDE2",
                                          scrollbar_button_hover_color="#0E6283")
    scrollable_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Adding content to the scrollable frame
    main_title = "\nTerms & Conditions"
    main_title_label = CTkLabel(master=scrollable_frame, text=main_title, font=("Helvetica", 35, "bold"), anchor="w", justify="left")
    main_title_label.pack(padx=10, pady=(10, 0))

    sections = [
        ("1. Introduction",
         "1.1. Welcome to ReVisit: Facial Recognition Attendance System, a facial recognition attendance system for non-resident visitors of Celina Homes 5 Subdivision, Brgy. Tagapo, Sta. Rosa City, Laguna. Please read these Terms of Service carefully before using this System or creating an account so that you are aware of your legal rights and obligations.\n"
         "1.2. The 'Services' provided include (a) the System, (b) the services provided by the System, and (c) all information, features, data, text, images, photographs, graphics, and other materials made available through the System. Any new features added to or augmenting the Services are also subject to these Terms of Service.\n"
         "1.3. By creating an Account, you give your irrevocable acceptance of and consent to the terms of this Agreement. If you do not agree to these terms, please do not use our Services or access the System."),
        ("2. Privacy",
         "2.1. Your privacy is very important to us. Our Privacy Policy explains how we collect, use, disclose, and protect your personal data. By using the Services or providing information on the System, you consent to the processing of your personal data as described in the Privacy Policy.\n"
         "2.2. Users in possession of another entity’s personal data agree to (a) comply with all applicable personal data protection laws, and (b) allow the User to review what information has been collected about them."),
        ("3. Accounts and Security",
         "3.1. Some functions of our Services require registration for an Account by selecting a unique username and password, and by providing certain personal information.\n"
         "3.2. You agree to:\n"
         "(a) keep your password confidential and use only your Username and password when logging in, \n"
         "(b) make sure that you log out from your account at the end of each session on the System, \n"
         "(c) immediately notify us of any unauthorized use of your Account, Username, and/or password, and\n"
         "(d) ensure that your Account information is accurate and up-to-date. You are fully responsible for all activities that occur under your Username and Account even if such activities or uses were not committed by you."
         "\nWe will not be liable for any loss or damage arising from unauthorized use of your password or your failure to comply with this Section."),
        ("4. Terms of Use",
         "4.1. The System is to be accessed only by authorized personnel, specifically security personnel, who are required to create user accounts to access the System. The authorized personnel are responsible for verifying the identity of non-resident visitors through a valid ID, although they are not required to collect the ID during the visitor's stay."
         "\n4.2. You agree not to:\n"
         "• Disclose data or any content stored in the system to unauthorized users.\n"
         "• Use the System for any unlawful or unauthorized purpose.\n"
         "• Attempt to gain unauthorized access to the System or its related systems or networks.\n"
         "• Use the System in a manner that could damage, disable, overburden, or impair the System or interfere with any other party’s use of the System."),
        ("5. System Components",
         "5.1. The System is composed of the following key components:\n"
         "• Register: Non-resident visitors must register their face data, which is stored as binaries for the duration of their visit. This data is deleted upon logout. The visitor's name is also collected.\n"
         "• Login/Logout: Visitors log in and out of the system, with their data reflecting their name, login date and time, logout time, the address they are visiting, and the security personnel on duty.\n"
         "• Visitor Data: Contains the names, system date and time information, area where they are headed, their purpose of visit, and the security personnel on duty.\n"
         "• Residents List: Contains the names and contact numbers of residents for reference and verification purposes."),
        ("6. Data Handling and Security",
         "6.1. Visitor Data: Visitor data, specifically face data, is temporarily stored during the visit and deleted upon logout. This data is used solely for verifying the visitor's identity to contribute to the security within the subdivision.\n"
         "6.2. Resident Data: Resident data includes names and contact numbers, used only for reference and verification of visits. This data is securely stored and accessed only by authorized personnel.\n"
         "6.3. Security Personnel: Authorized security personnel are required to create user accounts to access the system. They must verify the identity of non-resident visitors through a valid ID but are not required to collect the ID during the visit.\n"
         "6.4. Data Protection: Access to data is restricted to authorized personnel only.\n"
         "\n\nBy using the ReVisit: Facial Recognition Attendance System, you agree to these terms and conditions. If you have any questions or concerns, please contact us for further assistance.\n")
    ]

    for section_title, section_text in sections:
        title_label = CTkLabel(master=scrollable_frame, text=section_title, font=("Helvetica", 20, "bold"), anchor="w", justify="left")
        title_label.pack(fill="x", anchor="w", padx=10, pady=(10, 0))

        text_label = CTkLabel(master=scrollable_frame, text=section_text, wraplength=650, anchor="w", justify="left")
        text_label.pack(fill="x", anchor="w", padx=20, pady=(0, 0))

    # Checkbox for terms and conditions
    terms_var = IntVar()
    checkbox_frame = CTkFrame(terms_frame, fg_color="transparent", width=750, height=50,)
    checkbox_frame.place(relx=0.5, rely=0.83, anchor='n')
    
    checkbox = CTkCheckBox(checkbox_frame, text="By clicking, you are confirming that you have read, understood and agree to \nReVisit: Facial Recognition Attendance System Terms and Conditions.",
                           border_width= 1, hover_color="#D1DDE2", fg_color="#0E6283",variable=terms_var, onvalue=1, offvalue=0, command=toggle_submit_button)
    checkbox.place(relx=0.03, rely=0.5, anchor='w')

    # Buttons for submit and cancel
    submitbtn = CTkButton(terms_frame, text="Submit", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                                    hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#333333", state=DISABLED,
                                    command=lambda: agree_registration(full_name, username, password, security_question, security_answer, window, sec_frame))
    submitbtn.place(relx=0.52, rely=0.939, anchor="w")

    cancelbtn = CTkButton(terms_frame, text="Cancel", width=120, height=48, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 19, "bold"), text_color="#484848",
                        command=lambda: terms_frame.destroy())
    cancelbtn.place(relx=0.48, rely=0.939, anchor="e")