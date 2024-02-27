from typing import List

nums = [-2, 0, 3, -5, 2, -1]


class NumArray:
    def __init__(self, nums: List[int]):
        self.num = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num[left : right + 1])


obj = NumArray(nums)
param_1 = obj.sumRange(left=0, right=2)
print(param_1)  # 1
