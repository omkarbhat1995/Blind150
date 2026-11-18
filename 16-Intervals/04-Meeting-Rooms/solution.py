from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List['Interval']) -> bool:
        """
        Determines if a person could add all meetings to their schedule without conflicts.
        Sorts the intervals by start time and checks for any overlapping boundaries.
        """
        # Sort intervals based on their start times
        intervals.sort(key=lambda i: i.start)
        
        # Traverse and check if the current meeting starts before the previous one ends
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True