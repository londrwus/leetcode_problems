from typing import List

nums = [1, 2, 3, 1, 1, 3]


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        d = {}
        for num in nums:
            if num in d:
                cnt += d[num]
                d[num] += 1
            else:
                d[num] = 1

        return cnt


result = Solution().numIdenticalPairs(nums=nums)
print(result)  # 4
