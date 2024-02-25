from typing import List

n = 3


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [f"{i}" for i in range(1, n + 1)]

        for i in range(n):
            iter = i + 1
            if iter % 3 == 0 and iter % 5 == 0:
                output[i] = "FizzBuzz"
            elif iter % 3 == 0 and iter % 5 != 0:
                output[i] = "Fizz"
            elif iter % 3 != 0 and iter % 5 == 0:
                output[i] = "Buzz"
            else:
                output[i] = output[i]

        return output


result = Solution().fizzBuzz(n=n)
print(result)  # ['1', '2', 'Fizz']
