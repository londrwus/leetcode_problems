from typing import List

nums = [-1,-2,-3,-4,3,2,1]

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num == 0:
                return 0 
            
            res *= num

        if res > 0:
            return 1
        else:
            return -1

res = Solution().arraySign(nums=nums)
print(res)