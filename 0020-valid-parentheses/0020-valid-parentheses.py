class Solution:
    def isValid(self, s: str) -> bool:
        
        hash_map = { '}':'{', ']':'[', ')':'(' }

        stack = []
        for i in range(len(s)):

            if s[i] in hash_map:     #since the closing ones are the keys of the hasm_map
                if stack and stack[-1] == hash_map[s[i]]:
                    #so that means we can pop
                    stack.pop()

                else:
                    return False

            
            #if it's not in a hash_map as a key then it's an open bracket
            else:
                stack.append(s[i])


        #once it finish the loop and the stack is empty, 
        #that means the string is valid
        return False if stack else True
