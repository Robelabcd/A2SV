class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inbound(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False

            return True 
                
        def helper(i, j):
            # check boundary and water territory
            if (not inbound(i, j)) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0' #visited
            
            '''
            helper(i+1, j) #down
            helper(i-1, j) #up
            helper(i, j+1) #left
            helper(i, j-1) #right
            '''
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for row, col in directions:
                helper(i+row, j+col)

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #find land
                if grid[i][j] == '1':
                    helper(i, j)
                    num += 1
        
        return num