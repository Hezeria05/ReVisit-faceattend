from customtkinter import *
from db_con import fetch_resident_data, update_resident_data
from PageUtils import create_resident_table, toggle_edit_save


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
    entries_list, id_list = create_resident_table(Residentframe, resident_data)
    EditBtn = CTkButton(Residentframe, text="Edit", width=140, height=40, corner_radius=10, fg_color="#ADCBCF", hover_color="#93ACAF",
                        font=("Inter", 17, "bold"), text_color="#333333",
                        command=lambda: toggle_edit_save(Residentframe, EditBtn, entries_list, id_list, True))
    EditBtn.place(relx=0.5, rely=0.928, anchor='n')
