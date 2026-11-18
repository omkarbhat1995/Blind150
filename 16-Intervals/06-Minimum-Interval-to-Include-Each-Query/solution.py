import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Finds the minimum interval length to include each query point.
        Uses a min-heap to track active intervals by length for sorted queries.
        """
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        min_heap = []  # Stores tuples of (interval_length, right_endpoint)
        res = {}
        i = 0
        
        # Process queries in sorted order to monotonically move through the intervals
        for q in sorted(set(queries)):
            # 1. Push all intervals that start before or at the current query point
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            # 2. Remove all intervals from the heap that end before the current query point
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 3. The top of the heap is the shortest valid interval
            res[q] = min_heap[0][0] if min_heap else -1
            
        # Map the results back to the original query order
        return [res[q] for q in queries]