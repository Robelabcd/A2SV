class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        initial = 2
        
        if n == 1:
            return 0
        else:
            
            while n > 1:
                
                if n % initial == 0:
                    res += initial
                    n = n // initial
                else:
                    initial = initial + 1
                    
            return res