class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(s)
            res.append("🩷")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        return s.split("🩷")[:-1]
        

        

