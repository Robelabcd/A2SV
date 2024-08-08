class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
        two options:
            - use open parentheses as long as num_open_p <= n

            - use close parentheses if num_open_p > num_close_p
        
        '''
        

        res, sol = [], []

        def backtrack(open_p, close_p):

            #base case: if solution includes all parentheses 
            if len(sol) == 2*n:
                res.append(''.join(sol))


            #open_parentheses
            if open_p < n:
                sol.append('(')
                backtrack(open_p+1, close_p)
                sol.pop()

            
            #close parentheses
            if close_p < open_p:
                sol.append(')')
                backtrack(open_p, close_p + 1)
                sol.pop()
            
        
        backtrack(0, 0)

        return res

