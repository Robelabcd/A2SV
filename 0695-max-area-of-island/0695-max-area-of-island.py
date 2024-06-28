class Solution:
    #approach ---> not okay to go over the grid

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #global variable - to store visted box.
        visited = set()


        def inbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True

            return False

        def dfs(i, j):

            #base case
            #out of border or water area
            if (not inbound(i, j)) or grid[i][j] != 1:
                return 0

            if (i, j) in visited:
                return 0

            #mark it as visited
            visited.add((i, j))

            #initialize area
            area = 1


            #directions - up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for row_change, col_change in directions:
                
                area += dfs(i+row_change, j+col_change)


            return area


        #step 1 ---> iterate through the grid
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                #search for land

                if grid[i][j] == 1 and (not ((i, j) in visited)):
                    area = dfs(i, j)  #---> step 2: return area for each separate islands
                    max_area = max(max_area, area)


        return max_area


        
