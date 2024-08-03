# Defnition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for each in lists:
            cur = each
            while cur:
                heappush(heap, cur.val)
                cur = cur.next

        head = ListNode()
        cur = head

        for _ in range(len(heap)):

            num = heappop(heap)
            cur.next = ListNode(num)
            cur = cur.next

        return head.next