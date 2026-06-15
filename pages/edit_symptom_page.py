import customtkinter as ctk
from symptoms_db import SymptomsDB


class EditSymptomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_sympt_list_btn = None
        self.symptom_name_label = None
        self.symptom_name_entry = None
        self.symptom_type_label = None
        self.symptom_type_entry = None
        self.add_btn = None

        # DATA
        self.sympt_id = None
        self.sympt_name = None
        self.sympt_type = None


    def layout(self):
        """Build page layout"""
        self.get_symptom()

        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["edit_symptom_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=40)

        self.back_to_sympt_list_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_symptoms_list_page,
            width=50,
        )
        self.back_to_sympt_list_btn.pack(padx=5, pady=35, side="bottom")

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
        self.symptom_name_entry.insert(0, self.sympt_name)
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
        for i in values:
            if self.sympt_type in i:
                opt = i
                print(opt)

                self.symptom_type_entry.set(opt)
        self.symptom_type_entry.pack(padx=5, pady=5)

        self.add_btn = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["save_edit_sympt"],
            font=self.parent.button_font,
            width=250,
            command=self.edit_symptom,
        )
        self.add_btn.pack(padx=5, pady=15)


    def edit_symptom(self):
        """Update symptom in the database"""
        name_filled = self.symptom_name_entry.get().strip() != ""
        type_selected = self.symptom_type_entry.get() != self.parent.translator.dictionary["choose"]
        if name_filled and type_selected:
            db = SymptomsDB()
            try:
                symptom_name = self.symptom_name_entry.get()
                symptom_type = self.symptom_type_entry.get()
                db.update_symptom(symptom_name, symptom_type, self.sympt_id)
                self.parent.show_symptoms_list_page()
            except Exception as e:
                print("Error: ", e)
        else:
            pass


    def get_symptom(self):
        """Get the symptom from the database"""
        db = SymptomsDB()
        try:
            data = db.get_symptom_by_id(self.sympt_id)
            self.sympt_name = data[0][1]
            self.sympt_type = data[0][2]
        except Exception as e:
            print("Error: ", e)
