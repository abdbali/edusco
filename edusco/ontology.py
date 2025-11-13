from typing import List, Dict

class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t.get("root", t.get("token", "")) for t in cevap_tokens])
        model_set = set([t.get("root", t.get("token", "")) for t in model_tokens])
        ortak = list(cevap_set.intersection(model_set))
        return ortak
