class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, rows, cols, r1, c1, r2, c2):
            if row<0 or col<0 or row>=rows or col>=cols or not land[row][col]:
                return [r1,c1,r2,c2]
            
            r1,c1,r2,c2 = min(r1, row), min(c1,col), max(r2,row), max(c2,col)
            land[row][col] = 0

            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                r1,c1,r2,c2 = dfs(row+dr, col+dc, rows, cols, r1,c1,r2,c2)

            return [r1,c1,r2,c2]

        rows, cols = len(land), len(land[0])
        four_length_arrays = []

        for row in range(rows):
            for col in range(cols):
                if land[row][col]:
                    four_length_arrays.append(dfs(row, col, rows, cols, row, col, row, col))
        
        return four_length_arrays