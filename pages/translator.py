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

            # MENU WIDGETS
            "add_log": "NEW LOG",
            "analysis_btn": "INSIGHTS",
            "view_entries_btn": "SEE ALL ENTRIES",
            "settings_btn": "SETTINGS",
            "about_btn": "ABOUT",
            "add_symptoms_btn": "ADD SYMPTOMS\nTO TRACK",
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

            # VIEW LOG DETAILS
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