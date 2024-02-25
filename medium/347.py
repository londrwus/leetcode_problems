from typing import List

nums = [1, 1, 1, 2, 2, 3]
k = 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        out = [[] for i in range(len(nums) + 1)]

        for num in nums:
            d[num] = d.get(num, 0) + 1

        for key, value in d.items():
            out[value].append(key)

        ans = []
        for i in range(len(out) - 1, 0, -1):
            if len(out[i]) >= 1:
                ans.extend(out[i])
                if len(ans) == k:
                    return ans


result = Solution().topKFrequent(nums=nums, k=k)
print(result)  # [1, 2]
