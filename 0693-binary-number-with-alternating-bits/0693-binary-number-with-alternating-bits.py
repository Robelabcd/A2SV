class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        for i in range(3, len(bin(n))):

            if bin(n)[i] == bin(n)[i-1]:
                return False

        return True