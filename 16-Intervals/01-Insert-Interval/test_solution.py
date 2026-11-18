import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("intervals, newInterval, expected", [
    # --- Standard LeetCode Examples ---
    ([[1, 3], [4, 6]], [2, 5], [[1, 6]]),                                        # Example 1: Merges with two intervals
    ([[1, 2], [3, 5], [9, 10]], [6, 7], [[1, 2], [3, 5], [6, 7], [9, 10]]),      # Example 2: Clean insert, no merges

    # --- Array Size Constraints & Empty Cases ---
    ([], [5, 7], [[5, 7]]),                                                      # Empty intervals list
    ([[1, 5]], [2, 3], [[1, 5]]),                                                # New interval completely absorbed
    ([[2, 3]], [1, 5], [[1, 5]]),                                                # New interval completely absorbs existing
    
    # --- Giant Spans (Massive Merges) ---
    ([[1, 2], [3, 4], [5, 6]], [0, 10], [[0, 10]]),                              # One interval absorbs all existing intervals
    ([[1, 2], [4, 5], [7, 8]], [2, 7], [[1, 8]]),                                # Bridging multiple gaps precisely on boundaries

    # --- Positional Inserts (No Merges) ---
    ([[3, 4], [5, 6]], [1, 2], [[1, 2], [3, 4], [5, 6]]),                        # Insert at the absolute beginning
    ([[1, 2], [3, 4]], [5, 6], [[1, 2], [3, 4], [5, 6]]),                        # Insert at the absolute end
    ([[1, 2], [5, 6]], [3, 4], [[1, 2], [3, 4], [5, 6]]),                        # Clean fit right in the middle

    # --- Exact Boundary Overlaps ---
    ([[1, 5], [6, 8]], [5, 6], [[1, 8]]),                                        # Touching both the left and right neighbor boundaries
    ([[1, 5]], [1, 5], [[1, 5]]),                                                # Exact duplicate interval
    ([[10, 12]], [12, 15], [[10, 15]]),                                          # Connects exactly to the right edge
    ([[10, 12]], [8, 10], [[8, 12]]),                                            # Connects exactly to the left edge

    # --- Point Intervals (Start == End) ---
    ([[1, 5]], [6, 6], [[1, 5], [6, 6]]),                                        # Point interval, no overlap
    ([[1, 5], [8, 10]], [5, 5], [[1, 5], [8, 10]]),                              # Point interval, merges into the edge of an existing one

    # --- Extreme Value Constraints ---
    ([[0, 0]], [0, 100000], [[0, 100000]]),                                      # Maximum size constraint testing
])
def test_insert(intervals, newInterval, expected):
    """
    Tests the insert interval logic against 16 distinct boundary, overlap, and positional edge cases.
    """
    assert sol.insert(intervals, newInterval) == expected