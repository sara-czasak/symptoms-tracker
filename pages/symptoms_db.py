import sqlite3
from sqlite3 import IntegrityError, OperationalError
from schema import CREATE_LOGS_TABLE, CREATE_LOG_DETAILS_TABLE, CREATE_USER_PREFERENCES_TABLE, CREATE_SYMPTOMS_TABLE


class SymptomsDB:
    def __init__(self):
        self.create_database()


    def get_connection(self):
        conn = sqlite3.connect('symptom_tracker.db')
        conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def create_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(CREATE_LOGS_TABLE)
            cursor.execute(CREATE_LOG_DETAILS_TABLE)
            cursor.execute(CREATE_USER_PREFERENCES_TABLE)
            cursor.execute(CREATE_SYMPTOMS_TABLE)
            conn.commit()
        except OperationalError:
            print("Database creation failed")
        finally:
            conn.close()


    def add_symptom(self, symptom, type):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO symptoms (symptom, track_type) VALUES (?, ?)",
                           (symptom, type))
            conn.commit()
        except IntegrityError:
            print("Symptom already exists")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def check_if_symptoms(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM symptoms")
            symptoms = cursor.fetchall()
            if len(symptoms) == 0:
                return False
            else:
                return True
        except IntegrityError:
            print("Symptom already exists")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()