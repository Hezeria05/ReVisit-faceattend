from customtkinter import *
import datetime 
from dy_PageUtils import set_icon_image, toggle_edit_save, validate_length, configure_frame, load_image, validate_char, validate_phone_number
from db_con import fetch_resident_data, get_total_residents

def validate_search_entry(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" "):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

def Resident_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    # Initialize current page state
    current_page = 0
    entries_list = []
    id_list = []
    search_query = ""
    total_results = 0

    Residentframe = CTkFrame(visitorpage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    Residentframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Residentframe, [1, 2, 11, 2], [1, 7, 7, 7, 1])

    headingf = CTkFrame(Residentframe, fg_color="transparent")
    headingf.grid(row=1, column=1, columnspan=3, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    ResidentHeading = CTkLabel(headingf, text="Residents List", font=("Inter", 35, "bold"), fg_color="transparent", text_color="#333333")
    ResidentHeading.grid(row=0, column=0, columnspan=3, sticky="nw", padx=40)
    searchf = CTkFrame(headingf, fg_color="white", width=450, height=100, border_width=2, border_color="#BFC3C3", corner_radius=10)
    searchf.place(relx=0.85, rely=0.3, anchor="center")
    # Add search entry and button
    search_entry = CTkEntry(searchf, fg_color="white", border_width=0, width=220, height=35, placeholder_text="Search")
    search_entry.grid(row=0, column=0, padx=10, pady=10)
    search_entry.bind("<KeyPress>", lambda event: validate_length(event, search_entry, 35))
    search_entry.bind("<KeyPress>", lambda event: validate_search_entry(event))
    searchimage = load_image('search.png', (34, 34))
    search_button = CTkButton(searchf, text="", image=searchimage, width=34,
                            fg_color="transparent", hover_color="white", command=lambda: search_residents(search_entry.get()))
    search_button.grid(row=0, column=1, sticky="e", padx=10)

    tablef = CTkFrame(Residentframe, fg_color="transparent")
    tablef.grid(row=2, column=1, columnspan=3, sticky="nsew")
    configure_frame(tablef, [1, 8], [1, 1, 1])
    tableheading = CTkFrame(tablef, fg_color="#93ACAF", border_width=2, border_color="#93ACAF", corner_radius=0)
    tableheading.grid(row=0, column=0, columnspan=7, sticky="nsew")
    configure_frame(tableheading, [1], [1, 1, 1])
    headings = {
        "Name": 0,
        "Address": 1,
        "Phone Number": 2,
    }

    for heading, column in headings.items():
        heading_label = CTkLabel(tableheading, text=heading, font=("Inter", 20, "bold"), text_color="white", fg_color="transparent")
        heading_label.grid(row=0, column=column, sticky="nsew")

    tablebody = CTkFrame(tablef, fg_color="transparent", border_width=1, border_color="#BFC3C3", corner_radius=0)
    tablebody.grid(row=1, column=0, columnspan=3, sticky="nsew")
    configure_frame(tablebody, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1])  # rows and columns

    # Create Edit Button
    edit_button = CTkButton(Residentframe, text="Edit", width=120, height=50, corner_radius=10,
                    fg_color="#ADCBCF", hover_color="#93ACAF", font=("Inter", 20, "bold"),
                    text_color="#333333", command=lambda: toggle_edit_save(Residentframe, edit_button, entries_list, id_list, True))
    edit_button.place(relx=0.5, rely=0.9285, anchor="center")

    # Create pagination buttons
    pagination_frame = CTkFrame(Residentframe, fg_color="transparent")
    pagination_frame.place(relx=0.9, rely=0.93, anchor="center")
    configure_frame(pagination_frame, [1], [1,1])
    pageimage = load_image('paginationframe.png', (144, 54))
    pagelabel = CTkLabel(pagination_frame, image=pageimage, text="")
    pagelabel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    previmage = load_image('prev.png', (30, 30))
    prevdisimage = load_image('prevdis.png', (30, 30))
    nextimage = load_image('next.png', (30, 30))
    nextdisimage = load_image('nextdis.png', (30, 30))
   
    # Create back button with initial image
    back_button = CTkButton(pagination_frame, image=prevdisimage, text='', width=35,
                            fg_color="transparent", hover_color="white", state='disabled', command=lambda: navigate_page(-1))

    # Create next button with initial image
    next_button = CTkButton(pagination_frame, image=nextimage, text='', width=35,
                            fg_color="transparent", hover_color="white", command=lambda: navigate_page(1))

    # Update button images based on initial conditions
    back_button.grid(row=0, column=0)
    next_button.grid(row=0, column=1)

    def navigate_page(direction):
        nonlocal current_page, entries_list, id_list
        current_page += direction
        refresh_resident_table()

    def refresh_resident_table():
        nonlocal entries_list, id_list, search_query, total_results
        offset = current_page * 15
        resident_data, total_results = fetch_resident_data(offset, search_query)
        for widget in tablebody.winfo_children():
            widget.destroy()
        entries_list, id_list = create_resident_table(tablebody, resident_data)
        edit_button.configure(command=lambda: toggle_edit_save(Residentframe, edit_button, entries_list, id_list, True))

        # Update pagination buttons
        if current_page > 0:
            back_button.configure(state='normal', image=previmage)
        else:
            back_button.configure(state='disabled', image=prevdisimage)
        if (current_page + 1) * 15 < total_results:
            next_button.configure(state='normal', image=nextimage)
        else:
            next_button.configure(state='disabled', image=nextdisimage)

    def create_resident_table(Residentframe, resident_data):
        entries_list = []
        id_list = []  # Separate list to store res_ids
        for i, data_row in enumerate(resident_data):
            entries = []
            res_id = data_row[0]  # First element is res_id
            row_data = data_row[1:]  # Skip res_id for display purposes
            for j, value in enumerate(row_data):
                entry = CTkEntry(Residentframe, fg_color="white", corner_radius=0, border_width=1)
                entry.insert(0, value if value is not None else "")
                entry.configure(state='disabled')
                entry.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)  # Use grid method for positioning
                if j == 0:  # Name field
                    entry.bind("<KeyPress>", validate_char)
                elif j == 2:  # Phone number field
                    entry.bind("<KeyPress>", validate_phone_number)
                entries.append(entry)
            entries_list.append(entries)
            id_list.append(res_id)  # Store res_id separately

        return entries_list, id_list

    def search_residents(query):
        nonlocal search_query, current_page
        search_query = query
        current_page = 0  # Reset to first page on new search
        refresh_resident_table()

    refresh_resident_table()
