from typing import Dict, List
from difflib import SequenceMatcher


class SpellingCorrector:
    def correct(self, text: str) -> str:
        return text.lower()


class Tokenizer:
    def tokenize(self, text: str) -> List[str]:
        return text.split()


class POSParser:
    def parse(self, tokens: List[str]) -> List[Dict]:
        return [{"text": t, "pos": "noun"} for t in tokens]


class MorphologyAnalyzer:
    def analyze(self, token: str) -> Dict:
        return {"text": token, "root": token}


class OntologyMatcher:
    def match(self, tokens1: List[Dict], tokens2: List[Dict]) -> List[str]:
        words1 = [t["root"] for t in tokens1]
        words2 = [t["root"] for t in tokens2]
        return [w for w in words1 if w in words2]


class PronounResolver:
    def resolve(self, tokens: List[str]) -> List[str]:
        return tokens


class Extractor:
    def extract(self, tokens: List[str]) -> List[Dict]:
        if not tokens:
            return []
        return [{"ozne": tokens[0], "eylem": " ".join(tokens[1:]), "nesne": ""}]


class EduscoModel:
    def __init__(self, yanitlar: List[str]):
        self.yanitlar = yanitlar


class Edusco:
    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.extractor = Extractor()
        self.pronoun_resolver = PronounResolver()

    def semantik_skor(self, student: str, model: str) -> float:
        model_cumleler = [c.strip() for c in model.split(",")]
        student_cumleler = [c.strip() for c in student.split(",")]
        skorlar = []
        for mc in model_cumleler:
            max_skor = max([SequenceMatcher(None, mc.lower(), sc.lower()).ratio()
                            for sc in student_cumleler]) if student_cumleler else 0
            skorlar.append(max_skor)
        return sum(skorlar) / len(skorlar) if skorlar else 0

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        duzeltmis = self.spell.correct(cevap)
        tokens = self.tokenizer.tokenize(duzeltmis)
        tokens = self.pronoun_resolver.resolve(tokens)
        parsed = self.parser.parse(tokens)
        morph_tokens = [self.morph.analyze(t) for t in tokens]
        relations = self.extractor.extract(tokens)

        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar))
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]

        ortak = self.ontology.match(morph_tokens, model_tokens_morph)
        sem_score = self.semantik_skor(cevap, " ".join(model.yanitlar))

        skor_raw = (len(ortak) / len(model_tokens) * 0.4 + sem_score * 0.6) if model_tokens else sem_score

        skor = skor_raw * 2

        if skor >= 0.90:
            seviye, etiket = 4, "Tam Doğru"
        elif skor >= 0.70:
            seviye, etiket = 3, "Büyük Oranda Doğru"
        elif skor >= 0.52:
            seviye, etiket = 2, "Kısmen Doğru"
        elif skor >= 0.20:
            seviye, etiket = 1, "Yüzeysel Doğru"
        else:
            seviye, etiket = 0, "Yanlış"

        return {
            "duzeltmis": " ".join([t["text"] for t in morph_tokens]),
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket,
            "ortak_kelimeler": ortak,
            "relations": relations
        }
