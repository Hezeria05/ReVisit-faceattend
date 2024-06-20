from customtkinter import *
from dy_PageUtils import configure_frame, load_image, logout
from dy_PageHome import Home_page
from dy_PageResident import Resident_page
from dy_PageVisitor import Visitor_page

# def open_homepage(sec_id):
sec_id = 24
# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to hide indicators
def hide_indicators(Home_indct, Visitor_indct, Resident_indct):
    Home_indct.configure(fg_color="#F6FCFC")
    Visitor_indct.configure(fg_color="#F6FCFC")
    Resident_indct.configure(fg_color="#F6FCFC")

# Function to indicate the selected sidebar item and switch pages
def indicate(selected_indicator, Home_indct, Visitor_indct, Resident_indct, new_page):
    global current_frame
    hide_indicators(Home_indct, Visitor_indct, Resident_indct)
    selected_indicator.configure(fg_color="#00507E")
    if current_frame:
        current_frame.destroy()
    current_frame = new_page()

# Create the main window
homepage_window = CTk()
homepage_window.title('Main Window')
window_width = 1500
window_height = 900

# Center the window
center_window(homepage_window, window_width, window_height)

# Set minimum and maximum size
homepage_window.minsize(1500, 900)
homepage_window.maxsize(homepage_window.winfo_screenwidth(), homepage_window.winfo_screenheight())
homepage_window.configure(fg_color='#E9F3F2')

global current_frame
current_frame = None

def mainon_resize(event):
    width = event.width
    min_width = 1500

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
Sidebar = CTkFrame(homepage_window, fg_color="#F6FCFC", corner_radius=0)
Sidebar.grid(row=0, rowspan=3, column=0, columnspan=1, sticky="nsew")
configure_frame(Sidebar, [8, 2, 2, 2, 5, 5], [1, 5, 1])

SBLogo = CTkFrame(Sidebar, fg_color="#F6FCFC", corner_radius=0)
SBLogo.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsew")
configure_frame(SBLogo, [1], [1])
logoimage = load_image('REVISITlogosb.png', (216, 216))
logolabel = CTkLabel(SBLogo, image=logoimage, text="")
logolabel.grid(row=0, column=0, sticky="n")

LogbtnF = CTkFrame(Sidebar, fg_color="transparent", corner_radius=0)
LogbtnF.grid(row=6, column=0, columnspan=3, sticky="nsew")
configure_frame(LogbtnF, [1], [1])
# Add a logout button
logout_btn = CTkButton(LogbtnF, text="LOG OUT", fg_color="#F6FCFC", hover_color="#F6FCFC", font=("Inter", 25, "bold"),
                text_color="#333333", command=lambda:(logout(homepage_window, logout_btn), logout_btn.configure(state='disabled')))
logout_btn.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

def create_sidebar_button(parent, row, image_path, image_size, command, indicator_color="#F6FCFC"):
    frame = CTkFrame(parent, fg_color="transparent", corner_radius=0)
    frame.grid(row=row, column=1, sticky="sw", pady=2)
    configure_frame(frame, [1], [1])

    image = load_image(image_path, image_size)
    button = CTkButton(frame, image=image, text='', fg_color="#F6FCFC", hover_color="#F6FCFC", command=command)
    button.grid(row=0, column=0, sticky="w")

    indicator = CTkLabel(parent, text=' ', font=("Arial", 42), fg_color=indicator_color)
    indicator.grid(row=row, column=0, sticky="s")

    return button, indicator

home_button, Home_indct = create_sidebar_button(Sidebar, 2, 'home_icon.png', (131, 36), 
    lambda: indicate(Home_indct, Home_indct, Visitor_indct, Resident_indct, 
    lambda: Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn)), "#00507E")
visitor_button, Visitor_indct = create_sidebar_button(Sidebar, 3, 'visitor_icon.png', (208, 40), 
    lambda: indicate(Visitor_indct, Home_indct, Visitor_indct, Resident_indct, 
    lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn)))
resident_button, Resident_indct = create_sidebar_button(Sidebar, 4, 'list_icon.png', (220, 37), 
    lambda: indicate(Resident_indct, Home_indct, Visitor_indct, Resident_indct, 
    lambda: Resident_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn)))

current_frame = Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn)

Topbar = CTkFrame(homepage_window, fg_color="white", corner_radius=0, border_width=1, border_color="#C1C1C1")
Topbar.grid(row=0, column=1, sticky="nsew")
configure_frame(Topbar, [1], [1, 6, 1, 6, 1, 6, 1])
topblabel = CTkLabel(Topbar, text="REVISIT: FACIAL RECOGNITION ATTENDANCE SYSTEM",font=("Inter", 22, "bold"), fg_color="transparent",text_color="#333333")
topblabel.grid(row=0, column=1, columnspan=3, sticky="w", padx=25)

Btmbar = CTkFrame(homepage_window, fg_color="white", corner_radius=0, border_width=1, border_color="#C1C1C1")
Btmbar.grid(row=2, column=1, sticky="nsew")
configure_frame(Btmbar, [1], [1, 6, 1, 6, 1, 6, 1])
Btmbarlabel = CTkLabel(Btmbar, text="CELINA HOMES 5 SUBDIVISION, BRGY. TAGAPO",font=("Inter", 16, "bold"), fg_color="transparent",text_color="#333333")
Btmbarlabel.grid(row=0, column=3, columnspan=5, sticky="e", padx=45)

homepage_window.mainloop()
