class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}
        for i in range(len(s)):
            smap[s[i]] = s.count(s[i])
            tmap[t[i]] = t.count(t[i])
        
        for c in s:
            if smap[c] != tmap.get(c,0):
                return False
        return True
