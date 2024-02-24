class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            ints = []
            for j in range(len(matrix)):
                ints.append(matrix[j][i])
            ans.append(ints)
        return ans