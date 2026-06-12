langs = [
    {
        "English": {
            # PAGE TITLES
            "menu_page_title": "Personal Symptom\nTracker",
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