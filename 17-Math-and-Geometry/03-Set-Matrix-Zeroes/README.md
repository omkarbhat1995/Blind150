# Set Matrix Zeroes

**Difficulty**: Medium
**Topics**: Array, Hash Table, Matrix

## Problem Description
Given an `m x n` matrix of integers `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must update the matrix **in-place**.
---
**Example 1:**
- **Input:** `matrix = [[0,1],[1,0]]`
- **Output:** `[[0,0],[0,0]]`

**Example 2:**
- **Input:** `matrix = [[1,2,3],[4,0,5],[6,7,8]]`
- **Output:** `[[1,0,3],[0,0,0],[6,0,8]]`
---
**Constraints:**
- `1 <= matrix.length, matrix[0].length <= 100`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
---
## Optimal Approach
To achieve this in **O(m * n)** time and **O(1)** auxiliary space, we use the first row and the first column of the matrix itself to keep track of which rows and columns need to be zeroed out. 

Because the first row and first column overlap at `matrix[0][0]`, we use `matrix[0][0]` to track the first column's state, and an additional single boolean variable (`rowZero`) to track the first row's state. After marking the borders, we iterate through the inner matrix to set the zeroes, and finally zero out the borders if their respective markers indicate it.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```