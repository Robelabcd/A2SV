class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def dfs(i, j, seen):
            if i < 0 or i > row-1 or j < 0 or j > col-1 or grid[i][j] == 0:  #not inbound or adjecent to water body
                return 1  #conisder
           
            if seen[i][j]:  #bounded by land or seen before 
                return 0
            

            seen[i][j] = 1
            
            return dfs(i-1, j, seen) + dfs(i+1, j, seen) + dfs(i, j+1, seen) + dfs(i, j-1, seen)  #perimeter
        
        
        row, col = len(grid), len(grid[0])
        
        seen = [[0 for x in range(col)] for y in range(row)]
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:  #the one end of the land is found --no need of the water body
                    return dfs(x, y, seen)                