class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = height.copy()
        for i in range (1,n):
            prefix_max[i] = max(prefix_max[i-1], height[i])

        suffix_max = height.copy()
        for i in range (n-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1], height[i])

        total = 0
        for i in range(len(height)):
            left_max = prefix_max[i]
            right_max = suffix_max[i]

            if height[i] < left_max and height[i] < right_max:
                total += min(left_max, right_max) - height[i]
        
        return total


        