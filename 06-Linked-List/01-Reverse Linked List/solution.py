from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.
        """
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # Store the next node
            curr.next = prev    # Reverse the pointer
            prev = curr         # Step prev forward
            curr = nxt          # Step curr forward
            
        return prev