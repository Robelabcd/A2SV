# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        listt = set()
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur:

            if cur in listt:
                return True

            listt.add(cur)
            cur = cur.next

        return False
