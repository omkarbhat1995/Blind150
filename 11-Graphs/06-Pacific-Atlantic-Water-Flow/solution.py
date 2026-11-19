from collections import deque
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds all grid coordinates from which water can flow to both the
        Pacific (top/left) and Atlantic (bottom/right) oceans.
        Uses reverse multi-source BFS from each ocean's borders, moving uphill
        to neighboring cells with height >= current cell's height.
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [
            (r, cols - 1) for r in range(rows)
        ]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if (r, c) in pacific_reachable and (r, c) in atlantic_reachable
        ]