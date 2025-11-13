from edusco import Edusco, EduscoModel

sorular = [
    {"soru": "Fotosentez nedir?", 
     "model": ["bitki", "güneş", "karbondioksit", "su", "glikoz"]},
    {"soru": "Fotosentez için hangi ortam gereklidir?", 
     "model": ["ışık", "su", "karbondioksit", "klorofil", "yaprak"]},
    {"soru": "Fotosentez sonucu ne oluşur?", 
     "model": ["oksijen", "glikoz", "enerji", "su", "bitki"]}
]

cevaplar = [
    "O güneş ışığı ile şeker üretir",
    "Fotosentez için ışık ve yaprak gereklidir",
    "Oksijen ve glikoz oluşur"
]

edusco = Edusco()
for i, soru in enumerate(sorular):
    model = EduscoModel(soru["model"])
    sonuc = edusco.değerlendir(model, cevaplar[i])
    print(f"Soru {i+1}: {soru['soru']}")
    print(f"Cevap: {cevaplar[i]}")
    print(f"Değerlendirme: {sonuc}\n")
