from typing import List

nums = [1,2,2,3,1,4]

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        max_v = max(d.values())

        return sum(int(x) for x in d.values() if x == max_v)
    
res = Solution().maxFrequencyElements(nums=nums)
print(res)