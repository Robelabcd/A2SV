class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        conditions:
        ../   ----> to one step up to the main folder
        ./    ----> stay there
        x/    ----> move to child 'x'

        Use stack to contain the child folder and return the how many childrena re there in the stack to go back to the main folder
        '''

        stack = [] #to store the folders

        #go through the string/log
        for i in range(len(logs)):

            #chack the conditions
            if logs[i] == "./":
                continue   #no need to do any operation

            elif logs[i] == "../":
                if stack:
                    stack.pop()  #one step up to the main folder
                else:
                    continue
            else:

                stack.append(logs[i])  #otherwise add the child folders in the stack

        return len(stack) #number of child folder