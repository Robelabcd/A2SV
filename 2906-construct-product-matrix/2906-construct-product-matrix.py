class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        mat =  1  2     ans= 24  12
               3  4.         8    6

        forward prodct matrix
        1  2
        6  24

        
        back product matrix

        24 24
        12 4

        '''

        col, row = len(grid[0]), len(grid)

        forward = [[1]*col for c in range(row)]

        #forward[0][0] = grid[0][0]

        product = 1
        for r in range(row):
            for c in range(col):
                forward[r][c] = product % 12345
                product = (product * grid[r][c])%12345
                

        product = 1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                forward[r][c] = (product * forward[r][c])%12345
                product = (product*grid[r][c])%12345

        return forward

























        