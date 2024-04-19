#Page Register
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, check_entries_complete, check_password_match, ASSETS_PATH, enable_submit_button, disable_submit_button, register_user
from db_con import register_security_admin

def open_register_window(main_window):
    register_window = CTkToplevel(main_window)
    register_window.geometry('1200x800+400+100')
    register_window.title('Register Account')
    register_window.grab_set()
     # Set the background image using the utility function
    set_background_image(register_window, ASSETS_PATH / 'USER ENTRY.png')

    RegFrame = CTkFrame(register_window, width=530, height=600, fg_color="#F0F6F9")
    RegFrame.place(x=555, y=100)

    # Add components to Register frame
    heading = CTkLabel(RegFrame, text='Create Account', fg_color="#F0F6F9", font=("Inter", 35, "bold"), text_color="#333333")
    heading.place(relx=0.5, y=38, anchor='n')

    #FULL NAME
    Efullname = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Full Name", corner_radius=8, border_width=1, border_color='#DEE6EA')
    Efullname.place(relx=0.5, y=140, anchor='n')
    Lfullname = CTkLabel(RegFrame, text='Full Name', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lfullname.place(relx=0.17, y=110, anchor='n')
    create_asterisk(Efullname, RegFrame, relx=0.250, y=108, anchor='n')
    #USERNAME
    Eusername = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Username", corner_radius=8, border_width=1, border_color='#DEE6EA')
    Eusername.place(relx=0.5, y=230, anchor='n')
    Lusername = CTkLabel(RegFrame, text='Username', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lusername.place(relx=0.17, y=200, anchor='n')
    create_asterisk(Eusername, RegFrame, relx=0.250, y=198, anchor='n')
    #PASSWORD
    Epassword = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Password", corner_radius=8, border_width=1, border_color='#DEE6EA', show="*")
    Epassword.place(relx=0.5, y=320, anchor='n')
    Lpassword = CTkLabel(RegFrame, text='Password', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lpassword.place(relx=0.17, y=290, anchor='n')
    create_asterisk(Epassword, RegFrame, relx=0.250, y=288, anchor='n')
    #Eye Toggle
    create_password_toggle_button(Epassword, RegFrame, relx=0.82, y=330, anchor='n')
    #CONFIRM PASSWORD
    Ecpassword = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Password", corner_radius=8, border_width=1, border_color='#DEE6EA', show="*")
    Ecpassword.place(relx=0.5, y=410, anchor='n')
    Lcpassword = CTkLabel(RegFrame, text='Confirm Password', fg_color="#F0F6F9", font=("Inter", 15, "bold"), text_color="#333333")
    Lcpassword.place(relx=0.23, y=380, anchor='n')
    create_asterisk(Ecpassword, RegFrame, relx=0.369, y=378, anchor='n')
    #Eye Toggle
    create_password_toggle_button(Ecpassword, RegFrame, relx=0.82, y=420, anchor='n')

    # Add a label to show password match status
    match_label = CTkLabel(RegFrame, text='', fg_color="#F0F6F9", font=("Inter", 12), text_color="#333333")
    match_label.place(relx=0.11, y=456, anchor='nw')

    # Reg-in button
    createbtn = CTkButton(RegFrame, text="Register", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", state="disabled")
    createbtn.place(relx=0.6, rely=0.8)
    # Back button that closes this window and shows the main window
    back_button = CTkButton(RegFrame, text="Back", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"), text_color="#333333", command=register_window.destroy)
    back_button.place(relx=0.6, rely=0.9)

    # Bind the validation function to entry events
    entries = [Efullname, Eusername, Epassword, Ecpassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries: check_entries_complete(entries, match_label, createbtn))
    Epassword.bind("<KeyRelease>", lambda event: check_password_match(Epassword, Ecpassword, match_label, createbtn))
    Ecpassword.bind("<KeyRelease>", lambda event: check_password_match(Epassword, Ecpassword, match_label, createbtn))
    
     # Function to register the user when the 'Register' button is clicked
     # Bind the register function to the 'Register' button click event
    createbtn.configure(command=lambda: register_user(Efullname, Eusername, Epassword, Ecpassword, register_window))