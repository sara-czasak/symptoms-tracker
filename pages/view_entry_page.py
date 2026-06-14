import customtkinter as ctk
from symptoms_db import SymptomsDB

class ViewEntryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_logs_btn = None

        self.layout()


    def layout(self):
        """Create UI"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["view_details"],
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


    def back_to_view_logs(self):
        self.parent.hide_view_entry()
        self.parent.show_view_logs()