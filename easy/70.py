from functools import lru_cache

n = 38


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(0, n)

    @lru_cache()
    def helper(self, x: int, stop: int) -> int:
        if x > stop:
            return 0
        if x == stop:
            return 1

        return self.helper(x + 1, stop) + self.helper(x + 2, stop)


result = Solution().climbStairs(n=n)
print(result)  # 63245986
