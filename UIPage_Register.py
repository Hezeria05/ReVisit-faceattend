from customtkinter import *
from PIL import Image, ImageTk

class RegisterPage:
    def __init__(self, app):
        self.app = app
        self.clear_app()
        self.setup_ui()
    
    def clear_app(self):
        # Clear existing widgets
        for widget in self.app.winfo_children():
            widget.destroy()
        self.app.configure(fg_color="#F3FEFD")

    def setup_ui(self):
        self.app.geometry("1200x800+400+100")
        self.app.configure(fg_color="#D7E5E7")
        self.app.title("ReVisit")
        self.app.minsize(800, 400)

        # Configure the root window's grid
        self.app.columnconfigure((0, 1), weight=1, uniform='a')
        self.app.rowconfigure((0,4), weight=1, uniform='a')
        self.app.rowconfigure((1,2,3), weight=3, uniform='a')

        self.main_frame = MainFrame(self.app)
        self.main_frame.grid(row=1, rowspan=3, column=1, sticky='nsew', padx=50, pady=10)

        self.logo_frame = LogoFrame(self.app)  # Pass self.root as a parameter to ButtonFrame
        self.logo_frame.grid(row=2, column=0, sticky='nsew', padx=80)

class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#F0F6F9", corner_radius=20)
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 3, 4), weight=1, uniform='a')
        self.rowconfigure(2, weight=2, uniform='a')

        self.create = CreateFrame(self)
        self.create.pack(expand=True, fill='both', padx=20,pady=20)
class CreateFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="yellow", corner_radius=20)
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 3, 4), weight=1, uniform='a')
        self.rowconfigure(2, weight=2, uniform='a')

        #widgets
        clabel= CTkLabel(self,text='Create Account', fg_color="transparent", font=("Inter", 25, "bold"))
        clabel.pack(side='top', pady=30)

        self.entry = EntryFrame(self)
        self.entry.pack(expand=True, fill='both', padx=20,pady=20)
class EntryFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="green", corner_radius=20)
        createbtn = CTkButton(self, text="Create Account", width=140, height=40, corner_radius=10, fg_color="#92ACAF",
            hover_color="#AECED1", font=("Inter", 17, "bold"), text_color="#333333")
        createbtn.place(relx = 0.6, rely = 0.85)

class LogoFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent", corner_radius=20)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.logo_widgets()

    def logo_widgets(self):
        image_path = r'C:\Users\grace\Desktop\ReVisit-faceattend\assets\CarltonLOGO.png'
        image_orig = Image.open(image_path)
        resized_image = image_orig.resize((450, 180))
        image_tk = ImageTk.PhotoImage(resized_image)

        imagelogo = CTkLabel(master=self, image=image_tk, text='')
        imagelogo.image = image_tk  # Keep a reference
        imagelogo.grid(row=2, column=1, sticky='nsew', pady=20)



    # def register_user(self):
    #     # Handle registration logic
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()
    #     # You would add your registration logic here
    #     print(f"Registering user: {username} with password: {password}")

# Example usage
if __name__ == "__main__":
    app = CTk()
    app.geometry("600x400")
    register_page = RegisterPage(app)
    app.mainloop()
