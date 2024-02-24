jewels = "aA"
stones = "aAAbbbb"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        d = {}

        for word in jewels:
            d[word] = d.get(word, 0) + 1

        for stone in stones:
            if stone in d:
                cnt += 1

        return cnt


result = Solution().numJewelsInStones(jewels=jewels, stones=stones)
print(result)  # 3
