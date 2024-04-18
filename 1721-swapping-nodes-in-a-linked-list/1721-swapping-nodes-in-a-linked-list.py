# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        
        count = 0
        cur = head

        while cur:
            cur = cur.next
            count += 1

        left = k
        right = count - k + 1

        swap1 = head
        for _ in range(left-1):
            swap1 = swap1.next

        swap2 = head
        for _ in range(right-1):
            swap2 = swap2.next

        temp = swap1.val
        swap1.val = swap2.val
        swap2.val = temp


        return head
