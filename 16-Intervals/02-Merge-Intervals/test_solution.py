import pytest
from solution import Solution

sol = Solution()

def normalize(intervals):
    """
    Sorts the outer list of intervals to ensure order-agnostic comparison.
    Because the problem states 'return the answer in any order', this prevents arbitrary test failures.
    """
    return sorted(intervals)

@pytest.mark.parametrize("intervals, expected", [
    # --- Standard Examples ---
    ([[1, 3], [1, 5], [6, 7]], [[1, 5], [6, 7]]),                                 # Example 1
    ([[1, 2], [2, 3]], [[1, 3]]),                                                 # Example 2

    # --- Array Size Boundaries ---
    ([[1, 5]], [[1, 5]]),                                                         # Single element constraint boundary
    ([[0, 0], [0, 0], [0, 0]], [[0, 0]]),                                         # Minimum values, maximum duplicates
    
    # --- Structural Variations ---
    ([[1, 4], [4, 5]], [[1, 5]]),                                                 # Exact boundary touch (chain link)
    ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], [[1, 10]]),                       # One giant interval entirely engulfs many smaller ones
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),                       # Giant interval at the end (requires sorting to catch)
    ([[1, 4], [0, 4]], [[0, 4]]),                                                 # Out of order, completely swallowed
    ([[1, 4], [2, 5], [7, 9], [14, 18]], [[1, 5], [7, 9], [14, 18]]),             # Classic LeetCode disjoint segments
    ([[1, 4], [0, 1]], [[0, 4]]),                                                 # Out of order overlapping exactly at boundary

    # --- Cascading & Chaining ---
    ([[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 5]]),                                 # Domino chain
    ([[5, 6], [4, 5], [3, 4], [2, 3], [1, 2]], [[1, 6]]),                         # Reverse domino chain

    # --- Duplicate & Redundant Intersections ---
    ([[1, 4], [1, 4], [1, 4]], [[1, 4]]),                                         # Identical duplicates
    ([[1, 4], [2, 3], [1, 4]], [[1, 4]]),                                         # Enclosed duplicates
    ([[2, 6], [2, 6], [2, 6], [2, 6], [2, 6]], [[2, 6]]),                         # High frequency identical intervals
    
    # --- Constraint Boundaries ---
    ([[0, 1000]], [[0, 1000]]),                                                   # Minimum and maximum possible bounds
    ([[0, 1], [999, 1000]], [[0, 1], [999, 1000]]),                               # Dual extremes with massive gap
    ([[100, 200], [150, 1000]], [[100, 1000]]),                                   # Merge extending to maximum bound

    # --- Point Intervals (Start == End) ---
    ([[1, 1], [2, 2], [3, 3]], [[1, 1], [2, 2], [3, 3]]),                         # Distinct points
    ([[1, 2], [2, 2], [2, 3]], [[1, 3]]),                                         # Points connecting valid intervals
])
def test_merge(intervals, expected):
    """
    Tests the merge intervals logic against 19 distinct boundary, edge, and standard cases.
    """
    assert normalize(sol.merge(intervals)) == normalize(expected)