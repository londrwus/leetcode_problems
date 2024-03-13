import math

n = 8

class Solution:
    def pivotInteger(self, n: int) -> int:
        res = math.sqrt(n * (n + 1) / 2)

        if res % 1 != 0:
            return -1
        else:
            return int(res)

res = Solution().pivotInteger(n=n)
print(res)