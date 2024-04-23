class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack = []

        -- push the indices each time
        -- whenever we encounter biggest value:
        pop() - previous index
        i - current index

        i - pop() -----> the distance
        
        '''

        stack = []  
    
        result = [0]*len(temperatures)


        for i, val in enumerate(temperatures):
            
            while stack and val > temperatures[stack[-1]]:
                pointer = stack.pop()
                result[pointer] = i - pointer

            stack.append(i)


            
        return result



'''
Time complexity ---> O(n)

space complexity
worst case : O(n)
--> when the maximum value is at the end
e.g [23, 22, 21, 20, 19, 29]
[23, 22, ..........] - push until 29
pop
pop.....
-> we start popping after encountering 29


best case: O(1)

with increasing values
e.g [21, 22, 23, 24, 25]
push 
pop
push
pop.....


'''


