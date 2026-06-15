from symptoms_db import SymptomsDB
import os
from docx import Document
import openpyxl


class DataManager:
    def __init__(self):
        self.dir_path = None
        self.diary_path = None
        self.symptom_path = None


    def create_dir_if_not_exists(self):
        if os.path.isdir("./user_data"):
            pass
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
        pass


    def save_data(self):
        pass


test = DataManager()
test.create_dir_if_not_exists()