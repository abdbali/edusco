from .rubric import RubricEvaluator

class Edusco:
    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.rubric = RubricEvaluator()  

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        ...
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)

        rubric_sonuc = self.rubric.değerlendir(ortak)

        metinsel_donut = (
            f"Cevap {etiket} (Seviye {seviye}, Skor {round(skor,2)}). "
            f"Rubrik puanı: {rubric_sonuc['puan']}. "
            f"Açıklama: {rubric_sonuc['açıklama']}"
        )

        return {
            "duzeltmis": duzeltmis,
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket,
            "ortak_kelimeler": ortak,
            "rubrik_sonuc": rubric_sonuc,
            "metinsel_donut": metinsel_donut
        }
