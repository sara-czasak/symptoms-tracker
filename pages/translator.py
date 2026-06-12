langs = [
    {
        "English": {
            # PAGE TITLES
            "menu_page_title": "~ Personal Symptom ~\n~ Tracker ~",

            # MENU WIDGETS
            "add_log": "NEW LOG",
            "analysis_btn": "INSIGHTS",
            "view_entries_btn": "SEE ALL ENTRIES",
            "settings_btn": "SETTINGS",
            "about_btn": "ABOUT",
            "add_symptoms_btn": "ADD SYMPTOMS\nTO TRACK",
            "exit_btn": "EXIT"
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
        self.lang = lang
        self.get_dictionary(self.lang)


    def get_dictionary(self, lang):
        for i in langs:
            if lang in i:
                self.dictionary = i[lang]