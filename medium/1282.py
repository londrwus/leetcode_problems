from typing import List

groupSizes = [3, 3, 2, 3, 3, 2, 3, 1, 3, 1, 1, 2, 2]


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        out = []

        for num in groupSizes:
            d[num] = []

        for key, value in enumerate(groupSizes):
            d[value].append(key)

            if len(d[value]) == value:
                out.append(d[value])
                d[value] = []

        return out


result = Solution().groupThePeople(groupSizes=groupSizes)
print(result)  # [[0, 1, 3], [2, 5], [7], [4, 6, 8], [9], [10], [11, 12]]
