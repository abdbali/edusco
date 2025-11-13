from typing import List, Dict

# Basit eşanlamlı sözlük
EQUIVALENCES = {
    "arttırmak": ["çoğaltmak", "yükseltmek", "artırmak"],
    "üretmek": ["oluşturmak", "yapmak", "üretilmek"],
    "güneş": ["ışık"],
    "bitki": ["bitkiler"],
    "glikoz": ["şeker"],
    "oksijen": ["o2"],
    "fotosentez": ["fotosentez olayı"]
}

class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t["root"] for t in cevap_tokens])
        model_set = set([t["root"] for t in model_tokens])
        ortak = []

        for m in model_set:
            # Direkt eşleşme veya eşanlamlı
            if m in cevap_set:
                ortak.append(m)
            elif m in EQUIVALENCES:
                for eq in EQUIVALENCES[m]:
                    if eq in cevap_set:
                        ortak.append(m)
        return ortak
