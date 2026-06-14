import customtkinter as ctk
from symptoms_db import SymptomsDB


class EditLogFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_logs_btn = None
        self.scroll_screen = None
        self.save_changes_btn = None
        self.scroll_notes = None
        self.add_log_btn = None
        self.date_label = None
        self.date_entry = None
        self.date_frm = None
        self.notes_label = None
        self.notes_entry = None

        # WIDGET GROUPS
        self.checkbox_fields = []
        self.scale_fields = []
        self.text_fields = []

        # DATA
        self.checkbox_symptoms_dict = {}
        self.scale_symptoms_dict = {}
        self.text_symptoms_dict = {}
        self.scale_values = [str(i) for i in range(6)]
        self.log_data = {}
        self.log_details = None
        self.log_id = None


    def layout(self):
        """Create UI"""
        self.get_symptoms()
        print("scale: ", self.scale_symptoms_dict)

        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["edit_log_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=10)

        self.back_to_logs_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.back_to_view_logs,
            width=50,
        )
        self.back_to_logs_btn.pack(padx=5, pady=5, side="bottom")

        self.scroll_screen = ctk.CTkScrollableFrame(
            self,
        )
        self.scroll_screen.pack(fill="both", expand=True)

        self.date_frm = ctk.CTkFrame(
            self.scroll_screen,
        )
        self.date_frm.pack(fill="both", expand=True, pady=5)
        self.date_frm.grid_columnconfigure(1, weight=1)

        self.date_label = ctk.CTkLabel(
            self.date_frm,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["add_log_date"],
        )

        self.date_label.grid(row=0, column=0, padx=5)

        self.date_entry = ctk.CTkEntry(
            self.date_frm,
            width=150,
        )
        self.date_entry.insert(0, self.log_data["Date"])
        self.date_entry.grid(row=0, column=1, sticky='e')


        for i in self.checkbox_symptoms_dict.items():
            check_frm = ctk.CTkFrame(
                self.scroll_screen,
            )
            check_frm.grid_columnconfigure(1, weight=1)

            check_label = ctk.CTkLabel(
                check_frm,
                text=f"{i[1].capitalize()}:",
                font=self.parent.label_font,
            )
            check_label.grid(row=0, column=0, sticky="w", padx=5)

            for j in self.log_details:
                if i[1].lower() == j[2].lower() and j[4] == 'yes_no':
                    checkbox = ctk.CTkCheckBox(
                        check_frm,
                        text="",
                    )
                    checkbox.select()
                    checkbox.grid(row=0, column=1, sticky="w")

                    self.checkbox_fields.append(check_frm)

                elif i[1].lower() != j[2].lower() and j[4] == 'yes_no':
                    checkbox = ctk.CTkCheckBox(
                        check_frm,
                        text="",
                    )
                    checkbox.grid(row=0, column=1, sticky="w")

                    self.checkbox_fields.append(check_frm)
                    check_frm.pack(fill="both", expand=True, pady=5)
            self.checkbox_fields.append(check_frm)

        for i in self.scale_symptoms_dict.items():
            scale_frm = ctk.CTkFrame(
                self.scroll_screen,
            )
            scale_frm.grid_columnconfigure(1, weight=1)
            scale_frm.pack(fill="both", expand=True, pady=5)

            symptom_name = ctk.CTkLabel(
                scale_frm,
                text=f"{i[1].capitalize()}:",
                font=self.parent.label_font,
            )
            symptom_name.grid(row=0, column=0, padx=5)
            for j in self.log_details:
                if i[1].lower() == j[2].lower() and j[4] == 'scale':
                    scale = ctk.CTkOptionMenu(
                        scale_frm,
                        values=self.scale_values,
                    )
                    scale.set(j[3])
                    scale.grid(row=0, column=1, sticky="e")

                    self.scale_fields.append(scale_frm)
                    scale_frm.pack(fill="both", expand=True, pady=5)
                elif i[1].lower() != j[2].lower() and j[4] == 'scale':
                    scale = ctk.CTkOptionMenu(
                        scale_frm,
                        values=self.scale_values,
                    )
                    scale.grid(row=0, column=1, sticky="e")

                    self.scale_fields.append(scale_frm)
                    scale_frm.pack(fill="both", expand=True, pady=5)


        self.notes_label = ctk.CTkLabel(
            self.scroll_screen,
            text=self.parent.translator.dictionary["add_log_notes"],
            font=self.parent.label_font,
        )
        self.notes_label.pack(padx=5, pady=5)

        self.scroll_notes = ctk.CTkScrollableFrame(
            self.scroll_screen,
        )
        self.scroll_notes.pack(padx=5, pady=5, fill="both")

        self.notes_entry = ctk.CTkTextbox(
            self.scroll_notes,
        )
        if 'Notes' in self.log_data.keys():
            self.notes_entry.insert("1.0", self.log_data["Notes"])
        self.notes_entry.pack(padx=5, pady=5, fill="both")


        self.save_changes_btn = ctk.CTkButton(
            self,
            font=self.parent.button_font,
            text=self.parent.translator.dictionary["save_changes"],
        )
        self.save_changes_btn.pack(padx=5, pady=5)


    def get_log_and_details_ids(self):
        """Get log_id and details from db"""
        db = SymptomsDB()
        try:
            self.log_id = db.get_logs_id_by_date(self.log_data["Date"])[0]
            self.log_details = db.get_log_details_by_id(self.log_id)
        except Exception as e:
            print("Error: ", e)


    def get_symptoms(self):
        """Get all symptoms and sort by type"""
        db = SymptomsDB()
        try:
            data = db.get_symptoms()
            if len(data) > 0:
                for symptom in data:
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


    def back_to_view_logs(self):
        """Go back to view logs page"""
        self.parent.hide_edit_log()
        self.parent.show_view_logs()
