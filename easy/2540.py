from typing import List

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                return num

        return -1


res = Solution().getCommon(nums1=nums1, nums2=nums2)
print(res)