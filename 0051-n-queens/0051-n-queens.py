class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
         
        '''
         - placing a queen "Q" without violating the rule

         Rule:
            - more than one Q not allowed in the same column
                keep track of the column
            - No Q in the above diagonal
            - No Q in the below diagonal - no need to check since we're adding "Q" along the way
        '''

         #create the board
        board = [["."]*n for _ in range(n)]

        track_col = set()
        track_right = set()
        track_left = set()

        possible_pos = []
        def backtracking(row):

            #base case
            if row == n:
                possible_pos.append(["".join(r) for r in board])
                return 

            #iterate the col places
            for col in range(n):
                if col in track_col or (row+col) in track_right or (row-col) in track_left:
                    #not possible place
                    continue

                #otherwise
                track_col.add(col)
                track_right.add(row+col)
                track_left.add(row-col)
                #and place the queen
                board[row][col] = "Q"


                #Go to the next row - next Queen
                backtracking(row+1)


                #What if this way doesn't work?
                track_col.remove(col)
                track_right.remove(row+col)
                track_left.remove(row-col)
                #and replace the queen back to '.'
                board[row][col] = "."

        backtracking(0)
        return possible_pos







