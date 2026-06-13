import customtkinter as ctk
from symptoms_db import SymptomsDB


class ViewLogsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None

        self.layout()


    def layout(self):
        """Create UI"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["view_all_title"],
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


    def get_logs(self):
        pass


    def back_to_menu(self):
        """Reset fields and go back to menu"""
        self.parent.hide_show_logs()
        self.parent.show_menu()