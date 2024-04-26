class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.limit = k
        self.count = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        prev_first = self.head.next
        new = Node(value, prev_first, self.head)
        self.head.next = new
        prev_first.prev = new

        self.count += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        prev_last = self.tail.prev
        new = Node(value, self.tail, prev_last)
        self.tail.prev = new
        prev_last.next = new

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

        first = self.tail.prev
        second = self.tail.prev.prev

        self.tail.prev = second
        second.next = self.tail

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