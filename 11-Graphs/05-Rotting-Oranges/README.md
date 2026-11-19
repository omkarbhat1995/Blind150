# Rotting Fruit

**Difficulty:** Medium  
**Category:** Graphs / Breadth-First Search (Multi-Source BFS)

## Problem Description
You are given a 2-D matrix `grid`. Each cell can have one of three possible values:
* `0` representing an empty cell
* `1` representing a fresh fruit
* `2` representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return `-1`.
---
**Example 1:**
```text
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
Output: 4
```
**Example 2:**
```text
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
Output: -1
```
---
**Constraints:**   
* `1 <= grid.length, grid[i].length <= 10`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(M \cdot N)$ where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited at most once during the initial scan and the BFS traversal.   
* **Space Complexity:** $\mathcal{O}(M \cdot N)$ in the worst case for the BFS queue (e.g., when the entire grid is filled with rotten fruit).   
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```