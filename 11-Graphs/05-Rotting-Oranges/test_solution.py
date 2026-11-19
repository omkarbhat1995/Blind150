import copy
import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("grid, expected", [
    # --- Standard Examples ---
    ([[1, 1, 0], [0, 1, 1], [0, 1, 2]], 4),                     # Example 1
    ([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1),                    # Example 2 (diagonal unreachable)
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),                     # Classic LeetCode example

    # --- Single Cell Boundaries ---
    ([[0]], 0),                                                 # Single empty cell
    ([[1]], -1),                                                # Single fresh fruit (impossible)
    ([[2]], 0),                                                 # Single rotten fruit (0 minutes)

    # --- Uniform Grids ---
    ([[0, 0], [0, 0]], 0),                                      # All empty cells
    ([[2, 2], [2, 2]], 0),                                      # All already rotten
    ([[1, 1], [1, 1]], -1),                                     # All fresh, no rotten source

    # --- Multi-Source & Linear Spreads ---
    ([[2, 1, 1, 1, 2]], 2),                                     # Simultaneous rot from both ends
    ([[2, 1, 1, 1, 1]], 4),                                     # Single row linear spread
    ([[1], [1], [1], [2]], 3),                                  # Single column linear spread

    # --- Obstacles & Disconnected Components ---
    ([[2, 1, 0, 1]], -1),                                       # Empty cell blocks one fresh fruit
    ([[2, 1, 0, 1, 2]], 1),                                     # Disconnected regions, both have sources
    ([[2, 1, 1], [0, 0, 1], [1, 1, 1]], 6),                     # Winding snake path around obstacles
])
def test_orangesRotting(grid, expected):
    """
    Tests the orangesRotting multi-source BFS algorithm against 15 distinct
    standard, boundary, and edge cases.
    """
    test_grid = copy.deepcopy(grid)
    assert sol.orangesRotting(test_grid) == expected