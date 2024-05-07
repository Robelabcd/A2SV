class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ''' 
        base case: index = 0 ----> [1]

        previos = self.rec(2) ----> (1) ----> (0)

        return:
        [1], [1, 1], [1, 2, 1]

        prev = [1, 2, 1] 

        res = [1]

        for i in range(1, len(3))
        res.append(prev[i-1]+prev[i])

        [1] --> [1, 3, 3]



        res.append(1)

        res = [1, 3, 3, 1]
        
        '''

        if rowIndex == 0:
            return [1]

        

        before = self.getRow(rowIndex - 1)


        # 2 ---> 1 ----> 0 and return [1] ---> [1, 1] ----> [1, 2, 1]


        output = [1] #

        for i in range(1, len(before)):
            output.append(before[i-1] + before[i])

        output.append(1)


        return output

















