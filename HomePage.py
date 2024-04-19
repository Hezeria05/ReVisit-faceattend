from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import set_background_image, ASSETS_PATH


def open_homepage(sec_id):
    def logout():
        homepage_window.destroy()  # Destroy the homepage window

    homepage_window = CTk()
    homepage_window.title('Homepage')
    homepage_window.geometry('1200x800+400+100')
    homepage_window.minsize(800, 400)
    homepage_window.maxsize(1200, 800)

    # Background for the new window
    set_background_image(homepage_window, ASSETS_PATH / 'HOME PAGE.png')



    # Add a label to display the sec_id
    # sec_id_label = CTkLabel(homepage_window, text=f"Sec ID: {sec_id}", font=("Inter", 20))
    # sec_id_label.pack(pady=20)

    # Add a logout button
    # logout_button = CTkButton(homepage_window, text="Logout", command=logout)
    # logout_button.pack(pady=10)

    homepage_window.mainloop()
