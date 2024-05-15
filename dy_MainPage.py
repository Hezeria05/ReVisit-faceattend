from customtkinter import *
from dy_PageUtils import configure_frame, load_image, indicate
from dy_PageHome import Home_page
from dy_PageResident import Resident_page
from dy_PageVisitor import Visitor_page

homepage_window = CTk()
homepage_window.title('Main Window')
homepage_window.geometry('1300x900+300+70')
homepage_window.minsize(1200, 900)
homepage_window.maxsize(homepage_window.winfo_screenwidth(), homepage_window.winfo_screenheight())
homepage_window.configure(fg_color='#E9F3F2')

def mainon_resize(event):
    width = event.width
    min_width = 1200
    max_width = 1300
    if min_width <= width <= max_width:
        column_weights = (1, 7)
        row_weights = (1, 8, 1)
        home2image = load_image('home2_icon.png', (27, 27))
        home_button.configure(image=home2image)
        visitor2image = load_image('visitor2_icon.png', (31, 31))
        visitor_button.configure(image=visitor2image)
        resident2image = load_image('list2_icon.png', (30, 30))
        resident_button.configure(image=resident2image)
        configure_frame(Sidebar, [5, 2, 2, 2, 2, 9, 5], [3, 5, 3])
    elif width > max_width:
        column_weights = (2, 7)
        row_weights = (1, 8, 1)
        homeimage = load_image('home_icon.png', (131, 36))
        home_button.configure(image=homeimage)
        visitorimage = load_image('visitor_icon.png', (208, 40))
        visitor_button.configure(image=visitorimage)
        residentimage = load_image('list_icon.png', (220, 37))
        resident_button.configure(image=residentimage)
        configure_frame(Sidebar, [5, 2, 2, 2, 2, 9, 5], [1, 5, 1])

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

HomebtnF = CTkFrame(Sidebar, fg_color="transparent", corner_radius=0)
HomebtnF.grid(row=2, column=1, sticky="sw", pady=2)
configure_frame(HomebtnF, [1], [1])

homeimage = load_image('home_icon.png', (131, 36))
home_button = CTkButton(HomebtnF, image=homeimage, text='', fg_color="white", hover_color="white")
home_button.grid(row=0, column=0, sticky="w")
Home_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 42), fg_color="#00507E")
Home_indct.grid(row=2, column=0, sticky="s")

VisitorbtnF = CTkFrame(Sidebar, fg_color="transparent", corner_radius=0)
VisitorbtnF.grid(row=3, column=1, sticky="sw", pady=2)
configure_frame(VisitorbtnF, [1], [1])

visitorimage = load_image('visitor_icon.png', (208, 40))
visitor_button = CTkButton(VisitorbtnF, image=visitorimage, text='', fg_color="white", hover_color="white")
visitor_button.grid(row=0, column=0, sticky="w")
Visitor_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 42), fg_color="#FEFEFE")
Visitor_indct.grid(row=3, column=0, sticky="s")

ResidentsbtnF = CTkFrame(Sidebar, fg_color="transparent", corner_radius=0)
ResidentsbtnF.grid(row=4, column=1, sticky="sw", pady=2)
configure_frame(ResidentsbtnF, [1], [1])

residentimage = load_image('list_icon.png', (220, 37))
resident_button = CTkButton(ResidentsbtnF, image=residentimage, text='', fg_color="white", hover_color="white")
resident_button.grid(row=0, column=0, sticky="w")
Resident_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 42), fg_color="#FEFEFE")
Resident_indct.grid(row=4, column=0, sticky="s")

home_button.configure(command=lambda: indicate(Home_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct)))

visitor_button.configure(command=lambda: indicate(Visitor_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct)))
resident_button.configure(command=lambda: indicate(Resident_indct, Home_indct, Visitor_indct, Resident_indct, lambda: Resident_page(homepage_window, Home_indct, Visitor_indct, Resident_indct)))


Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct)

LogbtnF = CTkFrame(Sidebar, fg_color="yellow", corner_radius=0, border_width=1, border_color="#C1C1C1")
LogbtnF.grid(row=6, column=0, columnspan=3, sticky="nsew")

Topbar = CTkFrame(homepage_window, fg_color="red", corner_radius=0)
Topbar.grid(row=0, column=1, sticky="nsew")

Btmbar = CTkFrame(homepage_window, fg_color="green", corner_radius=0)
Btmbar.grid(row=2, column=1, sticky="nsew")

homepage_window.mainloop()
