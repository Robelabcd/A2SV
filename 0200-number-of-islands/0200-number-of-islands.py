class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                
        def helper(i, j):
            # check inbound
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0' #visited
            
            
            helper(i+1, j) #down
            helper(i-1, j) #up
            helper(i, j+1) #left
            helper(i, j-1) #right
        
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #find land
                if grid[i][j] == '1':
                    num += 1
                    helper(i, j)
        
        return num