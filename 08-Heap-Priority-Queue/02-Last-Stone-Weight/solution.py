import heapq
from typing import List

class Solution:
    def lastStoneWeight_using_min_heap_for_max_heap(self, stones: List[int]) -> int:
        """
        Simulates the smashing of the heaviest stones using a Max-Heap.
        Python's heapq is a Min-Heap, so we negate values to invert priority.
        """
        # Negate all values to simulate a Max-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # Process while there are at least two stones
        while len(max_heap) > 1:
            # Pop the two "smallest" (most negative) elements
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            # If they are not equal, push the remainder back
            if second > first:
                heapq.heappush(max_heap, first - second)

        # Return the absolute value of the last stone, or 0 if empty
        return abs(max_heap[0]) if len(max_heap)==1 else 0
    '''
    def lastStoneWeight_using_max_heap(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first-second>0:
                heapq.heappush_max(stones, first-second)
        return stones[0] if len(stones)>0 else 0
    '''