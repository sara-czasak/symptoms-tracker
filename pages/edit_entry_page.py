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
        self.log_details_data = {}

        # DATA TO VIEW
        self.log_data = {}
        self.log_details = None
        self.log_id = None


    def layout(self):
        """Create UI"""
        self.get_log_and_details_ids()
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


        # ADD UI ELEMENTS FOR EACH ITEM. SAME AS ADD LOG BUT PREFILL VALS
        self.scroll_screen = ctk.CTkScrollableFrame(
            self,
        )
        self.scroll_screen.pack(fill="both", expand=True)

        self.save_changes_btn = ctk.CTkButton(
            self,
            font=self.parent.button_font,
            text=self.parent.translator.dictionary["save_changes"],
        )
        self.save_changes_btn.pack(padx=5, pady=5)



    def get_log_and_details_ids(self):
        db = SymptomsDB()
        try:
            self.log_id = db.get_logs_id_by_date(self.log_data["Date"])[0]
            self.log_details = db.get_log_details_by_id(self.log_id)
        except Exception as e:
            print("Error: ", e)


    def back_to_view_logs(self):
        self.parent.hide_edit_log()
        self.parent.show_view_logs()
