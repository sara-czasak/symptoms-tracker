import customtkinter as ctk
from menu_page import MenuFrame
from translator import Translator


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x470')
        self.title('Symptoms Tracker')
        self.resizable(width=False, height=False)

        # HELPERS
        self.translator = Translator()
        self.translator.set_lang('English')

        # PAGES
        self.menu_page = MenuFrame(self)


        self.show_menu()


    def show_menu(self):
        self.menu_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_menu(self):
            self.menu_page.pack_forget()





app = App()
app.mainloop()