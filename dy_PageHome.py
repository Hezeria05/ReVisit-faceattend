from customtkinter import *
from dy_PageUtils import configure_frame, update_datetime, load_image
from dy_VisitorFaceReg import on_register_click
from dy_VisitorLogIn import on_login_click
from dy_VisitorLogOut import on_logout_click
from db_con import count_logged_in, count_logged_out, count_total_today

def create_frame(parent, row, column, rowspan=1, columnspan=1, fg_color="#E9F3F2", border_width=2, 
                 border_color="#BFC3C3", height=None, padx=None,pady=10, corner_radius=None):
    if height is None:
        frame = CTkFrame(parent, fg_color=fg_color, border_width=border_width, border_color=border_color, corner_radius=corner_radius)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=padx ,pady=pady)
    else:
        frame = CTkFrame(parent, fg_color=fg_color, height=height, corner_radius=corner_radius)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="new", padx=padx ,pady=pady)
    return frame

def create_inner_frame(parent, row, column, columnspan=1, rowspan=1, fg_color="white", padx=2, pady=5):
    inner_frame = CTkFrame(parent, fg_color=fg_color)
    inner_frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=padx, pady=pady)
    return inner_frame

def create_section(parent, row, column, text, image_path, button_text, button_command):
    frame = create_frame(parent, row=row, column=column)
    configure_frame(frame, [1, 2, 8, 2, 3, 1], [1, 1, 6, 1, 1])

    heading_frame = create_inner_frame(frame, row=1, column=2, fg_color="transparent")
    label = CTkLabel(heading_frame, fg_color="transparent", text=text, font=("Arial", 28, "bold"), text_color="#333333")
    label.place(relx=0.5, rely=0.5, anchor="center")

    icon_frame = create_inner_frame(frame, row=2, column=2, padx=0, pady=0)
    image = load_image(image_path, (135, 135))
    icon_label = CTkLabel(icon_frame, image=image, text="")
    icon_label.place(relx=0.5, rely=0.5, anchor='center')

    button_frame = create_inner_frame(frame, row=4, column=1, columnspan=3, padx=20, pady=0, fg_color="transparent")
    configure_frame(button_frame, [1], [1])
    button = CTkButton(button_frame, text=button_text, font=("Inter", 25, "bold"), hover_color="#93ACAF", text_color="#333333", 
                       width=220, height=40, fg_color="#ADCBCF", corner_radius=5, command=button_command)
    button.grid(row=0, column=0, sticky="nsew")

    return frame

def Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, home_button, visitor_button, resident_button):
    home_button.configure(state="normal")
    visitor_button.configure(state="normal")
    resident_button.configure(state="normal")
    logout_btn.configure(state="normal")
    logged_in_count = count_logged_in()
    logged_out_count = count_logged_out()
    total_count = count_total_today()
    Homeframe = CTkFrame(homepage_window, fg_color="white", border_width=1, border_color="#C1C1C1", corner_radius=0)
    Homeframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Homeframe, [1, 4, 12, 3, 1], [1, 6, 1, 6, 1, 6, 1])

    HeadingF = create_frame(Homeframe, row=1, column=1, columnspan=3, fg_color="transparent", height=60)
    configure_frame(HeadingF, [1], [1])
    HomeHeading = CTkLabel(HeadingF, text="Welcome to Home Page!", font=("Inter", 45, "bold"), fg_color="transparent",text_color="#333333" )
    HomeHeading.grid(row=0, column=0, sticky="nw")
    DateTimeF = create_frame(Homeframe, row=1, column=5, corner_radius=5)

    # Configure date and time display
    time_label = CTkLabel(DateTimeF, fg_color="transparent", text="", font=("Arial", 30, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(DateTimeF, fg_color="transparent", text="", font=("Inter", 16, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.55, anchor="n")
    calimage = load_image('calendar_icon.png', (75, 75))
    calendar = CTkLabel(DateTimeF, image=calimage, text="")
    calendar.place(relx=0.75, rely=0.5, anchor='center')

    # Update date and time periodically
    update_datetime(date_label, time_label)
    homepage_window.after(1000, lambda: update_datetime(date_label, time_label))

    # Register Visitor Section
    register_command = lambda: on_register_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, None, logout_btn, Home_page, home_button, visitor_button, resident_button)
    create_section(Homeframe, row=2, column=1, text="REGISTER", image_path='register_icon.png', button_text="REGISTER", button_command=register_command)
    TotalVisitF = create_frame(Homeframe, row=3, column=1, pady = 1)
    configure_frame(TotalVisitF, [1], [1])
    TVframe = create_inner_frame(TotalVisitF, row=0, column=0, padx=15, pady=15)
    configure_frame(TVframe, [3,3], [1,1,1])
    Totallabel = CTkLabel(TVframe, fg_color="transparent", text="Total Number of Visitors Today", font=("Arial", 18, "bold"), text_color="#333333")
    Totallabel.grid(row=0, column=0, columnspan=2, sticky="nw", padx=7, pady=4)
    TotalV = CTkLabel(TVframe, text=str(total_count), font=("Arial", 30, "bold"), text_color="#00507E")
    TotalV.place(relx=0.5, rely=0.65, anchor="center")

    # Log in Visitor Section
    login_command = lambda: on_login_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, Home_page, home_button, visitor_button, resident_button)
    create_section(Homeframe, row=2, column=3, text="LOGIN", image_path='login_icon.png', button_text="LOGIN", button_command=login_command)
    invisit = create_frame(Homeframe, row=3, column=3, pady = 1)
    configure_frame(invisit, [1], [1])
    invframe = create_inner_frame(invisit, row=0, column=0, padx=15, pady=15)
    configure_frame(invframe, [3,3], [1,1,1])
    Activelbl = CTkLabel(invframe, fg_color="transparent", text="Entered Visitors", font=("Arial", 21, "bold"), text_color="#333333")
    Activelbl.grid(row=0, column=0, columnspan=2, sticky="nw", padx=7, pady=4)
    actiV = CTkLabel(invframe, text=str(logged_in_count), font=("Arial", 30, "bold"), text_color="#00507E")
    actiV.place(relx=0.5, rely=0.65, anchor="center")



    # Log out Visitor Section
    logout_command = lambda: on_logout_click(homepage_window, Home_indct, Visitor_indct, Resident_indct, sec_id, logout_btn, Home_page, home_button, visitor_button, resident_button)
    create_section(Homeframe, row=2, column=5, text="LOGOUT", image_path='logout_icon.png', button_text="LOGOUT", button_command=logout_command)
    outvisit = create_frame(Homeframe, row=3, column=5, pady = 1)
    configure_frame(outvisit, [1], [1])
    outvframe = create_inner_frame(outvisit, row=0, column=0, padx=15, pady=15)
    configure_frame(outvframe, [3,3], [1,1,1])
    Departedlbl = CTkLabel(outvframe, fg_color="transparent", text="Exited Visitors", font=("Arial", 21, "bold"), text_color="#333333")
    Departedlbl.grid(row=0, column=0, columnspan=2, sticky="nw", padx=7, pady=4)
    departV = CTkLabel(outvframe, text=str(logged_out_count), font=("Arial", 30, "bold"), text_color="#00507E")
    departV.place(relx=0.5, rely=0.65, anchor="center")
