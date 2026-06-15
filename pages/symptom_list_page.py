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
            self.listbox.insert("end", v)


    def get_symptoms(self):
        """Return list of symptoms"""
        db = SymptomsDB()
        try:
            symptoms = db.get_symptoms()
            for i in symptoms:
                self.symptoms_dict[i[0]] = f"{i[1]}: {i[2]}"
        except Exception as e:
            print("Error: ", e)


    def make_choice(self):
        """Make choice button"""
        choice = self.symptom_options_menu.get()
        symptom_id = self.get_symptom_id_by_name_and_type()
        db = SymptomsDB()
        if choice != self.parent.translator.dictionary['opt'] and symptom_id is not None:
            if choice == self.parent.translator.dictionary['edit_sympt']:
                self.parent.edit_symptoms_page.sympt_id = symptom_id
                self.parent.show_edit_symptoms_page()
            elif choice == self.parent.translator.dictionary['delete_sympt']:
                try:
                    db.delete_symptom_by_id(symptom_id)
                    self.parent.show_symptoms_list_page()
                except Exception as e:
                    print("Error: ", e)
        else:
            print("MAKE A CHOICE")


    def get_symptom_id_by_name_and_type(self):
        db = SymptomsDB()
        try:
            data = self.listbox.get().split(":")
            name = data[0].strip()
            sympt_type = data[1].strip()
            sympt_id = db.get_sympt_id_by_name_and_type(name, sympt_type)
            return sympt_id[0][0]
        except Exception as e:
            print("Error: ", e)