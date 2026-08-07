import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the Min-Heap to track the top k elements.
        """
        self.k = k
        self.min_heap = nums
        
        # Transform the list into a heap in-place in O(n) time
        heapq.heapify(self.min_heap)
        
        # Pop elements until we only have the k largest remaining
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.
        """
        heapq.heappush(self.min_heap, val)
        
        # If adding the new value pushes us over size k, remove the smallest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the Min-Heap is always the kth largest element
        return self.min_heap[0]