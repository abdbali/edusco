from typing import Dict
from .models import EduscoModel
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .morphology import MorphologyAnalyzer
from .ontology import OntologyMatcher
from .extractor import Extractor
from .pronoun_resolver import PronounResolver

class Edusco:
    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.extractor = Extractor()
        self.pronoun_resolver = PronounResolver()

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        # 1. Yazım düzelt
        duzeltmis = self.spell.correct(cevap)

        # 2. Tokenize
        tokens = self.tokenizer.tokenize(duzeltmis)

        # 3. Zamir çöz
        tokens = self.pronoun_resolver.resolve(tokens)

        # 4. POS parse
        parsed = self.parser.parse(tokens)

        # 5. Morphology
        morph_tokens = [self.morph.analyze(t) for t in tokens]

        # 6. ÖZN-Eylem-Nesne çıkarımı
        relations = self.extractor.extract(tokens)

        # 7. Model tokenleri
        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar))
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]

        # 8. Ontoloji eşleştirme
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)

        # 9. Skor hesapla
        skor = len(ortak) / len(model_tokens) if model_tokens else 0

        if skor >= 0.8:
            seviye, etiket = 5, "Tam Doğru"
        elif skor >= 0.6:
            seviye, etiket = 4, "Büyük Oranda Doğru"
        elif skor >= 0.4:
            seviye, etiket = 3, "Kısmen Doğru"
        elif skor >= 0.2:
            seviye, etiket = 2, "Yüzeysel Doğru"
        else:
            seviye, etiket = 1, "Yanlış"

        return {
            "duzeltmis": " ".join([t["text"] for t in morph_tokens]),
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket,
            "ortak_kelimeler": ortak,
            "relations": relations
        }
