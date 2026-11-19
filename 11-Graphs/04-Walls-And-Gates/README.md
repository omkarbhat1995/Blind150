# Islands and Treasure

**Difficulty:** Medium
**Category:** Graphs (Multi-Source BFS)

## Problem Description
You are given a $m \times n$ 2D grid initialized with these three possible values:
* `-1` - A water cell that can not be traversed.
* `0` - A treasure chest.
* `INF` - A land cell that can be traversed. We use the integer $2^{31} - 1 = 2147483647$ to represent `INF`.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain `INF`.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
---
**Example 1:**
```text
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```
**Example 2:**
```text
Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
```
---
**Constraints:**
* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 100`
* `grid[i][j] is one of {-1, 0, 2147483647}`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns. Each cell is enqueued and processed at most once during the multi-source BFS.
* **Space Complexity:** $\mathcal{O}(m \times n)$ in the worst case for the BFS queue (e.g., when all cells are treasure chests).
---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```