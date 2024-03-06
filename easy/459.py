s = "abcabcabcabc"

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in "".join( (s[1:], s[:-1]) )

result = Solution().repeatedSubstringPattern(s=s)
print(result)