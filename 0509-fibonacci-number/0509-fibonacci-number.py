class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        def rec(n):
            
            if n is 0 or n is 1:
                return n

            if n in memo:
                return memo[n]

            else:
                memo[n] = rec(n-1) + rec(n-2)

        
            return memo[n]

        return rec(n)