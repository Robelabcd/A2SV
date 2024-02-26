class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        group = defaultdict(list)

        for i in range(m):
            for j in range(n):
                idx = i + j
                group[idx].append(mat[i][j])
        
        ans = []
        for idx in range(0, m + n - 1):
            if idx % 2 == 0:
                ans.extend(group[idx][::-1])
            else:
                ans.extend(group[idx])

        return ans