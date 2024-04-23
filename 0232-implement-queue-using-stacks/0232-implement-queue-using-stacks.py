class MyQueue:

    def __init__(self):
        self.stack1 = []  #enqueue stack
        self.stack2 = []  #dequeue stack

        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2: #no element to pop
        #check the other stack
            while self.stack1:
                #if so, transfer by popping
                self.stack2.append(self.stack1.pop())


        return self.stack2.pop() if self.stack2 else -1
        

    def peek(self) -> int:
        if not self.stack2:  
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1] if self.stack2 else -1  #not popping

        

    def empty(self) -> bool:
        #if only both are empty
        return not self.stack1 and not self.stack2

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()