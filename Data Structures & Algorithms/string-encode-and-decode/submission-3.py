class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += st + "🩷"
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("🩷")[:-1]
        

        

