s = "aA"

class Solution:
    def reverseVowels(self, s: str) -> str:
        all_vowels = [i for i in range(len(s)) if str(s[i]) in 'aeiouAEIOU']
        s_list = list(s)

        for i in range(len(all_vowels) // 2):
            last = all_vowels[-1]
            curr = all_vowels[0]

            temp_val = s_list[curr]
            s_list[curr] = str(s_list[last])
            s_list[last] = str(temp_val)

            all_vowels = all_vowels[1:len(all_vowels)-1]

        return "".join(s_list)
    
result = Solution().reverseVowels(s=s)
print(result)