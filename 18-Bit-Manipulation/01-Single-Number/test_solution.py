import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    
    # --- Single Element Constraint Boundary ---
    ([1], 1),
    
    # --- Negative Numbers ---
    ([-1, -1, -2], -2),
    ([-5, 2, -5, 2, -3], -3),
    
    # --- Mixed Positive and Negative Numbers ---
    ([2, -2, 2, 4, 4], -2),
    ([100, -100, 100, -50, -50], -100),
    
    # --- Zero Edge Cases ---
    ([2, 2, 0], 0),
    ([-1, 0, -1], 0),
    
    # --- Duplicates Separated by Large Distances ---
    ([7, 3, 5, 3, 7], 5),
    ([10, 20, 30, 20, 10], 30),
    
    # --- Constraint Boundaries for Values ---
    ([10000, 10000, 500], 500),
    ([-10000, -10000, -500], -500),
    
    # --- Sequential vs Scattered Pairs ---
    ([1, 1, 2, 2, 3, 3, 4], 4),          # Sequential pairs
    ([10, 5, 2, 5, 10, 7, 2], 7),        # Highly scattered pairs
])
def test_singleNumber(nums, expected):
    """
    Tests the singleNumber method against 15 standard, boundary, and edge cases.
    """
    sol = Solution()
    assert sol.singleNumber(nums) == expected