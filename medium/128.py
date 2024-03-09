from typing import List

nums = [9,1,4,7,3,-1,0,5,8,-1,6]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        d = {}
        cnt = 0
        new_val = 0
        temp = float('-inf')

        for num in nums:
            d[num] = d.get(num, 0) + 1

        for num in sorted(d.keys()):
            if num - 1 == temp:
                new_val += 1
                cnt = max(new_val, cnt)
            else:
                new_val = 0

            temp = num

        return cnt + 1

res = Solution().longestConsecutive(nums=nums)
print(res)