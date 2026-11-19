import pytest
from solution import Solution

sol = Solution()


def normalize(coords):
    """
    Sorts the list of [r, c] coordinates for order-agnostic comparison.
    """
    return sorted(coords)


@pytest.mark.parametrize("heights, expected", [
    # --- Standard Examples ---
    (
        [
            [4, 2, 7, 3, 4],
            [7, 4, 6, 4, 7],
            [6, 3, 5, 3, 6],
        ],
        [[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]],
    ),  # Example 1
    (
        [[1], [1]],
        [[0, 0], [1, 0]],
    ),  # Example 2
    (
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    ),  # Classic LeetCode example

    # --- Minimum Boundaries & 1D Shapes ---
    ([[5]], [[0, 0]]),                                                    # Single cell
    ([[0]], [[0, 0]]),                                                    # Single cell at min height (0)
    ([[1, 2, 3, 4]], [[0, 0], [0, 1], [0, 2], [0, 3]]),                   # Single row (all border both oceans)
    ([[4], [3], [2], [1]], [[0, 0], [1, 0], [2, 0], [3, 0]]),             # Single column (all border both oceans)

    # --- Uniform & Monotonic Slopes ---
    (
        [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5],
        ],
        [[r, c] for r in range(3) for c in range(3)],
    ),  # Flat plateau (equal heights allow flow everywhere)
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]],
    ),  # Strictly increasing toward Atlantic
    (
        [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1],
        ],
        [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]],
    ),  # Strictly decreasing toward Atlantic

    # --- Complex Topologies ---
    (
        [
            [1, 2, 1],
            [2, 10, 2],
            [1, 2, 1],
        ],
        [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]],
    ),  # Central peak with isolated opposite corners
    (
        [
            [10, 10, 10],
            [10, 1, 10],
            [10, 10, 10],
        ],
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
    ),  # Central valley / bowl (center cell trapped)
    (
        [
            [1, 1, 10],
            [1, 10, 1],
            [10, 1, 1],
        ],
        [[0, 2], [1, 1], [2, 0]],
    ),  # Diagonal ridge acting as continental divide

    # --- Constraint Boundaries & Stress Test ---
    (
        [
            [0, 1000],
            [1000, 0],
        ],
        [[0, 1], [1, 0]],
    ),  # Min (0) and Max (1000) height boundaries
    (
        [[1] * 100 for _ in range(100)],
        [[r, c] for r in range(100) for c in range(100)],
    ),  # Max 100x100 uniform grid (tests recursion/performance limits)
])
def test_pacificAtlantic(heights, expected):
    """
    Tests the pacificAtlantic method against 15 standard, boundary, and edge cases.
    """
    assert normalize(sol.pacificAtlantic(heights)) == normalize(expected)