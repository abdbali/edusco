import os
from spellchecker import SpellChecker

class SpellingCorrector:
    def __init__(self):

        tr_dict_path = os.path.join(os.path.dirname(__file__), "resources", "tr.json")
        self.spell = SpellChecker(language=None, local_dictionary=tr_dict_path)

    def correct(self, text: str) -> str:
        kelimeler = text.strip().lower().split()
        duzeltilmis = []
        for k in kelimeler:
            c = self.spell.correction(k)
            if c is None:
                c = k  
            duzeltilmis.append(c)
        return " ".join(duzeltilmis)
