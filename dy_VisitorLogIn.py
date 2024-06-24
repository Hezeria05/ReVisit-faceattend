from customtkinter import *
import cv2
import os
from face_recognition import load_face_data
from dy_PageUtils import (configure_frame, validate_all, view_history, create_image_label,
                          indicate, set_icon_image, load_image)
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from dy_PageVisitor import Visitor_page
from dy_VisitorLogOut import on_logout_click
from Utils_VisitorLogIn import toggle_search_frame

def on_login_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button):

    home_button.configure(state="normal")
    visitor_button.configure(state="normal")
    resident_button.configure(state="normal")
    logout_btn.configure(state="normal")

    # Main login frame
    LogInVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    LogInVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(LogInVframe, [3, 10, 2, 1], [1, 9, 1, 8, 1])

    # Heading
    backimage = load_image('Back_button.png', (35, 34))
    back_button = CTkButton(LogInVframe, image=backimage, text='', fg_color="white", hover_color="white", 
                            command=lambda:[home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button), LogInVframe.destroy(), cap.release()])
    back_button.place(relx=0.001, rely=0.06, anchor="nw")
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.095, rely=0.06, anchor="nw")


    CameraFrame = CTkFrame(LogInVframe, fg_color="white", width=600, height=450, border_color="#B9BDBD", border_width=2)
    CameraFrame.grid(row=1, column=1,)
    BscanFrame = CTkFrame(LogInVframe, fg_color="white")
    BscanFrame.grid(row=2, column=1, sticky="nsew")
    scanbtn = CTkButton(BscanFrame, text="Scan", width=140, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 18, "bold"), text_color="#333333", state="disabled")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')

    # Entry frame for name input
    LogInEframe = CTkFrame(LogInVframe, fg_color="#E9F3F2", corner_radius=10, border_color="#B9BDBD", border_width=2)
    LogInEframe.grid(row=1, column=3, rowspan=2, sticky="nsew")
    configure_frame(LogInEframe, [5, 5, 5, 5, 1, 8], [1, 6, 1])

    LogInHeading = CTkLabel(LogInEframe, text='Login', fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LogInHeading.place(relx=0.5, rely=0.08, anchor='n')

    # VISITOR FORM
    Vnamef = CTkFrame(LogInEframe, fg_color="transparent")
    Vnamef.grid(row=1, column=1, sticky="nsew", pady=3)
    configure_frame(Vnamef,  [2, 4, 1, 1], [1])
    LogVname = CTkEntry(Vnamef, placeholder_text="Enter Visitor Name", height=55,
                        corner_radius=8, border_width=1, border_color='#DEE6EA', state='disabled')
    LogVname.grid(row=1, column=0, sticky="new")
    LbVname = create_image_label(Vnamef, 'Visitor_Name.png', 134, 16)
    LbVname.grid(row=0, column=0, sticky="sw", pady=3)
    ExistingVisit = CTkLabel(Vnamef, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    ExistingVisit.grid(row=2, rowspan=4, column=0, sticky="nw", padx=1)

    # Resident
    Residf = CTkFrame(LogInEframe, fg_color="transparent")
    Residf.grid(row=2, column=1, sticky="nsew", pady=3)
    configure_frame(Residf,  [2, 4, 1, 1], [1])

    ResidID = CTkEntry(Residf, placeholder_text="Search Address..", height=55,
                        corner_radius=8, border_width=1, border_color='#DEE6EA')
    ResidID.grid(row=1, column=0, sticky="new")
    ResidID.bind("<KeyPress>", lambda event: validate_all(event, ResidID, 30, 1))
    LRname = create_image_label(Residf, 'Resident_Address.png', 174, 16)
    LRname.grid(row=0, column=0, sticky="sw", pady=3)
    Invalidwarn = CTkLabel(Residf, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Invalidwarn.grid(row=2, rowspan=4, column=0, sticky="nw", padx=4)

    # Purpose
    Purposef = CTkFrame(LogInEframe, fg_color="transparent")
    Purposef.grid(row=3, column=1, sticky="nsew", pady=3)
    configure_frame(Purposef, [2, 4, 1, 1], [1])

    LogPurpose = CTkEntry(Purposef, placeholder_text="State Purpose", height=55,
                          corner_radius=8, border_width=1, border_color='#DEE6EA')
    LogPurpose.grid(row=1, column=0, sticky="new")
    LogPurpose.bind("<KeyPress>", lambda event: validate_all(event, LogPurpose, 30, 1))
    LbPurpose = create_image_label(Purposef, 'Purpose.png', 94, 19)
    LbPurpose.grid(row=0, column=0, sticky="sw", pady=3)
    Selectwarn = CTkLabel(Purposef, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Selectwarn.grid(row=2, rowspan=4, column=0, sticky="nw", padx=1, pady=5)

    submitbtn = CTkButton(LogInEframe, text="SUBMIT", width=140, height=50, corner_radius=10, fg_color="#ADCBCF",
                          hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.75, anchor='n')

    # Create the frame
    Searchf = CTkFrame(LogInEframe, width=250, corner_radius=0, border_color= "#C1C1C1", border_width=1, fg_color= "white")
    Searchf.place(relx=0.13, rely=0.47, anchor="nw")
    Searchf.place_forget()

    # Bind keypress to toggle Searchf
    ResidID.bind("<KeyRelease>", lambda event: toggle_search_frame(ResidID, Searchf, Selectwarn, Invalidwarn, LogPurpose, submitbtn))

    entries = [LogVname, ResidID, LogPurpose]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_entries_and_enable_submit(entries, submitbtn))

    def check_entries_and_enable_submit(entries, submitbtn):
        residents = fetch_residents()
        resident_addresses = [res[1] for res in residents]
        selected_address = ResidID.get().strip()

        if ResidID.get() == "" and LogPurpose.get().strip() != "":
            Selectwarn.configure(text="Select Resident Address First!")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif ResidID.get() == "" and LogPurpose.get().strip() == "":
            Selectwarn.configure(text="")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif selected_address not in resident_addresses:
            Selectwarn.configure(text="")
            Invalidwarn.configure(text="Invalid Resident Address!")
            submitbtn.configure(state="disabled")
        elif LogVname.get() == "" and LogPurpose.get().strip() != "":
            Selectwarn.configure(text="Scan Visitor First!")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif LogVname.get() == "" and LogPurpose.get().strip() == "":
            Selectwarn.configure(text="")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif LogVname.get() != "" and LogPurpose.get().strip() != "" and ResidID.get() == "":
            Selectwarn.configure(text="Select Resident Address First!")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif LogVname.get() != "" and LogPurpose.get().strip() != "" and selected_address in resident_addresses:
            Selectwarn.configure(text="")
            Invalidwarn.configure(text="")
            submitbtn.configure(state="normal")
        else:
            if all(entry.get().strip() != '' for entry in entries) and selected_address in resident_addresses:
                Selectwarn.configure(text="")
                Invalidwarn.configure(text="")
                submitbtn.configure(state="normal")
            else:
                Selectwarn.configure(text="")
                Invalidwarn.configure(text="")
                submitbtn.configure(state="disabled")

    def handle_submit():
        visitor_name = LogVname.get()
        selected_address = ResidID.get()
        purpose = LogPurpose.get()

        resident_id = None
        for resident_tuple in fetch_residents():
            if resident_tuple[1] == selected_address:
                resident_id = resident_tuple[0]
                break

        if resident_id is not None:
            success = insert_visitor_data(visitor_name, resident_id, purpose, sec_id)
            if success:
                cap.release()
                logsuccess = "Login Successfully!"
                view_history(sec_id, LogInVframe, logsuccess, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct, logout_btn, home_page, home_button, visitor_button, resident_button)
            else:
                submitbtn.configure(
                    text="Logout",
                    command=lambda: logout_and_destroy(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, LogInVframe)
                )
                ExistingVisit.configure(text="Visitor already Logged in.")
                cap.release()
        else:
            print("Resident ID not found for the selected address.")

    submitbtn.configure(command=handle_submit)

    def logout_and_destroy(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, LogInVframe):
        LogInVframe.destroy()
        on_logout_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button)

    cap = cv2.VideoCapture(0)
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'data')

    # Construct the path to the haarcascade file
    cas_path = os.path.join(data_dir, 'haarcascade_frontalface_default.xml')
    face_dataset, face_labels, name = load_face_data(data_dir)

    if face_dataset is None or face_labels is None:
        scanbtn.configure(state="disabled")
    else:
        face_cascade = cv2.CascadeClassifier(cas_path)
        scanbtn.configure(state="normal")
        scanbtn.configure(command=lambda: start_camera(0, CameraFrame, None, scanbtn, Selectwarn, LogVname, face_dataset, face_labels, name,
        face_cascade, cap, on_login_click, homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, 
        visitor_button, resident_button))
