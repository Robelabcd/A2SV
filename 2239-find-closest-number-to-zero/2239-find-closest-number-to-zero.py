class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        num = 1000001

        for i in nums:

            if abs(i) < abs(num):
                num = i

            elif abs(i) == abs(num):
                if i > 0:
                    num = abs(i)
        
        return num
