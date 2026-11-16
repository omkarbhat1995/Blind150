import pytest
from solution import Solution

sol = Solution()

def normalize(subsets):
    """
    Sorts inner lists and the outer list to ensure order-agnostic comparison[cite: 1, 2].
    Because the problem states 'return the solution in any order', this prevents arbitrary failures[cite: 1, 2].
    """
    return sorted([sorted(sub) for sub in subsets])

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),                       # Example 1
    ([7, 7], [[], [7], [7, 7]]),                                                  # Example 2 (modified value)
    
    # --- Array Size Boundaries ---
    ([0], [[], [0]]),                                                             # Single element (zero)
    ([-20], [[], [-20]]),                                                         # Single element (min constraint)
    ([20], [[], [20]]),                                                           # Single element (max constraint)
    
    # --- No Duplicates (Standard Power Set) ---
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),          # Unique positive values
    ([-1, 0, 1], [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]),     # Unique mixed values
    
    # --- Heavy Duplicates ---
    ([4, 4, 4, 4], [[], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]),                   # All identical
    ([2, 2, 2, 2, 2], [[], [2], [2, 2], [2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2, 2]]), # Max identical scale check
    
    # --- Mixed Duplicates & Unordered Inputs ---
    ([2, 1, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),                       # Unordered identical numbers
    ([1, 2, 1, 2], [[], [1], [1, 1], [2], [1, 2], [1, 1, 2], [2, 2], [1, 2, 2], [1, 1, 2, 2]]), # Multiple pairs
    
    # --- Negative Variations with Duplicates ---
    ([-1, -1, 2], [[], [-1], [-1, -1], [-1, 2], [-1, -1, 2], [2]]),               # Negative dupes
    ([-5, -5, -5], [[], [-5], [-5, -5], [-5, -5, -5]]),                           # All negative dupes
    ([-20, -20, 0], [[], [-20], [-20, -20], [0], [-20, 0], [-20, -20, 0]]),       # Constraint extremes
    ([-10, 10, -10], [[], [-10], [-10, -10], [10], [-10, 10], [-10, -10, 10]]),   # Split unordered negatives
])
def test_subsetsWithDup(nums, expected):
    """
    Tests the subsetsWithDup backtracking logic against 15 distinct test cases[cite: 1, 2].
    Utilizes pytest.mark.parametrize to cleanly evaluate multiple duplicate distribution patterns[cite: 2].
    """
    assert normalize(sol.subsetsWithDup(nums)) == normalize(expected)