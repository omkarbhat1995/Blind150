import pytest
from solution import Solution

sol = Solution()


def normalize(boards):
    """
    Sorts the list of board layouts for order-agnostic comparison.
    """
    return sorted(boards)


def is_valid_board(board, n: int) -> bool:
    """
    Verifies that a board has dimensions n x n, contains only 'Q' and '.',
    and places exactly n queens with no shared row, column, or diagonal.
    """
    if len(board) != n:
        return False

    cols = set()
    pos_diag = set()
    neg_diag = set()

    for r, row in enumerate(board):
        if len(row) != n or row.count("Q") != 1:
            return False
        if any(ch not in ("Q", ".") for ch in row):
            return False

        c = row.index("Q")
        if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
            return False

        cols.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)

    return len(cols) == n


@pytest.mark.parametrize("n, expected_count, expected_exact", [
    # --- Standard Examples & Impossible Small Boards ---
    (1, 1, [["Q"]]),                                                            # Example 2: Min constraint
    (2, 0, []),                                                                 # Impossible board (2x2)
    (3, 0, []),                                                                 # Impossible board (3x3)
    (
        4,
        2,
        [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ],
    ),                                                                          # Example 1: First multi-solution board

    # --- Remaining Problem Constraint Range (OEIS A000170 counts) ---
    (5, 10, None),                                                              # Odd board with 10 solutions
    (6, 4, None),                                                               # Non-monotonic dip (fewer than n=5)
    (7, 40, None),                                                              # Mid-high constraint
    (8, 92, None),                                                              # Classic 8-Queens (max problem constraint)

    # --- Stress Tests Beyond Official Constraints ---
    (9, 352, None),                                                             # Beyond constraint (n=9)
    (10, 724, None),                                                            # Beyond constraint (n=10)
    (11, 2680, None),                                                           # Performance stress test (n=11)
])
def test_solveNQueens(n, expected_count, expected_exact):
    """
    Tests solveNQueens across n=1..11 by verifying exact solution count,
    uniqueness, queen placement validity, and exact layouts where provided.
    """
    results = sol.solveNQueens(n)

    # 1. Exact solution count matches OEIS A000170
    assert len(results) == expected_count

    # 2. All returned board layouts are distinct
    unique_boards = {tuple(board) for board in results}
    assert len(unique_boards) == expected_count

    # 3. Every board satisfies all N-Queens placement rules
    assert all(is_valid_board(board, n) for board in results)

    # 4. Exact order-agnostic match when expected layouts are specified
    if expected_exact is not None:
        assert normalize(results) == normalize(expected_exact)


def test_horizontal_reflection_symmetry():
    """
    Verifies that horizontally mirroring any valid solution produces another
    solution present in the returned set.
    """
    results = sol.solveNQueens(8)
    board_set = {tuple(board) for board in results}
    for board in results:
        mirrored = tuple(row[::-1] for row in board)
        assert mirrored in board_set


def test_vertical_reflection_symmetry():
    """
    Verifies that vertically flipping any valid solution produces another
    solution present in the returned set.
    """
    results = sol.solveNQueens(7)
    board_set = {tuple(board) for board in results}
    for board in results:
        flipped = tuple(board[::-1])
        assert flipped in board_set


def test_90_degree_rotation_symmetry():
    """
    Verifies that rotating any valid solution 90 degrees clockwise produces
    another solution present in the returned set.
    """
    n = 6
    results = sol.solveNQueens(n)
    board_set = {tuple(board) for board in results}
    for board in results:
        rotated = tuple(
            "".join(board[n - 1 - r][c] for r in range(n))
            for c in range(n)
        )
        assert rotated in board_set


def test_stateless_repeated_calls():
    """
    Ensures repeated calls on the same Solution instance do not leak mutable state.
    """
    first = sol.solveNQueens(5)
    second = sol.solveNQueens(5)
    assert normalize(first) == normalize(second)
    assert len(first) == 10