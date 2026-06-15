import customtkinter as ctk
from menu_page import MenuFrame
from view_entry_page import ViewEntryFrame
from settings_page import SettingsFrame
from translator import Translator
from add_symptom_page import AddSymptomFrame
from add_log_page import AddLogFrame
from view_logs_page import ViewLogsFrame
from edit_entry_page import EditLogFrame
from symptom_list_page import SymptomListFrame
from edit_symptom_page import EditSymptomFrame
from export_brain import DataManager
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # SCREEN SETUP
        self.geometry('400x470')
        self.title('Symptoms Tracker')
        self.resizable(width=False, height=False)

        # FLAGS
        self.has_symptoms = False
        self.has_logs = False

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
        self.label_font = ("Helvetica", 15)

        self.data_manager = DataManager()

        # PAGES
        self.menu_page = MenuFrame(self)
        self.settings_page = SettingsFrame(self)
        self.add_symptom_page = AddSymptomFrame(self)
        self.add_log_page = AddLogFrame(self)
        self.view_logs_page = ViewLogsFrame(self)
        self.view_entry_page = ViewEntryFrame(self)
        self.edit_log_page = EditLogFrame(self)
        self.symptom_list_page = SymptomListFrame(self)
        self.edit_symptoms_page = EditSymptomFrame(self)

        # CHECK IF BUTTONS SHOULD BE ENABLED
        self.menu_page.update_button_states()

        # SHOW MENU PAGE ON START
        self.show_menu()


    def refresh_screen(self):
        self.menu_page.destroy()
        self.menu_page = MenuFrame(self)

        self.settings_page.destroy()
        self.settings_page = SettingsFrame(self)

        self.add_log_page.destroy()
        self.add_symptom_page = AddSymptomFrame(self)

        self.add_log_page.destroy()
        self.add_log_page = AddLogFrame(self)

        self.view_logs_page.destroy()
        self.view_logs_page = ViewLogsFrame(self)

        self.view_entry_page.destroy()
        self.view_entry_page = ViewEntryFrame(self)

        self.edit_log_page.destroy()
        self.edit_log_page = EditLogFrame(self)

        self.symptom_list_page.destroy()
        self.symptom_list_page = SymptomListFrame(self)

        self.edit_symptoms_page.destroy()
        self.edit_symptoms_page = EditSymptomFrame(self)


    def show_menu(self):
        """Show menu page and hide other pages"""
        self.hide_settings()
        self.hide_add_symptom()
        self.menu_page.update_button_states()
        self.menu_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_menu(self):
        """hide menu page"""
        self.menu_page.pack_forget()


    def show_settings(self):
        """Show settings page and hide menu page"""
        self.hide_menu()
        self.hide_symptoms_list_page()
        self.settings_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_settings(self):
        """hide settings page"""
        self.settings_page.pack_forget()


    def show_add_symptom(self):
        """Show add symptom page and hide menu page"""
        self.menu_page.pack_forget()
        self.add_symptom_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_add_symptom(self):
        """hide add symptom page"""
        self.add_symptom_page.pack_forget()


    def show_add_log(self):
        """Hide menu and show add log"""
        self.menu_page.pack_forget()
        self.refresh_screen()
        self.add_log_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_add_log(self):
        """hide add log"""
        self.add_log_page.pack_forget()


    def show_view_logs(self):
        self.menu_page.pack_forget()
        self.refresh_screen()
        self.view_logs_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_show_logs(self):
        self.view_logs_page.pack_forget()


    def show_view_entry(self):
        self.hide_show_logs()
        self.view_entry_page.log_data = self.view_logs_page.view_log()
        self.view_entry_page.layout()
        self.view_entry_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_view_entry(self):
        self.refresh_screen()
        self.view_entry_page.pack_forget()


    def show_edit_log(self):
        self.hide_show_logs()
        self.edit_log_page.log_data = self.view_logs_page.view_log()
        self.edit_log_page.get_log_and_details_ids()
        self.edit_log_page.layout()
        self.edit_log_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_edit_log(self):
        self.refresh_screen()
        self.edit_log_page.pack_forget()


    def show_symptoms_list_page(self):
        self.refresh_screen()
        self.settings_page.pack_forget()
        self.symptom_list_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_symptoms_list_page(self):
        self.symptom_list_page.pack_forget()


    def show_edit_symptoms_page(self):
        self.hide_symptoms_list_page()
        self.edit_symptoms_page.layout()
        self.edit_symptoms_page.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_edit_symptoms_page(self):
        self.refresh_screen()
        self.edit_symptoms_page.pack_forget()
        self.show_symptoms_list_page()



app = App()
app.mainloop()