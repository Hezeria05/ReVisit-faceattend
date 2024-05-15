from customtkinter import *
from dy_PageUtils import configure_frame, update_datetime, load_image
from VisitorFaceReg import on_register_click
from VisitorLogIn import on_login_click
from VisitorLogOut import on_logout_click
from db_con import count_logged_in, count_logged_out, count_total_today

def create_frame(parent, row, column, rowspan=1, columnspan=1, fg_color="#C6DFDD", border_width=1, border_color="#BFC3C3", height=None):
    if height is None:
        frame = CTkFrame(parent, fg_color=fg_color, border_width=border_width, border_color=border_color)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", pady=10)
    else:
        frame = CTkFrame(parent, fg_color=fg_color, border_width=border_width, border_color=border_color, height=height)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="new", pady=10)
    return frame

def create_inner_frame(parent, row, column, columnspan=1, rowspan=1, fg_color="white", padx=2, pady=5):
    inner_frame = CTkFrame(parent, fg_color=fg_color)
    inner_frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=padx, pady=pady)
    return inner_frame

def Home_page(homepage_window, Home_indct, Visitor_indct, Resident_indct):
    logged_in_count = count_logged_in()
    logged_out_count = count_logged_out()
    total_count = count_total_today()
    Homeframe = CTkFrame(homepage_window, fg_color="white")
    Homeframe.grid(row=1, column=1, sticky="nsew")
    configure_frame(Homeframe, [1, 3, 3, 9, 3, 1], [1, 6, 1, 6, 1, 6, 1])

    HeadingF = create_frame(Homeframe, row=1, column=1, columnspan=2, height=60)
    DateTimeF = create_frame(Homeframe, row=1, column=5)
     # Configure date and time display
    time_label = CTkLabel(DateTimeF, fg_color="transparent", text="", font=("Arial", 28, "bold"), text_color="#333333")
    time_label.place(relx=0.3, rely=0.22, anchor="n")
    date_label = CTkLabel(DateTimeF, fg_color="transparent", text="", font=("Inter", 14, "bold"), text_color="#333333")
    date_label.place(relx=0.265, rely=0.52, anchor="n")
    calimage = load_image('calendar_icon.png', (75, 75))
    calendar = CTkLabel(DateTimeF, image=calimage, text="")
    calendar.place( relx=0.75, rely=0.09, anchor='n')


    # Update date and time periodically
    update_datetime(date_label, time_label)
    homepage_window.after(1000, lambda: update_datetime(date_label, time_label))

#__________________________________________________________
    TotalVisitF = create_frame(Homeframe, row=2, column=1)
    Totallabel = CTkLabel(TotalVisitF, fg_color="transparent", text="Total Number of Visitors Today", 
                          font=("Arial", 20, "bold"), text_color="#333333")
    Totallabel.place(relx=0.5, rely=0.125, anchor="n")
    TotalV = CTkLabel (TotalVisitF, text=str(total_count), font=("Arial", 30, "bold"), text_color="#00507E")
    TotalV.place(relx=0.5, rely=0.5, anchor="n")

    # Register Visitor Section
    RegisterVisitF = create_frame(Homeframe, row=3, column=1)
    configure_frame(RegisterVisitF, [1, 2, 8, 2, 3, 1], [1, 1, 6, 1, 1])
    regheading = create_inner_frame(RegisterVisitF, row=1, column=2)
    regicon = create_inner_frame(RegisterVisitF, row=2, column=2, padx=0, pady=0)
    regbtn = create_inner_frame(RegisterVisitF, row=4, column=1, columnspan=3, padx=20, pady=0)

    # Log in Visitor Section
    invisit = create_frame(Homeframe, row=4, column=3)
    configure_frame(invisit, [1], [1])
    invframe = create_inner_frame(invisit, row=0, column=0, padx=15, pady=15)

    LoginVisitF = create_frame(Homeframe, row=3, column=3)
    configure_frame(LoginVisitF, [1, 2, 8, 2, 3, 1], [1, 1, 6, 1, 1])
    loginheading = create_inner_frame(LoginVisitF, row=1, column=2)
    loginicon = create_inner_frame(LoginVisitF, row=2, column=2, padx=0, pady=0)
    loginbtn = create_inner_frame(LoginVisitF, row=4, column=1, columnspan=3, padx=20, pady=0)

    # Log out Visitor Section
    outvisit = create_frame(Homeframe, row=4, column=5)
    configure_frame(outvisit, [1], [1])
    outvframe = create_inner_frame(outvisit, row=0, column=0, padx=15, pady=15)

    LogoutVisitF = create_frame(Homeframe, row=3, column=5)
    configure_frame(LogoutVisitF, [1, 2, 8, 2, 3, 1], [1, 1, 6, 1, 1])
    logoutheading = create_inner_frame(LogoutVisitF, row=1, column=2)
    logouticon = create_inner_frame(LogoutVisitF, row=2, column=2, padx=0, pady=0)
    logoutbtn = create_inner_frame(LogoutVisitF, row=4, column=1, columnspan=3, padx=20, pady=0)