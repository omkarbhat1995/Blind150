from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum minutes until no fresh fruit remains using
        multi-source Breadth-First Search (BFS).
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Enqueue all initially rotten fruits and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Spread rot level-by-level (minute-by-minute)
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes if fresh_count == 0 else -1