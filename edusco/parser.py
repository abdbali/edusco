from typing import List, Dict

class POSParser:
    def parse(self, tokens: List[str]) -> List[Dict]:
        # Basit örnek: tüm kelimeleri isim (NOUN) olarak işaretle
        return [{"token": t, "pos": "NOUN"} for t in tokens]
