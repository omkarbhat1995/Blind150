import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("board, expected", [
    # --- Standard Examples ---
    (
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    ),  # Example 1
    ([["X"]], [["X"]]),                                                 # Example 2

    # --- Minimum Boundaries & Uniform Boards ---
    ([["O"]], [["O"]]),                                                 # Single cell 'O' (on border)
    (
        [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]],
        [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]],
    ),  # All 'X'
    (
        [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
        [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
    ),  # All 'O'

    # --- 1D & 2x2 Shapes (All Cells on Borders) ---
    (
        [["X", "O", "X", "O", "X"]],
        [["X", "O", "X", "O", "X"]],
    ),  # Single row
    (
        [["X"], ["O"], ["O"], ["X"]],
        [["X"], ["O"], ["O"], ["X"]],
    ),  # Single column
    (
        [["O", "X"], ["X", "O"]],
        [["O", "X"], ["X", "O"]],
    ),  # 2x2 board (no interior cells)

    # --- Surrounded & Diagonal Traps ---
    (
        [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "X"],
        ],
        [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ],
    ),  # Single interior 'O' captured
    (
        [
            ["O", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "O"],
        ],
        [
            ["O", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "O"],
        ],
    ),  # Diagonal 'O's do not connect; center is captured

    # --- Complex Topologies ---
    (
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "X"],
            ["X", "O", "X", "X"],
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    ),  # Interior region saved by a single bottom-edge connection
    (
        [
            ["X", "O", "X", "X", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "X"],
        ],
        [
            ["X", "O", "X", "X", "X"],
            ["X", "O", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ],
    ),  # Mixed: one border-connected region and one captured region
    (
        [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X"],
        ],
        [
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ],
    ),  # Surrounded hollow ring of 'O's
    (
        [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "O"],
            ["X", "X", "X", "X", "X"],
        ],
        [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "O"],
            ["X", "X", "X", "X", "X"],
        ],
    ),  # Winding corridor connected to right border

    # --- Maximum Constraint Stress Test ---
    (
        [["O"] * 200 for _ in range(200)],
        [["O"] * 200 for _ in range(200)],
    ),  # Max 200x200 all-'O' grid (tests BFS performance and recursion limits)
])
def test_solve(board, expected):
    """
    Tests the solve method against 15 standard, boundary, and edge cases.
    Copies the board before in-place modification to preserve parametrized test data.
    """
    board_copy = [row[:] for row in board]
    result = sol.solve(board_copy)
    assert result is None
    assert board_copy == expected