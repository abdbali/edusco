from spellchecker import SpellChecker
import os

class SpellingCorrector:
    def __init__(self):

        tr_dict_path = os.path.join(os.path.dirname(__file__), "resources", "tr.json")
        self.spell = SpellChecker(language=None, local_dictionary=tr_dict_path)

    def correct(self, text: str) -> str:
        kelimeler = text.strip().lower().split()

        duzeltilmis = []
        for k in kelimeler:
            if k:  
                c = self.spell.correction(k)
                if c is None:
                    c = k  
                duzeltilmis.append(c)
        return " ".join(duzeltilmis)
