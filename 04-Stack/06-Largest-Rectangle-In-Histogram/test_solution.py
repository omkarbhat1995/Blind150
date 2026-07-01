import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("heights, expected", [
    # Standard LeetCode Examples
    ([7, 1, 7, 2, 2, 4], 8),                                # Example 1
    ([1, 3, 7], 7),                                         # Example 2
    ([2, 1, 5, 6, 2, 3], 10),                               # Classic LeetCode Test Case

    # Boundary / Minimal Inputs
    ([1], 1),                                               # Single element
    ([0], 0),                                               # Single zero
    ([5, 5], 10),                                           # Two identical elements

    # Zero Involvements (Gaps)
    ([0, 0, 0, 0], 0),                                      # Completely flat at zero
    ([2, 0, 2], 2),                                         # Valley with zero
    ([5, 4, 0, 4, 5], 8),                                   # Tall bars separated by zero

    # Sequential / Directional States
    ([1, 2, 3, 4, 5], 9),                                   # Strictly increasing
    ([5, 4, 3, 2, 1], 9),                                   # Strictly decreasing
    ([1, 1, 1, 1, 1], 5),                                   # Completely flat plateau
    ([2, 1, 2], 3),                                         # Small valley

    # Complex Landscapes
    ([1, 2, 2, 1], 4),                                      # Symmetrical bump
    ([4, 2, 0, 3, 2, 4, 3, 4], 10),                         # Multiple jagged peaks and valleys
    ([5,5,2,0,0,11,0,5,5,2],11),
    # Extreme Constraints (Max Length & Max Heights)
    ([1000] * 1000, 1000000),                               # Max elements with max height limit
])
def test_largestRectangleArea(heights, expected):
    """
    Tests the largestRectangleArea method against 15+ distinct boundary, layout, and state-change cases.
    """
    assert sol.largestRectangleArea(heights) == expected