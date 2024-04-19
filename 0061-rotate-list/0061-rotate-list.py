# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        dummy = ListNode()
        dummy.next = head
        # prev = dummy
        cur = dummy.next

        
        # while k > 0:
        #     while cur and cur.next:
        #         cur = cur.next
        #         prev = prev.next

        #     cur.next = dummy.next
        #     dummy = cur
        #     cur = dummy.next
        #     prev = du
            
        #     k -= 1

        # return dummy.next
        count = 1
        while cur and cur.next:
            cur = cur.next
            count += 1
        m = k % count
        print(count, m)
        #cur.next = dummy.next   #create a loop
        if m == 0:
            return head

        ahead = behind = head

        j = m
        while j > 0:
            ahead = ahead.next
            j -= 1

        for _ in range(count - m - 1):
            ahead = ahead.next
            behind = behind.next

        print(ahead.val, behind.val)
        new_head = behind.next
        prev_head = dummy.next
        dummy.next = new_head
        ahead.next = prev_head
        behind.next = None

        return dummy.next
            








            