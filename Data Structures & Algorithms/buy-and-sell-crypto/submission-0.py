class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_l, max_r = 10000, 0
        l, r = 0, 1
        diff = 0
        while r < len(prices):
            if prices[l] < min_l:
                min_l = prices[l]
                max_r = prices[r]
            max_r = max(max_r, prices[r])
            diff = max(diff, max_r - min_l)
            l += 1
            r += 1
        if diff < 0:
            return 0
        else:
            return diff
