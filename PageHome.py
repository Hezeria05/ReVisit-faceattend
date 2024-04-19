from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import set_background_image, ASSETS_PATH


homepage_window = CTk()
homepage_window.title('Homepage')
homepage_window.geometry('1200x800+400+100')
homepage_window.minsize(1200, 800)
homepage_window.maxsize(1200, 800)

def logout():
    homepage_window.destroy()

def set_icon_image(frame, image_path, relx, rely, anchor, size=(22, 22)):
    icon_image_orig = Image.open(image_path)
    resized_iconimage = icon_image_orig.resize(size)
    icon_image_tk = ImageTk.PhotoImage(resized_iconimage)
    icon_image_label = CTkLabel(frame, image=icon_image_tk, text='')
    icon_image_label.place(relx=relx, rely=rely, anchor=anchor)

# Background for the new window
set_background_image(homepage_window, ASSETS_PATH / 'HOME PAGE.png')

Sidebar = CTkFrame(homepage_window, fg_color="#FEFEFE", width=316.8, height=648)
Sidebar.place(relx=0, rely=0.19)

# Add sidebar button
Home_btn = CTkButton(Sidebar, text="Home", width=20, height=20, fg_color="lightpink", hover_color="#FEFEFE", font=("Inter", 20, "bold"), text_color="#333333")
Home_btn.place(relx=0.2, rely=0.12, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'home_icon.png', relx=0.15, rely=0.12, anchor='n')

Visitor_btn = CTkButton(Sidebar, text="Visitor Data",  width=20, height=20, fg_color="lightpink", hover_color="#FEFEFE", font=("Inter", 20, "bold"), text_color="#333333")
Visitor_btn.place(relx=0.2, rely=0.22, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'visitor_icon.png', relx=0.15, rely=0.22, anchor='n')

Resident_btn = CTkButton(Sidebar, text="Residents List", width=20, height=20,fg_color="lightpink", hover_color="#FEFEFE", font=("Inter", 20, "bold"), text_color="#333333")
Resident_btn.place(relx=0.2, rely=0.32, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'list_icon.png', relx=0.15, rely=0.32, anchor='n')



Homeframe = CTkFrame(homepage_window, fg_color="lightpink", width=880, height=635)
Homeframe.place(relx=0.266, rely=0.118)


Registerframe = CTkFrame(Homeframe, fg_color="red", width=245, height=307, corner_radius=10, border_color="black", border_width=1)
Registerframe.place(relx=0.043, rely=0.36)

Loginframe = CTkFrame(Homeframe, fg_color="yellow", width=245, height=375, corner_radius=10, border_color="black", border_width=1)
Loginframe.place(relx=0.363, rely=0.36)

Logoutframe = CTkFrame(Homeframe, fg_color="#E9F3F2", width=245, height=375, corner_radius=10, border_color="black", border_width=1)
Logoutframe.place(relx=0.683, rely=0.36)

Totalframe = CTkFrame(Homeframe, fg_color="red", width=245, height=72, corner_radius=10, border_color="black", border_width=1)
Totalframe.place(relx=0.043, rely=0.2)

DateTimeframe = CTkFrame(Homeframe, fg_color="green", width=245, height=72, corner_radius=10, border_color="black", border_width=1)
DateTimeframe.place(relx=0.683, rely=0.05)




# Add a logout button
logout_btn = CTkButton(Sidebar, text="LOG OUT", fg_color="#FEFEFE", hover_color="#FEFEFE", font=("Inter", 20, "bold"), text_color="#333333", command=logout)
logout_btn.place(relx=0.5, rely=0.85, anchor='n')

def logout():
    homepage_window.destroy()

homepage_window.mainloop()
