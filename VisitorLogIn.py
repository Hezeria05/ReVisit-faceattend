from tkinter import *
import tkinter as tk
from customtkinter import *
import cv2
from face_recognition import load_face_data
from PageUtils import ASSETS_PATH, set_icon_image, create_asterisk, check_sign_complete, indicate, view_history
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from PageVisitor import Visitor_page
from VisitorLogOut import on_logout_click
import ttkbootstrap as tb

def on_login_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):
    # Main registration frame
    LogInVframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    LogInVframe.place(relx=0.266, rely=0.118)

    # Heading
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.043, rely=0.06)

    CameraFrame = CTkFrame(LogInVframe, fg_color="white", width=450, height=450, border_color="#B9BDBD", border_width=2)
    CameraFrame.place(relx=0.043, rely=0.15)
    BscanFrame = CTkFrame(LogInVframe, fg_color="transparent", width=450, height=50)
    BscanFrame.place(relx=0.043, rely=0.82)
    scanbtn = CTkButton(BscanFrame, text="Scan", width=140, height=40, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')

    # Entry frame for name input
    LogInEframe = CTkFrame(LogInVframe, fg_color="#E9F3F2", width=420, height=550, corner_radius=10,
                             border_color="#B9BDBD", border_width=2)
    LogInEframe.place(relx=0.75, rely=0.15, anchor='n')

    LogInHeading =CTkLabel(LogInEframe, text='Login', fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LogInHeading.place(relx=0.5, rely=0.08, anchor='n')

    LogVname = CTkEntry(LogInEframe, width=360.0, height=45, placeholder_text="Enter Visitor Name",
                    corner_radius=8, border_width=1, border_color='#DEE6EA', state='disabled')
    LogVname.place(relx=0.5, rely=0.26, anchor='n')
    LbVname = CTkLabel(LogInEframe, text='Visitor Name', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbVname.place(relx=0.185, rely=0.2, anchor='n')

    ResidID = CTkComboBox(LogInEframe, width=360.0, height=45, values=[resident[1] for resident in fetch_residents()], button_color="#DEE6EA",
                          button_hover_color="#ADCBCF", corner_radius=8, border_width=1, border_color='#DEE6EA',
                          dropdown_hover_color="#ADCBCF", fg_color="#DEE6EA")
    ResidID.place(relx=0.5, rely=0.43, anchor='n')
    LRname = CTkLabel(LogInEframe, text='Resident Address', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LRname.place(relx=0.225, rely=0.37, anchor='n')
    create_asterisk(ResidID, LogInEframe, relx=0.305, y=200, anchor='n')

    LogPurpose= CTkEntry(LogInEframe, width=360.0, height=45, placeholder_text="State Purpose",
                    corner_radius=8, border_width=1, border_color='#DEE6EA')
    LogPurpose.place(relx=0.5, rely=0.6, anchor='n')
    LbPurpose = CTkLabel(LogInEframe, text='Purpose of Visit', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbPurpose.place(relx=0.22, rely=0.54, anchor='n')
    create_asterisk(LogPurpose, LogInEframe, relx=0.375, y=293, anchor='n')

    Existinglabel = CTkLabel(LogInEframe, text='', height=10, fg_color="transparent", font=("Inter", 11), text_color="red")
    Existinglabel.place(relx=0.085, rely=0.693, anchor='nw')

    submitbtn = CTkButton(LogInEframe, text="Submit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF",
                          hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.8, anchor='n')


    # Validation and submission
    entries = [LogVname, ResidID, LogPurpose]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))

    def handle_submit():
        # Retrieve data from entries
        visitor_name = LogVname.get()
        # Get the selected address from the ComboBox
        selected_address = ResidID.get()
        # Find the corresponding resident ID for the selected address
        resident_id = None
        for resident_tuple in fetch_residents():
            if resident_tuple[1] == selected_address:
                resident_id = resident_tuple[0]
                break
        purpose = LogPurpose.get()
        if resident_id is not None:  # Check if resident ID is found
            # Assuming sec_id is globally available or passed to this function
            success = insert_visitor_data(visitor_name, resident_id, purpose, sec_id)
            if success:
                # Close the camera
                cap.release()
                logsucess="Login Successfully!"
                view_history(sec_id, LogInVframe, logsucess, ASSETS_PATH, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct)
            else:
                submitbtn.configure(
                    text="Logout",
                    command=lambda: logout_and_destroy(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, LogInVframe)
                )
                Existinglabel.configure(text="Visitor already Logged in.")
                cap.release()
        else:
            # Handle the case where resident ID is not found for the selected address
            print("Resident ID not found for the selected address.")

    # Link the new function to the submit button
    submitbtn.configure(command=handle_submit)

    def logout_and_destroy(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct, LogInVframe):
        LogInVframe.destroy()
        on_logout_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct)


    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    face_dataset, face_labels, name = load_face_data(dirpath)
    if face_dataset is None or face_labels is None:
        scanbtn.configure(state="disabled")  # Disable the scan button if no data is available
        # Existinglabel = CTkLabel(Entryframe, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
        # Existinglabel.place(relx=0.105, rely=0.58, anchor='nw')
    else:
        face_cascade = cv2.CascadeClassifier(cas_path)
        scanbtn.configure(command=lambda: start_camera(CameraFrame, scanbtn, LogVname, face_dataset, face_labels, name, face_cascade, cap))


if __name__ == "__main__":
    app = tk.Tk()
    on_login_click(app)
    app.mainloop()
