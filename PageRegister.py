#Page Register
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import create_asterisk, set_background_image, create_password_toggle_button, check_entries_complete, check_password_match, ASSETS_PATH, set_icon_image, display_success_and_close
from db_con import register_security_admin

def open_register_window(main_window):

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
    register_window = CTkToplevel(main_window)
    register_window.geometry('1200x800+400+100')
    register_window.title('Register Account')
    register_window.grab_set()
    register_window.minsize(800, 400)
    register_window.maxsize(1200, 800)
     # Set the background image using the utility function
    set_background_image(register_window, ASSETS_PATH / 'USER ENTRY.png',size=(1200, 800))

    RegFrame = CTkFrame(register_window, width=530, height=600, fg_color="#F0F6F9")
    RegFrame.place(x=555, y=100)

    # Add components to Register frame
    heading = CTkLabel(RegFrame, text='Create Account', fg_color="#F0F6F9",
                       font=("Inter", 35, "bold"), text_color="#333333")
    heading.place(relx=0.5, y=38, anchor='n')

    # FULL NAME
    Efullname = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Full Name",
                         corner_radius=8, border_width=1, border_color='#DEE6EA')
    Efullname.place(relx=0.5, y=140, anchor='n')
    Efullname.bind("<KeyPress>", validate_full_name)
    Lfullname = CTkLabel(RegFrame, text='Full Name', fg_color="#F0F6F9",
                         font=("Inter", 15, "bold"), text_color="#333333")
    Lfullname.place(relx=0.11, y=110, anchor='nw')
    create_asterisk(Efullname, RegFrame, relx=0.255, y=106, anchor='n')
    FnExistlabel = CTkLabel(RegFrame, text='', height=10, fg_color="transparent", font=("Inter", 12), text_color="red")
    FnExistlabel.place(relx=0.11, rely=0.310, anchor='nw')

    #USERNAME
    Eusername = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Username",
                        corner_radius=8, border_width=1, border_color='#DEE6EA')
    Eusername.place(relx=0.5, y=230, anchor='n')
    Lusername = CTkLabel(RegFrame, text='Username', fg_color="#F0F6F9",
                        font=("Inter", 15, "bold"), text_color="#333333")
    Lusername.place(relx=0.11, y=200, anchor='nw')
    create_asterisk(Eusername, RegFrame, relx=0.26, y=198, anchor='n')
    UnExistlabel = CTkLabel(RegFrame, text='', height=10, fg_color="transparent", font=("Inter", 12), text_color="red")
    UnExistlabel.place(relx=0.11, rely=0.465, anchor='nw')

    #PASSWORD
    Epassword = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Password",
                        corner_radius=8, border_width=1, border_color='#DEE6EA', show="*")
    Epassword.place(relx=0.5, y=328, anchor='n')
    Lpassword = CTkLabel(RegFrame, text='Password', fg_color="#F0F6F9",
                        font=("Inter", 15, "bold"), text_color="#333333")
    Lpassword.place(relx=0.11, y=298, anchor='nw')
    create_asterisk(Epassword, RegFrame, relx=0.255, y=290, anchor='n')
    #Eye Toggle
    create_password_toggle_button(Epassword, RegFrame, relx=0.82, y=335, anchor='n')

    #CONFIRM PASSWORD
    Ecpassword = CTkEntry(RegFrame, width=420.0, height=45.0, placeholder_text="Enter Password",
                        corner_radius=8, border_width=1, border_color='#DEE6EA', show="*")
    Ecpassword.place(relx=0.5, y=420, anchor='n')
    Lcpassword = CTkLabel(RegFrame, text='Confirm Password', fg_color="#F0F6F9",
                        font=("Inter", 15, "bold"), text_color="#333333")
    Lcpassword.place(relx=0.11, y=390, anchor='nw')
    create_asterisk(Ecpassword, RegFrame, relx=0.369, y=388, anchor='n')
    #Eye Toggle
    create_password_toggle_button(Ecpassword, RegFrame, relx=0.82, y=428, anchor='n')

    # Add a label to show password match status
    match_label = CTkLabel(RegFrame, text='', fg_color="#F0F6F9", font=("Inter", 12), text_color="#333333")
    match_label.place(relx=0.11, y=465, anchor='nw')

    # Reg-in button
    createbtn = CTkButton(RegFrame, text="Create Account", width=140, height=40, corner_radius=10,
                        fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 17, "bold"),
                        text_color="#333333", state="disabled")
    createbtn.place(relx=0.5, rely=0.9, anchor="center")

    back_icon_path = ASSETS_PATH / 'Back_icon.png'
    back_icon = Image.open(back_icon_path)
    resized_back_icon = back_icon.resize((85, 35))  # Adjust size as needed
    back_icon_tk = ImageTk.PhotoImage(resized_back_icon)

    # Back button that closes this window and shows the main window
    back_button = CTkButton(register_window, image=back_icon_tk, text='', width=120, height=50, corner_radius=10,
                            fg_color="white", hover_color="white", font=("Inter", 17, "bold"),
                            text_color="#333333", command=register_window.destroy)
    back_button.place(relx=0.07, rely=0.93, anchor="center")

    # Bind the validation function to entry events
    entries = [Efullname, Eusername, Epassword, Ecpassword]
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event, entries=entries, match_label=match_label, createbtn=createbtn, Epassword=Epassword, Ecpassword=Ecpassword: check_entries_complete(entries, match_label, createbtn, Epassword, Ecpassword))
    Epassword.bind("<KeyRelease>", lambda event: check_password_match(Epassword, Ecpassword, match_label, createbtn))
    Ecpassword.bind("<KeyRelease>", lambda event: check_password_match(Epassword, Ecpassword, match_label, createbtn))
    def handle_registration():
        # Disable the register button to prevent multiple submissions
        createbtn.configure(state="disabled")

        full_name = Efullname.get()
        username = Eusername.get()
        password = Ecpassword.get()

        try:
            success = register_security_admin(full_name, username, password, register_window, FnExistlabel, UnExistlabel)
            if success:
                # Display success message and close window after a delay
                display_success_and_close(register_window)
            else:
                # Clear error messages after 3 seconds (3000 milliseconds)
                register_window.after(3000, clear_error_labels)
                # Re-enable the button if registration failed
                createbtn.configure(state="normal")
        except Exception as e:
            # Log the exception or show it in a way appropriate for your application's logging strategy
            print(f"Error during registration: {e}")
            # Provide feedback to the user that an error occurred
            match_label.configure(text="An unexpected error occurred. Please try again.", text_color="red")
            # Re-enable the button to allow the user to try again
            createbtn.configure(state="normal")
            # Clear error messages after 3 seconds (3000 milliseconds)
            register_window.after(3000, clear_error_labels)

    def clear_error_labels():
        FnExistlabel.configure(text='')
        UnExistlabel.configure(text='')

    createbtn.configure(command=handle_registration)