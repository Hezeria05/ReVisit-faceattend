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

        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.rowconfigure((0, 2), weight=2, uniform='a')


    def register_user(self):
        # Handle registration logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        # You would add your registration logic here
        print(f"Registering user: {username} with password: {password}")

# Example usage
if __name__ == "__main__":
    app = CTk()
    app.geometry("600x400")
    register_page = RegisterPage(app)
    app.mainloop()
