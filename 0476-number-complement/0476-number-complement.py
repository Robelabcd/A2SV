class Solution:
    def findComplement(self, num: int) -> int:


        lenn_bit = num.bit_length()
        
        return num ^ ((1 << lenn_bit) - 1)