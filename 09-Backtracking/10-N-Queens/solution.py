from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Finds all distinct valid placements of n non-attacking queens on an n x n board.
        Uses row-by-row backtracking with sets tracking occupied columns, positive
        diagonals (r + c), and negative diagonals (r - c) for O(1) conflict checks.
        """
        cols: Set[int] = set()
        pos_diag: Set[int] = set()  # r + c
        neg_diag: Set[int] = set()  # r - c

        res: List[List[str]] = []
        board: List[List[str]] = [["."] * n for _ in range(n)]

        def backtrack(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res