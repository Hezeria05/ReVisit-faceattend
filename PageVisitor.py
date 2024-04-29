from customtkinter import *
import datetime 
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime
from db_con import fetch_visitor_data


def create_info_frame(parent, text, width, height, relx, rely):
    info_frame = CTkFrame(parent, fg_color="#E9F3F2", width=width, height=height, corner_radius=10,
                          border_color="#B9BDBD", border_width=2)
    info_frame.place(relx=relx, rely=rely)

    label = CTkLabel(info_frame, fg_color="transparent", text=text, font=("Arial", 15, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=0.125, anchor="n")

    return info_frame

def create_visitor_table(visitorframe, visitor_data):
    for i in range(15):  # Assuming 10 is the maximum number of rows you want
        y_offset = 0.36 + (i * 0.0375)  # Adjust the y offset for each row

        entries = []
        for j in range(7):  # Assuming 7 columns based on your data structure
            entry = CTkEntry(visitorframe, width=150, height=30, state='normal', fg_color="white", corner_radius=0, border_width=1)
            entry.place(relx=0.0465 + (j * 0.1277), rely=y_offset)  # Adjust x position based on column
            entries.append(entry)

        if i < len(visitor_data):
            for entry, value in zip(entries, visitor_data[i]):
                entry.insert(0, value if value is not None else "")

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct):
    Visitorframe = CTkFrame(visitorpage_window, fg_color="#F6FCFC", width=1057, height=715)
    Visitorframe.place(relx=0.266, rely=0.118)

    VisitorHeading = CTkLabel(Visitorframe, text="Visitor Data", font=("Inter", 35, "bold"),text_color="#333333" )
    VisitorHeading.place(relx=0.043, rely=0.06)

    DateTimeframe = create_info_frame(Visitorframe, "", 280, 102, 0.683, 0.05)
    # Configure date and time display
    time_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Arial", 28, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")

    date_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Inter", 14, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.52, anchor="n")
    set_icon_image(DateTimeframe, ASSETS_PATH / 'calendar_icon.png', relx=0.75, rely=0.09, anchor='n', size=(75, 75))

    # Update date and time periodically
    update_datetime(date_label, time_label)
    visitorpage_window.after(1000, lambda: update_datetime(date_label, time_label))

    VTfilter = CTkFrame (Visitorframe, width=290, height=50, fg_color="white", corner_radius=5,
                          border_color="#B9BDBD", border_width=1)
    VTfilter.place(relx=0.043, rely=0.2)

    FilterB = CTkComboBox(VTfilter, width=285.0, height=45, values=[" Recent"," Oldest"," A - Z", " Z - A"], button_color="white",
                          button_hover_color="#ADCBCF", corner_radius=0, dropdown_hover_color="#ADCBCF", fg_color="white",
                          border_width=0, font=("Inter", 16, "bold"))
    FilterB.place(relx=0.5, rely=0.5, anchor='center')

    VTCols = CTkFrame (Visitorframe, width=960, height=50, fg_color="#93ACAF", corner_radius=0,
                          border_color="#B9BDBD", border_width=1)
    VTCols.place(relx=0.5, rely=0.33, anchor="center")

    # Your specific headings and their relative positions
    headings = {
        "Name": 0.065,
        "Date": 0.21,
        "Log In": 0.35,
        "Log Out": 0.485,
        "Resident": 0.630,
        "Security": 0.775,
        "Purpose": 0.920
    }

    # Place each header label at the specified x position
    for heading, position in headings.items():
        heading_label = CTkLabel(VTCols, text=heading, font=("Inter", 14, "bold"), text_color="white", fg_color="transparent")
        heading_label.place(relx=position, rely=0.5, anchor="center")

    VTRows = CTkFrame (Visitorframe, width=960, height=400, fg_color="white", corner_radius=0,
                          border_color="#B9BDBD", border_width=0)
    VTRows.place(relx=0.5, rely=0.65, anchor="center")
    # Fetch data and create visitor table
    visitor_data = fetch_visitor_data()
    create_visitor_table(Visitorframe, visitor_data)

