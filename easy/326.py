n = 27


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n > 2:
                n = n / 3

            return n == 1


result = Solution().isPowerOfThree(n=n)
print(result)
