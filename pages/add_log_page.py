import customtkinter as ctk
from symptoms_db import SymptomsDB


class AddLogFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.scroll_symptoms = None

        # WIDGET GROUPS
        self.checkbox_fields = []
        self.scale_fields = []
        self.text_fields = []

        # DATA
        self.checkbox_symptoms_dict = {}
        self.scale_symptoms_dict = {}
        self.text_symptoms_dict = {}
        self.scale_values = [str(i) for i in range(6)]

        self.get_symptoms()
        self.layout()


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

        self.scroll_symptoms = ctk.CTkScrollableFrame(
            self
        )
        self.scroll_symptoms.pack(padx=5, pady=5, fill="both", expand=True)

        for i in self.checkbox_symptoms_dict.values():
            check_frm = ctk.CTkFrame(
                self.scroll_symptoms,
            )

            check_label = ctk.CTkLabel(
                check_frm,
                text=i,
                font=self.parent.label_font,
                width=150,
            )

            check_label.grid(row=0, column=0)

            checkbox = ctk.CTkCheckBox(
                check_frm,
                text="",
            )
            checkbox.grid(row=0, column=1)

            self.checkbox_fields.append(check_frm)
            check_frm.pack(fill="both", expand=True, pady=5)

        for i in self.scale_symptoms_dict.values():
            scale_frm = ctk.CTkFrame(
                self.scroll_symptoms,
            )
            scale_frm.grid_columnconfigure(1, weight=1)

            symptom_name = ctk.CTkLabel(
                scale_frm,
                text=i.capitalize(),
            )
            symptom_name.grid(row=0, column=0)

            scale = ctk.CTkOptionMenu(
                scale_frm,
                values=self.scale_values,
            )
            scale.grid(row=0, column=1, sticky="e")

            self.scale_fields.append(scale_frm)
            scale_frm.pack(fill="both", expand=True, pady=5)

        for i in self.text_symptoms_dict.values():
            text_frm = ctk.CTkFrame(
                self.scroll_symptoms,
            )
            text_frm.grid_columnconfigure(1, weight=1)

            symptom_name = ctk.CTkLabel(
                text_frm,
                text=i.capitalize(),
                font=self.parent.label_font,
            )
            symptom_name.grid(row=0, column=0, padx=5)

            symptom_text = ctk.CTkEntry(
                text_frm,
                width=250,
            )

            symptom_text.grid(row=0, column=1, sticky='e')

            self.scale_fields.append(text_frm)
            text_frm.pack(fill="both", expand=True, pady=5)


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
                    print(symptom[2])
                    if symptom[2] == self.parent.translator.dictionary["yes_no"]:
                        self.checkbox_symptoms_dict[symptom[0]] = symptom[1]
                    elif symptom[2] == self.parent.translator.dictionary["scale"]:
                        self.scale_symptoms_dict[symptom[0]] = symptom[1]
                    elif symptom[2] == self.parent.translator.dictionary["text"]:
                        self.text_symptoms_dict[symptom[0]] = symptom[1]
                    else:
                        pass
            else:
                pass
        except Exception as e:
            print("Error: ", e)


    def reset_fields(self):
        pass