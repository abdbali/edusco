class RubricEvaluator:

    def __init__(self):
        self.kriterler = {
            1: ["besin zinciri", "sürdür", "devam"],
            2: ["üretici", "tüketici", "enerji", "besin"],
            3: ["fotosentez", "üretir", "süreklilik"]
        }

    def değerlendir(self, ortak_kelimeler):
        puan = 0
        kapsanan = []
        for i, kelimeler in self.kriterler.items():
            if any(k in ortak_kelimeler for k in kelimeler):
                puan += 1
                kapsanan.append(i)

        if puan == 0:
            etiket = "İlgisiz veya yanlış cevap"
        elif puan == 1:
            etiket = "Fotosentezin besin zincirini sürdürdüğünü belirtir ancak nedenini açıklamaz."
        elif puan == 2:
            etiket = "Fotosentezin besin zincirindeki önemini ifade eder ve üç bileşenden yalnızca birini açıklar."
        elif puan == 3:
            etiket = "Fotosentezin besin zincirindeki önemini ifade eder ve üç bileşenden ikisini açıklar."
        else:
            etiket = "Fotosentezin besin zincirini sürdürdüğünü ve üç nedenini açıklar."

        return {"puan": puan, "kapsanan_kriterler": kapsanan, "açıklama": etiket}
