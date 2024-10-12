# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
            

    def merge(self,left, right):
        sorted_arr = ListNode()
        current = sorted_arr
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left:
            current.next = left
        if right:
            current.next = right


        return sorted_arr.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lefthalf = head#4
        righthalf = self.findmid(head)#2
        pointer = righthalf.next#1
        righthalf.next = None
        righthalf = pointer
        left_sorted = self.sortList(lefthalf)
        right_sorted = self.sortList(righthalf)
        return self.merge(left_sorted, right_sorted)
        
       

        