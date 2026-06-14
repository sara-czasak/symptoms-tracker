import customtkinter as ctk
from symptoms_db import SymptomsDB


class EditLogFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_logs_btn = None

        # WIDGET GROUP
        self.data_widgets = None

        # DATA TO VIEW
        self.log_data = {}
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
        self.back_to_logs_btn.pack(padx=5, pady=35, side="bottom")


        # ADD UI ELEMENTS FOR EACH ITEM. SAME AS ADD LOG BUT PREFILL VALS


    def get_log_and_details_ids(self):
        db = SymptomsDB()
        try:
            self.log_id = db.get_logs_id_by_date(self.log_data["Date"])[0]
            print(db.get_log_details_by_id(self.log_id))
        except Exception as e:
            print("Error: ", e)


    def back_to_view_logs(self):
        self.parent.hide_edit_log()
        self.parent.show_view_logs()
