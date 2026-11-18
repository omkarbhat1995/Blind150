from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Calculates the minimum number of intervals to remove to make the sequence non-overlapping.
        Uses a Greedy approach by sorting by start time and keeping the interval that ends earlier 
        whenever an overlap is detected.
        """
        if not intervals:
            return 0
            
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        removals = 0
        prev_end = intervals[0][1]
        
        # Iterate starting from the second interval
        for start, end in intervals[1:]:
            # If the current interval starts before the previous one ends, we have an overlap
            if start < prev_end:
                removals += 1
                # Greedily keep the interval that ends earlier to minimize future overlaps
                prev_end = min(prev_end, end)
            else:
                # No overlap, safely update the end pointer to the current interval's end
                prev_end = end
                
        return removals