from typing import List, Dict

class Extractor:
    def extract(self, tokens: List[str]) -> List[Dict]:
        """
        Basit ÖYN çıkarımı: 
        Özne → ilk isim, Yüklem → ilk fiil (burada tüm kelimeler NOUN olduğu için basit örnek)
        Nesne → geri kalan isimler
        """
        if not tokens:
            return []

        # Basit mantık: ilk kelime özne, son kelime nesne, ortası fiil
        return [{"ozne": tokens[0], "eylem": tokens[1] if len(tokens)>1 else "", "nesne": " ".join(tokens[2:])}]
