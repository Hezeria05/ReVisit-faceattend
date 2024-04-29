from customtkinter import *
from db_con import fetch_resident_data, update_resident_data

def on_entry_change(event, save_button):
    save_button.configure(state='normal')

def toggle_edit_save(edit_btn, entries_list, is_edit_mode):
    if is_edit_mode:
        # Switch to save mode and disable save button
        edit_btn.configure(text="Save", state='disabled', command=lambda: toggle_edit_save(edit_btn, entries_list, False))
        # Enable entries for editing and bind change detection
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='normal')
                entry.bind("<KeyRelease>", lambda event, btn=edit_btn: on_entry_change(event, btn))
    else:
        # Switch to edit mode
        edit_btn.configure(text="Edit", command=lambda: toggle_edit_save(edit_btn, entries_list, True))
        # Save data and disable entries
        save_edited_data(entries_list)
        for entries in entries_list:
            for entry in entries:
                entry.configure(state='disabled')
                entry.unbind("<KeyRelease>")

def save_edited_data(entries_list):
    new_data = []
    for entries in entries_list:
        row_data = [entry.get() for entry in entries]
        new_data.append(row_data)
    update_resident_data(new_data)  # This function needs to be implemented in your db_con module

def create_resident_table(Residentframe, resident_data):
    entries_list = []
    for i in range(18):  # Assuming 18 rows maximum
        y_offset = 0.234 + (i * 0.0375)
        entries = []
        for j in range(3):  # Assuming 3 columns
            entry = CTkEntry(Residentframe, width=320, height=30, fg_color="white", corner_radius=0, border_width=1)
            entry.place(relx=0.0465 + (j * 0.302), rely=y_offset)
            entries.append(entry)
        if i < len(resident_data):
            for entry, value in zip(entries, resident_data[i]):
                entry.insert(0, value if value is not None else "")
            for entry in entries:
                entry.configure(state='disabled')
        else:
            for entry in entries:
                entry.configure(state='disabled')
        entries_list.append(entries)
    return entries_list

def Resident_page(homepage_window):
    Residentframe = CTkFrame(homepage_window, fg_color="#F6FCFC", width=1057, height=715)
    Residentframe.place(relx=0.266, rely=0.118)
    ResidentHeading = CTkLabel(Residentframe, text="Resident's List", font=("Inter", 35, "bold"), text_color="#333333")
    ResidentHeading.place(relx=0.043, rely=0.06)
    RTCols = CTkFrame (Residentframe, width=960, height=50, fg_color="#93ACAF", corner_radius=0, border_color="#B9BDBD", border_width=1)
    RTCols.place(relx=0.5, rely=0.2, anchor="center")
    headings = {"Name": 0.25, "Address": 0.5, "Phone Number": 0.75}
    column_width = 1 / len(headings)
    for i, (heading, position) in enumerate(headings.items()):
        heading_label = CTkLabel(RTCols, text=heading, font=("Inter", 14, "bold"), text_color="white", fg_color="transparent")
        x_position = column_width * (i + 0.5)
        heading_label.place(relx=x_position, rely=0.5, anchor="center")
    RTRows = CTkFrame (Residentframe, width=960, height=380, fg_color="white", corner_radius=0, border_color="#B9BDBD", border_width=0)
    RTRows.place(relx=0.5, rely=0.65, anchor="center")
    resident_data = fetch_resident_data()
    entries_list = create_resident_table(Residentframe, resident_data)
    EditBtn = CTkButton(Residentframe, text="Edit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 17, "bold"), text_color="#333333", command=lambda: toggle_edit_save(EditBtn, entries_list, True))
    EditBtn.place(relx=0.5, rely=0.928, anchor='n')
