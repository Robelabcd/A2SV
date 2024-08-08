class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n, m = len(board), len(board[0])

        if n == 1 and m == 1:
            return board[0][0] == word

        #step 3:
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        #step 2:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def backtrack(pos, index):
            i, j = pos

            #base-case: reaching the len(word)
            if index == len(word):
                return True
            
            if board[i][j] != word[index]:
                return False

            #avoid repeating same char on the path
            char = board[i][j]
            board[i][j] = '-1'

            for i_chan, j_chan in direction:

                r = i + i_chan
                c = j + j_chan

                if inbound(r, c):
                    if backtrack((r, c), index+1):
                        return True

            

            board[i][j] = char
            return False

        
        #step 1:
        for i in range(n):
            for j in range(m):

                if backtrack((i, j), 0):
                    return True

        return False