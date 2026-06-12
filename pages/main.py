import customtkinter as ctk
from menu_page import MenuFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x470')
        self.title('Symptoms Tracker')
        self.resizable(width=False, height=False)

        # PAGES
        self.menu_page = MenuFrame(self)


        def show_menu(self):
            self.menu_frame.pack(padx=15, pady=15, fill="both", expand=True)


        def hide_menu(self):
            self.menu_frame.pack_forget()





app = App()
app.mainloop()