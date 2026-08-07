import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the K closest points to the origin using a Max-Heap.
        """
        max_heap = []
        
        for x, y in points:
            # Calculate squared distance to avoid expensive square root operations
            dist = (x ** 2) + (y ** 2)
            
            # Push negative distance to simulate a Max-Heap using Python's Min-Heap
            heapq.heappush(max_heap, (-dist, x, y))
            
            # Maintain heap size of exactly k
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the coordinates from the remaining k elements in the heap
        return [[x, y] for dist, x, y in max_heap]