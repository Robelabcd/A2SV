class MyStack:

    def __init__(self):
        self.q = deque()     #double ended queue - G4G for better explanation on this



    def push(self, x: int) -> None:
        self.q.append(x)    #simply append to push an element


    def pop(self) -> int:

        for i in range(len(self.q)-1):   #since we want the last elemet
            self.push((self.q.popleft()))   #pop and append at the end

        return self.q.popleft()  #now pop the first element

    def top(self) -> int:
        return self.q[-1]


    def empty(self) -> bool:
        return len(self.q) == 0   #if true then it's empty



















# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()