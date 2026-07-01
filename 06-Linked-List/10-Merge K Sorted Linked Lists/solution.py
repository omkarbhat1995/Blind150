from typing import List, Optional
import heapq

class ListNode:
    """A Node for the Singly Linked List."""
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list using a Min-Heap.
        """
        heap = []
        
        # 1. Initialize the heap with the first node of each list.
        # We use 'i' as a tie-breaker so Python doesn't try to compare ListNode objects.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        dummy = ListNode()
        curr = dummy
        
        # 2. Continually pop the smallest node and push its next node.
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next