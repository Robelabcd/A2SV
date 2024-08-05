class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        '''
        [1, 2, 3]

        with 1, with 2, with 3
        breaking down problems: 
               [1]                      [2].                       [3]
        [1, 2]     [1, 3].       [2, 1]     [2, 3].        [3, 1].     [3, 2]

        [1, 2, 3]. [1, 3, 2].    [2, 1, 3]. .............

        
        base case: if len(sol) = len(nums),  append copy of sol and return
        '''

        res, sol = [], []


        def backtrack():

            #basecase
            if len(sol) == len(nums):
                res.append(sol[:])
                return


            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res
        










