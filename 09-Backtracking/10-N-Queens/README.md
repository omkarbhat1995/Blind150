# N-Queens

**Difficulty:** Hard  
**Category:** Backtracking

## Problem Description
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer `n`, return all distinct solutions to the **n-queens puzzle**.

Each solution contains a unique board layout where the queen pieces are placed. `'Q'` indicates a queen and `'.'` indicates an empty space.

You may return the answer in **any order**.
---
**Example 1:**
```text
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.
```
**Example 2:**
```text
Input: n = 1
Output: [["Q"]]
```
Constraints:1 <= n <= 8
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(n!)$ — Placing one queen per row gives at most $n$ valid column choices in the first row, $n - 1$ in the second, $n - 2$ in the third, and so on, with diagonal pruning eliminating invalid branches early.
* **Space Complexity:** $\mathcal{O}(n^2)$ — Storing the $n \times n$ board state during backtracking, plus $\mathcal{O}(n)$ for the recursion call stack and the three hash sets tracking occupied columns and diagonals (excluding the space required for the output list).   
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```