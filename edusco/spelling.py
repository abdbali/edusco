from spellchecker import SpellChecker

class SpellingCorrector:
    def __init__(self):
        self.spell = SpellChecker(language=None, local_dictionary="tr.json")

    def correct(self, text: str) -> str:
        kelimeler = text.strip().lower().split()
        return " ".join([self.spell.correction(k) for k in kelimeler])
