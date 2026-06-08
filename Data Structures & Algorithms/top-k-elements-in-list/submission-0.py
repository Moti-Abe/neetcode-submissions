class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        sorted_dict = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))

        output = []
        for key, value in sorted_dict.items():
            output.append(key)
            if len(output) == k:
                break
        
        return output
