# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        once = head
        twice = head

        while twice is not None and twice.next is not None:
            once = once.next
            twice = twice.next.next

        return once 
