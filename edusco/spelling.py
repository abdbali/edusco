from spellchecker import SpellChecker

class SpellingCorrector:
    def __init__(self):
        try:
            self.spell = SpellChecker(language='tr')
        except Exception:
            self.spell = SpellChecker(language=None)

    def correct(self, text: str) -> str:
        kelimeler = text.strip().lower().split()
        duzeltilmis = []
        for k in kelimeler:
            c = self.spell.correction(k)
            if c is None:
                c = k
            duzeltilmis.append(c)
        return " ".join(duzeltilmis)
