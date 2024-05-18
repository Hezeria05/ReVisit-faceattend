from customtkinter import *
from dy_PageUtils import configure_frame, load_image, indicate, logout
from dy_PageHome import Home_page
from dy_PageResident import Resident_page
from dy_PageVisitor import Visitor_page

homepage_window = CTk()
homepage_window.title('Main Window')
homepage_window.geometry('1500x900+300+70')
homepage_window.minsize(1500, 900)
homepage_window.maxsize(homepage_window.winfo_screenwidth(), homepage_window.winfo_screenheight())
homepage_window.configure(fg_color='#E9F3F2')
sec_id = 24
def mainon_resize(event):
    width = event.width
    min_width = 1500
    # max_width = 1600
    # if min_width <= width <= max_width:
    #     column_weights = (1, 7)
    #     row_weights = (1, 8, 1)
    #     home2image = load_image('home2_icon.png', (43, 43))
    #     home_button.configure(image=home2image)
    #     visitor2image = load_image('visitor2_icon.png', (43, 43))
    #     visitor_button.configure(image=visitor2image)
    #     resident2image = load_image('list2_icon.png', (43, 43))
    #     resident_button.configure(image=resident2image)
    #     logout2image = load_image('userlogout_icon.png', (40, 40))
    #     logout_btn.configure(image=logout2image, text="")
    #     configure_frame(Sidebar, [5, 2, 2, 2, 2, 9, 5], [3, 5, 3])
    if width >= min_width:
        column_weights = (2, 7)
        row_weights = (1, 8, 1)
        homeimage = load_image('home_icon.png', (131, 36))
        home_button.configure(image=homeimage)
        visitorimage = load_image('visitor_icon.png', (208, 40))
        visitor_button.configure(image=visitorimage)
        residentimage = load_image('list_icon.png', (220, 37))
        resident_button.configure(image=residentimage)
        logout_btn.configure(text="LOG OUT", image=None)
        configure_frame(Sidebar, [5, 2, 2, 2, 2, 9, 5], [1, 5, 1])
    else:
        column_weights = (2, 7)
        row_weights = (1, 8, 1)

    for i, weight in enumerate(column_weights):
        homepage_window.columnconfigure(i, weight=weight, uniform='a')
    for i, weight in enumerate(row_weights):
        homepage_window.rowconfigure(i, weight=weight, uniform='a')

homepage_window.bind('<Configure>', mainon_resize)

# Sidebar
Sidebar = CTkFrame(homepage_window, fg_color="#FEFEFE", corner_radius=0, border_width=1, border_color="#C1C1C1")
Sidebar.grid(row=0, rowspan=3, column=0, columnspan=1, sticky="nsew")
configure_frame(Sidebar, [5, 3, 2, 2, 2, 8, 5], [1, 5, 1])

SBLogo = CTkFrame(Sidebar, fg_color="yellow", corner_radius=0, border_width=1, border_color="#C1C1C1")
SBLogo.grid(row=0, column=0, columnspan=3, sticky="nsew")

def create_sidebar_button(parent, row, image_path, image_size, command, indicator_color="#FEFEFE"):
    frame = CTkFrame(parent, fg_color="transparent", corner_radius=0)
    frame.grid(row=row, column=1, sticky="sw", pady=2)
    configure_frame(frame, [1], [1])

    image = load_image(image_path, image_size)
    button = CTkButton(frame, image=image, text='', fg_color="white", hover_color="white", command=command)
    button.grid(row=0, column=0, sticky="w")

    indicator = CTkLabel(parent, text=' ', font=("Arial", 42), fg_color=indicator_color)
    indicator.grid(row=row, column=0, sticky="s")

    return button, indicator

home_button, Home_indct = create_sidebar_button(Sidebar, 2, 'home_icon.png', (131, 36), lambda: indicate(Home_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id)), "#00507E")
visitor_button, Visitor_indct = create_sidebar_button(Sidebar, 3, 'visitor_icon.png', (208, 40), lambda: indicate(Visitor_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id)))
resident_button, Resident_indct = create_sidebar_button(Sidebar, 4, 'list_icon.png', (220, 37), lambda: indicate(Resident_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Resident_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id)))

Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id)

LogbtnF = CTkFrame(Sidebar, fg_color="transparent", corner_radius=0, border_width=1, border_color="#C1C1C1")
LogbtnF.grid(row=6, column=0, columnspan=3, sticky="nsew")
configure_frame(LogbtnF, [1], [1])
# Add a logout button
logout_btn = CTkButton(LogbtnF, text="LOG OUT", fg_color="#FEFEFE", hover_color="#FEFEFE", font=("Inter", 25, "bold"),
                text_color="#333333", command=lambda:(logout(homepage_window,logout_btn), logout_btn.configure(state='disabled')))
logout_btn.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

Topbar = CTkFrame(homepage_window, fg_color="red", corner_radius=0)
Topbar.grid(row=0, column=1, sticky="nsew")

Btmbar = CTkFrame(homepage_window, fg_color="green", corner_radius=0)
Btmbar.grid(row=2, column=1, sticky="nsew")

homepage_window.mainloop()
