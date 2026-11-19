from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum area of an island in a 2D binary grid.
        Uses iterative Breadth-First Search (BFS) to traverse and sink each
        discovered island in-place while counting its cells.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_r: int, start_c: int) -> int:
            queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = 0
            area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area += 1
                        queue.append((nr, nc))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area