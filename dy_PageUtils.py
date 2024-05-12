from customtkinter import *




#_______________________________________dyPAGEREGISTER

def create_standard_label(parent, text):
    # Standard label properties
    font = ("Inter", 18, "bold")
    text_color = "#333333"
    grid_options = {'row': 0, 'column': 0, 'sticky': 'ws', 'padx': 2}

    # Create and configure the label
    label = CTkLabel(parent, text=text, fg_color="transparent", font=font, text_color=text_color)
    label.grid(**grid_options)
    return label

def configure_grid(widget):
    widget.columnconfigure(0, weight=1, uniform='a')
    widget.rowconfigure(1, weight=4, uniform='a')
    widget.rowconfigure((0, 2), weight=2, uniform='a')

def create_standard_entry(parent, placeholder):
    # Standard entry properties
    font = ("Inter", 15)
    corner_radius = 8
    border_width = 1.5
    border_color = '#F47575'
    grid_options = {'row': 1, 'column': 0, 'sticky': 'nsew'}

    # Create and configure the entry
    entry = CTkEntry(parent, placeholder_text=placeholder, font=font,
                     corner_radius=corner_radius, border_width=border_width, border_color=border_color)
    entry.grid(**grid_options)
    return entry

def create_warning_label(parent, text):
    # Standard warning label properties
    font = ("Inter", 12)
    text_color = "red"
    grid_options = {'row': 2, 'column': 0, 'sticky': 'ws', 'padx': 2}

    # Create and configure the warning label
    warning_label = CTkLabel(parent, text=text, fg_color="transparent", font=font, text_color=text_color)
    warning_label.grid(**grid_options)
    return warning_label