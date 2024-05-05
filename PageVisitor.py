from customtkinter import *
import datetime 
from PageUtils import ASSETS_PATH, set_icon_image, update_datetime, btnind
from db_con import fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc


def create_info_frame(parent, text, width, height, relx, rely):
    info_frame = CTkFrame(parent, fg_color="#E9F3F2", width=width, height=height, corner_radius=10,
                          border_color="#B9BDBD", border_width=2)
    info_frame.place(relx=relx, rely=rely)

    label = CTkLabel(info_frame, fg_color="transparent", text=text, font=("Arial", 15, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=0.125, anchor="n")

    return info_frame

def create_visitor_table(visitorframe, visitor_data):
    for i in range(15):  # Assuming 15 is the maximum number of rows you want
        y_offset = 0 + (i * 0.065)  # Adjust the y offset for each row

        entries = []
        for j in range(7):  # Assuming 7 columns based on your data structure
            entry = CTkEntry(visitorframe, width=150, height=35, state='normal', fg_color="white", corner_radius=0, border_width=1)
            entry.place(relx=0 + (j * 0.1407), rely=y_offset)  # Adjust x position based on column
            entries.append(entry)

        if i < len(visitor_data):
            for entry, value in zip(entries, visitor_data[i]):
                entry.insert(0, value if value is not None else "")  # Insert data or empty string if data is None
            for entry in entries:
                if not entry.get():  # Check if entry is empty
                    entry.configure(state='disabled')  # Disable if empty
                else:
                    entry.configure(state='disabled')  # Disable after inserting data as well
        else:
            for entry in entries:  # Disable all entries in rows without data
                entry.configure(state='disabled')

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct):
    Visitorframe = CTkFrame(visitorpage_window, fg_color="#F6FCFC", width=1057, height=715)
    Visitorframe.place(relx=0.266, rely=0.118)

    VisitorHeading = CTkLabel(Visitorframe, text="Visitor Data", font=("Inter", 35, "bold"), text_color="#333333")
    VisitorHeading.place(relx=0.043, rely=0.06)

    DateTimeframe = create_info_frame(Visitorframe, "", 280, 102, 0.683, 0.05)
    time_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Arial", 28, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(DateTimeframe, fg_color="transparent", text="", font=("Inter", 14, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.52, anchor="n")
    set_icon_image(DateTimeframe, ASSETS_PATH / 'calendar_icon.png', relx=0.75, rely=0.09, anchor='n', size=(75, 75))
    update_datetime(date_label, time_label)
    visitorpage_window.after(1000, lambda: update_datetime(date_label, time_label))

    VTfilter = CTkFrame(Visitorframe, width=500, height=50, fg_color="transparent")
    VTfilter.place(relx=0.043, rely=0.215)

    def refresh_visitor_table(fetch_data_func):
        visitor_data = fetch_data_func()
        for widget in VTRows.winfo_children():
            widget.destroy()
        create_visitor_table(VTRows, visitor_data)

    btn1 = CTkButton(VTfilter, text="Recent",
                    font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                    width=100, height=30, fg_color="#93ACAF", corner_radius=25, border_width=3, border_color="#91ABAE")
    btn1.pack(side='left', padx=7, fill='both', expand=True)

    btn2 = CTkButton(VTfilter, text="Oldest",
                    font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                    width=100, height=30, fg_color="#FEFEFE", corner_radius=25, border_width=3, border_color="#91ABAE")
    btn2.pack(side='left', padx=7, fill='both', expand=True)

    btn3 = CTkButton(VTfilter, text="A - Z",
                    font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                    width=100, height=30, fg_color="#FEFEFE", corner_radius=25, border_width=3, border_color="#91ABAE")
    btn3.pack(side='left', padx=7, fill='both', expand=True)

    btn4 = CTkButton(VTfilter, text="Z - A",
                    font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                    width=100, height=30, fg_color="#FEFEFE", corner_radius=25, border_width=3, border_color="#91ABAE")
    btn4.pack(side='left', padx=7, fill='both', expand=True)

    VTCols = CTkFrame(Visitorframe, width=960, height=50, fg_color="#93ACAF", corner_radius=0,
                      border_color="#B9BDBD", border_width=1)
    VTCols.place(relx=0.5, rely=0.33, anchor="center")

    btn1.configure(command=lambda: (refresh_visitor_table(fetch_visitor_data_desc), btnind(btn1, btn1, btn2, btn3, btn4)))
    btn2.configure(command=lambda: (refresh_visitor_table(fetch_visitor_data_asc), btnind(btn2, btn1, btn2, btn3, btn4)))
    btn3.configure(command=lambda: (refresh_visitor_table(fetch_visitor_data_name_asc), btnind(btn3, btn1, btn2, btn3, btn4)))
    btn4.configure( command=lambda: (refresh_visitor_table(fetch_visitor_data_name_desc), btnind(btn4, btn1, btn2, btn3, btn4)))

    headings = {
        "Name": 0.065,
        "Date": 0.21,
        "Log In": 0.35,
        "Log Out": 0.485,
        "Resident": 0.630,
        "Security": 0.775,
        "Purpose": 0.920
    }

    for heading, position in headings.items():
        heading_label = CTkLabel(VTCols, text=heading, font=("Inter", 14, "bold"), text_color="white", fg_color="transparent")
        heading_label.place(relx=position, rely=0.5, anchor="center")

    VTRows = CTkFrame(Visitorframe, width=960, height=400, fg_color="white", corner_radius=0,
                      border_color="#B9BDBD", border_width=0)
    VTRows.place(relx=0.5, rely=0.64, anchor="center")

    # Call to refresh the visitor table with the most recent data by default
    refresh_visitor_table(fetch_visitor_data_desc)


