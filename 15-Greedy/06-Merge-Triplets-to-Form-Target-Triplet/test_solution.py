import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("triplets, target, expected", [
    # --- Standard LeetCode Examples ---
    ([[1, 2, 3], [7, 1, 1]], [7, 2, 3], True),                                       # Example 1: Direct merge
    ([[2, 5, 6], [1, 4, 4], [5, 7, 5]], [5, 4, 6], False),                           # Example 2: Overshoot trap

    # --- Triplet Constraints & Exact Matches ---
    ([[7, 2, 3]], [7, 2, 3], True),                                                  # Single triplet, exact match
    ([[1, 1, 1]], [2, 2, 2], False),                                                 # Single triplet, strictly smaller
    ([[3, 3, 3]], [2, 2, 2], False),                                                 # Single triplet, strictly larger
    
    # --- Valid Component Accumulation ---
    ([[5, 1, 1], [1, 5, 1], [1, 1, 5]], [5, 5, 5], True),                            # Perfect distribution across 3 valid triplets
    ([[5, 1, 1], [1, 5, 1], [1, 6, 5]], [5, 5, 5], False),                           # Third triplet invalidates the 'z' target by carrying a '6' in 'y'

    # --- Duplicates & Padding ---
    ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], [2, 2, 2], True),                            # Identical duplicates
    ([[5, 2, 2], [2, 5, 5], [10, 10, 10]], [5, 5, 5], True),                         # Valid targets present alongside a massive ignorable invalid triplet

    # --- Near Misses & Disconnected Targets ---
    ([[5, 4, 4], [4, 5, 4]], [5, 5, 5], False),                                      # Close but missing the third target dimension
    ([[5, 10, 1], [10, 5, 1], [1, 1, 5]], [5, 5, 5], False),                         # Every target dimension exists, but they are all coupled with overshoot values
    
    # --- Maximum & Minimum Value Boundaries ---
    ([[100, 100, 100]], [100, 100, 100], True),                                      # Maximum constraints simulator
    ([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [3, 3, 3], True),                 # Ordered staircase where target is in the middle

    # --- Two-Part Combos ---
    ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),                            # Triplet 1 gives 'x', Triplet 3 gives 'y' and 'z'. Triplet 2 is ignored.
    ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False)                                       # Every single item is larger than the target 'y' dimension
])
def test_mergeTriplets(triplets, target, expected):
    """
    Tests the mergeTriplets greedy algorithm against 15 distinct boundary, constraint, and edge cases.
    """
    assert sol.mergeTriplets(triplets, target) == expected