from typing import List

candies = [2,3,5,1,3]
extraCandies = 3

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ds = []
        maxi = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                ds.append(True)
            else:
                ds.append(False)

        return ds

result = Solution().kidsWithCandies(candies=candies, extraCandies=extraCandies)
print(result)