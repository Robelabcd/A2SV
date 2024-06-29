class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        '''
        possible Road routes

        1 - 3, 5
        2 - 5, 6
        3 - 2, 5, 6
        4 - 2, 5, 6
        5 - 1, 4
        6 - 1, 3


        source - (0, 0) & destination - (len(grid)-1, len(grid[0])-1)
        
        '''
        def inbound(x, y):

            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        visited = set()

        n, m = len(grid), len(grid[0])

        graph = {
            1: [(0, -1, [1, 4, 6]), (0, 1, [1, 3, 5])],  # left, right
            2: [(-1, 0, [2, 3, 4]), (1, 0, [2, 5, 6])],  # up, down
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])],  # left, down
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],   # right, down
            5: [(0, -1, [1, 4, 6]), (-1, 0, [2, 3, 4])], # left, up
            6: [(0, 1, [1, 3, 5]), (-1, 0, [2, 3, 4])]   # right, up
        }

        def dfs(i, j):

            #base case
            if i == n-1 and j == m-1:
                return True

            visited.add((i, j))
            
            #direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for x, y, valid in graph[grid[i][j]]:
                if inbound(i+x, j+y) and grid[i+x][j+y] in valid and (i+x, j+y) not in visited:
                    if dfs(i+x, j+y):
                        return True

            return False

        return dfs(0, 0)
            


        
