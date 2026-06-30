from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # pyright: ignore[reportOptionalMemberAccess]
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        second = slow.next # pyright: ignore[reportOptionalMemberAccess]
        prev = None
        slow.next = None  # Split the list into two halves # pyright: ignore[reportOptionalMemberAccess]
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            
        # Step 3: Merge the two halves alternately
        first = head
        second = prev  # 'prev' is the new head of the reversed second half
        
        while second:
            tmp1, tmp2 = first.next, second.next # pyright: ignore[reportOptionalMemberAccess]
            first.next = second # pyright: ignore[reportOptionalMemberAccess]
            second.next = tmp1
            first = tmp1
            second = tmp2