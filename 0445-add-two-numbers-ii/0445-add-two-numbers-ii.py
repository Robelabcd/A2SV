class Solution:
    def reverseLinkedList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev  # Return the reversed list's head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the input lists
        rev_l1 = self.reverseLinkedList(l1)
        rev_l2 = self.reverseLinkedList(l2)

        
        carry = 0
        dummy = ListNode(0)  
        prev = dummy  # Initialize prev to dummy

        while rev_l1 or rev_l2 or carry:
            val1 = rev_l1.val if rev_l1 else 0
            val2 = rev_l2.val if rev_l2 else 0
            total = val1 + val2 + carry
            carry = total // 10  # Update carry

            # Create a new node with the sum digit and append it to the result list
            prev.next = ListNode(total % 10)
            prev = prev.next  # Move prev to the newly added node

            if rev_l1:
                rev_l1 = rev_l1.next
            if rev_l2:
                rev_l2 = rev_l2.next

        # Reverse the result list if needed (again, depends on problem requirements)
        result = self.reverseLinkedList(dummy.next)

        return result  # Return the head of the result list
