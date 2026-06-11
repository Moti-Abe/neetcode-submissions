class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnums = ""
        for i in range (len(s)):
            if s[i].isalnum():
                alnums += s[i].lower()

        l, r  = 0, len(alnums)-1
        while l < r:
            if alnums[l] != alnums[r]:
                return False
            l += 1
            r -= 1
        return True
