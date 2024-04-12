class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        
        pushed = [1,2,3,4,5], popped = [4,5,3,2,1]

        is it possible to have this sequence by doing and popping the elements

        let's create a test stack to see the possiblities

        test = []
        [1] push elements from pushed stack
        .
        .
        .
        [1, 2, 3, 4] ---> now test == popped
        so pop 4 from test and check for next popped element = 5

        [1, 2, 3] 3 != 5 --->nope so continue pushing

        [1, 2, 3, 5] test == popped
        so pop from test
        .
        .
        .
        [1] test == popped

        now test = [] and also we reached the last element of popped
        so return True
        
        '''

        test = []

        i = j = 0
        while i < len(popped):

            test.append(pushed[i])

            
            while test and test[-1] == popped[j]:
                test.pop()
                j += 1


            #test.append(pushed[i])
            i += 1

        
        if j == len(popped):
            return True

        else:
            return False