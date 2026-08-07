import pytest
from solution import Solution

@pytest.mark.parametrize("stones, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 3, 6, 2, 4], 1),         # Example 1
    ([1, 2], 1),                  # Example 2
    
    # --- Boundary Constraints (Length) ---
    ([1], 1),                     # Absolute minimum array length
    ([1000], 1000),               # Single massive stone
    
    # --- Complete Destruction Scenarios ---
    ([2, 2], 0),                  # Two identical stones
    ([5, 5, 5, 5], 0),            # Even number of identical stones
    ([1000, 1000], 0),            # Maximum constraint identical stones
    
    # --- Partial Destruction / Identical Stones ---
    ([5, 5, 5], 5),               # Odd number of identical stones
    ([3, 3, 3, 3, 3], 3),         # Larger odd number of identical stones
    
    # --- Extreme Weight Disparities ---
    ([100, 1, 1, 1], 97),         # One massive stone dominating tiny stones
    ([1, 1000], 999),             # Exact two-stone boundary gap
    
    # --- Sequential & Patterned Layouts ---
    ([10, 4, 2, 1], 3),           # Strictly decreasing (10-4=6, 6-2=4, 4-1=3)
    ([1, 2, 4, 8, 16], 1),        # Powers of 2 ascending (16-8=8, 8-4=4, 4-2=2, 2-1=1)
    ([1, 2, 3, 4, 5, 6], 1),      # Simple sequential (6-5=1, 4-3=1, 2-1=1, 1-1=0 -> 1 left)
    
    # --- Random Jumbled Orders ---
    ([7, 9, 3, 2, 8], 1)          # Random permutation simulating multiple swaps
])
def test_lastStoneWeight(stones, expected):
    """
    Validates lastStoneWeight against 15 unique constraint and logic variations.
    """
    sol = Solution()
    # We pass a copy of the list because the solution modifies it in-place
    assert sol.lastStoneWeight_using_min_heap_for_max_heap(stones.copy()) == expected

