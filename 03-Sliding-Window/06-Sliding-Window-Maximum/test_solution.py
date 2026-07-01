import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, k, expected", [
    # Provided Examples
    ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]), # Example 1
    ([1], 1, [1]),                               # Example 2
    
    # Classic LeetCode & Standard Cases
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1, -1], 1, [1, -1]),                       # Small array, k = 1
    ([9, 11], 2, [11]),                          # Window size equals array size
    
    # Array Trend Constraints
    ([1, 2, 3, 4, 5], 3, [3, 4, 5]),             # Strictly increasing array
    ([5, 4, 3, 2, 1], 3, [5, 4, 3]),             # Strictly decreasing array
    ([2, 2, 2, 2, 2], 3, [2, 2, 2]),             # Stagnant values
    
    # Negative Numbers
    ([-10, -5, -1, -8, -3], 2, [-5, -1, -1, -3]),# All negative values
    ([-7, -8, -7, -6, -7], 3, [-7, -6, -6]),     # Fluctuating negative values
    
    # Extreme Window Sizes
    ([10, 9, 8, 7, 6, 5], 1, [10, 9, 8, 7, 6, 5]), # k = 1 evaluates every single element
    ([1, 2, 3, 4, 5, 6], 6, [6]),                  # k = len(nums) returns single absolute max
    
    # Boundary Value Constraints
    ([10000, 10000, 10000], 2, [10000, 10000]),  # Maximum absolute value constraints
    ([-10000, -10000, -10000], 2, [-10000, -10000]), # Minimum absolute value constraints
    
    # Large Arrays (Simulated)
    ([i for i in range(1000)], 10, [i for i in range(9, 1000)]),       # Large increasing scale
    ([i for i in range(1000, 0, -1)], 10, [i for i in range(1000, 9, -1)]) # Large decreasing scale
])
def test_maxSlidingWindow(nums, k, expected):
    """
    Tests the maxSlidingWindow method against standard, trend, and boundary constraint edge cases.
    """
    assert sol.maxSlidingWindow(nums, k) == expected