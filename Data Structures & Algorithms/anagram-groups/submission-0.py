class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Preserve original strings before mutating
        mp = {}
        n = len(strs)
        s = strs.copy()
        for i in range(n):
            strs[i] = list(strs[i])
            strs[i].sort()
            strs[i] = "".join(strs[i])
        
        for i in range(n):
            if strs[i] not in mp:
                mp[strs[i]] = []
            mp[strs[i]].append(i)
        
        output = []
        for key, values in mp.items():
            res = []
            # Loop directly through the list provided by .items()
            for val in values:
                res.append(s[val])
            output.append(res)

        
        return output