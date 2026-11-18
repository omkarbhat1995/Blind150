from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Calculates the minimum number of meeting rooms required to schedule all meetings.
        Uses a chronological ordering approach (Two Pointers) to track active meetings.
        """
        if not intervals:
            return 0
            
        # Separate and sort start and end times using object attributes
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        
        start_ptr = 0
        end_ptr = 0
        used_rooms = 0
        
        while start_ptr < len(intervals):
            # If the current meeting starts strictly before the earliest ending meeting finishes,
            # we have a conflict and must allocate an additional room.
            if start_times[start_ptr] < end_times[end_ptr]:
                used_rooms += 1
            else:
                # A previous meeting has ended, freeing up a room.
                end_ptr += 1
                
            start_ptr += 1
            
        return used_rooms