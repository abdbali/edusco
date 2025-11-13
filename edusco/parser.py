from typing import List, Dict

class POSParser:
    def parse(self, tokens: List[str]) -> List[Dict]:
        parsed = []
        for t in tokens:
            pos = "NOUN" if t.endswith("mak") or t.endswith("mek") else "NOUN"
            parsed.append({"token": t, "pos": pos, "root": t})
        return parsed
