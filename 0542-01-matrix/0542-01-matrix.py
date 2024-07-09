from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        
        dist = [[inf] * n for _ in range(m)]
        
        q = deque()
        # (i, j) == 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n:
                
                    if dist[new_x][new_y] > dist[x][y] + 1:
                        dist[new_x][new_y] = dist[x][y] + 1
                        q.append((new_x, new_y))
        
        return dist
