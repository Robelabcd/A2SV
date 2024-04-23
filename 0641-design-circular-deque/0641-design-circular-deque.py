class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next




class MyCircularDeque:

    def __init__(self, k: int):
        self.limit = k
        #dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)

        #make connections
        self.tail.prev = self.head
        self.head.next = self.tail

        #we need to count to not be out of the limit given (k)
        self.count = 0

    def insertFront(self, value: int) -> bool:
        #make sure it's not full
        if self.isFull():
            return False

        #otherwise
        previously_first = self.head.next
        curr = Node(value, self.head, previously_first)

        self.head.next = curr
        previously_first.prev = curr

        #increase the count
        self.count += 1
        

        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        prev_last = self.tail.prev
        curr = Node(value, prev_last, self.tail)

        self.tail.prev = curr
        prev_last.next = curr

        self.count += 1

        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        first = self.head.next
        second = self.head.next.next

        self.head.next = second
        second.prev = self.head

        self.count -= 1

        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        last = self.tail.prev
        before_to_last = self.tail.prev.prev

        self.tail.prev = before_to_last
        before_to_last.next = self.tail

        self.count -= 1

        return True
        

    def getFront(self) -> int:

        return self.head.next.val
        

    def getRear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()