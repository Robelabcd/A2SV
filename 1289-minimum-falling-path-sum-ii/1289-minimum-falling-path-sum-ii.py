class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        def dfs(i,j):# i is for row and j is for column
            if i==len(grid):return 0
            if (i,j) in dp:return dp[(i,j)]
            a=float("inf")
            for k in range(len(grid)):
                if j!=k:
                    a=min(dfs(i+1,k),a)
            a=a if a!=float("inf")  else 0
            dp[(i,j)]=grid[i][j]+a
            return dp[(i,j)]
        M=float("inf")
        for i in range(0,len(grid)):
            M=min(dfs(0,i),M)
        #print(dp)
        return M