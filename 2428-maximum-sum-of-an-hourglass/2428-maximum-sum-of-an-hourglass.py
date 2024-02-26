class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        lst = []
        for i in range(len(grid) - 2):
            for j in range(0, len(grid[i]) - 2):
                count = 0
                count += sum(grid[i][j:j+3])
                count += grid[i+1][j+1]
                count += sum(grid[i+2][j:j+3])
                lst.append(count)

        return max(lst)