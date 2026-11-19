import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("grid, expected", [
    # --- Standard Examples ---
    (
        [
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1],
        ],
        6,
    ),  # Example 1
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),  # Classic LeetCode example

    # --- Minimum Boundaries & Uniform Grids ---
    ([[1]], 1),                                                   # Single cell land
    ([[0]], 0),                                                   # Single cell water
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),                       # All water
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),                       # All land

    # --- 1D Grid Shapes ---
    ([[1, 0, 1, 1, 1, 0, 1, 1]], 3),                              # Single row, multiple islands
    ([[1], [1], [0], [1], [1], [1], [1]], 4),                     # Single column, multiple islands

    # --- Diagonal Traps ---
    (
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
        ],
        1,
    ),  # Checkerboard (diagonals do not connect)
    (
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ],
        4,
    ),  # Two 2x2 islands touching diagonally

    # --- Complex Topologies ---
    (
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ],
        8,
    ),  # Donut / ring shape
    (
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ],
        16,
    ),  # Island nested inside a lake
    (
        [
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        14,
    ),  # Winding spiral / snake island
    (
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
        ],
        3,
    ),  # Multiple islands tied for max area

    # --- Maximum Constraint Stress Test ---
    ([[1] * 50 for _ in range(50)], 2500),                        # Max 50x50 all-land grid (tests recursion limits)
])
def test_maxAreaOfIsland(grid, expected):
    """
    Tests the maxAreaOfIsland method against 15 standard, boundary, and edge cases.
    Passes a fresh copy of the grid to avoid mutating parametrized test data.
    """
    grid_copy = [row[:] for row in grid]
    assert sol.maxAreaOfIsland(grid_copy) == expected