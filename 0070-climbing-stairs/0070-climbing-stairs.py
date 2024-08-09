class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        stairs - ways to get there

        1 - 1 = 1 way
        2 - 1+1, 2 = 2 ways
        3 - 1+1+1, 1+2, 2+1 = 3 ways
        4 - 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 = 5ways

        recurrence relation => T(n) = T(n-1) + T(n-2)
                e.g for n = 4: T(4) = T(3) + T(2) = 3 + 2 = 5 ways 
        '''
        
        
        #Problem: TLE
        #recursive solution
        '''
        def rec(n):

            if n == 1:
                return 1

            if n == 2:
                return 2

            return rec(n-1) + rec(n-2)

        
        return rec(n)
        
        '''


        #Top-down approach / memoization


        memo = {1:1, 2:2}
        def dp(n):

            if n in memo:
                return memo[n]

            else:
                memo[n] = dp(n-1) + dp(n-2)


            return memo[n]

        
        return dp(n)




























            