from .evaluator import EduscoModel

class Edusco:
    def __init__(self):
        pass

    def değerlendir(self, model: EduscoModel, cevap: str):
    
        duzeltmis = cevap.strip().lower()

  
        model_text = " ".join(model.yanitlar).lower()
        model_kelimeler = set(model_text.split())
        cevap_kelimeler = set(duzeltmis.split())
        ortak = model_kelimeler.intersection(cevap_kelimeler)
        skor = len(ortak) / len(model_kelimeler) if model_kelimeler else 0

        # Skoru 0-4 seviyesine dönüştür
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
            "duzeltmis": duzeltmis,
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket
        }
