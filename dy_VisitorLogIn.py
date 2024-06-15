from customtkinter import *
import cv2
from face_recognition import load_face_data
from dy_PageUtils import (configure_frame, validate_length, view_history,
                          indicate, set_icon_image, validate_char)
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from dy_PageVisitor import Visitor_page
from dy_VisitorLogOut import on_logout_click

def on_login_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page):

    # Main login frame
    LogInVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    LogInVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(LogInVframe, [3, 10, 2, 1], [1, 9, 1, 8, 1])

    # Heading
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.043, rely=0.06)

    CameraFrame = CTkFrame(LogInVframe, fg_color="white",width=600, height=450, border_color="#B9BDBD", border_width=2)
    CameraFrame.grid(row=1, column=1,)
    BscanFrame = CTkFrame(LogInVframe, fg_color="white")
    BscanFrame.grid(row=2, column=1, sticky="nsew")
    scanbtn = CTkButton(BscanFrame, text="Scan", width=140, height=50, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 18, "bold"), text_color="#333333", state="disabled")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')

    # Entry frame for name input
    LogInEframe = CTkFrame(LogInVframe, fg_color="#E9F3F2", corner_radius=10, border_color="#B9BDBD", border_width=2)
    LogInEframe.grid(row=1, column=3, rowspan=2, sticky="nsew")
    configure_frame(LogInEframe, [5, 4, 4, 5, 1, 8], [1, 6, 1])

    LogInHeading = CTkLabel(LogInEframe, text='Login', fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LogInHeading.place(relx=0.5, rely=0.08, anchor='n')
    Vnamef = CTkFrame(LogInEframe, fg_color="transparent")
    Vnamef.grid(row=1, column=1, sticky="nsew", pady=3)
    configure_frame(Vnamef, [1, 2], [1])
    LogVname = CTkEntry(Vnamef, placeholder_text="Enter Visitor Name", height=45,
                        corner_radius=8, border_width=1, border_color='#DEE6EA', state='disabled')
    LogVname.grid(row=1, column=0, sticky="new")
    LbVname = CTkLabel(Vnamef, text='Visitor Name', fg_color="transparent", font=("Inter", 17, "bold"), text_color="#333333")
    LbVname.grid(row=0, column=0, sticky="sw")

    Residf = CTkFrame(LogInEframe, fg_color="transparent")
    Residf.grid(row=2, column=1, sticky="nsew", pady=3)
    configure_frame(Residf, [1, 2], [1])

    # Inside the on_login_click function
    ResidID = CTkComboBox(Residf, height=45,
                          values=["--Select--"] + [resident[1] for resident in fetch_residents()],
                          button_color="#DEE6EA", button_hover_color="#ADCBCF",
                          corner_radius=8, border_width=1, border_color='#DEE6EA',
                          dropdown_hover_color="#ADCBCF", fg_color="#DEE6EA", state='readonly')
    ResidID.set("--Select--")  # Set the placeholder as the initially selected item
    ResidID.grid(row=1, column=0, sticky="new")
    LRname = CTkLabel(Residf, text='Resident Address', fg_color="transparent", font=("Inter", 17, "bold"), text_color="#333333")
    LRname.grid(row=0, column=0, sticky="sw")

    Purposef = CTkFrame(LogInEframe, fg_color="transparent")
    Purposef.grid(row=3, column=1, sticky="nsew", pady=3)
    configure_frame(Purposef, [1, 2, 1], [1])
    LogPurpose = CTkEntry(Purposef, placeholder_text="State Purpose", height=45,
                          corner_radius=8, border_width=2, border_color='#FB6B6B')
    LogPurpose.grid(row=1, column=0, sticky="new")
    LogPurpose.bind("<KeyPress>", validate_char)
    LogPurpose.bind("<KeyPress>", lambda event: validate_length(event, LogPurpose, 50))
    LbPurpose = CTkLabel(Purposef, text='Purpose of Visit', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbPurpose.grid(row=0, column=0, sticky="sw")
    Existinglabel = CTkLabel(Purposef, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Existinglabel.grid(row=2, column=0, sticky="sw", padx=1)

    submitbtn = CTkButton(LogInEframe, text="SUBMIT", width=140, height=50, corner_radius=10, fg_color="#ADCBCF",
                          hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.75, anchor='n')

    entries = [LogVname, ResidID, LogPurpose]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_entries_and_enable_submit(entries, submitbtn))

    def check_entries_and_enable_submit(entries, submitbtn):
        if ResidID.get() == "--Select--":
            LogPurpose.delete(0, 'end')
            LogPurpose.configure(border_color="#FB6B6B")
            Existinglabel.configure(text="Select Resident Address First!")
            submitbtn.configure(state="disabled")
        else:
            ResidID.configure(values=[resident[1] for resident in fetch_residents()])
            Existinglabel.configure(text="")
            if all(entry.get().strip() != '' for entry in entries):
                submitbtn.configure(state="normal")
            else:
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
                Existinglabel.configure(text="Visitor already Logged in.")
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


