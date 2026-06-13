import sqlite3
from sqlite3 import IntegrityError, OperationalError
from schema import CREATE_LOGS_TABLE, CREATE_LOG_DETAILS_TABLE, CREATE_USER_PREFERENCES_TABLE, CREATE_SYMPTOMS_TABLE


class SymptomsDB:
    def __init__(self):
        self.create_database()


    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect('symptom_tracker.db')
        conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def create_database(self):
        """Create tables if they don't exist"""
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


    def add_symptom(self, symptom, type_):
        """Add a symptom to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO symptoms (symptom, track_type) VALUES (?, ?)",
                           (symptom, type_))
            conn.commit()
        except IntegrityError:
            print("Symptom already exists")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def check_if_symptoms(self):
        """Check if symptoms exist in the database"""
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


    def get_symptoms(self):
        """Get list of all symptoms"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM symptoms")
            symptoms = cursor.fetchall()
            if len(symptoms) == 0:
                return []
            else:
                return symptoms
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")


    def add_log(self, date, sympt_num, notes):
        """Add a log to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO logs (date, sympt_num, notes) VALUES (?, ?, ?)", (date, sympt_num, notes))
            conn.commit()
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")


    def get_logs_id_by_date(self, date):
        """Get logs id by date"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM logs WHERE date = ?", (date,))
            log_id = cursor.fetchone()
            return log_id
            conn.commit()
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")

    def add_log_details(self):
        """Add a log details to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            pass
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")

