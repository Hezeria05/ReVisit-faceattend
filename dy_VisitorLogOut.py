from customtkinter import *
import cv2
import os
from face_recognition import load_face_data
from dy_PageUtils import (configure_frame, view_history, load_image,
                          indicate, set_icon_image)
from face_scan import start_camera
from db_con import logout_visitor
from dy_PageVisitor import Visitor_page


def on_logout_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button):

    home_button.configure(state="normal")
    visitor_button.configure(state="normal")
    resident_button.configure(state="normal")
    # Main registration frame
    LogOutVframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    LogOutVframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(LogOutVframe, [2,8,1,2], [1,4,1])
    # Heading
    backimage = load_image('Back_button.png', (35, 34))
    back_button = CTkButton(LogOutVframe, image=backimage, text='', fg_color="white", hover_color="white", 
                            command=lambda:[home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button), LogOutVframe.destroy(), cap.release()])
    back_button.place(relx=0.001, rely=0.06, anchor="nw")
    LogOutVHeading = CTkLabel(LogOutVframe, text="Log Out Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogOutVHeading.place(relx=0.095, rely=0.06, anchor="nw")


    CameraFrame = CTkFrame(LogOutVframe, fg_color="white", width=640, height=480, border_color="#B9BDBD", border_width=2)
    CameraFrame.place(relx=0.5, rely=0.5, anchor='center')

    # Entry frame for name input
    LogOutEframe = CTkFrame(LogOutVframe, fg_color="transparent", width=640, height=100, corner_radius=10,)
    LogOutEframe.place(relx=0.5, rely=0.915, anchor='center')

    # Initially invisible elements
    LogVname = CTkEntry(LogOutEframe, width=370.0, height=45, placeholder_text="Visitor Name",
                        corner_radius=8, border_width=1, border_color='#DEE6EA', state='disabled')
    LbVname = CTkLabel(LogOutEframe, text='Visitor Name:', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    logoutbtn = CTkButton(LogOutEframe, text="Logout", width=230, height=45, corner_radius=10, fg_color="#ADCBCF",
                      hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333")
    Existinglabel = CTkLabel(LogOutEframe, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    Existinglabel.place(relx=0, rely=0.75, anchor='nw')

    def handle_logout():
        visitor_name = LogVname.get()
        success = logout_visitor(visitor_name, sec_id, Existinglabel)
        if success:
            cap.release()
            data_path = os.path.join(dirpath, f"{visitor_name}.npy")
            if os.path.exists(data_path):
                os.remove(data_path)
            logsucess = "Logout successfully!"
            view_history(sec_id, LogOutVframe, logsucess, set_icon_image, indicate, Visitor_page, homepage_window, Home_indct, Visitor_indct, Resident_indct, logout_btn, home_page, home_button, visitor_button, resident_button)

    # Now update the logout button command to use handle_logout
    logoutbtn.configure(command=handle_logout)

    def display_fields():
        # Place entry and label and logout button after scan
        LogVname.place(relx=0, rely=0.5, anchor='w')
        LbVname.place(relx=0, rely=0.12, anchor='w')
        logoutbtn.place(relx=0.97, rely=0.5, anchor='e')
        scanbtn.place_forget()  # Hide scan button

    scanbtn = CTkButton(LogOutEframe, text="Scan", width=140, height=50, corner_radius=10, fg_color="#ADCBCF",
                        hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')

    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    face_dataset, face_labels, name = load_face_data(dirpath)
    if face_dataset is None or face_labels is None:
        scanbtn.configure(state="disabled")  # Disable the scan button if no data is available
    else:
        face_cascade = cv2.CascadeClassifier(cas_path)
        scanbtn.configure(command=lambda: start_camera(1, CameraFrame, logoutbtn, scanbtn, None, LogVname, face_dataset, face_labels, name, face_cascade, cap,  
                                                       on_logout_click, homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_page, home_button, visitor_button, resident_button, callback=display_fields))
