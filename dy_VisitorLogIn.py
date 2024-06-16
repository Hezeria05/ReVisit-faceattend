from customtkinter import *
import cv2
from face_recognition import load_face_data
from dy_PageUtils import (configure_frame, validate_all, view_history,
                          indicate, set_icon_image, validate_no_space)
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from dy_PageVisitor import Visitor_page
from dy_VisitorLogOut import on_logout_click
from Utils_VisitorLogIn import toggle_search_frame

def on_login_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page):

    # Main login frame
    LogInVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    LogInVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(LogInVframe, [3, 10, 2, 1], [1, 9, 1, 8, 1])

    # Heading
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.043, rely=0.06)

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
    configure_frame(Vnamef,  [1, 3, 1], [1])
    LogVname = CTkEntry(Vnamef, placeholder_text="Enter Visitor Name", height=45,
                        corner_radius=8, border_width=1, border_color='#DEE6EA', state='disabled')
    LogVname.grid(row=1, column=0, sticky="new")
    LbVname = CTkLabel(Vnamef, text='Visitor Name', fg_color="transparent", font=("Inter", 17, "bold"), text_color="#333333")
    LbVname.grid(row=0, column=0, sticky="sw", pady=3)
    ExistingVisit = CTkLabel(Vnamef, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    ExistingVisit.grid(row=2, column=0, sticky="sw", padx=1)

    # Resident
    Residf = CTkFrame(LogInEframe, fg_color="transparent")
    Residf.grid(row=2, column=1, sticky="nsew", pady=3)
    configure_frame(Residf,  [1, 3, 1], [1])

    ResidID = CTkEntry(Residf, placeholder_text="Search Address..", height=45,
                        corner_radius=8, border_width=1, border_color='#DEE6EA')
    ResidID.grid(row=1, column=0, sticky="new")
    ResidID.bind("<KeyPress>", lambda event: validate_all(event, ResidID, 30, 1))
    LRname = CTkLabel(Residf, text='Resident Address', fg_color="transparent", font=("Inter", 17, "bold"), text_color="#333333")
    LRname.grid(row=0, column=0, sticky="sw", pady=3)
    Invalidwarn = CTkLabel(Residf, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Invalidwarn.grid(row=2, column=0, sticky="sw", padx=2)

    # Purpose
    Purposef = CTkFrame(LogInEframe, fg_color="transparent")
    Purposef.grid(row=3, column=1, sticky="nsew", pady=3)
    configure_frame(Purposef, [1, 3, 1], [1])

    LogPurpose = CTkEntry(Purposef, placeholder_text="State Purpose", height=45,
                          corner_radius=8, border_width=2, border_color='#ADCBCF')
    LogPurpose.grid(row=1, column=0, sticky="new")
    LogPurpose.bind("<KeyPress>", lambda event: validate_all(event, LogPurpose, 30, 1))
    LbPurpose = CTkLabel(Purposef, text='Purpose', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbPurpose.grid(row=0, column=0, sticky="sw", pady=3)
    Selectwarn = CTkLabel(Purposef, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Selectwarn.grid(row=2, column=0, sticky="sw", padx=1)

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
            LogPurpose.delete(0, 'end')
            Selectwarn.configure(text="Select Resident Address First!")
            submitbtn.configure(state="disabled")
        elif ResidID.get() == "" and LogPurpose.get().strip() == "":
            Invalidwarn.configure(text="")
            submitbtn.configure(state="disabled")
        elif LogVname.get() == "" and LogPurpose.get().strip() != "":
            LogPurpose.delete(0, 'end')
            Selectwarn.configure(text="Scan Visitor First!")
            submitbtn.configure(state="disabled")
        elif selected_address not in resident_addresses:
            Invalidwarn.configure(text="Invalid Resident Address!")
            submitbtn.configure(state="disabled")
        else:
            if all(entry.get().strip() != '' for entry in entries)and selected_address in resident_addresses:
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
                logsucess = "Login Successfully!"
                view_history(sec_id, LogInVframe, logsucess, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct, logout_btn, home_page)
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
        on_logout_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page)

    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    face_dataset, face_labels, name = load_face_data(dirpath)

    if face_dataset is None or face_labels is None:
        scanbtn.configure(state="disabled")
    else:
        face_cascade = cv2.CascadeClassifier(cas_path)
        scanbtn.configure(state="normal")
        scanbtn.configure(command=lambda: start_camera(0, CameraFrame, None, scanbtn, LogVname, face_dataset, face_labels, name, face_cascade, cap, on_login_click, homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page))
