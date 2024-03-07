class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        minSum = 0
        mid = len(nums)//2
        for ind in range(mid):
            if nums[ind] + nums[-ind-1] > minSum:
                minSum = nums[ind] + nums[-ind-1]
        return minSum