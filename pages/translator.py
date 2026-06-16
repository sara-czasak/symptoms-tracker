langs = [
    {
        "English": {
            # PAGE TITLES
            "menu_page_title": "~ Personal Symptom ~\n~ Tracker ~",
            "settings_title": "~ SETTINGS ~",
            "add_symptom_title": "~ ADD SYMPTOM ~",
            "add_log_title": "~ ADD LOG ~",
            "view_all_title": "~ ALL LOGS ~",
            "view_details": "~ LOG DETAILS ~",
            "edit_log_title": "~ EDIT LOG ~",
            "sympt_list_title": "~ SYMPTOMS ~",
            "edit_symptom_title": "~ EDIT SYMPTOM ~",
            "lang_title": "~ CHOOSE LANGUAGE ~",
            "theme_title": "~ CHOOSE THEME ~",
            "about_title": "~ ABOUT SYMPTOM\nTRACKER ~",

            # MESSAGE BOXES
            "failed_save_title": "SOMETHING WENT WRONG...",
            "failed_save_message": "Your data didn't save. Please try again.",
            "saved_title": "DATA SAVED",
            "saved_message": "Your data was successfully saved",

            # MENU WIDGETS
            "add_log": "NEW LOG",
            "analysis_btn": "INSIGHTS",
            "view_entries_btn": "SEE ALL ENTRIES",
            "settings_btn": "SETTINGS",
            "about_btn": "ABOUT",
            "add_symptoms_btn": "ADD SYMPTOMS TO TRACK",
            "exit_btn": "EXIT",

            # SETTINGS WIDGETS
            "export_btn": "EXPORT DATA",
            "lang_btn": "LANGUAGES",
            "theme_btn": "THEMES",
            "see_symptoms": "VIEW SYMPTOMS",

            # ADD SYMPTOM WIDGETS
            "add_symptom_name": "Symptom name:",
            "scale": "SCALE (0-5)",
            "yes_no": "PRESENT/NOT PRESENT",
            "text": "PLANE TEXT",
            "choose": "SELECT OPTION",
            "type": "How would you like to track?",
            "add_symptom": "ADD SYMPTOM",

            # ADD LOG WIDGETS
            "save": "SAVE",
            "add_log_date": "Date (YYYY-MM-DD): ",
            "add_log_notes": "Notes: ",
            "yes": "YES",

            # VIEW ALL LOGS
            "view": "SEE DETAILS",
            "edit": "EDIT LOG",
            "delete": "DELETE LOG",
            "opt": "OPTIONS",
            "confirm": "SELECT",

            # EDIT LOG DETAILS
            "save_changes": "SAVE CHANGES",

            # ALL SYMPTOMS LIST
            "edit_sympt": "EDIT SYMPTOM",
            "delete_sympt": "DELETE SYMPTOM",

            # EDIT SYMPTOMS
            "save_edit_sympt": "SAVE CHANGES",
        }
    },
    {
        "Polski": {
            # PAGE TITLES
            "menu_page_title": "~ PL ~",
            "settings_title": "~ PL ~",
            "add_symptom_title": "~ PL ~",
            "add_log_title": "~ PL ~",
            "view_all_title": "~ PL ~",
            "view_details": "~ PL ~",
            "edit_log_title": "~ PL ~",
            "sympt_list_title": "~ PL ~",
            "edit_symptom_title": "~ PL ~",
            "lang_title": "~ PL ~",
            "theme_title": "~ PL ~",
            "about_title": "~ PL ~",

            # MESSAGE BOXES
            "failed_save_title": "PL",
            "failed_save_message": "PL",
            "saved_title": "PL",
            "saved_message": "PL",

            # MENU WIDGETS
            "add_log": "PL",
            "analysis_btn": "PL",
            "view_entries_btn": "PL",
            "settings_btn": "PL",
            "about_btn": "PL",
            "add_symptoms_btn": "PL",
            "exit_btn": "PL",

            # SETTINGS WIDGETS
            "export_btn": "PL",
            "lang_btn": "PL",
            "theme_btn": "PL",
            "see_symptoms": "PL",

            # ADD SYMPTOM WIDGETS
            "add_symptom_name": "PL",
            "scale": "PL",
            "yes_no": "PL",
            "text": "PL",
            "choose": "PL",
            "type": "PL",
            "add_symptom": "PL",

            # ADD LOG WIDGETS
            "save": "PL",
            "add_log_date": "PL",
            "add_log_notes": "PL",
            "yes": "PL",

            # VIEW ALL LOGS
            "view": "PL",
            "edit": "PL",
            "delete": "PL",
            "opt": "PL",
            "confirm": "PL",

            # EDIT LOG DETAILS
            "save_changes": "PL",

            # ALL SYMPTOMS LIST
            "edit_sympt": "PL",
            "delete_sympt": "PL",

            # EDIT SYMPTOMS
            "save_edit_sympt": "PL",
        }
    }
]



class Translator:
    def __init__(self):
        self.dictionary = None
        self.lang = None
        self.available_languages = [
            "English",
        ]


    def set_lang(self, lang):
        """Choose language"""
        self.lang = lang
        self.get_dictionary(self.lang)


    def get_dictionary(self, lang):
        """Fetch translation from dictionary"""
        for i in langs:
            if lang in i:
                self.dictionary = i[lang]