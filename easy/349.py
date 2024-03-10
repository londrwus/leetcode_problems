from typing import List

nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for num in nums2:
            d[num] = d.get(num, 0) + 1

        for num in nums1:
            if num in d:
                res.append(num)
                del d[num]

        return res


res = Solution().intersection(nums1=nums1, nums2=nums2)
print(res)