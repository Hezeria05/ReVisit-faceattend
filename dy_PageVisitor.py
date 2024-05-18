from customtkinter import *
import datetime
from dy_PageUtils import set_icon_image, update_datetime, btnind, configure_frame
from db_con import fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    Visitorframe = CTkFrame(visitorpage_window, fg_color="white")
    Visitorframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Visitorframe, [1, 2, 2, 9, 2], [1,7,7,1])

    headingf = CTkFrame (Visitorframe, fg_color="transparent", border_width=2, border_color="gray")
    headingf.grid(row=1, column=1, sticky="nsew")
    btnf = CTkFrame (Visitorframe, fg_color="transparent", border_width=2, border_color="gray")
    btnf.grid(row=2,column=1, sticky="nsew", pady=10)
    tablef = CTkFrame (Visitorframe, fg_color="transparent", border_width=2, border_color="gray")
    tablef.grid(row=3,column=1,columnspan=2, sticky="nsew")
