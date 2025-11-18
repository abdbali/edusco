from typing import Dict, List
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .morphology import MorphologyAnalyzer
from .ontology import OntologyMatcher
from .extractor import Extractor
from .pronoun_resolver import PronounResolver
from .models import EduscoModel

class Edusco:
    """Edusco motoru: yazım düzeltme, anlamsal eşleşme, rubrik puanlama"""

    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.extractor = Extractor()
        self.pronoun_resolver = PronounResolver()

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        #  Yazım düzeltme
        duzeltmis = self.spell.correct(cevap)

        #  Tokenize
        tokens = self.tokenizer.tokenize(duzeltmis)

        # Zamir çözme
        tokens = self.pronoun_resolver.resolve(tokens)

        #  POS & Parser
        parsed = self.parser.parse(tokens)

        #  Morphology
        morph_tokens = [self.morph.analyze(t) for t in tokens]

        #  Anlamsal ilişkiler çıkar
        relations = self.extractor.extract(tokens)

        #  Model ile eşleşme
        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar))
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)

        #  Skor hesapla
        skor = len(ortak)/len(model_tokens) if model_tokens else 0

        #  Rubrik seviyesini belirle
        if skor >= 0.8: 
            seviye, etiket = 5,"Tam Doğru"
        elif skor >= 0.6: 
            seviye, etiket = 4,"Büyük Oranda Doğru"
        elif skor >= 0.4: 
            seviye, etiket = 3,"Kısmen Doğru"
        elif skor >= 0.2: 
            seviye, etiket = 2,"Yüzeysel Doğru"
        else: 
            seviye, etiket = 1,"Yanlış"

        return {
            "duzeltmis":" ".join([t["text"] for t in morph_tokens]),
            "skor": round(skor,2),
            "seviye": seviye,
            "etiket": etiket,
            "ortak_kelimeler":ortak,
            "relations": relations
        }
