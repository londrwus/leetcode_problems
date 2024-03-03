from typing import List

nums = [1,2,3,4]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = 0
        for num in nums:
            cnt += num
            ans.append(cnt)

        return ans
    
result = Solution().runningSum(nums=nums)
print(result)  # [1, 3, 6, 10]