from customtkinter import *
from PIL import Image, ImageTk

app = CTk(fg_color="#E9F3F2")
app.geometry("1200x800+400+100")

# Widgets
mainframe = CTkFrame(master=app, fg_color="#C1C1C1", corner_radius=20)
logoframe = CTkFrame(master=mainframe, fg_color="transparent", corner_radius=20)


image_path = r'C:\Users\grace\Desktop\ReVisit-faceattend\assets\CarltonLOGO.png'
image_orig = Image.open(image_path)
resized_image = image_orig.resize((450, 200))  # Resized to fit within the UI better
image_tk = ImageTk.PhotoImage(resized_image)
imagelogo = CTkLabel(master=logoframe, image=image_tk, text='')
imagelogo.image = image_tk


buttonframe = CTkFrame(master=mainframe, fg_color="transparent", corner_radius=20)
btnregister = CTkButton(
    buttonframe,
    text="REGISTER",
    width=150, height=42,
    corner_radius=10,
    fg_color="#92ACAF",
    hover_color="#ADCBCF",
    font=("Inter", 18, "bold"),
    text_color="#333333")
btnlogin = CTkButton(
    buttonframe,
    text="SIGN IN",
    width=150,
    height=42,
    corner_radius=10,
    fg_color="#92ACAF",
    hover_color="#ADCBCF",
    font=("Inter", 18, "bold"),
    text_color="#333333")
clabel = CTkLabel(logoframe,
    text='CARLTON RESIDENCES, BRGY. DITA, STA. ROSA CITY',
    fg_color="transparent",
    font=("Inter", 18, "bold"),
    text_color="#333333")

# App and frame configuration
app.columnconfigure((0,2), weight=2, uniform='a')
app.columnconfigure(1, weight=10, uniform='a')
app.rowconfigure((0,2), weight=2, uniform='a')
app.rowconfigure(1, weight=10, uniform='a')
mainframe.columnconfigure((0,1,2,3), weight=1, uniform='a')
mainframe.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
buttonframe.columnconfigure((0,1,2,3), weight=1, uniform='a')
buttonframe.rowconfigure((0,3), weight=1, uniform='a')
buttonframe.rowconfigure((1,2), weight=4, uniform='a')
logoframe.grid_columnconfigure((0,1,2), weight=2)
logoframe.grid_rowconfigure((1,2), weight=2)
logoframe.grid_rowconfigure((0), weight=1)


# Grid placement for frames and buttons
mainframe.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
logoframe.grid(row=0, rowspan=3, column=1, columnspan=2, sticky='nsew', padx=10)
imagelogo.grid(row=2, column=1, sticky='nsew')
clabel.grid(row=1, column=1, sticky='nsew')
buttonframe.grid(row=3, rowspan=4, column=1, columnspan=2, sticky='nsew', padx=80)
btnregister.grid(row=2, column=1, columnspan=2, sticky='nsew', padx=50, pady=10)
btnlogin.grid(row=1, column=1, columnspan=2, sticky='nsew',  padx=50, pady=10)

app.mainloop()
