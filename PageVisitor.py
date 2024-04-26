from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime
from db_con import fetch_visitor_data

def create_info_frame(parent, text, width, height, relx, rely):
    info_frame = CTkFrame(parent, fg_color="#E9F3F2", width=width, height=height, corner_radius=10,
                          border_color="#B9BDBD", border_width=2)
    info_frame.place(relx=relx, rely=rely)

    label = CTkLabel(info_frame, fg_color="transparent", text=text, font=("Arial", 15, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=0.125, anchor="n")

    return info_frame

def create_table(frame, rows, cols):
    headers = ["ID", "Name", "Date", "Time", "Purpose", "Duration", "Remarks"]  # Define the column headers
    # Create headers
    for c in range(cols):
        header = CTkLabel(frame, text=headers[c], font=("Arial", 12, "bold"), fg_color="white", text_color="#333333")
        header.grid(row=0, column=c, padx=10, pady=5, sticky="ew")

    # Create the table cells
    for r in range(1, rows + 1):
        for c in range(cols):
            cell = CTkEntry(frame, state='readonly', fg_color="white", text_color="#333333", border_width=1, corner_radius=1)
            cell.grid(row=r, column=c,padx=0, pady=0, sticky="ew")
            cell.insert(0, "Sample Data")

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

    VTable = CTkFrame (Visitorframe, width=960, height=500, fg_color="white", corner_radius=10,
                          border_color="#B9BDBD", border_width=2)
    VTable.place(relx=0.5, rely=0.6, anchor="center")
    create_table(VTable, 10, 7)


