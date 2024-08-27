class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # The number of 1s in 'i' is the number of 1s in 'i // 2' (which is 'i >> 1') plus 'i % 2'
            result[i] = result[i >> 1] + (i & 1)
        
        return result