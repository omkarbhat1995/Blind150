import pytest
import copy
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("matrix, expected", [
    # --- Standard LeetCode Examples ---
    (
        [[0, 1], [1, 0]], 
        [[0, 0], [0, 0]]
    ),
    (
        [[1, 2, 3], [4, 0, 5], [6, 7, 8]], 
        [[1, 0, 3], [0, 0, 0], [6, 0, 8]]
    ),
    
    # --- No Zeroes & All Zeroes ---
    (
        [[1, 2], [3, 4]], 
        [[1, 2], [3, 4]]
    ),
    (
        [[0, 0], [0, 0]], 
        [[0, 0], [0, 0]]
    ),
    
    # --- Border Zero Cases (Testing the O(1) state tracking) ---
    (
        [[0, 2, 3], [4, 5, 6]], 
        [[0, 0, 0], [0, 5, 6]]
    ),
    (
        [[1, 2], [0, 4], [5, 6]], 
        [[0, 2], [0, 0], [0, 6]]
    ),
    (
        [[0, 1], [2, 3]], 
        [[0, 0], [0, 3]]
    ),
    (
        [[1, 2], [3, 0]], 
        [[1, 0], [0, 0]]
    ),
    
    # --- 1D Array Constraints ---
    (
        [[0]], 
        [[0]]
    ),
    (
        [[1]], 
        [[1]]
    ),
    (
        [[1, 0, 3]], 
        [[0, 0, 0]]
    ),
    (
        [[1], [0], [3]], 
        [[0], [0], [0]]
    ),
    
    # --- Center Crossing & Disjoint Zeroes ---
    (
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]], 
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    ),
    (
        [[1, 0, 3], [4, 5, 6], [7, 8, 0]], 
        [[0, 0, 0], [4, 0, 0], [0, 0, 0]]
    ),
    
    # --- Extreme Values Constraint Bound ---
    (
        [[-2147483648, 1], [1, 2147483647]], 
        [[-2147483648, 1], [1, 2147483647]]
    )
])
def test_setZeroes(matrix, expected):
    """
    Validates in-place matrix zeroing across 15 distinct scenarios.
    Creates a deepcopy to ensure test purity.
    """
    # Create a fresh copy to pass to the in-place solution
    test_matrix = copy.deepcopy(matrix)
    sol.setZeroes(test_matrix)
    
    assert test_matrix == expected