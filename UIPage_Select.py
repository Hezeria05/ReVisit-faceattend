from customtkinter import *
from PIL import Image, ImageTk


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("1200x800+400+100")
        self.root.configure(fg_color="#F3FEFD")
        self.root.title("ReVisit")
        self.root.minsize(800, 400)

        # Configure the root window's grid
        self.root.columnconfigure((0, 2), weight=2, uniform='a')
        self.root.columnconfigure(1, weight=10, uniform='a')
        self.root.rowconfigure((0, 2), weight=2, uniform='a')
        self.root.rowconfigure(1, weight=10, uniform='a')

        self.main_frame = MainFrame(self.root)
        self.main_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

        self.button_frame = ButtonFrame(self.main_frame, self.root)  # Pass self.root as a parameter to ButtonFrame
        self.button_frame.grid(row=3, rowspan=2, column=1, columnspan=2, sticky='nsew', padx=80)

class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#E4E4E4", corner_radius=20)
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 3, 4), weight=1, uniform='a')
        self.rowconfigure(2, weight=2, uniform='a')
        self.setup_logo = LogoFrame(self)
        self.setup_logo.grid(row=0, rowspan=3, column=1, columnspan=2, sticky='nsew', padx=10)
        self.setup_button = ButtonFrame(self, parent)  # Pass the parent to ButtonFrame for register_page
        self.setup_button.grid(row=3, column=1, columnspan=2, padx=80)

class LogoFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent", corner_radius=20)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.logo_widgets()

    def logo_widgets(self):
        image_path = r'C:\Users\grace\Desktop\ReVisit-faceattend\assets\CarltonLOGO.png'
        image_orig = Image.open(image_path)
        resized_image = image_orig.resize((450, 200))
        image_tk = ImageTk.PhotoImage(resized_image)

        imagelogo = CTkLabel(master=self, image=image_tk, text='')
        imagelogo.image = image_tk  # Keep a reference
        imagelogo.grid(row=2, column=1, sticky='nsew', pady=20)

        clabel = CTkLabel(self, text='CARLTON RESIDENCES, BRGY. DITA, STA. ROSA CITY',
                          fg_color="transparent", font=("Inter", 20, "bold"), text_color="#333333")
        clabel.grid(row=1, column=1, sticky='nsew')

class ButtonFrame(CTkFrame):
    def __init__(self, parent, root_window):
        super().__init__(parent, fg_color="transparent", corner_radius=20)
        self.root_window = root_window
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 3), weight=1, uniform='a')
        self.rowconfigure((1, 2), weight=2, uniform='a')
        self.button_widgets()

    def button_widgets(self):
        btnlogin = CTkButton(self, text="SIGN IN", width=285, height=60, corner_radius=10, fg_color="#92ACAF",
            hover_color="#AECED1", font=("Inter", 18, "bold"), text_color="#333333")
        btnlogin.pack(side='top', padx=10)
        btnregister = CTkButton(self, text="REGISTER", width=285, height=60, corner_radius=10, fg_color="#92ACAF",
            hover_color="#AECED1", font=("Inter", 18, "bold"), text_color="#333333")
        btnregister.pack(side='top', padx=10, pady=10)




if __name__ == "__main__":
    app = CTk()
    main_app = MainApplication(app)

    app.mainloop()
