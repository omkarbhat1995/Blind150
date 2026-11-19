# Number of Islands

**Difficulty:** Medium
**Category:** Graphs (BFS / DFS)

## Problem Description
Given a 2D grid `grid` where `'1'` represents land and `'0'` represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
---
**Example 1:**
```text
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
```
**Example 2:**
```text
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 4
```
---
**Constraints:**
* `1 <= grid.length, grid[i].length <= 100`
* `grid[i][j] is '0' or '1'.`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns. Each cell is visited at most once.
* **Space Complexity:** $\mathcal{O}(\min(m, n))$ in the worst case (a grid completely filled with land) for the BFS queue, as we mark visited land cells in-place to avoid an extra visited set.
---

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```