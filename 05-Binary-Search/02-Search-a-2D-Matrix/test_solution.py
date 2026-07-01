import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("matrix, target, expected", [
    # Standard LeetCode Examples
    ([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10, True),             # Example 1: Target exists at the start of a row
    ([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15, False),            # Example 2: Target does not exist

    # Single Element Matrices
    ([[5]], 5, True),                                                           # Single element, target exists
    ([[5]], 2, False),                                                          # Single element, target missing

    # 1D Vector Matrices (Single Row / Column)
    ([[1, 3, 5, 7]], 3, True),                                                  # Single row, target exists
    ([[1, 3, 5, 7]], 8, False),                                                 # Single row, target missing
    ([[1], [3], [5]], 3, True),                                                 # Single column, target exists
    ([[1], [3], [5]], 2, False),                                                # Single column, target missing

    # Boundary Testing (Exact Corners)
    ([[1, 2], [3, 4]], 1, True),                                                # Target is the absolute first element
    ([[1, 2], [3, 4]], 4, True),                                                # Target is the absolute last element

    # Negative Numbers
    ([[-10, -5, -2], [-1, 0, 3]], -5, True),                                    # Finding a negative number
    ([[-100, -50], [0, 50]], -75, False),                                       # Missing negative number
    
    # Missing Target Logic (Out of bounds & Between bounds)
    ([[10, 20], [30, 40]], 5, False),                                           # Target is smaller than the smallest element
    ([[10, 20], [30, 40]], 50, False),                                          # Target is larger than the largest element
    ([[1, 5], [10, 15]], 8, False),                                             # Target falls in the gap between two rows
])
def test_searchMatrix(matrix, target, expected):
    """
    Tests the searchMatrix method against 15 standard, boundary, and edge cases,
    evaluating exact matches, missing items, and varying matrix dimensions.
    """
    assert sol.searchMatrix(matrix, target) == expected