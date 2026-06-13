import customtkinter as ctk
from symptoms_db import SymptomsDB


class AddLogFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None

        # DATA
        self.symptoms_dict = {}


        self.layout()
        self.get_symptoms()


    def layout(self):
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["add_log_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=40)

        self.back_to_menu_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.back_to_menu,
            width=50,
        )
        self.back_to_menu_btn.pack(padx=5, pady=35, side="bottom")


    def back_to_menu(self):
        """Reset fields and go back to menu"""
        self.parent.hide_add_log()
        self.parent.show_menu()


    def get_symptoms(self):
        db = SymptomsDB()
        try:
            data = db.get_symptoms()
            if len(data) > 0:
                for symptom in data:
                    self.symptoms_dict[symptom[1]] = symptom[2]
            else:
                pass
        except Exception as e:
            print("Error: ", e)
        print(self.symptoms_dict)