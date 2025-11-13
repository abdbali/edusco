class RubricEvaluator:
    """
    Değerlendirme skoruna göre seviye ve nitelik belirler.
    """
    def __init__(self):
        self.levels = {
            0: (0.0, 0.2),
            1: (0.2, 0.4),
            2: (0.4, 0.6),
            3: (0.6, 0.8),
            4: (0.8, 1.0)
        }

    def evaluate(self, skor: float) -> dict:
        if skor < 0:
            skor = 0
        if skor > 1:
            skor = 1

        for seviye, (alt, ust) in self.levels.items():
            if alt <= skor <= ust:
                break

        aciklama = {
            0: "Yanlış veya alakasız cevap.",
            1: "Kısmen doğru ama eksik veya yüzeysel ifade.",
            2: "Temel kavram doğru ancak açıklama yüzeysel.",
            3: "Açıklama çoğunlukla doğru ve mantıklı.",
            4: "Cevap tamamen doğru ve kapsamlı."
        }

        return {
            "seviye": seviye,
            "skor": round(skor, 2),
            "yorum": aciklama[seviye]   
        }
