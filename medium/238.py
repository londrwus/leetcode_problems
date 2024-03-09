from typing import List

nums = [1,2,3,4]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        result = [0]*len(nums)

        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]

        return result
    
res = Solution().productExceptSelf(nums=nums)
print(res)