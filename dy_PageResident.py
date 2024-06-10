from customtkinter import *
import datetime 
from dy_PageUtils import set_icon_image, update_datetime, btnind, configure_frame, load_image, validate_full_name, validate_phone_number
from db_con import fetch_resident_data, get_total_residents, update_resident_data

def Resident_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id):
    # Initialize current page state
    current_page = 0
    entries_list = []
    id_list = []

    Residentframe = CTkFrame(visitorpage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    Residentframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Residentframe, [1, 2, 11, 2], [1, 7, 7, 7, 1])

    headingf = CTkFrame(Residentframe, fg_color="transparent")
    headingf.grid(row=1, column=1, columnspan=3, sticky="nsew")
    configure_frame(headingf, [1], [6, 1, 6, 2, 6])
    ResidentHeading = CTkLabel(headingf, text="Residents List", font=("Inter", 35, "bold"), fg_color="transparent", text_color="#333333")
    ResidentHeading.grid(row=0, column=0, columnspan=3, sticky="nw", padx=40)
    searchf = CTkFrame(headingf, fg_color="white", border_width=2, border_color="#BFC3C3", corner_radius=10)
    searchf.grid(row=0, column=3, columnspan=4, sticky="new", padx=20)

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
    edit_button = CTkButton(Residentframe, text="Edit", command=lambda: toggle_edit_save(Residentframe, edit_button, entries_list, id_list, True))
    edit_button.grid(row=3, column=1, pady=20)

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
   
    # Configure Buttons
    total_residents = get_total_residents()
    total_pages = (total_residents + 14) // 15  # Calculate the total number of pages
    initial_back_image = previmage if current_page > 0 else prevdisimage
    initial_next_image = nextimage if current_page < total_pages - 1 else nextdisimage

    # Create back button with initial image
    back_button = CTkButton(pagination_frame, image=initial_back_image, text='', width=35,
                            fg_color="transparent", hover_color="white", command=lambda: navigate_page(-1))

    # Create next button with initial image
    next_button = CTkButton(pagination_frame, image=initial_next_image, text='', width=35,
                            fg_color="transparent", hover_color="white", command=lambda: navigate_page(1))

    # Update button images based on initial conditions
    back_button.grid(row=0, column=0)
    next_button.grid(row=0, column=1)

    def navigate_page(direction):
        nonlocal current_page, entries_list, id_list
        current_page += direction
        refresh_resident_table()

    def refresh_resident_table():
        nonlocal entries_list, id_list
        offset = current_page * 15
        resident_data = fetch_resident_data(offset)
        for widget in tablebody.winfo_children():
            widget.destroy()
        entries_list, id_list = create_resident_table(tablebody, resident_data)
        edit_button.configure(command=lambda: toggle_edit_save(Residentframe, edit_button, entries_list, id_list, True))

        # Disable buttons if necessary
        if current_page > 0:
            back_button.configure(state='normal', image=previmage)
        else:
            back_button.configure(state='disabled', image=prevdisimage)
        if current_page < total_pages - 1:
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
                    entry.bind("<KeyPress>", validate_full_name)
                elif j == 2:  # Phone number field
                    entry.bind("<KeyPress>", validate_phone_number)
                entries.append(entry)
            entries_list.append(entries)
            id_list.append(res_id)  # Store res_id separately

        return entries_list, id_list

    refresh_resident_table()

def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

def validate_phone_number(event):
    if event.keysym in ('BackSpace', 'Delete', 'Left', 'Right', 'Tab'):
        return True
    elif event.char.isdigit():
        current_text = event.widget.get()
        selection_length = len(event.widget.selection_get()) if event.widget.selection_present() else 0
        new_text = current_text[:event.widget.index("insert")] + event.char + current_text[event.widget.index("insert"):]

        # Allow starting to type "09"
        if len(new_text) == 1 and event.char == "0":
            return True
        elif len(new_text) == 2 and new_text.startswith("09"):
            return True

        # Check if the text starts with '09' and respects the maximum length condition
        if new_text.startswith("09") and len(new_text) - selection_length <= 11:
            return True
        else:
            return "break"
    else:
        return "break"

def toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, is_edit_mode):
    if is_edit_mode:
        edit_btn.configure(text="Save", state='disabled', command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, False))
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='normal')
                entry.bind("<KeyRelease>", lambda event, btn=edit_btn, elist=entries_list: on_entry_change(event, btn, elist))
    else:
        edit_btn.configure(text="Edit", command=lambda: toggle_edit_save(Residentframe, edit_btn, entries_list, id_list, True))
        save_edited_data(Residentframe, entries_list, id_list)
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='disabled')
                entry.unbind("<KeyRelease>")

def on_entry_change(event, save_button, entries_list):
    all_valid = True
    for entries in entries_list:
        phone_entry = entries[2]
        if len(phone_entry.get()) < 11:  # Check for valid phone number length
            all_valid = False
            break
    save_button.configure(state='normal' if all_valid else 'disabled')

def save_edited_data(Residentframe, entries_list, id_list):
    for entries, res_id in zip(entries_list, id_list):
        name, address, phone = [entry.get() for entry in entries]
        update_resident_data(Residentframe, res_id, name, address, phone)  # This function needs to be implemented in your db_con module
        save_success(Residentframe)

def save_success(window):
    SaveSucessfr = CTkFrame(window, fg_color="white", width=700, height=300, border_color="#B9BDBD", border_width=2, corner_radius=10)
    SaveSucessfr.place(relx=0.5, rely=0.5, anchor='center')

    # Assuming the function set_icon_image is implemented and ASSETS_PATH is defined correctly
    set_icon_image(SaveSucessfr, 'success_icon.png', relx=0.5, rely=0.15, anchor='n', size=(95, 95))

    LbSuccess = CTkLabel(SaveSucessfr, text="Saved Successfully!", fg_color="transparent", font=("Inter", 35, "bold"), text_color="#333333")
    LbSuccess.place(relx=0.5, rely=0.62, anchor='n')

    # Automatically destroy the frame after 3000 milliseconds (3 seconds)
    SaveSucessfr.after(2500, SaveSucessfr.destroy)

# Call the Resident_page function with appropriate parameters (example usage)
# Resident_page(visitorpage_window, Home_indct, Visitor_indct, Resident_indct, sec_id)
