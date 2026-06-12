import customtkinter as ctk


class AddSymptomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None


        self.layout()


    def layout(self):
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["add_symptom_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=40)

        self.back_to_menu_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_menu,
        )
        self.back_to_menu_btn.pack(padx=5, pady=35, side="bottom")
