class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        row = len(img)
        col = len(img[0])

        new_img = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):

                sum = 0
                count = 0

                for a in (i-1, i, i+1):
                    for b in (j-1, j, j+1):

                        if 0 <= a < row and 0 <= b < col:
                            sum += img[a][b]
                            count += 1

                new_img[i][j] = sum // count

        return new_img