from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Captures all 'O' regions completely surrounded by 'X' in-place.
        Uses multi-source BFS from all border 'O' cells to mark unsurrounded
        regions temporarily as 'T', then flips remaining 'O's to 'X' and restores 'T's.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Enqueue all 'O' cells on the four borders and mark them as safe ('T')
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "T"
                    queue.append((r, c))

        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    board[r][c] = "T"
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark all 'O' cells connected to the border as safe ('T')
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    queue.append((nr, nc))

        # Capture remaining 'O's and restore safe 'T's back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"