class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        def rec(num):

            if num == n:
                return True

            if num > n:
                return False

            return rec(num*4)


        return rec(4) if n != 1 else True