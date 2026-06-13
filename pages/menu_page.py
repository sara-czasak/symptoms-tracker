import customtkinter as ctk
from symptoms_db import SymptomsDB


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.add_log_btn = None
        self.analysis_btn = None
        self.view_entries_btn = None
        self.settings_btn = None
        self.about_btn = None
        self.add_symptoms_btn = None
        self.exit_btn = None


        # BUILD PAGE
        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["menu_page_title"],
            font=self.parent.title_font
        )
        self.page_title.pack(padx=5, pady=15)

        self.add_log_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["add_log"],
            font=self.parent.button_font,
            command=self.parent.show_add_log,
        )
        self.add_log_btn.pack(padx=5, pady=5)

        self.analysis_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["analysis_btn"],
            font=self.parent.button_font,
        )
        self.analysis_btn.pack(padx=5, pady=5)

        self.view_entries_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["view_entries_btn"],
            font=self.parent.button_font,
        )
        self.view_entries_btn.pack(padx=5, pady=5)

        self.add_symptoms_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["add_symptoms_btn"],
            font=self.parent.button_font,
            command=self.parent.show_add_symptom,
        )
        self.add_symptoms_btn.pack(padx=5, pady=5)

        self.settings_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["settings_btn"],
            font=self.parent.button_font,
            command=self.parent.show_settings,
        )
        self.settings_btn.pack(padx=5, pady=5)

        self.about_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["about_btn"],
            font=self.parent.button_font,
        )
        self.about_btn.pack(padx=5, pady=5)

        self.exit_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["exit_btn"],
            font=self.parent.button_font,
            command=self.parent.destroy,
        )
        self.exit_btn.pack(padx=5, pady=5)


    def update_button_states(self):
        """Check if symptoms exist and enable/disable buttons"""
        db = SymptomsDB()
        try:
            self.parent.has_symptoms = db.check_if_symptoms()
        except Exception as e:
            print("Error: ", e)
        if self.parent.has_symptoms:
            self.add_log_btn.configure(state="normal")
        else:
            self.add_log_btn.configure(state="disabled")

        if self.parent.has_logs:
            self.analysis_btn.configure(state="normal")
            self.view_entries_btn.configure(state="normal")
        else:
            self.analysis_btn.configure(state="disabled")
            self.view_entries_btn.configure(state="disabled")