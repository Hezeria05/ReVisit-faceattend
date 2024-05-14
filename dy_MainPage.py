from customtkinter import *
from PageUtils import set_background_image, ASSETS_PATH, set_icon_image, logout, indicate
from PageHome import Home_page
from PageVisitor import Visitor_page
from PageResident import Resident_page

homepage_window = CTk()
homepage_window.title('Main Window')
homepage_window.geometry('1440x900+300+70')
homepage_window.minsize(1440, 900)
homepage_window.maxsize(homepage_window.winfo_screenwidth(), homepage_window.winfo_screenheight())
homepage_window.configure(fg_color='#E9F3F2')




#_______________________________________________________________________SIDEBAR
Sidebar = CTkFrame(homepage_window, fg_color="#FEFEFE", width=380, height=728)
Sidebar.place(relx=0, rely=0.19)

homepage_window.mainloop()
