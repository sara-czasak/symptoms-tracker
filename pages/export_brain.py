from symptoms_db import SymptomsDB
import os
from docx import Document
from docx.shared import Pt
import openpyxl


class DataManager:
    """MAnage gathering data and saving to excel and word"""
    def __init__(self):
        self.dir_path = None
        self.diary_path = None
        self.symptom_path = None

        self.log_data = {}


    def create_dir_if_not_exists(self):
        if os.path.isdir("./user_data"):
            self.dir_path = os.path.abspath("./user_data")
            self.diary_path = os.path.abspath(os.path.join(self.dir_path, 'diary.docx'))
            self.symptom_path = os.path.abspath(os.path.join(self.dir_path, 'symptoms.xlsx'))
        else:
            os.mkdir("./user_data")
            self.dir_path = os.path.abspath("./user_data")
            self.diary_path = os.path.abspath(os.path.join(self.dir_path, 'diary.docx'))
            self.symptom_path = os.path.abspath(os.path.join(self.dir_path, 'symptoms.xlsx'))
            document = Document()
            document.save(self.diary_path)
            symptoms_file = openpyxl.Workbook()
            sheet = symptoms_file.active
            headers = ['Date', 'Symptom', 'Severity']
            for col_num, header in enumerate(headers, start=1):
                sheet.cell(row=1, column=col_num, value=header)
            sheet.column_dimensions["A"].width = 20
            sheet.column_dimensions["B"].width = 20
            sheet.column_dimensions["C"].width = 20
            symptoms_file.save(self.symptom_path)

    def get_current_data_to_save(self):
        db = SymptomsDB()
        try:
            logs = db.get_logs_in_reverse_date_order()
            for log in logs:
                if log[3] != "":
                    self.log_data[log[1]] = log[3]
                else:
                    pass
            self.save_diary_data()
        except Exception as e:
            print("Error: ", e)


    def save_diary_data(self):
        try:
            if os.path.exists(self.diary_path):
                os.remove(self.diary_path)
            diary = Document()
            diary.save(self.diary_path)
            for k, v in self.log_data.items():
                diary.add_heading(f"~ Date: {k} ~\n", level=1)
                paragraph = diary.add_paragraph()
                run = paragraph.add_run(f"\t{v}")
                run.font_size = Pt(12)
            diary.save(self.diary_path)
        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    test = DataManager()
    test.create_dir_if_not_exists()
    test.get_current_data_to_save()