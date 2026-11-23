# Max Area of Island

**Difficulty:** Medium
**Category:** Graphs (BFS / DFS)

## Problem Description
You are given a matrix `grid` where `grid[i]` is either a `0` (representing water) or `1` (representing land).

An island is defined as a group of `1`'s connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in `grid`. If no island exists, return `0`.
---
**Example 1:**
```text
Input: grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
]
Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
```
---
**Constraints:**
* `1 <= grid.length, grid[i].length <= 50`
---
## Complexity Analysis
* **Time Complexity:**  $\mathcal{O}(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns. Each cell is visited at most once.
* **Space Complexity:** $\mathcal{O}(\min(m, n))$ in the worst case (a grid completely filled with land) for the BFS queue, as visited land cells are sunk in-place to avoid an extra visited set.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```