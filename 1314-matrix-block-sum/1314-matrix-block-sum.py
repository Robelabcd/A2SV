class Solution:
    
    def pref(self, matrix: List[List[int]]):
        col, row = len(matrix[0]), len(matrix)

        self.prefix = [[0]*(col+1) for c in range(row+1)]
        
        for i in range(row):
            for j in range(col):
                self.prefix[i][j] = matrix[i][j] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]

    
    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
         
        ans = self.prefix[row2][col2] - self.prefix[row1-1][col2] -  self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]

        return ans
    
    
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        self.pref(mat)

        output = [[0]*len(mat[0]) for c in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                right = min(j+k, len(mat[0])-1)
                left = max(j-k, 0)
                top = max(i-k, 0)
                bottom = min(i+k, len(mat)-1)
                output[i][j] = self.sumRegion(top, left, bottom, right)
        
        return output