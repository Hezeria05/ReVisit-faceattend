from customtkinter import *
from PageUtils import set_background_image, ASSETS_PATH, set_icon_image, logout, indicate
from PageHome import Home_page
from PageVisitor import Visitor_page
from PageResident import Resident_page
# def open_homepage(sec_id):
homepage_window = CTk()
homepage_window.title('Home')
homepage_window.geometry('1440x900+300+70')
homepage_window.minsize(1440, 900)
homepage_window.maxsize(1440, 900)

sec_id = 7

# Background for the new window
set_background_image(homepage_window, ASSETS_PATH / 'HOME PAGE.png', size=(1440,900))

#_______________________________________________________________________SIDEBAR
Sidebar = CTkFrame(homepage_window, fg_color="#FEFEFE", width=380, height=728)
Sidebar.place(relx=0, rely=0.19)

#Home Button
Home_btn = CTkButton(Sidebar, text="Home", width=20, height=20, fg_color="#FEFEFE",
                hover_color="#FEFEFE", font=("Inter", 25, "bold"), text_color="#333333")
Home_btn.place(relx=0.2, rely=0.1, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'home_icon.png', relx=0.15, rely=0.105, anchor='n', size=(27, 27))
Home_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 30),fg_color="#00507E")
Home_indct.place(relx=0.05, rely=0.1, anchor='n')

#Visitor Button
Visitor_btn = CTkButton(Sidebar, text="Visitor Data",  width=20, height=20, fg_color="#FEFEFE",
                hover_color="#FEFEFE", font=("Inter", 25, "bold"), text_color="#333333")
Visitor_btn.place(relx=0.2, rely=0.2, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'visitor_icon.png', relx=0.15, rely=0.205, anchor='n', size=(27, 27))
Visitor_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 30), fg_color="#FEFEFE")
Visitor_indct.place(relx=0.05, rely=0.2, anchor='n')

#Resident Button
Resident_btn = CTkButton(Sidebar, text="Residents List", width=20, height=20,fg_color="#FEFEFE",
                hover_color="#FEFEFE", font=("Inter", 25, "bold"), text_color="#333333")
Resident_btn.place(relx=0.2, rely=0.3, anchor='nw')
set_icon_image(Sidebar, ASSETS_PATH / 'list_icon.png', relx=0.15, rely=0.305, anchor='n', size=(27, 27))
Resident_indct = CTkLabel(Sidebar, text=' ', font=("Arial", 30), fg_color="#FEFEFE")
Resident_indct.place(relx=0.05, rely=0.3, anchor='n')

#Configure Button
# Modify the button commands to pass the indicators
Home_btn.configure(command=lambda: indicate(Home_indct, lambda: Home_page(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct), Home_indct, Visitor_indct, Resident_indct))
Visitor_btn.configure(command=lambda: indicate(Visitor_indct, lambda: Visitor_page(homepage_window, Home_indct, Visitor_indct, Resident_indct), Home_indct, Visitor_indct, Resident_indct))
Resident_btn.configure(command=lambda: indicate(Resident_indct, lambda: Resident_page(homepage_window), Home_indct, Visitor_indct, Resident_indct))

# Add a logout button
logout_btn = CTkButton(Sidebar, text="LOG OUT", fg_color="#FEFEFE", hover_color="#FEFEFE", font=("Inter", 25, "bold"),
                text_color="#333333", command=lambda:logout(homepage_window))
logout_btn.place(relx=0.5, rely=0.85, anchor='n')

# Call Home_page() to display the home page by default
Home_page(homepage_window, sec_id, Home_indct, Visitor_indct, Resident_indct)


# Add a label to display the sec_id
# sec_id_label = CTkLabel(homepage_window, text=f"Sec ID: {sec_id}", font=("Inter", 20))
# sec_id_label.pack(pady=20)

homepage_window.mainloop()
