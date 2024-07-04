from customtkinter import *
import datetime
from dy_PageUtils import update_datetime, btnind, configure_frame, load_image
from db_con import fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc, get_total_visitors

# Store the current fetch function
current_fetch_func = fetch_visitor_data_desc

def create_visitor_table(visitorframe, visitor_data):
    for i in range(15):
        entries = []
        for j in range(7):
            entry = CTkEntry(visitorframe, state='normal', fg_color="white", corner_radius=0, border_width=1, border_color="#93ACAF")
            entry.grid(row=i, column=j, sticky="nsew")
            entries.append(entry)

        if i < len(visitor_data):
            for entry, value in zip(entries, visitor_data[i]):
                entry.insert(0, value if value is not None else "")
            for entry in entries:
                entry.configure(state='disabled')
        else:
            for entry in entries:
                entry.configure(state='disabled')

def Visitor_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button):
    global current_fetch_func
    home_button.configure(state="normal")
    visitor_button.configure(state="normal")
    resident_button.configure(state="normal")
    logout_btn.configure(state="normal")

    current_page = 0

    def refresh_visitor_table():
        offset = current_page * 15
        visitor_data = current_fetch_func(offset)
        for widget in tablebody.winfo_children():
            widget.destroy()
        create_visitor_table(tablebody, visitor_data)

        # Disable buttons if necessary
        back_button.configure(state='normal' if current_page > 0 else 'disabled')
        next_button.configure(state='normal' if current_page < total_pages - 1 else 'disabled')
        update_pagination_labels()

    def update_pagination_labels():
        start_page = (current_page // 3) * 3
        currentpage_button.configure(text=str(start_page + 1), text_color="#00507E" if current_page == start_page else "#B9B9B9")
        nextpage_button.configure(text=str(start_page + 2), text_color="#00507E" if current_page == start_page + 1 else "#B9B9B9")
        nnxpage_button.configure(text=str(start_page + 3), text_color="#00507E" if current_page == start_page + 2 else "#B9B9B9")

    def create_pagination_buttons():
        nonlocal current_page
        currentpage_button.configure(command=lambda: go_to_page((current_page // 3) * 3))
        nextpage_button.configure(command=lambda: go_to_page((current_page // 3) * 3 + 1))
        nnxpage_button.configure(command=lambda: go_to_page((current_page // 3) * 3 + 2))

    def go_to_page(page):
        nonlocal current_page
        if 0 <= page < total_pages:
            current_page = page
            refresh_visitor_table()
            highlight_current_page()

    def highlight_current_page():
        start_page = (current_page // 3) * 3
        currentpage_button.configure(text=str(start_page + 1), text_color="#00507E" if current_page == start_page else "#B9B9B9")
        nextpage_button.configure(text=str(start_page + 2), text_color="#00507E" if current_page == start_page + 1 else "#B9B9B9")
        nnxpage_button.configure(text=str(start_page + 3), text_color="#00507E" if current_page == start_page + 2 else "#B9B9B9")
        back_button.configure(image=previmage if current_page > 0 else prevdisimage)
        next_button.configure(image=nextimage if current_page < total_pages - 1 else nextdisimage)

    Visitorframe = CTkFrame(visitorpage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    Visitorframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Visitorframe, [1, 2, 1, 9, 2], [1, 7, 7, 1])

    headingf = CTkFrame(Visitorframe, fg_color="transparent")
    headingf.grid(row=1, column=1, columnspan=2, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    VisitorHeading = CTkLabel(headingf, text="Visitor Data", font=("Inter", 45, "bold"), fg_color="transparent", text_color="#333333")
    VisitorHeading.grid(row=0, column=0, columnspan=3, sticky="nw", padx=20)
    timef = CTkFrame(headingf, fg_color="#E9F3F2", border_width=2, border_color="#BFC3C3", corner_radius=5)
    timef.grid(row=0, column=4, sticky="nsew", padx=20)

    time_label = CTkLabel(timef, fg_color="transparent", text="", font=("Arial", 30, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(timef, fg_color="transparent", text="", font=("Inter", 16, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.55, anchor="n")
    calimage = load_image('calendar_icon.png', (75, 75))
    calendar = CTkLabel(timef, image=calimage, text="")
    calendar.place(relx=0.75, rely=0.09, anchor='n')

    update_datetime(date_label, time_label)
    visitorpage_window.after(1000, lambda: update_datetime(date_label, time_label))

    btn_labels = ["Recent", "Oldest", "A - Z", "Z - A"]
    btns = []

    btnf = CTkFrame(Visitorframe, fg_color="transparent")
    btnf.grid(row=1, rowspan=2, column=1, sticky="sew", pady=10, padx=20)
    configure_frame(btnf, [1], [1, 1, 1, 1])

    def btn_command_wrapper(fetch_func, btn_index):
        def command():
            global current_fetch_func
            current_fetch_func = fetch_func
            refresh_visitor_table()
            btnind(btns[btn_index], *btns)
        return command

    fetch_functions = [fetch_visitor_data_desc, fetch_visitor_data_asc, fetch_visitor_data_name_asc, fetch_visitor_data_name_desc]

    for i, label in enumerate(btn_labels):
        btn = CTkButton(btnf, text=label,
                        font=("Inter", 15, "bold"), hover_color="#93ACAF", text_color="#333333",
                        width=100, height=40, fg_color="#93ACAF" if i == 0 else "#FEFEFE",
                        corner_radius=25, border_width=3, border_color="#91ABAE")
        btn.grid(row=0, column=i, sticky="sew", padx=10, pady=17)
        btn.configure(command=btn_command_wrapper(fetch_functions[i], i))

        btns.append(btn)

    tablef = CTkFrame(Visitorframe, fg_color="transparent")
    tablef.grid(row=3, column=1, columnspan=2, sticky="nsew", padx=20)
    configure_frame(tablef, [1, 8], [1, 1, 1, 1, 1, 1, 1])
    tableheading = CTkFrame(tablef, fg_color="#93ACAF", border_width=2, border_color="#93ACAF", corner_radius=0)
    tableheading.grid(row=0, column=0, columnspan=7, sticky="nsew")
    configure_frame(tableheading, [1], [2, 2, 1, 1, 3, 2, 2])
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

    tablebody = CTkFrame(tablef, fg_color="transparent", border_width=1, border_color="#93ACAF", corner_radius=0)
    tablebody.grid(row=1, column=0, columnspan=7, sticky="nsew")
    configure_frame(tablebody, [1]*15, [2, 2, 1, 1, 3, 2, 2])

    # Initiate the canvas
    pagination_frame = CTkFrame(Visitorframe, fg_color="transparent", width=250, height=60)
    pagination_frame.place(relx=0.5, rely=0.93, anchor="center")
    configure_frame(pagination_frame, [1], [1,1,1,1,1])
    pagination_frame.grid_propagate(False)
    previmage = load_image('prev.png', (30, 30))
    prevdisimage = load_image('prevdis.png', (30, 30))
    nextimage = load_image('next.png', (30, 30))
    nextdisimage = load_image('nextdis.png', (30, 30))

    # Configure Buttons
    total_visitors = get_total_visitors()
    total_pages = (total_visitors + 14) // 15

    # Create back button with initial image
    back_button = CTkButton(pagination_frame, image=prevdisimage, text='', width=35,
                            fg_color="transparent", hover_color="white", state='disabled', command=lambda: navigate_page(-1))
    back_button.grid(row=0, column=0)

    currentpage_button = CTkButton(pagination_frame, text=str(1), width=35, font=("Inter", 18, "bold"), text_color="#00507E",
                                   fg_color="transparent", hover_color="white", command=lambda: go_to_page(0))
    currentpage_button.grid(row=0, column=1)

    nextpage_button = CTkButton(pagination_frame, text=str(2), width=35, font=("Inter", 18, "bold"), text_color="#B9B9B9",
                                fg_color="transparent", hover_color="white", command=lambda: go_to_page(1))
    nextpage_button.grid(row=0, column=2)

    nnxpage_button = CTkButton(pagination_frame, text=str(3), width=35, font=("Inter", 18, "bold"), text_color="#B9B9B9",
                               fg_color="transparent", hover_color="white", command=lambda: go_to_page(2))
    nnxpage_button.grid(row=0, column=3)

    # Create next button with initial image
    next_button = CTkButton(pagination_frame, image=nextimage if total_pages > 1 else nextdisimage, text='', width=35,
                            fg_color="transparent", hover_color="white", state='normal' if total_pages > 1 else 'disabled', command=lambda: navigate_page(1))
    next_button.grid(row=0, column=4)

    # Function to navigate pages
    def navigate_page(direction):
        nonlocal current_page
        if 0 <= current_page + direction < total_pages:
            current_page += direction
            refresh_visitor_table()
            highlight_current_page()

    create_pagination_buttons()
    refresh_visitor_table()
    highlight_current_page()
