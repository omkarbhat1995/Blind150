from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Fills each reachable land cell (2147483647) in-place with the distance
        to its nearest treasure chest (0) using multi-source Breadth-First Search.
        """
        if not grid or not grid[0]:
            return

        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Enqueue all treasure chests as simultaneous BFS starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))