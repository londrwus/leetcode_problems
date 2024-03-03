word1 = "abc"
word2 = "pqr"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = []
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            final.append(word1[i])
            final.append(word2[i])

        final.extend([word1[min_len:], word2[min_len:]])

        return ''.join(final)
    
result = Solution().mergeAlternately(word1=word1, word2=word2)
print(result)