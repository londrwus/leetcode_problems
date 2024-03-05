str1 = "ABCABC"
str2 = "ABC"

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1 = str1.replace(f"{str2}", '*')

        if str1.count('*') >= 2:
            return str2
        if str1.count('*') == 1:
            return str2[len(str2)//2:]

        return ''
    
result = Solution().gcdOfStrings(str1=str1, str2=str2)
print(result)