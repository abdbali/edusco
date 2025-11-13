from typing import List, Dict

class PronounResolver:
    def __init__(self):
        self.last_subject = None

    def resolve(self, tokens: List[str]) -> List[str]:
        resolved = []
        for t in tokens:
            if t.lower() in ["o", "bu", "şu", "onlar"]:
                # Basit çözüm: önceki özneyi kullan
                resolved.append(self.last_subject if self.last_subject else t)
            else:
                resolved.append(t)
                self.last_subject = t
        return resolved
