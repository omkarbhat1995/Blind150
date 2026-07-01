import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Standard LeetCode Examples
    ([3, 4, 5, 6, 1, 2], 1),                                    # Example 1: Rotated right
    ([4, 5, 0, 1, 2, 3], 0),                                    # Example 2: Rotated middle
    ([4, 5, 6, 7], 4),                                          # Example 3: Sorted array (rotated n times)

    # Boundary and Single/Double Element Arrays
    ([1], 1),                                                   # Single element
    ([2, 1], 1),                                                # Two elements, rotated
    ([1, 2], 1),                                                # Two elements, sorted
    
    # Exact Boundary Minimums
    ([2, 3, 4, 5, 1], 1),                                       # Minimum is the absolute last element
    ([5, 1, 2, 3, 4], 1),                                       # Minimum is exactly at index 1

    # Negative Numbers
    ([-5, -4, -3, -2, -1], -5),                                 # Fully sorted negative array
    ([-1, -5, -4, -3, -2], -5),                                 # Negative array rotated
    ([10, 20, 30, -50, -40, -30], -50),                         # Mix of positive and negative

    # Array Parity (Even vs Odd Lengths)
    ([7, 8, 9, 10, 11, 2, 3, 4, 5], 2),                         # Odd length array search
    ([8, 9, 10, 1, 2, 3, 4, 5], 1),                             # Even length array search

    # Values at Extreme Constraints
    ([1000, -1000], -1000),                                     # Absolute max constraint boundaries
    
    # Large Scale Simulation
    (list(range(500, 1000)) + list(range(-1000, 500)), -1000),  # Massive array split perfectly in half
])
def test_findMin(nums, expected):
    """
    Tests the findMin method against 15 standard, boundary, and edge cases,
    evaluating exact match shifts, scale, and numeric limits.
    """
    assert sol.findMin(nums) == expected