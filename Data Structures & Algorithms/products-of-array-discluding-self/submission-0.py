class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        n = len(nums)
        if zeros > 1:
            return [0]*n
        if zeros == 1:
            ind = nums.index(0)
            nums[ind] = 1
            res = [0]*n
            product = math.prod(nums)
            res[ind] = product
            return res
        
        product = math.prod(nums)
        for i in range (n):
            nums[i] = product//nums[i]
        return nums
            
