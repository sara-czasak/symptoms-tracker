import customtkinter as ctk
from symptoms_db import SymptomsDB


class SymptomListFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_settings_btn = None

        # DATA
        self.symptoms_dict = {}

        self.layout()


    def layout(self):
        """Build page layout"""
        self.get_symptoms()

        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["sympt_list_title"],
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


    def get_symptoms(self):
        """Return list of symptoms"""
        db = SymptomsDB()
        try:
            symptoms = db.get_symptoms()
            for i in symptoms:
                self.symptoms_dict[i[1]] = i[2]
        except Exception as e:
            print("Error: ", e)