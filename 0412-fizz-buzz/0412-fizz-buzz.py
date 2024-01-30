class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 != 0:
                ans.append("Fizz")
            if num % 5 == 0 and num % 3 != 0:
                ans.append("Buzz")
            if num % 5 == 0 and num % 3 == 0:
                ans.append("FizzBuzz")
            if num % 5 != 0 and num % 3 != 0:
                ans.append(str(num))
        return ans
                