class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        
        def helper(index):

            if index == 0:
                return nums[index]

            if index < 0:
                return 0

            if dp[index] != -1:
                return dp[index]

            
            rob = nums[index] + helper(index - 2)
            not_rob = 0 + helper(index-1)

            dp[index] = max(rob, not_rob)

            return dp[index]

        
        return helper(n-1)

