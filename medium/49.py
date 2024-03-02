from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        final = []
        for s in strs:
            abc = "".join(sorted(s))

            if abc in d:
                final[d[abc]].append(s)
            else:
                d[abc] = len(final)
                final.append([s])

        return final


result = Solution().groupAnagrams(strs=strs)
print(result)
