import re
from difflib import get_close_matches

class ModelCevap:
    def __init__(self, yanitlar):
        if isinstance(yanitlar, str):
            yanitlar = [yanitlar]
        self.yanitlar = [y.strip().lower() for y in yanitlar]


class YazimDuzeltici:
    def __init__(self):
        self.kelimeler = set("""
            fotosentez bitki karbondioksit oksijen su ışık enerji glikoz güneş
            yaprak klorofil besin üretmek karanlık deney kontrol değişken
        """.split())

    def duzelt(self, kelime):
        if kelime.lower() in self.kelimeler:
            return kelime
        eslesen = get_close_matches(kelime.lower(), self.kelimeler, n=1, cutoff=0.8)
        return eslesen[0] if eslesen else kelime

    def cumle_duzelt(self, cumle):
        kelimeler = re.findall(r"\w+|[^\w\s]", cumle)
        duzeltmis = []
        for k in kelimeler:
            if re.match(r"\w+", k):
                duzeltmis.append(self.duzelt(k))
            else:
                duzeltmis.append(k)
        return " ".join(duzeltmis)


class Ontoloji:
    def __init__(self):
        self.kavramlar = {
            "fotosentez": {"fotosentez", "besin üretimi", "bitkilerin besin yapması"},
            "karbondioksit": {"karbondioksit", "co2", "hava gazı"},
            "oksijen": {"oksijen", "o2"},
            "ışık": {"ışık", "güneş", "güneş ışığı"},
            "su": {"su", "h2o"},
            "glikoz": {"şeker", "glikoz", "enerji"},
        }

    def kavram_bul(self, metin):
        bulunan = set()
        m = metin.lower()
        for kavram, ifadeler in self.kavramlar.items():
            for ifade in ifadeler:
                if ifade in m:
                    bulunan.add(kavram)
        return bulunan



class EslesmeMotoru:
    def __init__(self, ontoloji=None):
        self.ontoloji = ontoloji or Ontoloji()

    def benzerlik(self, a, b):
        a_kelimeler = set(re.findall(r"\w+", a.lower()))
        b_kelimeler = set(re.findall(r"\w+", b.lower()))
        if not a_kelimeler:
            return 0.0
        kesisim = len(a_kelimeler & b_kelimeler)
        birlesim = len(a_kelimeler | b_kelimeler)
        return kesisim / birlesim

    def değerlendir(self, model_cevap, ogrenci_cevap):
        en_iyi_skor = 0.0
        kavram_puan = 0.0

        for dogru in model_cevap.yanitlar:
            skor = self.benzerlik(dogru, ogrenci_cevap)
            kavram_model = self.ontoloji.kavram_bul(dogru)
            kavram_ogrenci = self.ontoloji.kavram_bul(ogrenci_cevap)
            ortak = kavram_model & kavram_ogrenci
            if ortak:
                kavram_puan += len(ortak) * 0.1
            if skor > en_iyi_skor:
                en_iyi_skor = skor

        toplam = min(en_iyi_skor + kavram_puan, 1.0)
        return toplam


class Edusco:
    def __init__(self):
        self.yazim = YazimDuzeltici()
        self.ontoloji = Ontoloji()
        self.eslesme = EslesmeMotoru(self.ontoloji)

    def değerlendir(self, model, ogrenci_cevap):
        duzeltmis = self.yazim.cumle_duzelt(ogrenci_cevap)
        skor = self.eslesme.değerlendir(model, duzeltmis)

        # Skor aralıkları → 5 seviye
        if skor < 0.2:
            etiket, seviye = "Yanlış", 0
        elif skor < 0.4:
            etiket, seviye = "Düşük Doğruluk", 1
        elif skor < 0.6:
            etiket, seviye = "Orta", 2
        elif skor < 0.8:
            etiket, seviye = "Yüksek", 3
        else:
            etiket, seviye = "Tam Doğru", 4

        return {
            "duzeltmis": duzeltmis,
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket
        }



if __name__ == "__main__":
    edusco = Edusco()

    # SORU 1: Fotosentez nedir?
    soru1 = ModelCevap([
        "Fotosentez, bitkilerin güneş ışığını kullanarak karbondioksit ve sudan besin (glikoz) ve oksijen üretmesidir."
    ])

    # SORU 2: Fotosentez için hangi maddeler gerekir?
    soru2 = ModelCevap([
        "Fotosentez için karbondioksit, su ve ışık gerekir."
    ])

    # SORU 3: Fotosentez sonucu hangi maddeler oluşur?
    soru3 = ModelCevap([
        "Fotosentez sonucunda glikoz ve oksijen oluşur."
    ])

    cevaplar = [
        ("Fotosentez, bitkilerin ışıkla besin yapmasıdır.", soru1),
        ("Bitkiler su ve karbondioksit alır, güneşle oksijen üretir.", soru1),
        ("Bitkiler besin yapar.", soru1),

        ("Su ve karbondioksit gereklidir.", soru2),
        ("Sadece güneş ışığı yeterlidir.", soru2),
        ("Su, ışık ve karbondioksit gerekir.", soru2),

        ("Oksijen çıkar.", soru3),
        ("Şeker ve oksijen oluşur.", soru3),
        ("Bitkiler enerji üretir.", soru3)
    ]

    print(" FOTOSENTEZ CEVAP DEĞERLENDİRMELERİ\n")
    for cevap, model in cevaplar:
        sonuc = edusco.değerlendir(model, cevap)
        print(f"Cevap: {cevap}")
        print(f"→ Düzeltme: {sonuc['duzeltmis']}")
        print(f"→ Skor: {sonuc['skor']} | Seviye: {sonuc['seviye']} ({sonuc['etiket']})\n")
