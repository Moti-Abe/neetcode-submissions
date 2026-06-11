class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnums = []
        for ch in s:
            if ch.isalnum():
                alnums.append(ch.lower())
        alnums = "".join(alnums)

        l, r  = 0, len(alnums)-1
        while l < r:
            if alnums[l] != alnums[r]:
                return False
            l += 1
            r -= 1
        return True
