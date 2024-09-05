class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        x ^ x = 0
        Xoring every element : twice appearance == 0 and left with unique ones
        
        3 : 0011
        5 : 0101

        3^5 = 0110

        '''
        
        total_xor = 0
        for x in nums: total_xor ^= x

        bit = 31
        while bit >= 0:
            if (total_xor >> bit) & 1:
                break
            bit -= 1
        
        x = 0 
        y = 0
        for num in nums:
            
            if (num >> bit) & 1:
                x ^= num
            
            else:
                y ^= num
        
        
        return [x, y]
