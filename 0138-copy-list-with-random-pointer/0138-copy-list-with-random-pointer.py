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
        
        '''
        curr = head
        hash = {curr_node: Node(current.value)........}


        ptr = head

        hash[ptr].next = hash.get(ptr.next)
        hash[ptr].random = hash.get(ptr.random)
        ptr ++

        return hash[head]
        '''
        if not head:
            return head

        deep_copy = {}

        start = head
        while start:
            deep_copy[start] = Node(start.val)
            start = start.next

        ptr = head
        while ptr:
            deep_copy[ptr].next = deep_copy.get(ptr.next)
            deep_copy[ptr].random = deep_copy.get(ptr.random)
            ptr = ptr.next

        return deep_copy[head]






















