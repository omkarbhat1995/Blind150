import pytest
from solution import Solution, Interval

sol = Solution()

@pytest.mark.parametrize("raw_intervals, expected", [
    # --- Standard Examples ---
    ([[0, 30], [5, 10], [15, 20]], False),               # Example 1: Multiple overlaps
    ([[5, 8], [9, 15]], True),                           # Example 2: Clean separation

    # --- Boundaries and Edge Cases ---
    ([], True),                                          # Empty schedule constraint
    ([[10, 20]], True),                                  # Single meeting constraint
    ([[0, 8], [8, 10]], True),                           # Exact touch (problem states no conflict)
    ([[1, 5], [5, 10], [10, 15]], True),                 # Multiple exact touches

    # --- Overlap Variations ---
    ([[1, 10], [2, 3]], False),                          # Fully contained meeting
    ([[1, 5], [4, 6]], False),                           # Standard partial overlap
    ([[5, 10], [5, 10]], False),                         # Exact duplicates

    # --- Ordering Traps ---
    ([[10, 20], [0, 5]], True),                          # Unsorted valid
    ([[20, 30], [10, 15], [0, 25]], False),              # Unsorted invalid
    ([[100, 200], [300, 400], [200, 250]], True),        # Unsorted, exact touches, and spaced

    # --- Sequences & Chains ---
    ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], True),    # Long contiguous valid sequence
    ([[1, 10], [10, 20], [20, 30], [29, 40]], False),    # Overlap hiding at the very end of a chain
    ([[0, 2], [1, 3], [2, 4]], False),                   # Chained cascading overlaps

    # --- Extreme Value Constraints ---
    ([[0, 1000000], [1000000, 1000001]], True),          # Maximum possible size constraint testing
])
def test_canAttendMeetings(raw_intervals, expected):
    """
    Tests the canAttendMeetings method against 16 distinct standard, boundary, and edge cases.
    Automatically converts list inputs into Interval objects to match platform architecture.
    """
    # Convert the raw lists into Interval objects for the Solution class
    interval_objects = [Interval(start, end) for start, end in raw_intervals]
    
    assert sol.canAttendMeetings(interval_objects) == expected