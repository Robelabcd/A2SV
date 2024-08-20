class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        '''
        Assume infinite champagne poured = Amount

        0th row:  0th glass  ----> takes 1 and poured (Amount-1)

        1th row: 0th glass --> 0.5 * 0th glass_leftover(Amount-1)
                 1th glass --> 0.5 * 0th glass_leftover(Amount-1)

        2nd row:
            0th glass: only right of 0th glass
            1st glass: left of 0th glass + right of 1st glass
            2nd glass: only left of 1st glass 
        
        --> we only need the two rows, no need to carry the previous rows

        0th row:
            original_row = [poured]

        1st row:
            if excess after reducing one:
                distribute to the left and right of the next row
        '''

        original_row = [poured]

        #Go until the required row inclusive
        for i in range(1, query_row+1):

            cur_row = [0] * (i+1)
            
            for j in range(i):
                excess = original_row[j] - 1
                if excess > 0:
                    cur_row[j] += 0.5 * excess
                    cur_row[j+1] += 0.5 * excess
            
            original_row = cur_row
        
        return min(1, original_row[query_glass]) 
                














        