import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("matrix, expected", [
    # --- Standard LeetCode Examples ---
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    ),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    ),
    
    # --- Rectangular (m != n) Variations ---
    (
        [[1, 2], [3, 4], [5, 6]], 
        [1, 2, 4, 6, 5, 3]
    ),
    (
        [[1, 2, 3], [4, 5, 6]], 
        [1, 2, 3, 6, 5, 4]
    ),
    
    # --- Minimal Boundary Constraints (m=1 or n=1) ---
    (
        [[1]], 
        [1]
    ),
    (
        [[1, 2, 3, 4, 5]], 
        [1, 2, 3, 4, 5]
    ),
    (
        [[1], [2], [3], [4], [5]], 
        [1, 2, 3, 4, 5]
    ),
    
    # --- Small Square Dimensions ---
    (
        [[1, 2], [3, 4]], 
        [1, 2, 4, 3]
    ),
    
    # --- Large Square Matrices ---
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    ),
    
    # --- Negative Numbers & Zeroes ---
    (
        [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
        [-1, -2, -3, -6, -9, -8, -7, -4, -5]
    ),
    (
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    (
        [[-1, 0, 1], [-2, 0, 2]],
        [-1, 0, 1, 2, 0, -2]
    ),
    
    # --- Extremely Narrow Matrices ---
    (
        [[7, 8, 9]], 
        [7, 8, 9]
    ),
    (
        [[7], [8], [9]], 
        [7, 8, 9]
    ),
    
    # --- Non-Sequential Random Values ---
    (
        [[99, 44], [11, 22]],
        [99, 44, 22, 11]
    )
])
def test_spiralOrder(matrix, expected):
    """
    Validates spiral matrix traversal over 15 unique structural and value variations.
    """
    assert sol.spiralOrder(matrix) == expected