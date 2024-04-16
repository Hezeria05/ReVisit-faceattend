from customtkinter import *


app = CTk(fg_color="#E9F3F2")
app.geometry("1200x800+400+100")

#widgets
mainframe = CTkFrame(master=app, fg_color="#C1C1C1", corner_radius= 20)
logoframe = CTkFrame(master=mainframe, fg_color="blue", corner_radius= 20)
buttonframe = CTkFrame(master=mainframe, fg_color="transparent", corner_radius= 20)
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
    font=("Istok", 18, "bold"),
    text_color="#333333")


#app column and row
app.columnconfigure((0,2), weight= 2, uniform='a')
app.columnconfigure(1, weight= 10, uniform='a')
app.rowconfigure((0,2), weight= 2, uniform='a')
app.rowconfigure(1, weight= 10, uniform='a')

#mainframe column and row
mainframe.columnconfigure((0,1,2,3), weight= 1, uniform='a')
mainframe.rowconfigure((0,1,2,3,4), weight= 1, uniform='a')

#buttonframe column and row
buttonframe.columnconfigure((0,1,2,3), weight= 1, uniform='a')
buttonframe.rowconfigure((0,3), weight= 1, uniform='a')
buttonframe.rowconfigure((1,2), weight= 4, uniform='a')

#grid
mainframe.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
logoframe.grid(row=0,rowspan=3,column=1, columnspan=2, sticky='nsew', padx = 10, pady=10)
buttonframe.grid(row=3,rowspan=4,column=1, columnspan=2, sticky='nsew', padx=80, pady=20)
btnregister.grid(row=2, column=1, columnspan=2, sticky='nsew', pady=10)
btnlogin.grid(row=1, column=1, columnspan=2, sticky='nsew', pady=10)

app.mainloop()