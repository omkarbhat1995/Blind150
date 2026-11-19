import pytest
from solution import Solution

sol = Solution()
INF = 2147483647


@pytest.mark.parametrize("grid, expected", [
    # --- Standard Examples ---
    (
        [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ],
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    ),  # Example 1
    (
        [
            [0, -1],
            [INF, INF],
        ],
        [
            [0, -1],
            [1, 2],
        ],
    ),  # Example 2

    # --- Minimum Boundaries & Uniform Grids ---
    ([[0]], [[0]]),                                                 # Single cell treasure
    ([[-1]], [[-1]]),                                               # Single cell water
    ([[INF]], [[INF]]),                                             # Single cell unreachable land
    ([[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]]),                   # All water
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),                           # All treasures
    ([[INF, INF], [INF, INF]], [[INF, INF], [INF, INF]]),           # All land, no treasures

    # --- 1D Grid Shapes ---
    (
        [[INF, INF, 0, INF, -1, INF, 0]],
        [[2, 1, 0, 1, -1, 1, 0]],
    ),  # Single row with multiple treasures and water wall
    (
        [[0], [INF], [INF], [-1], [INF]],
        [[0], [1], [2], [-1], [INF]],
    ),  # Single column with unreachable section

    # --- Multi-Source Competition & Isolation ---
    (
        [
            [0, INF, INF, INF, 0],
            [INF, INF, INF, INF, INF],
        ],
        [
            [0, 1, 2, 1, 0],
            [1, 2, 3, 2, 1],
        ],
    ),  # Competing treasures meeting at equidistant cells
    (
        [
            [0, -1, INF],
            [-1, -1, -1],
            [INF, -1, 0],
        ],
        [
            [0, -1, INF],
            [-1, -1, -1],
            [INF, -1, 0],
        ],
    ),  # Diagonal isolation (diagonals do not connect)
    (
        [
            [INF, INF, INF],
            [INF, 0, INF],
            [INF, INF, INF],
        ],
        [
            [2, 1, 2],
            [1, 0, 1],
            [2, 1, 2],
        ],
    ),  # Center treasure radiating Manhattan distances

    # --- Complex Topology ---
    (
        [
            [0, INF, INF, INF],
            [-1, -1, -1, INF],
            [INF, INF, INF, INF],
            [INF, -1, -1, -1],
            [INF, INF, INF, INF],
        ],
        [
            [0, 1, 2, 3],
            [-1, -1, -1, 4],
            [8, 7, 6, 5],
            [9, -1, -1, -1],
            [10, 11, 12, 13],
        ],
    ),  # Winding snake corridor

    # --- Maximum Constraint Stress Test ---
    (
        [[0 if (r == 0 and c == 0) else INF for c in range(100)] for r in range(100)],
        [[r + c for c in range(100)] for r in range(100)],
    ),  # Max 100x100 grid with single treasure at top-left
])
def test_islandsAndTreasure(grid, expected):
    """
    Tests the islandsAndTreasure method against 15 standard, boundary, and edge cases.
    Copies the grid before in-place modification to preserve parametrized test data.
    """
    grid_copy = [row[:] for row in grid]
    result = sol.islandsAndTreasure(grid_copy)
    assert result is None
    assert grid_copy == expected