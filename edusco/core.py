from typing import Dict
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .morphology import MorphologyAnalyzer
from .ontology import OntologyMatcher
from .rubric import RubricEvaluator
from .models import EduscoModel

class Edusco:
    """
    Türkçe öğrenci yanıtlarını anlamaya dayalı değerlendirme motoru
    """

    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.rubric = RubricEvaluator()

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        duzeltmis = self.spell.correct(cevap)
        tokens = self.tokenizer.tokenize(duzeltmis)
        morph_tokens = self.parser.parse(tokens)

        model_tokens_morph = []
        for y in model.get_all():
            y_duzeltmis = self.spell.correct(y)
            y_tokens = self.tokenizer.tokenize(y_duzeltmis)
            y_morph = self.parser.parse(y_tokens)
            model_tokens_morph.extend(y_morph)

        ortak = self.ontology.match(morph_tokens, model_tokens_morph)
        skor = len(ortak) / max(len(tokens), 1)

        rubric_sonuc = self.rubric.evaluate(skor)
        metinsel_donut = self._metinsel_donut_uret(rubric_sonuc, ortak)

        return {
            "duzeltmis": duzeltmis,
            "skor": round(skor, 2),
            "seviye": rubric_sonuc["seviye"],
            "etiket": rubric_sonuc["etiket"],
            "yorum": rubric_sonuc["yorum"],
            "ortak_kelimeler": ortak,
            "metinsel_donut": metinsel_donut
        }

    def _metinsel_donut_uret(self, rubric_sonuc: dict, ortak: list) -> str:
        ortak_str = ", ".join(ortak) if ortak else "henüz belirgin anahtar kavram yok"
        seviye = rubric_sonuc["seviye"]
        if seviye >= 4:
            return f" Harika! Cevabın {rubric_sonuc['etiket'].lower()}. Anahtar kavramlar: {ortak_str}."
        elif seviye == 3:
            return f" İyi bir cevap verdin. {rubric_sonuc['yorum']} Anahtar kavramlar: {ortak_str}."
        elif seviye == 2:
            return f" Cevabın yüzeysel doğru. {rubric_sonuc['yorum']} Eksik kalan kavramları gözden geçir."
        else:
            return f" Cevabın konu dışı veya eksik. {rubric_sonuc['yorum']}"
