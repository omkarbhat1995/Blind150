import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("intervals, queries, expected", [
    # --- Standard LeetCode Examples ---
    ([[1, 3], [2, 3], [3, 7], [6, 6]], [2, 3, 1, 7, 6, 8], [2, 2, 3, 5, 1, -1]),   # Example 1
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),                # Example 2

    # --- Boundaries and Misses ---
    ([[1, 5], [10, 15]], [0, 6, 9, 16], [-1, -1, -1, -1]),                         # Completely out of bounds queries
    ([[1, 2], [3, 4]], [2, 3], [2, 2]),                                            # Queries exactly on the boundaries
    
    # --- Exact Point Intervals ---
    ([[2, 2], [4, 4], [6, 6]], [1, 2, 3, 4, 5, 6, 7], [-1, 1, -1, 1, -1, 1, -1]),  # Point intervals with misses in between
    ([[5, 5]], [5], [1]),                                                          # Single exact point match

    # --- Nested & Overlapping Intervals ---
    ([[1, 10], [2, 9], [3, 8], [4, 7]], [5], [4]),                                 # Deeply nested intervals (should pick innermost)
    ([[1, 5], [4, 8], [7, 10]], [4, 7], [5, 4]),                                   # Overlapping ties (picks first encountered matching length if tied)
    ([[1, 10], [5, 5]], [5], [1]),                                                 # Massive interval hiding a tiny point interval

    # --- Duplicates & Identical States ---
    ([[1, 5], [1, 5], [1, 5]], [3], [5]),                                          # Exact duplicate intervals
    ([[1, 3]], [2, 2, 2, 2], [3, 3, 3, 3]),                                        # Duplicate queries

    # --- Array Size Constraints & Edge Cases ---
    ([[1, 10000000]], [1, 5000000, 10000000], [10000000, 10000000, 10000000]),     # Maximum coordinate boundaries
    ([[1, 2]], [1], [2]),                                                          # Minimal interval constraint
    
    # --- Disjoint and Separated ---
    ([[10, 20], [30, 40], [50, 60]], [15, 35, 55], [11, 11, 11]),                  # Widely spaced intervals
    ([[1, 2], [11, 12], [21, 22]], [1, 11, 21], [2, 2, 2]),                        # Spaced out short intervals
])
def test_minInterval(intervals, queries, expected):
    """
    Tests the minInterval method against 15 distinct boundary, overlap, and edge cases.
    """
    assert sol.minInterval(intervals, queries) == expected