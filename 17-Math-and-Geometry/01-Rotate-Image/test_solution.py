import pytest
from solution import Solution
import copy

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("matrix, expected", [
    # --- Standard LeetCode Examples ---
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    ), # Example 1
    (
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], 
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    ), # Example 2

    # --- Smallest Bounds ---
    (
        [[1]], 
        [[1]]
    ), # 1x1 Matrix (Base constraint bound)
    (
        [[1, 2], [3, 4]], 
        [[3, 1], [4, 2]]
    ), # 2x2 Matrix

    # --- Negative & Mixed Numbers ---
    (
        [[-1, -2], [-3, -4]], 
        [[-3, -1], [-4, -2]]
    ), # All negative numbers
    (
        [[-1000, 1000], [0, -500]], 
        [[0, -1000], [-500, 1000]]
    ), # Max/Min constraint boundaries
    
    # --- Identical Elements & Zeros ---
    (
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ), # All zeros
    (
        [[5, 5], [5, 5]], 
        [[5, 5], [5, 5]]
    ), # All identical elements

    # --- Symmetric / Asymmetric Patterns ---
    (
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
        [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    ), # Identity Matrix (diagonal)
    (
        [[1, 1, 1], [2, 2, 2], [3, 3, 3]], 
        [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
    ), # Horizontal bands become vertical bands
    (
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]], 
        [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    ), # Vertical bands become horizontal bands

    # --- Larger Scale Sequences ---
    (
        [
            [1, 2, 3, 4, 5], 
            [6, 7, 8, 9, 10], 
            [11, 12, 13, 14, 15], 
            [16, 17, 18, 19, 20], 
            [21, 22, 23, 24, 25]
        ],
        [
            [21, 16, 11, 6, 1], 
            [22, 17, 12, 7, 2], 
            [23, 18, 13, 8, 3], 
            [24, 19, 14, 9, 4], 
            [25, 20, 15, 10, 5]
        ]
    ), # 5x5 Matrix (multiple inner rings)

    # --- Edge Cases with Alternating Values ---
    (
        [[1, -1], [-1, 1]], 
        [[-1, 1], [1, -1]]
    ), # 2x2 Checkerboard pattern
    (
        [[1, 2, 1], [2, 1, 2], [1, 2, 1]], 
        [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    ), # 3x3 Checkerboard pattern
    (
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], 
        [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    )  # 4x4 Checkerboard pattern
])
def test_rotate(sol, matrix, expected):
    """
    Tests the rotate method against 15 standard, boundary, and edge cases.
    """
    # Create a deep copy to ensure we don't accidentally mutate the Pytest cache
    matrix_copy = copy.deepcopy(matrix)
    
    # Execute the strictly in-place modification
    sol.rotate(matrix_copy)
    
    # Assert the modified list matches our expected output
    assert matrix_copy == expected