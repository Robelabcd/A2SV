# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         prev = None
#         cur = head

#         while cur:
#             next_node = cur.next
#             cur.next = prev
#             prev = cur
#             cur = next_node

#         return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

            
        listt = []
        cur = head
        
        while cur:
            listt.append(cur.val)
            cur = cur.next


        reversed_values = listt[::-1]

    
        new_head = ListNode(reversed_values[0])
        cur = new_head
        for val in reversed_values[1:]:
            cur.next = ListNode(val)
            cur = cur.next

        return new_head



             

