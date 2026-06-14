import customtkinter as ctk
from symptoms_db import SymptomsDB
from CTkListbox import *


class ViewLogsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # WIDGETS
        self.page_title = None
        self.back_to_menu_btn = None
        self.option_frm = None
        self.option_menu = None
        self.select_opt = None
        self.listbox = None

        self.log_data = []
        self.options = [
            self.parent.translator.dictionary["view"],
            self.parent.translator.dictionary["edit"],
            self.parent.translator.dictionary["delete"],
        ]

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

        self.option_frm = ctk.CTkFrame(
            self
        )
        self.option_frm.pack(pady=15)

        self.option_menu = ctk.CTkOptionMenu(
            self.option_frm,
            values=self.options,
            font=self.parent.button_font,
        )

        self.option_menu.set(self.parent.translator.dictionary["opt"])
        self.option_menu.grid(row=0, column=0, padx=10)

        self.select_opt = ctk.CTkButton(
            self.option_frm,
            text=self.parent.translator.dictionary["confirm"],
            font=self.parent.button_font,
            width=100,
            command=self.choose_option,
        )

        self.select_opt.grid(row=0, column=1, padx=10)

        self.listbox = CTkListbox(
            self,
            height=240,
        )

        self.get_logs()
        for i in self.log_data:
            self.listbox.insert('end', i['date'])

        self.listbox.pack(expand=True, fill="both")


    def get_logs(self):
        """Get all logs"""
        db = SymptomsDB()
        try:
            logs = db.get_logs_in_reverse_date_order()
            for i in logs:
                data = {
                    "date": i[1],
                    "id": i[0],
                    "notes": i[3]
                }
                self.log_data.append(data)
        except Exception as e:
            print("Error: ", e)


    def choose_option(self):
        """Check which option is selected and redirect accordingly"""
        opt = self.option_menu.get()
        if opt == self.parent.translator.dictionary["view"]:
            self.parent.show_view_entry()
        elif opt == self.parent.translator.dictionary["edit"]:
            self.parent.show_edit_log()
        elif opt == self.parent.translator.dictionary["delete"]:
            self.delete_log()


    def view_log(self):
        db = SymptomsDB()
        log_view_data = {}
        if self.listbox.get() is not None:
            try:
                log_id = db.get_logs_id_by_date(self.listbox.get())[0]
                log_details = db.get_log_details_by_id(log_id)
                log = db.get_log_by_date(self.listbox.get())[0]
                log_view_data["Date"] = log[1]
                for symptom in log_details:
                    log_view_data[symptom[2]] = symptom[3]
                if log[3] != "":
                    log_view_data["Notes"] = log[3].capitalize()
                return log_view_data
            except Exception as e:
                print("Error: ", e)
        else:
            print("MAKE A SELECTION")
            return log_view_data


    def delete_log(self):
        """Delete selected log"""
        db = SymptomsDB()
        if self.listbox.get() is not None:
            try:
                db.delete_log(self.listbox.get())
                self.parent.refresh_screen()
                if (self.listbox.size() - 1) == 0:
                    self.parent.show_menu()
                else:
                    self.parent.show_view_logs()
            except Exception as e:
                print("Error: ", e)
        else:
            print("MAKE A SELECTION")


    def back_to_menu(self):
        """Reset fields and go back to menu"""
        self.parent.hide_show_logs()
        self.parent.show_menu()

