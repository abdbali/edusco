from .evaluator import EduscoModel
from .core import Tokenizer, POSParser, MorphologyAnalyzer, OntologyMatcher

class Edusco:
    def __init__(self):
        # Core pipeline modülleri
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
    
    def değerlendir(self, model: EduscoModel, cevap: str):
        duzeltmis = cevap.strip().lower()
        tokens = self.tokenizer.tokenize(duzeltmis)
        parsed = self.parser.parse(tokens)
        morph_tokens = [self.morph.analyze(t) for t in tokens]
        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar).lower())
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)  
        skor = len(ortak) / len(model_tokens) if model_tokens else 0

        if skor >= 0.8:
            seviye, etiket = 4, "Tam Doğru"
        elif skor >= 0.6:
            seviye, etiket = 3, "Yüksek"
        elif skor >= 0.4:
            seviye, etiket = 2, "Orta"
        elif skor >= 0.2:
            seviye, etiket = 1, "Düşük Doğruluk"
        else:
            seviye, etiket = 0, "Yanlış"

        return {
            "duzeltmis": " ".join([t["text"] for t in morph_tokens]),  # düzeltmiş metin
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket
        }
