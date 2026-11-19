import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("grid, expected", [
    # --- Standard LeetCode Examples ---
    (
        [
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),  # Example 1
    (
        [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        4,
    ),  # Example 2
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),  # Classic LeetCode example

    # --- Minimum Boundaries & Uniform Grids ---
    ([["1"]], 1),                                                   # Single cell land
    ([["0"]], 0),                                                   # Single cell water
    ([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]], 0),       # All water
    ([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]], 1),       # All land

    # --- 1D Grid Shapes ---
    ([["1", "0", "1", "1", "0", "1"]], 3),                          # Single row, multiple islands
    ([["1"], ["0"], ["1"], ["0"], ["1"]], 3),                       # Single column, multiple islands

    # --- Diagonal & Corner Traps ---
    (
        [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"],
        ],
        5,
    ),  # Checkerboard (diagonals do not connect)
    (
        [
            ["1", "0", "1"],
            ["0", "0", "0"],
            ["1", "0", "1"],
        ],
        4,
    ),  # Four isolated corners

    # --- Complex Topologies ---
    (
        [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"],
        ],
        1,
    ),  # Donut / ring shape
    (
        [
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "0", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "0", "0", "0", "1"],
            ["1", "1", "1", "1", "1"],
        ],
        2,
    ),  # Island nested inside a lake
    (
        [
            ["1", "1", "1", "1"],
            ["0", "0", "0", "1"],
            ["1", "1", "0", "1"],
            ["1", "0", "0", "1"],
            ["1", "1", "1", "1"],
        ],
        1,
    ),  # Winding spiral / snake island

    # --- Maximum Constraint Stress Test ---
    ([["1"] * 100 for _ in range(100)], 1),                         # Max 100x100 all-land grid (tests recursion limits)
])
def test_numIslands(grid, expected):
    """
    Tests the numIslands method against 15 standard, boundary, and edge cases.
    Passes a fresh copy of the grid to avoid mutating parametrized test data.
    """
    grid_copy = [row[:] for row in grid]
    assert sol.numIslands(grid_copy) == expected