import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


    def layout(self):
        pass