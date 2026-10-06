class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l, r = 0, 0
        n, m = len(nums1), len(nums2)
        nums = []
        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                nums.append(nums1[l])
                l += 1
            else:
                nums.append(nums2[r])
                r += 1
        
        while l < n:
            nums.append(nums1[l])
            l += 1
        
        while r < m:
            nums.append(nums2[r])
            r += 1
        
        median = 0
        if len(nums)%2 != 0:
            median = nums[len(nums)//2]
        else:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
            
        return median
