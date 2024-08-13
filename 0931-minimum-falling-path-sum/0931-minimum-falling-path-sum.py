class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n, m = len(matrix), len(matrix[0])

        for i in range(n-2, -1, -1):
            for j in range(m-1, -1, -1):

                if j == 0:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])

                elif j==m-1:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
                
                else:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j-1])


        return min(matrix[0])      