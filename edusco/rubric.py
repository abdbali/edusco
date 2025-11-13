class RubricEvaluator:
    """
    Değerlendirme skoruna göre seviye, nitelik ve etiket belirler.
    """
    def __init__(self):
        # Seviye aralıkları
        self.levels = {
            0: (0.0, 0.2),
            1: (0.2, 0.4),
            2: (0.4, 0.6),
            3: (0.6, 0.8),
            4: (0.8, 1.0)
        }

        # Seviye açıklamaları
        self.aciklama = {
            0: "Yanlış veya alakasız cevap.",
            1: "Kısmen doğru ama eksik veya yüzeysel ifade.",
            2: "Temel kavram doğru ancak açıklama yüzeysel.",
            3: "Açıklama çoğunlukla doğru ve mantıklı.",
            4: "Cevap tamamen doğru ve kapsamlı."
        }

        # Seviye etiketleri
        self.etiketler = {
            0: "yanlış",
            1: "kısmen_doğru",
            2: "temel_doğru",
            3: "çoğunlukla_doğru",
            4: "tamamen_doğru"
        }

    def evaluate(self, skor: float) -> dict:
        # Skoru 0-1 aralığına sınırla
        skor = max(0, min(skor, 1))

        # Seviye belirleme
        for seviye, (alt, ust) in self.levels.items():
            if alt <= skor <= ust:
                break

        return {
            "seviye": seviye,
            "skor": round(skor, 2),
            "yorum": self.aciklama[seviye],
            "etiket": self.etiketler[seviye]   # Artık etiket de var
        }
