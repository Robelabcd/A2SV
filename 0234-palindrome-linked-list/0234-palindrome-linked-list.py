# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #now reverse the direction from the middle to last
        #slow is now at the middle

        prev = None
        while slow:
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt

        #compare 
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            right = right.next
            left = left.next

        return True