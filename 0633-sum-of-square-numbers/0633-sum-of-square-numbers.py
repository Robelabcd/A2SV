import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(math.sqrt(c))
        i, j = 0, limit
    
        while i <= j:

            if (pow(i, 2) + pow(j, 2)) > c:
                j -= 1
            elif (pow(i, 2) + pow(j, 2)) < c:
                i += 1
            elif (pow(i, 2) + pow(j, 2)) == c:
                return True

        return False
