class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_mp = {}
        s2_mp = {}
        for i in range(len(s1)):
            s1_mp[s1[i]] = s1_mp.get(s1[i], 0) + 1
            s2_mp[s2[i]] = s2_mp.get(s2[i], 0) + 1
        
        l, r = 0, len(s1)
        while r <= len(s2):
            if s1_mp == s2_mp:
                return True
            
                
            s2_mp[s2[l]] -= 1
            if s2_mp[s2[l]] == 0:
                del s2_mp[s2[l]]

            if r < len(s2):
                s2_mp[s2[r]] = s2_mp.get(s2[r], 0) + 1
            
            l += 1
            r += 1
            
        
        return False

