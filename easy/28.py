haystack = "mississippi"
needle = "issip"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ids = []
        if needle in haystack:
            ids.append([int(i) for i in range(len(haystack)) if needle[0] == haystack[i]])
            for i in range(len(ids[0])):
                if haystack[ids[0][i]:ids[0][i]+len(needle)] == needle:
                    return int(ids[0][i])
                
            return -1
        else:
            return -1
    
result = Solution().strStr(haystack=haystack, needle=needle)
print(result)