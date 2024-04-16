class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        cur = self.head
        
        ind = 0
        while cur:
            if ind == index:
                return cur.val
            cur = cur.next
            ind += 1

        #otherwise
        return -1
        

    def addAtHead(self, val: int) -> None:
        new = Node(val, self.head)
        self.head = new
        

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
            return
        
        cur = self.head
        '''
        1

        curr -> 1 -> 3
        curr.next -> none

        '''
        
        while cur.next:
            cur = cur.next

        cur.next = new

        

    def addAtIndex(self, index: int, val: int) -> None:

        dummy = Node(0, self.head)
        new = Node(val)

        prev = dummy
        cur = self.head

        ind = 0
        while cur:
            if ind == index:
                prev.next = new
                new.next = cur
                break

            cur = cur.next
            prev = prev.next
            ind += 1

        if ind == index:
            prev.next = new

        self.head = dummy.next 

        '''
        A -> B -> C-> None
        dummy -> A
        new = D

        prev -> A
        curr -> B

        A -> D -> B -> C -> None
        
        

        '''  

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0, self.head)
        #new = Node(val)

        prev = dummy
        cur = self.head

        ind = 0
        while cur:
            if ind == index:
                prev.next = cur.next
                break

            cur = cur.next
            prev = prev.next
            ind += 1

        #if ind == index:
        #   prev.next = new

        self.head = dummy.next 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)