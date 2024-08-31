class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        num = x ^ y
        num_1bit = 0
        for i in range(32):
            if ((num >> i) & 1) == 1:
                num_1bit += 1

        return num_1bit