n = 00000000000000000000000000001011


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count("1")


result = Solution().hammingWeight(n=n)
print(result) # 3
