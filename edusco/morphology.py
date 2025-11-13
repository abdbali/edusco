from typing import Dict

class MorphologyAnalyzer:
    def analyze(self, token: str) -> Dict:
        # Basit: kök = kelime kendisi
        return {"text": token, "root": token}
