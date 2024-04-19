# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # if not head:
        #     return None

        dummy = ListNode(0)
        dummy.next = head
        before_swap = dummy

        for _ in range(left-1):
            before_swap = before_swap.next

        '''
        1             2    3    4           5
        bef_sw        sf   sl

        2 - 4
        3 - 2

        '''

        
        swap_follow = before_swap.next
        swap_lead = swap_follow.next

        for _ in range(right-left):
            swap_follow.next = swap_lead.next
            swap_lead.next = before_swap.next
            before_swap.next = swap_lead
            swap_lead = swap_follow.next


        return dummy.next


        