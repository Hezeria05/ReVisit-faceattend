from customtkinter import *
import datetime
from dy_PageUtils import set_icon_image, update_datetime, btnind, configure_frame, load_image
from db_con import fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc, get_total_visitors

def create_visitor_table(visitorframe, visitor_data):
    for i in range(15):
        y_offset = 0 + (i * 0.065)

        entries = []
        for j in range(7):
            entry = CTkEntry(visitorframe, width=150, height=35, state='normal', fg_color="white", corner_radius=0, border_width=1)
            entry.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)
            entries.append(entry)

        if i < len(visitor_data):
            for entry, value in zip(entries, visitor_data[i]):
                entry.insert(0, value if value is not None else "")
            for entry in entries:
                entry.configure(state='disabled')
        else:
            for entry in entries:
                entry.configure(state='disabled')

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    current_page = 0

    Visitorframe = CTkFrame(visitorpage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    Visitorframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Visitorframe, [1, 2, 2, 9, 2], [1, 7, 7, 1])

    headingf = CTkFrame(Visitorframe, fg_color="transparent")
    headingf.grid(row=1, column=1, columnspan=2, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    VisitorHeading = CTkLabel(headingf, text="Visitor Data", font=("Inter", 35, "bold"), fg_color="transparent", text_color="#333333")
    VisitorHeading.grid(row=0, column=0, columnspan=3, sticky="nw")
    timef = CTkFrame(headingf, fg_color="#E9F3F2", border_width=2, border_color="#BFC3C3", corner_radius=10)
    timef.grid(row=0, column=4, sticky="nsew")

    time_label = CTkLabel(timef, fg_color="transparent", text="", font=("Arial", 30, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(timef, fg_color="transparent", text="", font=("Inter", 16, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.55, anchor="n")
    calimage = load_image('calendar_icon.png', (75, 75))
    calendar = CTkLabel(timef, image=calimage, text="")
    calendar.place(relx=0.75, rely=0.09, anchor='n')

    update_datetime(date_label, time_label)
    visitorpage_window.after(1000, lambda: update_datetime(date_label, time_label))

    def refresh_visitor_table(fetch_data_func):
        offset = current_page * 15
        visitor_data = fetch_data_func(offset)
        for widget in tablebody.winfo_children():
            widget.destroy()
        create_visitor_table(tablebody, visitor_data)

        # Disable buttons if necessary
        back_button.configure(state='normal' if current_page > 0 else 'disabled')
        next_button.configure(state='normal' if len(visitor_data) == 15 and current_page < total_pages - 1 else 'disabled')

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

    fetch_functions = [fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc]

    for i, label in enumerate(btn_labels):
        btn = CTkButton(btnf, text=label,
                        font=("Inter", 12, "bold"), hover_color="#93ACAF", text_color="#333333",
                        width=100, height=30, fg_color="#93ACAF" if i == 0 else "#FEFEFE",
                        corner_radius=25, border_width=3, border_color="#91ABAE")
        btn.grid(row=0, column=i, sticky="sew", padx=10, pady=2)
        btn.configure(command=btn_command_wrapper(fetch_functions[i], i))

        btns.append(btn)

    tablef = CTkFrame(Visitorframe, fg_color="transparent")
    tablef.grid(row=3, column=1, columnspan=2, sticky="nsew")
    configure_frame(tablef, [1, 8], [1, 1, 1, 1, 1, 1, 1])
    tableheading = CTkFrame(tablef, fg_color="#93ACAF", border_width=2, border_color="#93ACAF", corner_radius=0)
    tableheading.grid(row=0, column=0, columnspan=7, sticky="nsew")
    configure_frame(tableheading, [1], [1, 1, 1, 1, 1, 1, 1])
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
        heading_label.grid(row=0, column=column, sticky="nsew", padx=0, pady=0)

    tablebody = CTkFrame(tablef, fg_color="transparent", border_width=2, border_color="#93ACAF", corner_radius=0)
    tablebody.grid(row=1, column=0, columnspan=7, sticky="nsew")
    configure_frame(tablebody, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1])

    #Initiate the canvas
    pagination_frame = CTkFrame(Visitorframe, fg_color="transparent")
    pagination_frame.place(relx=0.5, rely=0.93, anchor="center")
    configure_frame(pagination_frame, [1], [1,1])
    pageimage = load_image('paginationframe.png', (144, 54))
    pagelabel = CTkLabel(pagination_frame, image=pageimage, text="")
    pagelabel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    previmage = load_image('prev.png', (30, 30))
    prevdisimage = load_image('prevdis.png', (30, 30))
    nextimage = load_image('next.png', (30, 30))
    nextdisimage = load_image('nextdis.png', (30, 30))

    #Configure Buttons
    total_visitors = get_total_visitors()
    total_pages = (total_visitors + 14) // 15
    initial_back_image = previmage if current_page > 0 else prevdisimage
    initial_next_image = nextimage if current_page < total_pages - 1 else nextdisimage

    # Create back button with initial image
    back_button = CTkButton(pagination_frame, image=initial_back_image, text='', width=35,
                            fg_color="transparent", hover_color="white", command=lambda: navigate_page(-1))

    # Create next button with initial image
    next_button = CTkButton(pagination_frame, image=initial_next_image, text='', width=35,
                            fg_color="transparent", hover_color="white", command=lambda: navigate_page(1))

    # Function to navigate pages
    def navigate_page(direction):
        nonlocal current_page
        current_page += direction
        refresh_visitor_table(fetch_visitor_data_desc)
        if current_page > 0:
            back_button.configure(state='normal', image=previmage)
        else:
            back_button.configure(state='disabled', image=prevdisimage)
        if current_page < total_pages - 1:
            next_button.configure(state='normal', image=nextimage)
        else:
            next_button.configure(state='disabled', image=nextdisimage)

    # Update button images based on initial conditions
    back_button.grid(row=0, column=0)
    next_button.grid(row=0, column=1)


    refresh_visitor_table(fetch_visitor_data_desc)