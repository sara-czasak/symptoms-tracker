import customtkinter as ctk


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.symptoms_list_btn = None
        self.export_btn = None
        self.lang_btn = None
        self.theme_btn = None


        # BUILD PAGE
        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["settings_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=40)

        self.symptoms_list_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["see_symptoms"],
            font=self.parent.button_font,
            command=self.parent.show_symptoms_list_page,
        )
        self.symptoms_list_btn.pack(padx=5, pady=5, fill="both")

        self.back_to_menu_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_menu,
            width=50,
        )
        self.back_to_menu_btn.pack(padx=5, pady=35, side="bottom")

        self.export_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["export_btn"],
            font=self.parent.button_font,
        )
        self.export_btn.pack(padx=5, pady=5, fill="both")

        self.lang_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["lang_btn"],
            font=self.parent.button_font,
        )
        self.lang_btn.pack(padx=5, pady=5, fill="both")

        self.theme_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["theme_btn"],
            font=self.parent.button_font,
        )
        self.theme_btn.pack(padx=5, pady=5, fill="both")




