#from collections import deque ----not needed here but to use deque we need to import the library

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deque = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        #check if there are k elements
        if len(self.deque) == self.k:
            #if so, check there's a value at from that equals to self.value
            if self.deque[0] == self.value:
                self.count -= 1 #if so, decrease the number of count and pop it
            self.deque.popleft()

        #receive the new element    
        self.deque.append(num)

        #if it satisfy the condition, add the count
        if num == self.value:
            self.count += 1

        #return true if we have enough amount(k) values otherwise false
        return self.count == self.k





# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)