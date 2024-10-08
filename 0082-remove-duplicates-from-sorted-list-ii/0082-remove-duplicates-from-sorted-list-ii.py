# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #practice 
        
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = head

        while cur and cur.next:
            
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur = prev.next

            else:
                cur = cur.next
                prev = prev.next

        return dummy.next



        
        