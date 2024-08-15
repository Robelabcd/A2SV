class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        
        dp = [[0]*(m) for _ in range(n)]
        
    
        for i in range(n):
            for j in range(m):

                up = dp[i-1][j] if i-1 >= 0 else inf 
                left = dp[i][j-1] if j-1 >= 0 else inf

                minn = min(up, left) if up != inf or left != inf else 0

                dp[i][j] = grid[i][j] + minn
                

        # print(dp)
        return dp[n-1][m-1]
