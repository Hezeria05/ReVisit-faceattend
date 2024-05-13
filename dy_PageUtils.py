from customtkinter import *
from PIL import Image
import os

#_______________________________________GENERAL

def configure_frame(frame, row_weights, column_weights):
    for i, weight in enumerate(row_weights):
        frame.rowconfigure(i, weight=weight, uniform='a')

    for i, weight in enumerate(column_weights):
        frame.columnconfigure(i, weight=weight, uniform='a')

def load_image(file_name, size):
    image_path = os.path.join(os.path.dirname(__file__), 'assets', file_name)
    image = CTkImage(light_image=Image.open(image_path), size=size)
    return image

def validate_length(event, entry, max):
    if len(entry.get()) >= max:
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Delete', 'Tab'):
            return True
        else:
            return "break"
    return True

def validate_full_name(event):
    if event.char.isalpha() or event.char.isdigit() or event.char in (" ", "-", "."):
        return True
    elif event.keysym in ('BackSpace', 'Left', 'Right', 'Tab'):
        return True
    else:
        return "break"

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