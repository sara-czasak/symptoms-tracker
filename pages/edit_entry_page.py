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
        self.log_details_to_save = {}
        self.log_to_save = {}


    def layout(self):
        """Create UI"""
        self.get_symptoms()

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
            checkbox = ctk.CTkCheckBox(
                check_frm,
                text="",
            )

            for j in self.log_details:
                if i[1].lower() == j[2].lower() and j[4] == 'yes_no':
                    checkbox.select()

            checkbox.grid(row=0, column=1, sticky="w")
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

            scale = ctk.CTkOptionMenu(
                scale_frm,
                values=self.scale_values,
            )

            for j in self.log_details:
                if i[1].lower() == j[2].lower() and j[4] == 'scale':
                    scale.set(j[3])

            scale.grid(row=0, column=1, sticky="e")
            scale_frm.pack(fill="both", expand=True, pady=5)
            self.scale_fields.append(scale_frm)

        for i in self.text_symptoms_dict.items():
            text_frm = ctk.CTkFrame(
                self.scroll_screen,
            )
            text_frm.grid_columnconfigure(1, weight=1)

            symptom_name = ctk.CTkLabel(
                text_frm,
                text=f"{i[1].capitalize()}:",
                font=self.parent.label_font,
            )
            symptom_name.grid(row=0, column=0, padx=5)

            symptom_text = ctk.CTkEntry(
                text_frm,
            )

            for j in self.log_details:
                if i[1].lower() == j[2].lower() and j[4] == 'text':
                    symptom_text.insert("end", j[3])

            symptom_text.grid(row=0, column=1, sticky='e')
            text_frm.pack(fill="both", expand=True, pady=5)
            self.text_fields.append(text_frm)

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
            command=self.get_data_and_save,
        )
        self.save_changes_btn.pack(padx=5, pady=5, fill="both")


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

    def get_data_and_save(self):
        self.get_data()
        self.save_data()
        self.parent.refresh_screen()
        self.back_to_view_logs()


    def get_data(self):
        """Get data from log and sort by log and details"""
        self.log_to_save['date'] = self.date_entry.get()
        self.log_to_save['notes'] = self.notes_entry.get("1.0", 'end').strip()
        symptoms = 0
        label = None
        for i in self.checkbox_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkCheckBox) and j.get() == 1:
                    symptoms += 1
                    self.log_details_to_save[label] = [self.parent.translator.dictionary["yes"], "yes_no"]
                    label = None
        for i in self.scale_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkOptionMenu) and j.get() != "0":
                    symptoms += 1
                    self.log_details_to_save[label] = [j.get(), "scale"]
                    label = None
        for i in self.text_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkEntry) and j.get() != "":
                    symptoms += 1
                    self.log_details_to_save[label] = [j.get(), "text"]
                    label = None
        self.log_to_save['symptoms'] = symptoms


    def save_data(self):
        """Save log data to database"""
        db = SymptomsDB()
        try:
            db.delete_log(self.log_to_save['date'])
            notes = ""
            if self.log_to_save['notes'] != "":
                notes = self.log_to_save['notes']
            db.add_log(
                date=self.log_to_save['date'],
                sympt_num=self.log_to_save['symptoms'],
                notes=notes,
            )
            log_id = db.get_logs_id_by_date(self.log_to_save['date'])[0]
            for k, v in self.log_details_to_save.items():
                db.add_log_details(log_id, k.replace(":", ""), v[0], v[1])
            self.parent.data_manager.get_current_data_to_save()
        except Exception as e:
            print("Error save data: ", e)
