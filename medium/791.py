order = "bcafg"
s = "abcd" 

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for word in s:
            d[word] = d.get(word, 0) + 1

        out = ''
        for word in order:
            if word in d.keys():
                out += word * d[word]
                del d[word]

        for word in d:
            out += word * d[word]
        
        return out

res = Solution().customSortString(order=order, s=s)
print(res)