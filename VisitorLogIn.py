import tkinter as tk
from customtkinter import *
from tkinter import simpledialog, Canvas
import cv2
from face_recognition import load_face_data, KNN
import sys
import time
from PIL import Image, ImageTk
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime, create_asterisk, check_sign_complete

def on_login_click(homepage_window):
    # Main registration frame
    LogInVframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    LogInVframe.place(relx=0.266, rely=0.118)

    # Heading
    LogInVHeading = CTkLabel(LogInVframe, text="Log In Visitor", font=("Inter", 35, "bold"), text_color="#333333")
    LogInVHeading.place(relx=0.043, rely=0.06)

    CameraFrame = CTkFrame(LogInVframe, fg_color="white", width=450, height=350, border_color="#B9BDBD", border_width=2)
    CameraFrame.place(relx=0.043, rely=0.15)
    BscanFrame = CTkFrame(LogInVframe, fg_color="transparent", width=450, height=50)
    BscanFrame.place(relx=0.043, rely=0.68)
    scanbtn = CTkButton(BscanFrame, text="Scan", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"), text_color="#333333")
    scanbtn.place(relx=0.5, rely=0.5, anchor='center')
    

    # Entry frame for name input
    LogInEframe = CTkFrame(LogInVframe, fg_color="#E9F3F2", width=420, height=550, corner_radius=10,
                             border_color="#B9BDBD", border_width=2)
    LogInEframe.place(relx=0.75, rely=0.15, anchor='n')
    
    LogInHeading =CTkLabel(LogInEframe, text='Login', fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LogInHeading.place(relx=0.5, rely=0.08, anchor='n')
    
    LogVname = CTkEntry(LogInEframe, width=360.0, height=45, placeholder_text="Enter Visitor Name", corner_radius=8, border_width=1, border_color='#DEE6EA')
    LogVname.place(relx=0.5, rely=0.26, anchor='n')
    LbVname = CTkLabel(LogInEframe, text='Visitor Name', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbVname.place(relx=0.185, rely=0.2, anchor='n')
    # create_asterisk(LogVname, LogInEframe, relx=0.314, y=105, anchor='n')
    
    Residname = CTkEntry(LogInEframe, width=360.0, height=45, placeholder_text="Enter Resident Name to be Visited", corner_radius=8, border_width=1, border_color='#DEE6EA')
    Residname.place(relx=0.5, rely=0.43, anchor='n')
    LRname = CTkLabel(LogInEframe, text='Resident Name', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LRname.place(relx=0.21, rely=0.37, anchor='n')
    create_asterisk(Residname, LogInEframe, relx=0.361, y=200, anchor='n')
    
    LogPurpose= CTkEntry(LogInEframe, width=360.0, height=45, placeholder_text="State Purpose", corner_radius=8, border_width=1, border_color='#DEE6EA')
    LogPurpose.place(relx=0.5, rely=0.6, anchor='n')
    LbPurpose = CTkLabel(LogInEframe, text='Purpose of Visit', fg_color="transparent", font=("Inter", 15, "bold"), text_color="#333333")
    LbPurpose.place(relx=0.22, rely=0.54, anchor='n')
    create_asterisk(LogPurpose, LogInEframe, relx=0.375, y=293, anchor='n')

    submitbtn = CTkButton(LogInEframe, text="Submit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    submitbtn.place(relx=0.5, rely=0.8, anchor='n')
    
    # Existinglabel = CTkLabel(Entryframe, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
    # Existinglabel.place(relx=0.105, rely=0.58, anchor='nw')

    # Validation and submission
    entries = [LogVname, Residname, LogPurpose]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))
    # submitbtn.configure(command=lambda: try_opencamera(Vname.get(), RegVframe, Entryframe, Existinglabel))
    
    cap = cv2.VideoCapture(0)
    cas_path = r"C:\Users\grace\Desktop\ReVisit-faceattend\data\haarcascade_frontalface_default.xml"
    dirpath = r"C:\Users\grace\Desktop\ReVisit-faceattend\data"
    face_dataset, face_labels, name = load_face_data(dirpath)
    face_cascade = cv2.CascadeClassifier(cas_path)

    # Define the `start_camera` function.
    def start_camera(CameraFrame, scanbtn, LogVname):
        # Disable the scan button immediately when the camera starts
        scanbtn.configure(state="disabled")
        camera_label = CTkLabel(CameraFrame, width=450, height=350, text="")
        camera_label.place(relx=0, rely=0)

        def update_frame():
            ret, frame = cap.read()
            if not ret:
                camera_label.after(10, update_frame)
                return
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
            faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)

            for face in faces[-1:]:
                x, y, w, h = face
                face_section = gray_frame[y:y+h, x:x+w]
                face_section = cv2.resize(face_section, (100, 100))
                pred = KNN(face_dataset, face_labels, face_section)
                pred_name = name[int(pred)]
                cv2.putText(frame, pred_name, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # cv2.imshow("camera", frame)
                LogVname.delete(0, tk.END)
                LogVname.insert(0, pred_name)

            # Convert the image to PIL format and then to ImageTk format.
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            camera_label.imgtk = imgtk
            camera_label.configure(image=imgtk)

            # Repeat after an interval to get the next frame.
            camera_label.after(10, update_frame)

        update_frame()  # Start the loop
    # Bind the `start_camera` function to the "Scan" button.
    scanbtn.configure(command=lambda: start_camera(CameraFrame, scanbtn, LogVname))

if __name__ == "__main__":
    app = tk.Tk()
    on_login_click(app)
    app.mainloop()
