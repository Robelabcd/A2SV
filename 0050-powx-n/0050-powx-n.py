class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        '''
        x ^ n

        0 / 0 ---> undefined

        for any number x^0 = 
        '''

        if n == 0:
            return 1

        if n == -1:
            return 1/x
        
        if n == 1:
            return x

        return self.myPow(x*x, n//2) * self.myPow(x, n % 2)