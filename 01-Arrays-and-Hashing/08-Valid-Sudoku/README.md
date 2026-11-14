# Valid Sudoku

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

You are given a `9 x 9` Sudoku board. A Sudoku board is valid if the following rules are followed:
1. Each row must contain the digits `1-9` without duplicates.
2. Each column must contain the digits `1-9` without duplicates.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without duplicates.

Return `true` if the Sudoku board is valid, otherwise return `false`.

**Note:** A board does not need to be full or be solvable to be valid. Only the filled cells need to be validated according to the mentioned rules.

### Constraints
* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit `1-9` or `'.'`.

---

## 💡 Approach

A naive approach might involve checking every single row, then every single column, and finally every single `3x3` square in three separate passes. However, we can validate the entire board in a **single pass**.

We use three Hash Maps (or sets) to keep track of the numbers we have seen so far:
1. One for the rows.
2. One for the columns.
3. One for the `3x3` squares.

The trickiest part is tracking the `3x3` squares. We can identify which square a cell belongs to by taking its coordinates and performing integer division by 3: `(row // 3, col // 3)`. This maps the `9x9` grid perfectly into a `3x3` grid of sub-boxes.

As we iterate through every cell, if the cell is not empty (`'.'`), we check if the number already exists in its corresponding row set, column set, or square set. If it does, the board is invalid. If not, we add it to all three sets and continue.

### ⏱️ Complexity
* **Time Complexity:** `O(9^2)` $\rightarrow$ `O(1)` — We iterate through a strictly `9 x 9` matrix. Since the board size is fixed and does not scale, the time complexity is mathematically constant.
* **Space Complexity:** `O(9^2)` $\rightarrow$ `O(1)` — In the worst case (a full board), we store 81 elements in our Hash Maps. Because this memory footprint is bounded by the fixed board size, it requires constant auxiliary space.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/08-Valid-Sudoku/test_solution.py -v
```