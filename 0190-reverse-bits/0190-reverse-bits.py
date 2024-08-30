class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        lenn = 32

        for i in range(lenn):
            
            check = (n >> i) & 1

            res = (res<<1) | check

        return res