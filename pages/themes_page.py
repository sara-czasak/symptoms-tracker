import customtkinter as ctk
from symptoms_db import SymptomsDB
from CTkMessagebox import CTkMessagebox


class ThemeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_settings_btn = None

        # WIDGET GROUP
        self.theme_btns = {}

        # DATA
        self.available_themes = [
            "green",
            "blue",
            "purple",
            'red'
        ]

        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["theme_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=40)

        self.back_to_settings_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_settings,
            width=50,
        )
        self.back_to_settings_btn.pack(padx=5, pady=35, side="bottom")

        for i in self.available_themes:
            option = ctk.CTkButton(
                self,
                text=i,
                command=lambda theme=i: self.get_lang_and_back_to_settings(theme),
                font=self.parent.button_font
            )
            option.pack(padx=5, pady=5, fill="both")
            self.theme_btns[i] = option


    def get_lang_and_back_to_settings(self, theme):
        db = SymptomsDB()
        try:
            db.update_theme(theme)
            CTkMessagebox(
                self,
                title=self.parent.translator.dictionary["theme_title_success"],
                message=self.parent.translator.dictionary["theme_message_success"],
            )
        except Exception as e:
            print("Error: ", e)
            CTkMessagebox(
                self,
                title=self.parent.translator.dictionary["failed_save_title"],
                message=self.parent.translator.dictionary["theme_message_fail"],
            )
        self.parent.theme = ctk.set_default_color_theme(f'./themes/{theme}.json')
        self.parent.show_settings()