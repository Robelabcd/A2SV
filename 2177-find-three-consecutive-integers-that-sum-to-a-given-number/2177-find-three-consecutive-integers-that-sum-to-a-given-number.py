class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result  = []
        if num % 3 == 0:
            x = int(num / 3)
            result.append(x - 1)
            result.append(x)
            result.append(x + 1)
        return result
        