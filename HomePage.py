from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path


def open_homepage(sec_id):
    def logout():
        homepage_window.destroy()  # Destroy the homepage window

    homepage_window = CTk()
    homepage_window.geometry('800x600+300+100')
    homepage_window.title('Homepage')

    # Add a label to display the sec_id
    sec_id_label = CTkLabel(homepage_window, text=f"Sec ID: {sec_id}", font=("Inter", 20))
    sec_id_label.pack(pady=20)

    # Add a logout button
    logout_button = CTkButton(homepage_window, text="Logout", command=logout)
    logout_button.pack(pady=10)

    homepage_window.mainloop()
