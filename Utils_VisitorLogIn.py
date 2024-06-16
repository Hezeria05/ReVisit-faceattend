from customtkinter import *
import cv2
from face_recognition import load_face_data
from dy_PageUtils import (configure_frame, validate_all, view_history,
                          indicate, set_icon_image, validate_no_space)
from face_scan import start_camera
from db_con import insert_visitor_data, fetch_residents
from dy_PageVisitor import Visitor_page
from dy_VisitorLogOut import on_logout_click

# Query Result
def create_button(Searchf, text, row, ResidID, Selectwarn, Invalidwarn, LogPurpose, submitbtn):
    button = CTkButton(Searchf, text=text, font=("Inter", 12.5 , "bold"), fg_color="white", hover_color="#ADCBCF",
                    corner_radius=0, border_width=1, border_color='#C1C1C1', text_color="#333333",
                    command=lambda: set_residid(Searchf, text, ResidID, Selectwarn, Invalidwarn, LogPurpose, submitbtn))
    button.grid(row=row, column=0, sticky="ew")
    return button

def set_residid(Searchf, text, ResidID, Selectwarn, Invalidwarn, LogPurpose, submitbtn):
    ResidID.delete(0, END)
    ResidID.insert(0, text)
    Searchf.place_forget()
    Selectwarn.configure(text="")
    Invalidwarn.configure(text="")
    if LogPurpose.get().strip() != "":
        submitbtn.configure(state="normal")


# Dynamically create buttons based on fetched resident data
def update_search_frame(query, ResidID, Searchf, Selectwarn, Invalidwarn, LogPurpose, submitbtn):
    for widget in Searchf.winfo_children():
        widget.destroy()  # Clear previous buttons

    residents = fetch_residents()
    filtered_residents = [res for res in residents if query.lower() in res[1].lower()]

    if filtered_residents:
        num_residents = len(filtered_residents)
        max_residents = min(num_residents, 5)  # Limit to 8 residents
        button_height = 30
        frame_height = button_height * max_residents

        Searchf.configure(height=frame_height)  # Configure frame height based on number of buttons
        Searchf.place(relx=0.13, rely=0.47, anchor="nw")

        # Adjust row configuration based on the number of filtered residents
        row_config = [1] * max_residents  # Create a list with '1' repeated 'max_residents' times
        configure_frame(Searchf, row_config, [1])

        for i in range(max_residents):
            create_button(Searchf, filtered_residents[i][1], i, ResidID, Selectwarn, Invalidwarn, LogPurpose, submitbtn)
    else:
        Searchf.place_forget()

# Function to show or hide Searchf based on ResidID content
def toggle_search_frame(ResidID, Searchf, Selectwarn, Invalidwarn, LogPurpose, submitbtn):
    query = ResidID.get().strip()
    if query:
        update_search_frame(query, ResidID, Searchf, Selectwarn, Invalidwarn, LogPurpose, submitbtn)
    else:
        Searchf.place_forget()

