from typing import List, Dict

EQUIVALENCES = {
    "arttırmak": ["çoğaltmak", "yükseltmek", "artırmak", "geliştirmek", "çoğaltılmak", "arttırılmak"],
    "üretmek": ["oluşturmak", "yapmak", "üretilmek", "hazırlamak", "elde etmek", "ortaya çıkarmak"],
    "güneş": ["ışık", "güneş ışığı", "güneşten enerji", "güneş enerjisi", "ışını", "güneş ışınları"],
    "bitki": ["bitkiler", "yeşil bitkiler", "çiçek", "ağaç", "ot", "üretici canlı", "fotosentetik organizma", "yeşil yapraklı bitki", "alg", "su bitkisi"],
    "glikoz": ["şeker", "karbonhidrat", "besin", "enerji kaynağı", "gıda", "glikoz molekülü", "bitki şekeri", "enerji molekülü"],
    "oksijen": ["o2", "hava", "solunabilir gaz", "atmosfer gazı", "solunum için gerekli gaz", "bitki oksijeni", "ekosistem gazı"],
    "fotosentez": [
        "fotosentez olayı",
        "ışık enerjisi ile besin üretimi",
        "şeker üretimi",
        "bitki besini üretme",
        "bitkilerde glikoz üretimi",
        "karbondioksit ve suyun şeker ve oksijene dönüşümü",
        "bitkilerde enerji üretimi",
        "ışıkla besin oluşturma",
        "güneş ışığı ile enerji üretimi",
        "bitkilerin fotosentezi",
        # Besin zinciri bağlantıları
        "üretici besin kaynağı",
        "besin zinciri başlangıcı",
        "otçulların besini",
        "ekosistem için enerji üretimi",
        "tüketicilere enerji sağlama",
        "besin ağının temeli",
        "fotosentez ve ekosistem dengesi",
        "bitkiler ve otçullar arası ilişki",
        # Çok daha geniş varyasyonlar
        "bitkilerin enerji üretmesi",
        "ışık enerjisini kimyasal enerjiye dönüştürme",
        "karbondioksit tüketimi ve oksijen üretimi",
        "bitki hücrelerinde enerji depolama",
        "güneş enerjisini şeker enerjisine çevirme",
        "otçullar ve diğer tüketiciler için temel besin üretimi",
        "ekosistemde enerji akışı",
        "doğadaki besin döngüsü",
        "bitkilerin yaşamı için gerekli enerji üretimi",
        "biyosferde enerji transferi",
        "karbon döngüsüne katkı",
        "atmosfere oksijen salınımı",
        "fotosentetik süreç",
        "fotosentez ve bitki büyümesi",
        "gıda zincirindeki ilk halkayı oluşturma",
        "enerji dönüşümü ve depolanması",
        "bitki hücrelerinde glikoz üretimi",
        "su ve karbondioksitten besin oluşturma",
        "biyolojik enerji üretimi",
        "bitkilerin yaşam döngüsü ve enerji üretimi",
        "üretici organizmaların besin üretimi",
        "otçullara ve etçillere enerji sağlama",
        "ekosistem dengesi ve enerji akışı",
        "fotosentez ve doğal denge",
        "karbondioksit ve suyun besin ve oksijene dönüşümü",
        "ışık ve klorofil aracılığıyla enerji üretimi",
        "besin zincirinde başlangıç noktası",
        "bitkilerde kimyasal enerji üretimi",
        "doğadaki enerji dönüşümü",
        "yeşil bitkilerin enerji üretimi",
        "fotosentez sırasında oksijen açığa çıkması",
        "bitkilerde glikoz depolama",
        "enerji üretimi ve besin döngüsü"
        #Sınırlayıcılar
        "miktar..." 
    ]
}


class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t["root"] for t in cevap_tokens])
        model_set = set([t["root"] for t in model_tokens])
        ortak = []
        for m in model_set:
            if m in cevap_set:
                ortak.append(m)
            elif m in EQUIVALENCES:
                for eq in EQUIVALENCES[m]:
                    if eq in cevap_set:
                        ortak.append(m)
        return ortak
