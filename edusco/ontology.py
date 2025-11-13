from typing import List, Dict

class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t["root"] for t in cevap_tokens])
        model_set = set([t["root"] for t in model_tokens])
        return list(cevap_set.intersection(model_set))
