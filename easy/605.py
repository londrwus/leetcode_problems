from typing import List

flowerbed = [0,0]
n = 1

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and (n <= 1)) or (flowerbed[0] == 1 and n == 0):
                return True
            else:
                return False

        for i in range(0, len(flowerbed) - 1):
            if i == 1 and flowerbed[1] == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
            elif i == len(flowerbed) - 2 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i-1] != 1 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                n -= 1

        if n <= 0:
            return True
        else:
            return False

res = Solution().canPlaceFlowers(flowerbed=flowerbed, n=n)
print(res)