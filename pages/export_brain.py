from symptoms_db import SymptomsDB
import os


class DataManager:
    def __init__(self):
        pass


    def create_dir_if_not_exists(self):
        if os.path.isdir("../user_data"):
            pass
        else:
            os.mkdir("../user_data")


    def get_current_data_to_save(self):
        pass


    def save_data(self):
        pass


test = DataManager()
test.create_dir_if_not_exists()