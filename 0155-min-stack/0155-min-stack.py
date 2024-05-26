'''
    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


Using the built-in function: min() ----> the code got accepted

But how do we make the getMin() operation of a stack O(1)


what if we create another array to store the minimum value each time we push
and pop it each time we pop from stack array

e.g stack = [-2, 1, 3]   min_stack = [-2, -2, -2]

let's add '-3' and now, 
   stack = [-2, 1, 3, -3]   min_stack = [-2, -2, -2, -3]


let's pop from stack

    stack = [-2, 1, 3].   min_stack = [-2, -2, -2]



from this we can simply get the minimum value by doing:  min_stack[-1]
'''


class MinStack:
    def __init__(self):
        self.stack = []     #initialize the main stack
        self.minimum = []   #initialize the stack that store only minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = min(val, self.minimum[-1]if self.minimum else val)
        self.minimum.append(min_value)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()  #also pop the minimum for that position

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1] #now the last element is the minimum
        #O(1) --- time complexity












# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()