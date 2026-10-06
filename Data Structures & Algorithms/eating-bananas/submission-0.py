class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)

            if total > h:
                l = mid+1
            else:
                r = mid-1
                res = min(res, mid)

        return res
