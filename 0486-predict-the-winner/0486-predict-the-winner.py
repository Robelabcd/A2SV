class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]
        
        # Base case: when there's only one element to pick, the score difference is that element itself
        for i in range(n):
            dp[i][i] = nums[i]
        
        for length in range(2, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1
                # The current player can either pick nums[i] or nums[j]
                pick_left = nums[i] - dp[i + 1][j]
                pick_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)
        
        # If dp[0][n-1] is non-negative, player 1 can win or tie
        return dp[0][n - 1] >= 0
