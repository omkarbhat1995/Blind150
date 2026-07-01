from typing import Optional

class ListNode:
    """A Node for the Singly Linked List."""
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes in groups of k using O(1) space.
        """
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. Find the k-th node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # 2. Reverse the group
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Stitch the reversed group back into the list
            tmp = groupPrev.next  # type: ignore
            groupPrev.next = kth  # type: ignore
            groupPrev = tmp
            
        return dummy.next
        
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Helper method to find the k-th node from a starting position."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr