from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists in reverse order.
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Loop continues as long as there is a node in l1, l2, or a lingering carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate current total and the carry for the next decimal place
            total = val1 + val2 + carry
            carry = total // 10
            
            # Append the 1s digit to the result list
            curr.next = ListNode(total % 10)
            
            # Advance all pointers
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next