import customtkinter as ctk


class AboutFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.symptoms_list_btn = None
        self.export_btn = None
        self.lang_btn = None
        self.theme_btn = None
        self.scroll_screen = None

        # BUILD PAGE
        self.layout()


    def layout(self):
        """Build page layout"""
        self.page_title = ctk.CTkLabel(
            self,
            text=self.parent.translator.dictionary["about_title"],
            font=self.parent.title_font,
        )
        self.page_title.pack(padx=5, pady=10)

        self.back_to_menu_btn = ctk.CTkButton(
            self,
            text="",
            image=self.parent.back_img,
            font=self.parent.back_btn_font,
            command=self.parent.show_menu,
            width=50,
        )
        self.back_to_menu_btn.pack(padx=5, pady=10, side="bottom")

        self.scroll_screen = ctk.CTkScrollableFrame(
            self,
        )
        self.scroll_screen.pack(fill="both", expand=True)

        header_1 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_1"],
            wraplength=320,
        )
        header_1.pack(padx=5, pady=10)

        paraph_1 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["paragraph_1"],
            wraplength=320,
        )
        paraph_1.pack(padx=5, pady=5)

        header_2 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_2"],
            wraplength=320,
        )
        header_2.pack(padx=5, pady=10)

        li_1_head_2 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_1_head_2"],
            wraplength=320,
        )
        li_1_head_2.pack(padx=5, pady=5)

        li_2_head_2 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_2_head_2"],
            wraplength=320,
        )
        li_2_head_2.pack(padx=5, pady=5)

        li_3_head_2 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_3_head_2"],
            wraplength=320,
        )
        li_3_head_2.pack(padx=5, pady=5)

        li_4_head_2 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_4_head_2"],
        )
        li_4_head_2.pack(padx=5, pady=5)

        header_3 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_3"],
            wraplength=320,
        )
        header_3.pack(padx=5, pady=10)

        paragraph_3 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["paragraph_3"],
            wraplength=320,
        )
        paragraph_3.pack(padx=5, pady=5)

        header_4 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_4"],
            wraplength=320,
        )
        header_4.pack(padx=5, pady=10)

        li_1_head_4 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_1_head_4"],
            wraplength=320,
        )

        li_1_head_4.pack(padx=5, pady=5)

        li_2_head_4 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_2_head_4"],
            wraplength=320,
        )

        li_2_head_4.pack(padx=5, pady=5)

        li_3_head_4 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_3_head_4"],
            wraplength=320,
        )
        li_3_head_4.pack(padx=5, pady=5)

        li_4_head_4 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_4_head_4"],
            wraplength=320,
        )
        li_4_head_4.pack(padx=5, pady=5)

        header_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_5"],
            wraplength=320,
        )
        header_5.pack(padx=5, pady=10)

        li_1_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_1_head_5"],
            wraplength=320,
        )
        li_1_head_5.pack(padx=5, pady=5)

        li_2_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_2_head_5"],
            wraplength=320,
        )
        li_2_head_5.pack(padx=5, pady=5)

        li_3_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_3_head_5"],
            wraplength=320,
        )
        li_3_head_5.pack(padx=5, pady=5)

        li_4_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_4_head_5"],
            wraplength=320,
        )
        li_4_head_5.pack(padx=5, pady=5)

        li_5_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_5_head_5"],
            wraplength=320,
        )
        li_5_head_5.pack(padx=5, pady=5)

        li_6_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_6_head_5"],
            wraplength=320,
        )
        li_6_head_5.pack(padx=5, pady=5)

        li_7_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_7_head_5"],
            wraplength=320,
        )
        li_7_head_5.pack(padx=5, pady=5)

        li_8_head_5 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["li_8_head_5"],
            wraplength=320,
        )
        li_8_head_5.pack(padx=5, pady=5)

        header_6 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.title_font,
            text=self.parent.translator.dictionary["header_6"],
            wraplength=320,
        )
        header_6.pack(padx=5, pady=10)

        paragraph_6 = ctk.CTkLabel(
            self.scroll_screen,
            font=self.parent.label_font,
            text=self.parent.translator.dictionary["paragraph_6"],
            wraplength=320,
        )
        paragraph_6.pack(padx=5, pady=5)
