class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        

        left = 0
        right = row * col - 1
        while left <= right:
            mid = (right + left) // 2

            row_mid, col_mid = divmod(mid, col)
            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False    