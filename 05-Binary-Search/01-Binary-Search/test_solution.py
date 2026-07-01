import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, target, expected", [
    # Standard LeetCode Examples
    ([-1, 0, 2, 4, 6, 8], 4, 3),                                 # Example 1: Target exists in the middle
    ([-1, 0, 2, 4, 6, 8], 3, -1),                                # Example 2: Target does not exist

    # Boundary Cases (Edges of the array)
    ([1, 2, 3, 4, 5], 1, 0),                                     # Target is the very first element
    ([1, 2, 3, 4, 5], 5, 4),                                     # Target is the very last element
    
    # Missing Targets (Out of bounds)
    ([10, 20, 30, 40, 50], 5, -1),                               # Target is smaller than the smallest element
    ([10, 20, 30, 40, 50], 60, -1),                              # Target is larger than the largest element
    
    # Small / Minimal Inputs
    ([5], 5, 0),                                                 # Array length 1, target exists
    ([5], 10, -1),                                               # Array length 1, target missing
    ([2, 8], 2, 0),                                              # Array length 2, target is first
    ([2, 8], 8, 1),                                              # Array length 2, target is second
    ([2, 8], 5, -1),                                             # Array length 2, target missing between elements

    # Negative Number Variations
    ([-10, -5, -2, -1], -5, 1),                                  # All negative numbers
    ([-100, -50, 0, 50, 100], 0, 2),                             # Target is exactly zero

    # Array Parity (Even vs Odd Lengths)
    ([1, 3, 5, 7, 9, 11, 13], 5, 2),                             # Odd length array search
    ([2, 4, 6, 8, 10, 12], 8, 3),                                # Even length array search

    # Massive Scale (Stress testing bounds)
    (list(range(-5000, 5000)), 4999, 9999),                      # Target at the end of a 10,000 element array
    (list(range(-5000, 5000)), -5001, -1),                       # Missing target in a 10,000 element array
])
def test_search(nums, target, expected):
    """
    Tests the binary search method against 15+ standard, boundary, and edge cases,
    evaluating exact matches, missing items, and massive scale inputs.
    """
    assert sol.search(nums, target) == expected