import customtkinter as ctk
from symptoms_db import SymptomsDB


class AddSymptomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.symptom_name_label = None
        self.symptom_name_entry = None
        self.symptom_type_label = None
        self.symptom_type_entry = None
        self.add_btn = None


        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["add_symptom_title"],
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

        self.symptom_name_label = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["add_symptom_name"],
            font=self.parent.label_font,
        )
        self.symptom_name_label.pack(padx=5, pady=5)

        self.symptom_name_entry = ctk.CTkEntry(
            self,
            width=250,
        )
        self.symptom_name_entry.pack(padx=5, pady=5)

        self.symptom_type_label = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["type"],
            font=self.parent.label_font,
        )
        self.symptom_type_label.pack(padx=5, pady=5)

        values = [
            self.parent.translator.dictionary["scale"],
            self.parent.translator.dictionary["yes_no"],
            self.parent.translator.dictionary["text"],
        ]

        self.symptom_type_entry = ctk.CTkOptionMenu(
            self,
            values=values,
            width=250,
        )
        self.symptom_type_entry.set(self.parent.translator.dictionary["choose"])
        self.symptom_type_entry.pack(padx=5, pady=5)

        self.add_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["add_symptom"],
            font=self.parent.button_font,
            width=250,
            command=self.add_symptom,
        )
        self.add_btn.pack(padx=5, pady=15)


    def back_to_menu(self):
        """Reset fields and go back to menu"""
        self.reset_options()
        self.parent.show_menu()


    def reset_options(self):
        """Reset fields"""
        if self.symptom_type_entry is not None:
            self.symptom_type_entry.set(self.parent.translator.dictionary["choose"])
        if self.symptom_name_entry is not None:
            self.symptom_name_entry.delete(0, "end")


    def add_symptom(self):
        """Add a new symptom to the database"""
        name_filled = self.symptom_name_entry.get().strip() != ""
        type_selected = self.symptom_type_entry.get() != self.parent.translator.dictionary["choose"]
        if name_filled and type_selected:
            db = SymptomsDB()
            try:
                symptom_name = self.symptom_name_entry.get()
                symptom_type = self.symptom_type_entry.get()
                db.add_symptom(symptom_name, symptom_type)
                self.reset_options()
                self.parent.has_symptoms = True
            except Exception as e:
                print("Error: ", e)
        else:
            pass
