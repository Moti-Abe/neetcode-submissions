class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tmpp, smpp = {}, {}
        res = ""
        res_len = len(s)
        for c in t:
            tmpp[c] = tmpp.get(c,0) + 1
        def isTrue():
            for key, val in tmpp.items():
                if smpp.get(key, 0) < val:
                    return False
            return True

        l, r = 0, 0
        
        while r < len(s):
            if s[r] in  t:
                smpp[s[r]] = smpp.get(s[r], 0) + 1
            while len(tmpp) == len(smpp) and isTrue():
                 
                if r-l+1 <= res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                if s[l] in smpp:
                    smpp[s[l]] -= 1
                if s[l] in smpp and smpp[s[l]] == 0:
                    del smpp[s[l]]
                l += 1
            r += 1
        return res