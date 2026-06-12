import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.page_title = None

        self.layout()


    def layout(self):
        self.page_title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["menu_page_title"])
        self.page_title.pack(padx=5, pady=5)