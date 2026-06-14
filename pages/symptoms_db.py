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


    def check_if_logs(self):
        """Check if logs exist in the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM logs")
            logs = cursor.fetchall()
            if len(logs) == 0:
                return False
            else:
                return True
        except IntegrityError:
            print("IntegrityError")
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
        finally:
            conn.close()


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
        finally:
            conn.close()


    def get_logs_id_by_date(self, date):
        """Get logs id by date"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM logs WHERE date = ?", (date,))
            log_id = cursor.fetchone()
            return log_id
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def get_log_by_logs_id(self, log_id):
        """Get logs id by log_id"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM logs WHERE log_id = ?", (log_id,))
            log = cursor.fetchall()
            return log
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def add_log_details(self, log_id, symptom, level, type_):
        """Add a log details to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO log_details (logs_id, symptom, level, track_type) VALUES (?, ?, ?, ?)", (log_id, symptom, level, type_))
            conn.commit()
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def get_logs_in_reverse_date_order(self):
        """Get records by date in reverse order"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM logs ORDER BY date DESC")
            logs = cursor.fetchall()
            return logs
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def delete_log(self, date):
        """Delete a log from the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM logs WHERE date = ?", (date,))
            conn.commit()
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def get_log_details_by_id(self, logs_id):
        """Get logs details by id"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM log_details WHERE logs_id = ?", (logs_id,))
            log_details_data = cursor.fetchall()
            return log_details_data
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()


    def get_log_by_date(self, date):
        """Get log details by date"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM logs WHERE date = ?", (date,))
            log_data = cursor.fetchall()
            return log_data
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Database error")
        finally:
            conn.close()







