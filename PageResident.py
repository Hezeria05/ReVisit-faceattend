from customtkinter import *
from db_con import fetch_resident_data, update_resident_data
from PageUtils import create_resident_table, toggle_edit_save

def update_table_display(Residentframe, offset, entries_list, id_list):
    """Update the table display based on the given offset."""
    new_data = fetch_resident_data(offset)
    if not new_data:
        return False, entries_list, id_list  # Return current lists if no more data to display

    # Clear existing entries in the UI
    for entries in entries_list:
        for entry in entries:
            entry.destroy()

    # Create new entries with the updated data
    entries_list, id_list = create_resident_table(Residentframe, new_data)
    return True, entries_list, id_list


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
    RTRows = CTkFrame (Residentframe, width=960, height=210, fg_color="white", corner_radius=0, border_color="#B9BDBD", border_width=0)
    RTRows.place(relx=0.5, rely=0.65, anchor="center")

    # Pagination controls
    current_offset = 0

    next_button = CTkButton(Residentframe, text="Next",width=50, height=40, corner_radius=10, fg_color="transparent", hover_color="#F6FCFC",
                        font=("Inter", 17, "bold"), text_color="#333333", command=lambda: navigate("next"))
    next_button.place(relx=0.9, rely=0.9, anchor="center")
    back_button = CTkButton(Residentframe, text="Back",width=50, height=40, corner_radius=10, fg_color="transparent", hover_color="#F6FCFC",
                        font=("Inter", 17, "bold"), text_color="#333333", command=lambda: navigate("back"))
    back_button.place(relx=0.8, rely=0.9, anchor="center")
    back_button.configure(state='disabled')  # Initially disabled

    def navigate(direction):
        nonlocal current_offset, entries_list, id_list
        if direction == "next":
            new_offset = current_offset + 15
        elif direction == "back":
            new_offset = max(0, current_offset - 15)

        updated, new_entries_list, new_id_list = update_table_display(Residentframe, new_offset, entries_list, id_list)
        if updated:
            entries_list, id_list = new_entries_list, new_id_list
            current_offset = new_offset
            back_button.configure(state='normal' if current_offset > 0 else 'disabled')
            if not fetch_resident_data(current_offset + 15):
                next_button.configure(state='disabled')
            else:
                next_button.configure(state='normal')

            # Reset Edit button to initial state when new data is loaded
            EditBtn.configure(text="Edit", command=lambda: toggle_edit_save(Residentframe, EditBtn, entries_list, id_list, True))
        else:
            next_button.configure(state='disabled')
        # Initial data display
    # Ensure initial data fetch is always called with an offset
    resident_data = fetch_resident_data(0)
    entries_list, id_list = create_resident_table(Residentframe, resident_data)
    EditBtn = CTkButton(Residentframe, text="Edit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 17, "bold"), text_color="#333333",
                        command=lambda: toggle_edit_save(Residentframe, EditBtn, entries_list, id_list, True))
    EditBtn.place(relx=0.5, rely=0.87, anchor='n')