from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a sorted list of non-overlapping intervals,
        merging any overlapping intervals in a single pass.
        """
        res = []
        
        for i in range(len(intervals)):
            # If the new interval is completely before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # The rest of the intervals are guaranteed to not overlap, so append them all
                return res + intervals[i:]
                
            # If the new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # If the intervals overlap, mutate the newInterval to merge them
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If the newInterval is the largest and belongs at the very end, append it here
        res.append(newInterval)
        return res