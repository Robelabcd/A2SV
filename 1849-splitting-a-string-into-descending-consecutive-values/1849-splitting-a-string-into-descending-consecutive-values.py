class Solution:
    def splitString(self, s: str) -> bool:
        
        def helper(index, val):
            #base case: we we reach the end of the string, return True
            if index == len(s):
                return True  

            for j in range(index, len(s)):
                next_val = int(s[index:j+1])
                '''
                now we can avoid the unnecessary branches: O(n**n) to O(n**2) 
                - next_val == val-1
                e.g:  4321
                4 - 3  ----> only this one will be done because of the condition
                4 - 32
                4 - 321
                
                '''
                if next_val == val-1 and helper(j+1, next_val):   
                    return True

            return False

        for i in range(len(s)-1):  #since we have to split 's' at least into two

            val = int(s[:i+1])
            if helper(i+1, val):           #we need dfs to backtrack and find the required number
                return True

        return False