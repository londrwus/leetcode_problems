from typing import List

arr = [3,5,1]

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s_arr = sorted(arr)
        consq = s_arr[1] - s_arr[0]

        for i in range(len(arr)-1):
            if s_arr[i+1] - s_arr[i] != consq:
                return False
            
        return True
    
res = Solution().canMakeArithmeticProgression(arr=arr)
print(res)