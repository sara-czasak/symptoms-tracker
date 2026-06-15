import customtkinter as ctk
from symptoms_db import SymptomsDB
from CTkListbox import *


class SymptomListFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_settings_btn = None
        self.symptom_options_menu = None
        self.select_option_btn = None
        self.listbox = None
        self.frm = None

        # DATA
        self.symptoms_dict = {}
        self.options = [
            self.parent.translator.dictionary['edit_sympt'],
            self.parent.translator.dictionary['delete_sympt'],
        ]

        self.layout()


    def layout(self):
        """Build page layout"""
        self.get_symptoms()

        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["sympt_list_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=15)

        self.back_to_settings_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_settings,
            width=50,
        )
        self.back_to_settings_btn.pack(padx=5, pady=35, side="bottom")

        self.frm = ctk.CTkFrame(
            self
        )
        self.frm.grid_columnconfigure([0, 1], weight=1)
        self.frm.pack(padx=5, pady=5)

        self.symptom_options_menu = ctk.CTkOptionMenu(
            self.frm,
            values=self.options,
        )
        self.symptom_options_menu.set(self.parent.translator.dictionary['opt'])
        self.symptom_options_menu.grid(row=0, column=0, sticky="e", padx=5)

        self.select_option_btn = ctk.CTkButton(
            self.frm,
            text=self.parent.translator.dictionary['confirm'],
            font=self.parent.button_font,
            command=self.make_choice,
        )
        self.select_option_btn.grid(row=0, column=1, sticky="w", padx=5)

        self.listbox = CTkListbox(
            self,
            height=170,
        )
        self.listbox.pack(padx=5, pady=5, fill="both", expand=True)

        for k, v in self.symptoms_dict.items():
            self.listbox.insert("end", f"{k.title()}: {v}")


    def get_symptoms(self):
        """Return list of symptoms"""
        db = SymptomsDB()
        try:
            symptoms = db.get_symptoms()
            for i in symptoms:
                self.symptoms_dict[i[1]] = i[2]
        except Exception as e:
            print("Error: ", e)


    def make_choice(self):
        """Make choice button"""
        choice = self.symptom_options_menu.get()
        if choice != self.parent.translator.dictionary['opt']:
            if choice == self.parent.translator.dictionary['edit_sympt']:
                print("edit")
            elif choice == self.parent.translator.dictionary['delete_sympt']:
                print("delete")
        else:
            print("MAKE A CHOICE")


    def delete_symptom(self):
        pass