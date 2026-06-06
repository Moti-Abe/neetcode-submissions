class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i

        
        for i in range(len(nums)):
            num = target - nums[i]
            if num in mp and i != mp[num]:
                return [i,mp[num]]
            
        