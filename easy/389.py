s = "ae"
t = "aea"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        d2 = {}
        for word in s:
            d[word] = d.get(word, 0) + 1

        for word in t:
            d2[word] = d2.get(word, 0) + 1

        for key, value in d.items():
            try:
                d2[key] -= value
            except:
                pass

        return max(d2.items(), key=lambda item: item[1])[0]


result = Solution().findTheDifference(s=s, t=t)
print(result)