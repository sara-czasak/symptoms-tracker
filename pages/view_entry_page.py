import customtkinter as ctk
from symptoms_db import SymptomsDB

class ViewEntryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

