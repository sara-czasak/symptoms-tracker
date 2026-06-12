import customtkinter as ctk


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

        # FLAGS
        self.has_data = False

        self.layout()


    def layout(self):
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["menu_page_title"],
            font=self.parent.title_font
        )
        self.page_title.pack(padx=5, pady=30)

        self.add_log_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["add_log"],
            font=self.parent.button_font,
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
        )
        self.add_symptoms_btn.pack(padx=5, pady=5)

        self.settings_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["settings_btn"],
            font=self.parent.button_font,
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
        )
        self.exit_btn.pack(padx=5, pady=5)


    def update_button_states(self):
        if self.has_data:
            self.add_log_btn.configure(state="normal")
            self.analysis_btn.configure(state="normal")
            self.view_entries_btn.configure(state="normal")
        else:
            self.add_log_btn.configure(state="disabled")
            self.analysis_btn.configure(state="disabled")
            self.view_entries_btn.configure(state="disabled")