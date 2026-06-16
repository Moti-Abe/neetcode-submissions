class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        maxLen, maxFreq = 0, 0
        l, r = 0, 0
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxFreq = max(maxFreq, mp[s[r]])
            while (r-l+1)-maxFreq > k:
                mp[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1

        return maxLen




