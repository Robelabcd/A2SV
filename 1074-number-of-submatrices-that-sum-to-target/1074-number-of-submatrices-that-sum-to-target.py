class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        count = 0
    
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
    
    
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                prefix_sum = {0: 1} 
                cur_sum = 0  
            
            
                for i in range(rows):
                    cur_sum += matrix[i][col_end]
                    if col_start > 0:
                        cur_sum -= matrix[i][col_start - 1]
                
                    if cur_sum - target in prefix_sum:
                        count += prefix_sum[cur_sum - target]
                
                    prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
            
        return count
