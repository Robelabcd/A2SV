class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        
        def count(n):
            if n == 0:
                return 1

            if n < 0:
                return 0

            return self.climbStairs(n-1) + self.climbStairs(n-2)

        return count(n)