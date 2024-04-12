class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        

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