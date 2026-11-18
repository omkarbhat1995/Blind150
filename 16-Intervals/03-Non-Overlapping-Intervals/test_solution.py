import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("intervals, expected", [
    # --- Standard LeetCode Examples ---
    ([[1, 2], [2, 4], [1, 4]], 1),                                     # Example 1: Remove [1,4]
    ([[1, 2], [2, 4]], 0),                                             # Example 2: No overlaps
    ([[1, 2], [1, 2], [1, 2]], 2),                                     # Example 3: Exact duplicates

    # --- Array Size Constraints & Empty Cases ---
    ([[1, 5]], 0),                                                     # Single interval
    ([[1, 2], [3, 4], [5, 6]], 0),                                     # Distinct spaced intervals
    
    # --- Boundary Connections (Touching Intervals) ---
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 0),                             # Perfectly chained, no overlaps
    ([[1, 5], [5, 10], [10, 15]], 0),                                  # Chained with larger ranges

    # --- Enveloping / Greedy Traps ---
    ([[1, 10], [2, 3], [4, 5], [6, 7]], 1),                            # One massive interval overlapping multiple small distinct ones
    ([[1, 4], [3, 6], [2, 8]], 2),                                     # Multiple overlapping lengths
    ([[-50000, 50000], [-50000, 0], [0, 50000]], 1),                   # Maximum constraint bounds overlapping

    # --- Same Start, Different Ends ---
    ([[1, 5], [1, 4], [1, 3], [1, 2]], 3),                             # Should greedily keep [1,2] and remove the rest
    
    # --- Negative Ranges & Crossing Zero ---
    ([[-10, -5], [-7, -2], [-3, 1]], 1),                               # Overlaps purely in negatives
    ([[-5, 5], [-2, 2], [0, 10]], 2),                                  # Zero-crossing overlaps
    
    # --- Cascading Overlaps ---
    ([[1, 3], [2, 4], [3, 5], [4, 6]], 2),                             # Staggered overlapping sequence
    
    # --- Disconnected Overlap Clusters ---
    ([[1, 3], [1, 3], [5, 7], [5, 7], [9, 11], [9, 11]], 3),           # Multiple distinct clusters of overlaps
])
def test_eraseOverlapIntervals(intervals, expected):
    """
    Tests the eraseOverlapIntervals greedy algorithm against 15 distinct boundary, overlap, and edge cases.
    """
    assert sol.eraseOverlapIntervals(intervals) == expected