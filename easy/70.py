from functools import lru_cache


@lru_cache()
def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 1, stop) + f(x + 2, stop)


n = 38


class Solution:
    def climbStairs(self, n: int) -> int:
        return f(0, n)


result = Solution().climbStairs(n=n)
print(result)
