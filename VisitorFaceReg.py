import tkinter as tk
from customtkinter import *
from PageUtils import create_asterisk, check_sign_complete
from face_registration import face_register

def on_register_click(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct):
    def validate_full_name(event):
        # Check if the character typed is a letter
        if event.char.isalpha() or event.char == " ":
            return True
        # Allow space and control characters like backspace
        elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
            return True
        else:
            # Reject the character by returning "break" to stop the event from propagating
            return "break"
    # Main registration frame
    RegVframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    RegVframe.place(relx=0.266, rely=0.118)

    # Heading
    RegVHeading = CTkLabel(RegVframe, text="Face Registration", font=("Inter", 35, "bold"), text_color="#333333")
    RegVHeading.place(relx=0.043, rely=0.06)
    RCameraFrame = CTkFrame(RegVframe, fg_color="white", width=680, height=480, border_color="#B9BDBD", border_width=2)
    RCameraFrame.place(relx=0.5, rely=0.5, anchor='center')

    def setup_entry_frame():
            global Vname
            vname_text = tk.StringVar()

            Entryframe = CTkFrame(RegVframe, fg_color="#E9F3F2", width=600, height=220, corner_radius=10, border_color="#B9BDBD", border_width=2)
            Entryframe.place(relx=0.5, rely=0.35, anchor='n')

            Vname = CTkEntry(Entryframe, textvariable=vname_text, width=485.0, height=50, placeholder_text="Enter Visitor Name", corner_radius=8, border_width=1, border_color='#DEE6EA')
            Vname.place(relx=0.5, rely=0.35, anchor='n')
            Vname.bind("<KeyPress>", validate_full_name)
            Vname.bind("<KeyRelease>", lambda event: vname_text.set(Vname.get().upper()))

            LVname = CTkLabel(Entryframe, text='Visitor Name', fg_color="transparent", font=("Inter", 20, "bold"), text_color="#333333")
            LVname.place(relx=0.2, rely=0.18, anchor='n')

            create_asterisk(Vname, Entryframe, relx=0.314, y=32, anchor='n')

            submitbtn = CTkButton(Entryframe, text="Submit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
            submitbtn.place(relx=0.5, rely=0.7, anchor='n')

            Existinglabel = CTkLabel(Entryframe, text='', fg_color="transparent", font=("Inter", 11), text_color="red")
            Existinglabel.place(relx=0.105, rely=0.58, anchor='nw')

            entries = [Vname]
            for entry in entries:
                entry.bind("<KeyRelease>", lambda event, entries=entries: check_sign_complete(entries, submitbtn))
            submitbtn.configure(command=lambda: face_register(Vname.get(), RegVframe, RCameraFrame, Entryframe, Existinglabel, homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct))

        # Delay the display of Entryframe for 5000 milliseconds (5 seconds)
    homepage_window.after(300, setup_entry_frame)

if __name__ == "__main__":
    app = tk.Tk()
    on_register_click(app)
    app.mainloop()
