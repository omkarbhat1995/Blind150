# Surrounded Regions

**Difficulty:** Medium  
**Category:** Graphs (BFS / DFS)

## Problem Description
You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

* **Connect:** A cell is connected to adjacent cells horizontally or vertically.
* **Region:** To form a region connect every `'O'` cell. Regions can have any shape; they do not need to be squares or rectangles.
* **Surround:** A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are completely enclosed by `'X'` cells.

To capture a surrounded region, replace all `'O'`s with `'X'`s in-place within the original board. You do not need to return anything.
---
**Example 1:**
```text
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.
```
**Example 2:**
```text
Input: board = [["X"]]
Output: [["X"]]
```
---
**Constraints:**   
* `1 <= board.length, board[i].length <= 200`
* `board[i][j] is 'X' or 'O'`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns. Each cell is visited at most once during the border BFS and once during the final in-place pass.   
* **Space Complexity:** $\mathcal{O}(m \times n)$ in the worst case for the BFS queue (e.g., when the entire board is filled with 'O's).
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```