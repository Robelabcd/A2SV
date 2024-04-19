# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur, cur2 = l1, l2
        dummy = ListNode()
        prev = None

        r = 0    #remainder
        while cur and cur2:

            
            temp = cur.val
            # temp2 = cur2.val
            total =  (cur.val + cur2.val + r) % 10
            # cur2.val =  cur.val
            r = (temp + cur2.val) // 10

            new = ListNode(total)
            prev.next = new
            prev = prev.next

            cur = cur.next
            cur2 = cur2.next


        if cur:
            while cur:
                temp = cur.val
                total = (cur.val + r) % 10
                r = (temp) // 10

                new = ListNode(total)
                prev.next = new
                prev = prev.next

                cur = cur.next
            # return l1

        elif cur2:
            while cur2:
                temp = cur2.val
                total = (cur2.val + r) % 10
                r = (temp) // 10

                new = ListNode(total)
                prev.next = new
                prev = prev.next

                cur2 = cur2.next

            # return l2


        return dummy.next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur, cur2 = l1, l2
        dummy = ListNode(0)  # Initialize dummy with value 0
        prev = dummy  # Initialize prev to dummy

        r = 0  # remainder
        while cur or cur2 or r:
            val1 = cur.val if cur else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + r
            r = total // 10  # Update remainder

            # Create a new node with the sum digit and append it to the result list
            prev.next = ListNode(total % 10)
            prev = prev.next  # Move prev to the newly added node

            if cur:
                cur = cur.next
            if cur2:
                cur2 = cur2.next

        return dummy.next  # Return the head of the result list (excluding dummy)
