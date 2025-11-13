class RubricEvaluator:
    """
    Değerlendirme skoruna göre seviye, nitelik ve etiket belirler.
    """
    def __init__(self):
        self.levels = {
            0: (0.0, 0.2),
            1: (0.2, 0.4),
            2: (0.4, 0.6),
            3: (0.6, 0.8),
            4: (0.8, 1.0)
        }
        self.aciklama = {
            0: "Yanlış veya alakasız cevap.",
            1: "Kısmen doğru ama eksik veya yüzeysel ifade.",
            2: "Temel kavram doğru ancak açıklama yüzeysel.",
            3: "Açıklama çoğunlukla doğru ve mantıklı.",
            4: "Cevap tamamen doğru ve kapsamlı."
        }
        self.etiketler = {
            0: "yanlış",
            1: "kısmen_doğru",
            2: "temel_doğru",
            3: "çoğunlukla_doğru",
            4: "tamamen_doğru"
        }

    def evaluate(self, skor: float) -> dict:
        skor = max(0, min(skor, 1))  # 0-1 aralığına sınırla
        for seviye, (alt, ust) in self.levels.items():
            if alt <= skor <= ust:
                break
        return {
            "seviye": seviye,
            "skor": round(skor, 2),
            "yorum": self.aciklama[seviye],
            "etiket": self.etiketler[seviye]
        }


def degerlendir(cevap: str) -> dict:


    anahtar_kelimeler = ["fotosentez", "besin", "enerji", "bitki"]
    ortak = [kelime for kelime in anahtar_kelimeler if kelime in cevap.lower()]
    skor = min(1.0, 0.2 * len(ortak))  

    evaluator = RubricEvaluator()
    rubrik_sonuc = evaluator.evaluate(skor)

    sonuc = {
        "cevap": cevap,
        "skor": round(skor, 2),
        "ortak_kelimeler": ortak,
        "rubrik_sonuc": rubrik_sonuc,
        "metinsel_donut": f"{rubrik_sonuc['seviye']}/4 seviyesinde, etiket: {rubrik_sonuc['etiket']}"
    }
    return sonuc


cevap = input("Soru: Fotosentezin besin zincirindeki önemi nedir?\nCevabınız: ")

sonuc = degerlendir(cevap)

print("\n--- Dönüt ---")
print("Cevap:", sonuc["cevap"])
print("Skor:", sonuc["skor"])
print("Ortak Kelimeler:", sonuc["ortak_kelimeler"])
print("Metinsel Donut:", sonuc["metinsel_donut"])
print("Detaylı Rubrik Değerlendirmesi:", sonuc["rubrik_sonuc"])
