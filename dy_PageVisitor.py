from customtkinter import *
import datetime
from dy_PageUtils import set_icon_image, update_datetime, btnind, configure_frame, load_image
from db_con import fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc

def create_visitor_table(visitorframe, visitor_data):
    for i in range(15):  # Assuming 15 is the maximum number of rows you want
        y_offset = 0 + (i * 0.065)  # Adjust the y offset for each row

        entries = []
        for j in range(7):  # Assuming 7 columns based on your data structure
            entry = CTkEntry(visitorframe, width=150, height=35, state='normal', fg_color="white", corner_radius=0, border_width=1)
            entry.grid(row=i, column=j, sticky="nsew")  # Use grid instead of place
            entries.append(entry)

        if i < len(visitor_data):
            for entry, value in zip(entries, visitor_data[i]):
                entry.insert(0, value if value is not None else "")  # Insert data or empty string if data is None
            for entry in entries:
                entry.configure(state='disabled')  # Disable all entries in the row after inserting data
        else:
            for entry in entries:  # Disable all entries in rows without data
                entry.configure(state='disabled')

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    Visitorframe = CTkFrame(visitorpage_window, fg_color="white")
    Visitorframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Visitorframe, [1, 2, 2, 9, 2], [1,7,7,1])

    headingf = CTkFrame (Visitorframe, fg_color="transparent")
    headingf.grid(row=1, column=1,columnspan=2, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    VisitorHeading = CTkLabel(headingf, text="Visitor Data", font=("Inter", 35, "bold"), fg_color="transparent",text_color="#333333" )
    VisitorHeading.grid(row=0, column=0, columnspan=3, sticky="nw")
    timef = CTkFrame (headingf, fg_color="#E9F3F2", border_width=2, border_color="#BFC3C3", corner_radius=10)
    timef.grid(row=0, column=4, sticky="nsew")
    # Configure date and time display
    time_label = CTkLabel(timef, fg_color="transparent", text="", font=("Arial", 30, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(timef, fg_color="transparent", text="", font=("Inter", 16, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.55, anchor="n")
    calimage = load_image('calendar_icon.png', (75, 75))
    calendar = CTkLabel(timef, image=calimage, text="")
    calendar.place(relx=0.75, rely=0.09, anchor='n')

    # Update date and time periodically
    update_datetime(date_label, time_label)
    visitorpage_window.after(1000, lambda: update_datetime(date_label, time_label))

    def refresh_visitor_table(fetch_data_func):
        visitor_data = fetch_data_func()
        for widget in tablebody.winfo_children():
            widget.destroy()
        create_visitor_table(tablebody, visitor_data)

    btn_labels = ["Recent", "Oldest", "A - Z", "Z - A"]
    btns = []

    btnf = CTkFrame(Visitorframe, fg_color="transparent")
    btnf.grid(row=2, column=1, sticky="nsew", pady=10)
    configure_frame(btnf, [1], [1, 1, 1, 1])

    def btn_command_wrapper(fetch_func, btn_index):
        def command():
            refresh_visitor_table(fetch_func)
            btnind(btns[btn_index], *btns)
        return command

    for i, label in enumerate(btn_labels):
        btn = CTkButton(btnf, text=label,
                        font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                        width=100, height=30, fg_color="#93ACAF" if i == 0 else "#FEFEFE",
                        corner_radius=25, border_width=3, border_color="#91ABAE")
        btn.grid(row=0, column=i, sticky="sew", padx=10, pady=2)
        btn.configure(command=btn_command_wrapper([fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc][i], i))

        btns.append(btn)

    tablef = CTkFrame (Visitorframe, fg_color="transparent")
    tablef.grid(row=3,column=1,columnspan=2, sticky="nsew")
    configure_frame(tablef, [1,8], [1,1,1,1,1,1,1])
    tableheading = CTkFrame (tablef, fg_color="#93ACAF", border_width=2, border_color="#93ACAF", corner_radius=0)
    tableheading.grid(row=0,column=0,columnspan=7, sticky="nsew")
    configure_frame(tableheading, [1], [1,1,1,1,1,1,1])
    headings = {
        "Name": 0,
        "Date": 1,
        "Log In": 2,
        "Log Out": 3,
        "Resident": 4,
        "Security": 5,
        "Purpose": 6
    }

    for heading, column in headings.items():
        heading_label = CTkLabel(tableheading, text=heading, font=("Inter", 14, "bold"), text_color="white", fg_color="transparent")
        heading_label.grid(row=0, column=column, sticky="nsew")

    tablebody = CTkFrame (tablef, fg_color="transparent", border_width=2, border_color="green", corner_radius=0)
    tablebody.grid(row=1,column=0,columnspan=7, sticky="nsew")
    configure_frame(tablebody, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1]) #rows and columns
    refresh_visitor_table(fetch_visitor_data_desc)