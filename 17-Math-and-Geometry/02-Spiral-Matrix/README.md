# Spiral Matrix

**Difficulty**: Medium
**Topics**: Array, Matrix, Simulation

## Problem Description
Given an `m x n` matrix of integers `matrix`, return a list of all elements within the matrix in spiral order.
---
**Example 1:**
- **Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[1,2,3,6,9,8,7,4,5]`

**Example 2:**
- **Input:** `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
- **Output:** `[1,2,3,4,8,12,11,10,9,5,6,7]`
---
**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`
---
## Optimal Approach
To achieve this in **O(m * n)** time and **O(1)** auxiliary space, we can maintain four pointers representing the boundaries of the unvisited matrix: `left`, `right`, `top`, and `bottom`. 
We simulate the spiral by shrinking these boundaries inward as we traverse the top row, right column, bottom row, and left column iteratively. We must carefully check boundary overlaps within the loop to prevent double-counting elements in non-square matrices.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```