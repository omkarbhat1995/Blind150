# Search a 2D Matrix

## Problem Description
You are given an `m x n` 2-D integer array `matrix` and an integer `target`.

Each row in `matrix` is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.

Return `true` if `target` exists within `matrix` or `false` otherwise.

**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## Approach: 1D Binary Search on a 2D Matrix
Because each row is sorted and the first element of each row is strictly greater than the last element of the previous row, the entire matrix can be logically flattened into a strictly increasing 1D array.

Instead of actually creating a new 1D array (which would take $O(m \times n)$ space), we can map our 1D binary search indices directly to the 2D matrix coordinates dynamically. 

1. We set our `left` pointer to `0` and our `right` pointer to `(rows * cols) - 1`.
2. While `left <= right`, we find the `mid` index.
3. We translate this 1D `mid` index into 2D coordinates:
   - `row = mid // cols`
   - `col = mid % cols`
4. We compare `matrix[row][col]` to our `target`.
5. If it matches, return `True`. If the value is less than the target, search the right half. If the value is greater than the target, search the left half.

## Complexity
- **Time Complexity:** $O(\log(m \times n))$ - We eliminate half of the remaining matrix elements at every step of our binary search.
- **Space Complexity:** $O(1)$ - We are only using a few pointers and variables to perform the math, requiring no extra memory.