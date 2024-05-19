from customtkinter import *
import datetime 
from dy_PageUtils import set_icon_image, update_datetime, btnind, configure_frame, load_image
from db_con import fetch_resident_data, update_resident_data

def Resident_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    Residentframe = CTkFrame(visitorpage_window, fg_color="white")
    Residentframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Residentframe, [1, 2, 11, 2], [1,7,7,7,1])

    headingf = CTkFrame (Residentframe, fg_color="transparent")
    headingf.grid(row=1, column=1,columnspan=3, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    ResidentHeading = CTkLabel(headingf, text="Residents List", font=("Inter", 35, "bold"), fg_color="transparent",text_color="#333333" )
    ResidentHeading.grid(row=0, column=0, columnspan=3, sticky="nw", padx=40)
    searchf = CTkFrame (headingf, fg_color="white", border_width=2, border_color="#BFC3C3", corner_radius=10)
    searchf.grid(row=0, column=3, columnspan=4, sticky="new", padx=20)

    tablef = CTkFrame (Residentframe, fg_color="transparent")
    tablef.grid(row=2,column=1,columnspan=3, sticky="nsew")
    configure_frame(tablef, [1,8], [1,1,1])
    tableheading = CTkFrame (tablef, fg_color="#93ACAF", border_width=2, border_color="#93ACAF", corner_radius=0)
    tableheading.grid(row=0,column=0,columnspan=7, sticky="nsew")
    configure_frame(tableheading, [1], [1,1,1])
    headings = {
        "Name": 0,
        "Address": 1,
        "Phone Number": 2,
    }

    for heading, column in headings.items():
        heading_label = CTkLabel(tableheading, text=heading, font=("Inter", 20, "bold"), text_color="white", fg_color="transparent")
        heading_label.grid(row=0, column=column, sticky="nsew")

    tablebody = CTkFrame (tablef, fg_color="transparent", border_width=2, border_color="green", corner_radius=0)
    tablebody.grid(row=1,column=0,columnspan=3, sticky="nsew")
    configure_frame(tablebody, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1]) #rows and columns