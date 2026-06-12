import customtkinter as ctk
from menu_page import MenuFrame
from settings_page import SettingsFrame
from translator import Translator
from add_symptom_page import AddSymptomFrame
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x470')
        self.title('Symptoms Tracker')
        self.resizable(width=False, height=False)

        # HELPERS
        self.translator = Translator()
        self.translator.set_lang('English')

        # ICONS
        self.back_img = ctk.CTkImage(light_image=Image.open(r'img/go_back.png'))

        # THEME AND FONT
        self.theme = ctk.set_appearance_mode('light')
        self.title_font = ("Helvetica", 25)
        self.button_font = ("Helvetica", 15)
        self.hint_font = ("Helvetica", 12)
        self.back_btn_font = ("Helvetica", 25)

        # PAGES
        self.menu_page = MenuFrame(self)
        self.settings_page = SettingsFrame(self)
        self.add_symptom_page = AddSymptomFrame(self)

        # CHECK IF BUTTONS SHOULD BE ENABLED
        self.menu_page.update_button_states()


        self.show_menu()


    def show_menu(self):
        self.settings_page.pack_forget()
        self.add_symptom_page.pack_forget()
        self.menu_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_menu(self):
            self.menu_page.pack_forget()


    def show_settings(self):
        self.hide_menu()
        self.settings_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_settings(self):
        self.settings_page.pack_forget()


    def show_add_symptom(self):
        self.menu_page.pack_forget()
        self.add_symptom_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_add_symptom(self):
        self.add_symptom_page.pack_forget()





app = App()
app.mainloop()