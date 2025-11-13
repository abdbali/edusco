from edusco import Edusco, EduscoModel

# Sorular ve model yanıtları
sorular = [
    {"soru": "Fotosentez nedir?", 
     "model": ["bitki", "güneş", "karbondioksit", "su", "glikoz"]},
    {"soru": "Fotosentez için hangi ortam gereklidir?", 
     "model": ["ışık", "su", "karbondioksit", "klorofil", "yaprak"]},
    {"soru": "Fotosentez sonucu ne oluşur?", 
     "model": ["oksijen", "glikoz", "enerji", "su", "bitki"]}
]

# Öğrenci cevapları
cevaplar = [
    "Bitkiler güneş ışığı ve karbondioksit ile glikoz üretir",
    "Fotosentez için ışık, yaprak ve klorofil gerekir",
    "Fotosentez sırasında oksijen ve glikoz oluşur"
]

edusco = Edusco()
for i, soru in enumerate(sorular):
    model = EduscoModel(soru["model"])
    sonuc = edusco.değerlendir(model, cevaplar[i])
    print(f"Soru {i+1}: {soru['soru']}")
    print(f"Cevap: {cevaplar[i]}")
    print(f"Değerlendirme: {sonuc}\n")
