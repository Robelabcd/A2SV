class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c:
            return mat

        store = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                store.append(mat[row][col])

        
        new = []
        res = []
        for i in range(r):
            for j in range(c):

                if store:
                    new.append(store.popleft())

            res.append(new)
            new = []

        return res


