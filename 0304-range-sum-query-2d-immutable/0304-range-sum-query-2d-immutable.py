class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])    #columns
        row = len(matrix)       #rows

        #initialize the prefix sum matrix
        #make it row+1 by column+1 to avoid index out of range problem
        self.prefix_SumMat = [[0]*(col+1) for c in range(row+1)]

        #iterate through the given matrix and start filling the prefix sum matrix
        for i in range(1, row+1):
            
            #initialize the variable that contain the row's prefix sum
            prefix = 0
            for j in range(1, col+1):
                
                prefix += matrix[i-1][j-1]
                #one step up from the current postion contains all the previous prefix sum
                #except the current row's prefix sum
                above_matrix = self.prefix_SumMat[i-1][j]

                #add the above_matrix and prefix to get the current prefix_sum_matrix
                self.prefix_SumMat[i][j] = above_matrix + prefix
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        #adjust the points since we add 1 row and column to the prefix_SumMat 
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1

        #find the prefix sum from (r2, c2) to (0, 0)
        total_prefixMat = self.prefix_SumMat[r2][c2]

        #find the prefix sum from (r1-1, c2) to (0, 0)
        right_top = self.prefix_SumMat[r1-1][c2]
        #find the prefix sum from (r2, c1-1) to (0, 0)
        left_bottom = self.prefix_SumMat[r2][c1-1]

        #store the prefix sum from (r1-1, c2-1) since it's going to be reduced later
        twice_reduced = self.prefix_SumMat[r1-1][c1-1]

        #find the sumRegion(row1, col1, row2, col2)
        answer = total_prefixMat - right_top - left_bottom + twice_reduced

        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



#Time complexity to create the matrix = O(Row*column)
#Time complexity to find the sumRegion = linear time O(1)