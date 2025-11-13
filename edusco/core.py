from typing import Dict
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .ontology import OntologyMatcher
from .rubric import RubricEvaluator
from .model import EduscoModel


class Edusco:
    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
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
            "ortak_kelimeler": ortak,
            "rubrik_sonuc": rubric_sonuc,
            "metinsel_donut": metinsel_donut
        }

    def _metinsel_donut_uret(self, rubric_sonuc, ortak):
        seviye = rubric_sonuc["seviye"]
        etiket = rubric_sonuc["etiket"]
        ortak_kelimeler = ", ".join(ortak) if ortak else "henüz belirgin anahtar kelime yok"

        if seviye == 0:
            return f"Cevabınız konudan uzak. Önemli kavramları içermiyor ({ortak_kelimeler})."
        elif seviye == 1:
            return f"Cevabınız fotosentezin rolünü belirtmiş ancak nedenini açıklamamış. Anahtar kelimeler: {ortak_kelimeler}."
        elif seviye == 2:
            return f"Cevabınız kısmen doğru; yalnızca bir bileşenden bahsetmişsiniz. Anahtar kelimeler: {ortak_kelimeler}."
        elif seviye == 3:
            return f"Cevabınız büyük oranda doğru, ancak açıklama iki bileşenle sınırlı kalmış. Anahtar kelimeler: {ortak_kelimeler}."
        else:
            return f"Tebrikler! Cevabınız tam ve bütüncül. Fotosentezin besin zincirindeki önemini doğru açıklamışsınız ({ortak_kelimeler})."
