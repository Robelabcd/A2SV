class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n else 0

        dp = [[inf for _ in range(m + 1)] for _ in range(n + 1)]

        dp[n - 1][m] = 1
        dp[n][m - 1] = 1
        
    
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - grid[i][j])
        
        return dp[0][0] 