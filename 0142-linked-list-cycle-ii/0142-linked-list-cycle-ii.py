# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rabbit = turtle = head

        cycle = False

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next

            if turtle == rabbit:
                cycle = True
                break

        if cycle == False:
            return 

        result = head
        while result != rabbit:
            result = result.next
            rabbit = rabbit.next

        return result