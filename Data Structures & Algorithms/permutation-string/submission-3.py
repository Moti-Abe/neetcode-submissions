class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        for i in range (len(s2)-len(s1)+1):
            s = s2[i : i + len(s1)]

            sorted_s = "".join(sorted(s))
            if sorted_s == sorted_s1:
                return True

        return False

