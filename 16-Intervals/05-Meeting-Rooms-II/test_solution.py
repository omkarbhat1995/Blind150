import pytest
from solution import Solution, Interval

sol = Solution()

def build_intervals(intervals_list):
    """Helper to convert a list of lists into a list of Interval objects."""
    return [Interval(start, end) for start, end in intervals_list]

@pytest.mark.parametrize("raw_intervals, expected", [
    # --- Standard LeetCode Examples ---
    ([[0, 40], [5, 10], [15, 20]], 2),                       
    ([[4, 9]], 1),                                           

    # --- Boundaries and Constraints ---
    ([], 0),                                                 
    ([[1, 5], [5, 10], [10, 15]], 1),                        
    ([[1, 10], [2, 3], [4, 5], [6, 7]], 2),                  

    # --- Complete Overlaps (Worst Case) ---
    ([[1, 5], [1, 5], [1, 5], [1, 5]], 4),                   
    ([[1, 10], [2, 9], [3, 8], [4, 7]], 4),                  

    # --- Disjoint and Separated ---
    ([[100, 200], [300, 400], [500, 600]], 1),               
    ([[1, 2], [11, 12], [21, 22], [31, 32]], 1),             

    # --- Shifted Overlaps (Staircase) ---
    ([[1, 3], [2, 4], [3, 5], [4, 6]], 2),                   
    ([[1, 10], [5, 15], [10, 20], [15, 25]], 2),             

    # --- Extreme Value Constraints ---
    ([[0, 1000000], [1000000, 1000001]], 1),                 
    ([[0, 1000000], [0, 1000000], [0, 1000000]], 3),         

    # --- Ordering Traps ---
    ([[20, 30], [10, 15], [0, 5]], 1),                       
    ([[20, 30], [0, 25], [10, 15]], 2),                      
])
def test_minMeetingRooms(raw_intervals, expected):
    """
    Tests the minMeetingRooms method against 15 distinct boundary, overlap, and edge cases.
    """
    intervals = build_intervals(raw_intervals)
    assert sol.minMeetingRooms(intervals) == expected