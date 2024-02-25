from typing import List

s = ["H", "e", "l", "l", "o"]

# o l l e h


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s[:] = s[::-1]
        # s.reverse()
        for i in range(len(s) // 2):
            temp = s[-i - 1]
            s[-i - 1] = s[i]
            s[i] = temp

        print(s)


result = Solution().reverseString(s=s)
result  # run program.
