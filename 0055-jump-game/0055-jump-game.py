class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        
        cur = nums[0]
        for i in range(n-1):
            
            if nums[i] > cur:
                cur = nums[i]
            
            if cur == 0:
                return False
            
            cur -= 1
        return True