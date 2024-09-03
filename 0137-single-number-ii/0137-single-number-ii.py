class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(32):
        
            cnt = 0
            for num in nums:
                if num & (1 << i):
                    cnt += 1
        
            if cnt % 3 != 0:
                res |= (1 << i)
        
        if res >= (1 << 31):
            res -= (1 << 32)
        
        return res  