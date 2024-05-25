"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #practice - not for the first timee
        if not head:
            return 

        #create a hashmap to copy the value
        copy = {}
        start = head

        while start:
            copy[start] = Node(start.val)
            start = start.next

        
        ptr = head
        while ptr:
            copy[ptr].next = copy.get(ptr.next)
            copy[ptr].random = copy.get(ptr.random)
            ptr = ptr.next

        return copy[head]





















