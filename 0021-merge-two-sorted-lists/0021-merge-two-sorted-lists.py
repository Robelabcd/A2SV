# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a dummy node to avoid the edge case at the beginning

        dummy = ListNode(0)
        cur = dummy

        #start iterating through the linked lists
        #by comparing the value

        while list1 and list2:

            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next
        
            #update the cur
            cur = cur.next

        #what if the lists are not equal in size
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        
        return dummy.next