class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col
        

        q = deque()
        count_fresh = 0
        for i in range(row):
            for j in range(col):

                if grid[i][j] == 1:
                    count_fresh += 1

                if grid[i][j] == 2:
                    q.append((i, j))

        if count_fresh == 0:
            return 0 
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q:

            if count_fresh == 0:
                return time

            for _ in range(len(q)):

                r, c = q.popleft()

                for i, j in direction:
                    i, j = i+r, j+c

                    if inbound(i, j) and grid[i][j]==1:
                        grid[i][j] = 2
                        count_fresh -= 1
                        q.append((i, j))

            time += 1
        
        return -1












