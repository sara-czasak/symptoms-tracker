import customtkinter as ctk
from symptoms_db import SymptomsDB
import datetime as dt


class AddLogFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.scroll_symptoms = None
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
        self.log_details_data = {}

        self.get_symptoms()
        self.layout()


    def layout(self):
        """Create UI"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["add_log_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=10)

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

        self.date_frm = ctk.CTkFrame(
            self.scroll_symptoms,
        )
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
        self.date_entry.insert(0, dt.date.today().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=0, column=1, sticky='e')

        self.date_frm.pack(pady=5, fill="both", expand=True)

        for i in self.checkbox_symptoms_dict.values():
            check_frm = ctk.CTkFrame(
                self.scroll_symptoms,
            )
            check_frm.grid_columnconfigure(1, weight=1)

            check_label = ctk.CTkLabel(
                check_frm,
                text=f"{i}:",
                font=self.parent.label_font,
            )

            check_label.grid(row=0, column=0, sticky="w", padx=5)

            checkbox = ctk.CTkCheckBox(
                check_frm,
                text="",
            )
            checkbox.grid(row=0, column=1, sticky="w")

            self.checkbox_fields.append(check_frm)
            check_frm.pack(fill="both", expand=True, pady=5)

        for i in self.scale_symptoms_dict.values():
            scale_frm = ctk.CTkFrame(
                self.scroll_symptoms,
            )
            scale_frm.grid_columnconfigure(1, weight=1)

            symptom_name = ctk.CTkLabel(
                scale_frm,
                text=f"{i.capitalize()}:",
                font=self.parent.label_font,
            )
            symptom_name.grid(row=0, column=0, padx=5)

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
                text=f"{i.capitalize()}:",
                font=self.parent.label_font,
            )
            symptom_name.grid(row=0, column=0, padx=5)

            symptom_text = ctk.CTkEntry(
                text_frm,
            )

            symptom_text.grid(row=0, column=1, sticky='e')

            self.text_fields.append(text_frm)
            text_frm.pack(fill="both", expand=True, pady=5)

        self.notes_label = ctk.CTkLabel(
            self.scroll_symptoms,
            text=self.parent.translator.dictionary["add_log_notes"],
            font=self.parent.label_font,
        )
        self.notes_label.pack(padx=5, pady=5)

        self.scroll_notes = ctk.CTkScrollableFrame(
            self.scroll_symptoms,
        )
        self.scroll_notes.pack(padx=5, pady=5, fill="both")

        self.notes_entry = ctk.CTkTextbox(
            self.scroll_notes,
        )
        self.notes_entry.pack(padx=5, pady=5, fill="both")

        self.add_log_btn = ctk.CTkButton(
            self.scroll_symptoms,
            text=self.parent.translator.dictionary["save"],
            font=self.parent.button_font,
            command=self.get_data_and_save,
        )
        self.add_log_btn.pack(padx=5, pady=5)


    def back_to_menu(self):
        """Reset fields and go back to menu"""
        self.parent.hide_add_log()
        self.reset_fields()
        self.parent.show_menu()


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


    def reset_fields(self):
        """Reset fields"""
        for i in self.checkbox_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkCheckBox):
                    j.deselect()

        for i in self.scale_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkOptionMenu):
                    j.set(self.scale_values[0])

        for i in self.text_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkEntry):
                    j.delete(0, "end")

        self.notes_entry.delete("1.0", "end")


    def get_data_and_save(self):
        self.get_data()
        self.save_data()
        self.reset_fields()
        self.back_to_menu()


    def get_data(self):
        """Get data from log and sort by log and details"""
        self.log_data['date'] = self.date_entry.get()
        self.log_data['notes'] = self.notes_entry.get("1.0", 'end').strip()
        symptoms = 0
        label = None
        for i in self.checkbox_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkCheckBox) and j.get() == 1:
                    symptoms += 1
                    self.log_details_data[label] = self.parent.translator.dictionary["yes"]
                    label = None
        for i in self.scale_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkOptionMenu) and j.get() != "0":
                    symptoms += 1
                    self.log_details_data[label] = j.get()
                    label = None
        for i in self.text_fields:
            for j in i.winfo_children():
                if isinstance(j, ctk.CTkLabel):
                    label = j.cget("text")
                if isinstance(j, ctk.CTkEntry) and j.get() != "":
                    symptoms += 1
                    self.log_details_data[label] = j.get()
                    label = None
        self.log_data['symptoms'] = symptoms


    def save_data(self):
        """Save log data to database"""
        db = SymptomsDB()
        try:
            db.add_log(
                date = self.log_data['date'],
                sympt_num = self.log_data['symptoms'],
                notes = self.log_data['notes'],
            )
            log_id = db.get_logs_id_by_date(self.log_data['date'])[0]
            for k, v in enumerate(self.log_details_data):
                db.add_log_details(log_id, v.replace(":", ""), k)
        except Exception as e:
            print("Error: ", e)

