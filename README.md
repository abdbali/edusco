<img width="400" height="150" alt="2" src="https://github.com/user-attachments/assets/e37e2906-0163-4069-86f0-277f4ab97ed3" />
<img width="400" height="150" alt="1" src="https://github.com/user-attachments/assets/cb0c3840-5919-4c81-b66c-7891de0d4ef1" />



# Edusco — Anlamsal Öğrenci Cevabı Değerlendirme Sistemi  

**Edusco**, öğrencilerin kısa ve açık uçlu cevaplarını anlam açısından değerlendiren bir Python kütüphanesidir.  
Özellikle fen eğitimi, STEM, robotik ve yapay zeka tabanlı ölçme-değerlendirme çalışmaları için geliştirilmiştir.

---

## 1. Amaç

Edusco, öğrencilerin cevaplarını yalnızca kelime düzeyinde değil, anlam düzeyinde karşılaştırır.  
Bu sayede, farklı biçimlerde ifade edilen ama aynı fikri taşıyan cevapları anlamca eş kabul eder.  

---

## 2. Sistem Bileşenleri

| Aşama | Ad | Açıklama |
|-------|----|----------|
| 1 | Madde ve Model | Değerlendirilecek soru ve doğru cevap modeli sisteme girilir. |
| 2 | Yazım Düzeltici | Öğrencinin cevabındaki yazım hataları düzeltilir. |
| 3 | Ontoloji | Eş anlamlı bilimsel kavramlar (ör. “glikoz” = “şeker”) tanımlanır. |
| 4 | Eşleştirme Motoru | Öğrenci cevabı, modelle yapısal ve anlamsal olarak karşılaştırılır. |
| 5 | Skorlayıcı | Sonuç, beş seviyeli bir doğruluk skalasında değerlendirilir. |

---

## 3. Skor Sistemi (0–4)

| Skor | Etiket | Açıklama |
|------|---------|----------|
| 0 | Yanlış | Cevap tamamen hatalı veya ilgisizdir. |
| 1 | Düşük Doğruluk | Cevap kısmen doğru ancak önemli eksikler veya hatalar içerir. |
| 2 | Orta | Temel fikir doğru ancak ifade eksik veya yüzeyseldir. |
| 3 | Yüksek | Küçük dil hataları olsa da anlam doğru biçimde verilmiştir. |
| 4 | Tam Doğru | Cevap anlamca ve yapısal olarak modelle tamamen uyumludur. |

---

## 4. Fotosentez Konulu Örnekler

### Soru 1: Fotosentez nedir?  
**Model cevap:**  
“Fotosentez, bitkilerin güneş ışığını kullanarak karbondioksit ve sudan besin (glikoz) ve oksijen üretmesidir.”

| Öğrenci Cevabı | Değerlendirme |
|-----------------|----------------|
| Fotosentez, bitkilerin ışıkla besin yapmasıdır. | Tam Doğru |
| Bitkiler su ve karbondioksit alır, güneşle oksijen üretir. | Yüksek |
| Bitkiler besin yapar. | Orta |

---

### Soru 2: Fotosentez için hangi maddeler gerekir?  
**Model cevap:**  
“Fotosentez için karbondioksit, su ve ışık gerekir.”

| Öğrenci Cevabı | Değerlendirme |
|-----------------|----------------|
| Su ve karbondioksit gereklidir. | Orta |
| Sadece güneş ışığı yeterlidir. | Düşük Doğruluk |
| Su, ışık ve karbondioksit gerekir. | Tam Doğru |

---

### Soru 3: Fotosentez sonucu hangi maddeler oluşur?  
**Model cevap:**  
“Fotosentez sonucunda glikoz ve oksijen oluşur.”

| Öğrenci Cevabı | Değerlendirme |
|-----------------|----------------|
| Oksijen çıkar. | Düşük Doğruluk |
| Şeker ve oksijen oluşur. | Tam Doğru |
| Bitkiler enerji üretir. | Orta |


---

## 5. Kurulum

git clone https://github.com/abdbali/edusco.git
cd edusco
pip install -e .

!pip install --upgrade git+https://github.com/abdbali/edusco.git


!pip install --force-reinstall git+https://github.com/abdbali/edusco.git


<img width="675" height="668" alt="image" src="https://github.com/user-attachments/assets/d857df6c-5063-424b-aefd-f7095c520c36" />
