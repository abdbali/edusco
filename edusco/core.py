from spellchecker import SpellChecker
from typing import List, Dict

class Tokenizer:
    def tokenize(self, text: str) -> List[str]:
        return text.strip().lower().replace(",", "").replace(".", "").split()

class MorphologyAnalyzer:
    def analyze(self, token: str) -> Dict:
        return {"text": token, "root": token}

class POSParser:
    def parse(self, tokens: List[str]) -> List[Dict]:
        return [{"token": t, "pos": "NOUN"} for t in tokens]

class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t["root"] for t in cevap_tokens])
        model_set = set([t["root"] for t in model_tokens])
        return list(cevap_set.intersection(model_set))

class EduscoModel:
    def __init__(self, yanitlar: List[str]):
        self.yanitlar = yanitlar

class Edusco:
    def __init__(self):
        self.spell = SpellChecker(language='tr')
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        kelimeler = cevap.strip().lower().split()
        duzeltmis = " ".join([self.spell.correction(k) for k in kelimeler])
        tokens = self.tokenizer.tokenize(duzeltmis)
        parsed = self.parser.parse(tokens)
        morph_tokens = [self.morph.analyze(t) for t in tokens]
        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar).lower())
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)
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
            "ortak_kelimeler": ortak
        }
