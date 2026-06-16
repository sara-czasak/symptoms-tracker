import customtkinter as ctk
from symptoms_db import SymptomsDB


class LangFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_settings_btn = None

        # WIDGET GROUP
        self.lang_btns = {}

        # DATA
        self.available_lags = [
            "English",
            "Polski"
        ]

        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["lang_title"],
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

        for i in self.available_lags:
            option = ctk.CTkButton(
                self,
                text=i,
                command=lambda lang=i: self.get_lang_and_back_to_settings(lang),
                font=self.parent.button_font
            )
            option.pack(padx=5, pady=5, fill="both")
            self.lang_btns[i] = option


    def get_lang_and_back_to_settings(self, lang):
        db = SymptomsDB()
        try:
            db.update_lang(lang)
        except Exception as e:
            print("Error: ", e)
        self.parent.translator.set_lang(lang)
        self.parent.show_settings()